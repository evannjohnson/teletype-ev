### II protocol

The II protocol was originally created for the purpose of Teletype controlling Monome trilogy modules via i2c. It was later expanded to support other i2c devices, both as followers and as leaders (see the complete list below). This document only describes the protocol itself and does not include information on the hardware setup.  
  
The protocol is very simple. Each device gets a unique i2c address. An i2c leader sends a command to a follower device. No acknowledgement is expected from a follower device other than what is part of the i2c protocol itself. A leader can also poll followers for data by issuing a poll request and waiting for the follower to respond.  
  
Please note that Teletype does not support multiple leaders sending messages simultaneously on the same i2c bus - you can have multiple leaders on the same bus if you only send from one leader at a time, but multiple leaders sending messages can lead to i2c not working until you power cycle.  
  
### Format

Each command uses the following format:  
  
**`[address byte] [command byte] [data bytes (optional)]`**  
  
`[address byte]`  
> The unique i2c device address as unsigned byte. The protocol uses 7bit addressing, which means there are 128 possible addresses available. Depending on the i2c implementation the address can be either in LSBs or MSBs - make sure to adjust for this (by right bitshifting MSB address by 1). For Monome ecosystem these addresses are typically tracked here: https://github.com/monome/libavr32/blob/main/src/ii.h (it's not mandatory to add new addresses there but it's highly recommended so that we can avoid address collisions). In some cases it's possible to connect multiple devices of the same type - typically such devices provide a way to either select their i2c address (ER-301) or select their device index (Telex) which is then added to the device's base address. Address 0 is a special address - each follower will respond to commands sent to that address. We might utilize this in the future to provide global commands.  
  
`[command byte]`  
> The command as unsigned byte. Each device has its own set of commands, so each device can have up to 256 commands in total. However, range 0xC0-0xFF is reserved for future use.  
  
`[data bytes (optional)]`  
> Additional parameters as unsigned byte array. Optional for those commands that don't require parameters. This is sent as a byte array, so parameters of any other data types should be converted by the leader and reassembled by the follower. Or if you need to pass a signed byte you can simply cast it before sending / after receiving.  
  
Parameter range can differ between different devices and commands. For something that translates into voltage, parameters typically use 14 bit precision, and the -16384..16384 numeric range will translate into the -10V..10V voltage range. Same applies to pitch parameters where voltage is assumed to be in 1V/Oct scale (so adding 1638 will produce a result an octave higher). 

Since the i2c implementation was originally intended to only be used by a few monome modules, there was no attempt to standardize messages such as "play a note" (there was a [proposal](https://llllllll.co/t/universal-ops/13758) but it got no traction). This means that, unfortunately, different modules use different format and different commands for similar tasks. Additionally, some modules have multiple modes, so you might need to send additional commands to set the mode. For Teletype that is typically done with dedicated ops (such as `JF.MODE`), but other devices might need to take care of it themselves - see the `ii_init_` functions used by [the ansible i2c implementation](https://github.com/monome/ansible/blob/main/src/ansible_ii_leader.c) as an example of how it can be done.

The following lists some commonly used commands - it wouldn't be practical to list every single one as there are hundreds of them. For Disting Ex you can see the complete list [here](https://github.com/scanner-darkly/teletype/wiki/DISTING-EX-I2C-SPECIFICATION). For others you could refer to the aforementioned ansible i2c implementation, [the multipass implementation](https://github.com/scanner-darkly/multipass/blob/526e8bfe1cd8265b37d5f3d0c9b6c91fe880c5e0/monome_euro/main.c#L587) or the [teletype source code](https://github.com/monome/teletype/tree/main/src/ops). 
  
### ER-301  
Device address: `0x31..0x33` (up to 3 devices)  
   
| command | binary_format | parameters |
| --- | ------------ | --- |
| set CV | `0x11 I H L` | `I` - output (0..99), `H`/`L` - value as signed int, high/low byte |
| set CV slew | `0x12 I H L` | `I` - output (0..99), `H`/`L` - slew value in ms as signed int, high/low byte |
| set gate | `0x00 I S` | `I` - output (0..99), `S` - state (0 - low, 1 - high) |
    
### Telexo  
Device address: `0x60..0x67` (up to 8 devices)  
   
| command | binary_format | parameters |
| --- | ------------- | --- |
| set CV | `0x11 I H L` | `I` - output (0..3), `H`/`L` - value as signed int, high/low byte |
| set CV slew | `0x12 I H L` | `I` - output (0..3), `H`/`L` - slew value in ms as signed int, high/low byte |
| set gate | `0x00 I S` | `I` - output (0..3), `S` - state (0 - low, 1 - high) |
| set envelope mode | `0x60 I S` | `I` - output (0..3), `S` - mode (0 - disabled, 1 - enabled) |
| set envelope | `0x6D I S` | `I` - output (0..3), `S` - envelope (0 - off, 1 - on) |
| set osc pitch | `0x41 I H L` | `I` - output (0..3), `H`/`L` - pitch, high/low byte |
| set osc waveform| `0x4A I H L` | `I` - output (0..3), `H`/`L` - waveform value (0..5000) high/low byte |
    
### Just Friends  
Device address: `0x70`  
   
| command | binary_format | parameters |
| --- | -------------- | --- |
| play note | `0x8 I PH PL VH VL` | `I` - output (1..6, 0 for all), `PH`/`PL` - pitch, high/low byte, `VH`/`VL` - volume, high/low byte |
| set gate | `0x1 I S` | `I` - output (1..6, 0 for all), `S` - state (0 - low, 1 - high) |
  
### List of supported devices:
- Monome Teletype (leader)
- Monome White Whale (follower, leader or follower with polyearthsea or orca's heart firmware)
- Monome Meadowphysics (same as white whale)
- Monome Earthsea (same as white whale)
- Monome Ansible (same as white whale)
- Monome Crow (follower or leader)
- Telexo (follower)
- Telexi (follower)
- Mannequins Just Friends (follower)
- Mannequins W/ (follower)
- Orthogonal Devices ER-301 (follower)
- SSSR Labs SM-010 (follower)
- 16n Faderbank (follower or leader)
- ADDAC 221 (follower)
- Tesseract Modular Sweet Sixteen (follower or leader)
- CalSynth 16n Faderbank (follower or leader)
- Michigan Synth Works F8R (follower or leader)
- Expert Sleepers Disting EX (follower)
  
Discussion thread on lines forum: https://llllllll.co/t/teletype-i2c-protocol/13642  