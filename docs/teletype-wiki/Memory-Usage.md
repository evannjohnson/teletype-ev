## General

The following is a compilation / summary of @samdoshi’s post ["AVR32 RAM and ROM usage"](https://samdoshi.com/post/2016/10/avr32-ram-and-rom-usage) and @trentgill’s [investigation](https://llllllll.co/t/teletype-firmware-discussion/13961/102) and the fix - huge thanks to both of you!

  
| Module   | MCU           | RAM  | ROM   |
|----------|---------------|------|-------|
| teletype | AT32UC3B05123 | 96kb | 512kb |
| ansible  | AT32UC3B05123 | 96kb | 512kb |
| trilogy  | AT32UC3B0256  | 32kb | 256kb |

The address space is unified, so a 32-bit pointer can refer to a location in RAM or in ROM. The RAM starts at location 0x0, the ROM starts at 0x80000000 (2147483648).
  
Every loadable or allocatable output section has two addresses. The first is the VMA, or virtual memory address. This is the address the section will have when the output file is run. The second is the LMA, or load memory address. This is the address at which the section will be loaded. In most cases the two addresses will be the same. An example of when the LMA and VMA might be different is when a data section is loaded into ROM, and then copied into RAM when the program starts up. In this case, the ROM address would be the LMA and the RAM address would be the VMA.
  
By taking [memory measurements](#measuring-memory) you can get a list of different memory sections with their sizes and addresses:

```

.comment                47            0        0x2f          0x0
.dalign                  4            4         0x4          0x4
.ctors                   8            8         0x8          0x8
.dtors                   8           16         0x8         0x10
.jcr                     4           24         0x4         0x18
.got                     0           28         0x0         0x1c
.data                 7484           28      0x1d3c         0x1c
.balign                  0         7512         0x0       0x1d58
.bss                  8064         7512      0x1f80       0x1d58
.heap                74536        15576     0x12328       0x3cd8
.stack                8192        90112      0x2000      0x16000
.reset                8204   2147483648      0x200c   0x80000000
.rela.got                0   2147491852         0x0   0x8000200c
.init                   26   2147491852        0x1a   0x8000200c
.text                55604   2147491880      0xd934   0x80002028
.exception             512   2147547648       0x200   0x8000fa00
.fini                   24   2147548160        0x18   0x8000fc00
.rodata              16664   2147548184      0x4118   0x8000fc18
.flash_nvram        147076   2147745792     0x23e84   0x80040000
```

See below for explanation on what the various sections represent.

## RAM

RAM usage is governed by the size of .data, .bss and .stack. These are the things we have control over. Any free RAM is allocated to the .heap, in effect this is how much free RAM you have (malloc use aside).

`.data` initialised data  
> This takes the form `int x = 10;` and is stored in .data in both ROM and RAM. ROM stores the initial values and is copied into RAM after the bootloader has run. Unfortunately the ROM address is not given in the output of avr32-size, use avr32-objdump for that.
    
`.bss` uninitialised data  
> This takes the form `int x;` and is stored in .bss in RAM only.
  
`.stack` the call stack  
> The size is set by the linker script, it may be changed by updating the linker variable __stack_size__, ideally by updating LDFLAGS in config.mk, e.g. `LDFLAGS = -Wl,-e,_trampoline,--defsym=__stack_size__=0x1000` for a 4096 byte stack. Current value used for teletype / ansible is 0x2000 (8kb).

`.heap` all unused RAM  
> By default all unused RAM is allocated to the heap for use with malloc and such.

## ROM

The flash ROM is divided into ROM and NVRAM.
  
The ROM contains your code and any read-only data, as well as the initial value for any read-write data. The size of ROM is primarily determined by the size of .text, .data and .rodata.
  
NVRAM is marked in the code using `.flash_nvram` attribute (teletype uses it [here](https://github.com/monome/teletype/blob/772b900559eee302c62069429a2b7bd089a70f68/module/flash.c#L41)). Its size is determined by the linker variable `__flash_nvram_size__` (which was decreased from the default 256kb in [this PR](https://github.com/monome/teletype/pull/252)).

`.text` code  
> This is the code segment, it contains your program.
    
`.data` initialised data
> This takes the form `int x = 10;` and is stored in .data in both ROM and RAM. ROM stores the initial values and is copied into RAM after the bootloader has run.
    
`.rodata` read-only data
> This takes the form `const int x = 10;` and is stored in .rodata in ROM only.
    
`.flash_nvram` NVRAM data
> The location of the NVRAM data, plus the size of any variables you’ve explicitly stored in there via `__attribute__((__section__(".flash_nvram")))`. The total size of flash that you wish to dedicate to NVRAM usage is configured with the linker variable `__flash_nvram_size__` (ideally set in `LDFLAGS`). 

## Considerations

The previous issue discussed in the [thread](https://llllllll.co/t/teletype-firmware-discussion/13961/102) was due to the ROM copy of the .data section overflowing into the .flash_nvram section. This was evidenced by the fact that the .flash_nvram section's VMA and LMA address were different (this is from looking at module/teletype.lss after building the firmware). Why reducing the number of scripts didn't fix the issue: it would only reduce the .flash_nvram size, so unless its address was also changed to a higher address, .data would still overflow into it.

With the above information taken into account, here are the things we should consider in order to optimize memory consumption:

- When adding constants, we reduce available ROM only (.rodata section)
- When adding any global variables, we reduce available RAM (.data section), and if they are initialized, we reduce available ROM (.data section)
- When adding more code, we reduce available ROM only (.text section)
- When adding to anything stored in `nvram_data_t` (which includes the scenes stored to flash), we reduce available NVRAM (.flash_nvram section, currently fixed at 200k)

To ensure we don't hit memory issues:

- It's better to not initialize large arrays or do it programmatically (since this would translate into lower ROM usage)
- We should take a look at all the dynamic memory allocation (several places in libavr32) and calculate how much is used, this should tell us how much RAM we have available (96kb total - 8kb stack - malloc - .data = available heap)
- If expanding the storage needed by NVRAM (such as adding more fields to the scene state), we need to check how much memory it needs and make sure we allocate enough in the `__flash_nvram_size__` linker variable (currently 200kb).
- For any code changes we should ensure .text + .data + .rodata sections don't overflow into .flash_nvram section by comparing VMA/LMA addresses of .flash_nvram section (they should be the same).


## Measuring memory

### overall sizes/addresses:

```
pr -w 85 -m -t \
   <(avr32-size -Ad teletype.elf) \
   <(avr32-size -Ax teletype.elf | cut -c 19-) \
| grep '^\..*' \
| grep -v '^.debug.*' \
| sort -k 3
```

There can be gaps between sections, for example there is a gap between the end of .rodata and the start of .flash_nvram, there is a copy of .data stored there for use at initialisation.

### VMA/LMA:

```
avr32-objdump -h teletype.elf
```

## Links
  
Sam Doshi "AVR32 RAM and ROM usage" https://samdoshi.com/post/2016/10/avr32-ram-and-rom-usage  
Thread discussion: https://llllllll.co/t/teletype-firmware-discussion/13961/102  
