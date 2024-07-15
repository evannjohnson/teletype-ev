## Disting EX I2C Messages

Dedicated teletype ops will use the following 4 addresses specifically reserved for the EX:
- **0x41..0x44**

Pitch and velocity parameters use 14 bit precision:
- pitch range -16384..+16384 translates to 10 octaves range (-10V..+10V using 1V/Oct)
- max velocity is 16384
  
Dual algorithms have their own commands - see the section below.

---

### Presets

load preset  
`<address> 0x40 <preset number MSB> <preset number LSB>`  

save preset  
`<address> 0x41 <preset number MSB> <preset number LSB>`  
   
reset preset  
`<address> 0x42`
  
get current preset  
`<address> 0x43`
Returns 2 bytes.

---

### Algorithms

load algorithm  
`<address> 0x44 <algorithm number>`

get current algorithm  
`<address> 0x45`
  
set i2c controller X to value Y  
`<address> 0x11 <controller number> <value MSB> <value LSB>`

set parameter X to value Y (using the actual parameter value)  
`<address> 0x46 <parameter number> <value MSB> <value LSB>`

set parameter X to value Y (using 0..16384 range, will be scaled to min..max by EX)  
`<address> 0x47 <parameter number> <value MSB> <value LSB>`
  
get current parameter value  
`<address> 0x48 <parameter number>`
  
get parameter min  
`<address> 0x49 <parameter number>`
  
get parameter max  
`<address> 0x4A <parameter number>`
  
WAV Recorder, start / stop recording  
`<address> 0x4B <0 - stop, 1 - start>`
 
WAV Recorder, start / stop playback  
`<address> 0x4C <0 - stop, 1 - start>`

Augustus Loop, set pitch  
`<address> 0x4D <pitch MSB> <pitch LSB>`
 
Augustus Loop, send clock  
`<address> 0x4E`
  
Looper, clear target loop  
`<address> 0x58`

Looper, get current state  
`<address> 0x59 <loop index>`  
returns a byte. loop index is 0-based
  
  
the low nibble represents one of the following states:  
0 - initial state  
1 - recording  
2 - recording extra material for crossfade  
3 - playback  
4 - overdub  
5 - paused / muted  
6 - fading out towards pause
  
bit 4 - reverse on/off  
bit 5 - octave down on/off

--- 

### MIDI / Select Bus

send MIDI message  
`<address> 0x4F <status> <optional data byte 0> <optional data byte 1>`

send Select Bus message  
`<address> 0x50 <status> <optional data byte 0> <optional data byte 1>`

---

### Voice Control (for specified voice)

set voice pitch for the specified voice  
`<address> 0x51 <voice> <pitch MSB> <pitch LSB>`

note on for the specified voice  
`<address> 0x52 <voice> <velocity MSB> <velocity LSB>`

note off for the specified voice  
`<address> 0x53 <voice>`

---

### Voice Control (voice allocated by the disting)

commands that don't specify the channel will default to channel one if the channel is not set

set channel for note commands  
`<address> 0x6B <channel>`

set voice pitch for note id  
`<address> 0x54 <note id> <pitch MSB> <pitch LSB>`

set voice pitch for note id with channel  
`<address> 0x68 <channel> <note id> <pitch MSB> <pitch LSB>`

note on for specified note id  
`<address> 0x55 <note id> <velocity MSB> <velocity LSB>`

note on for specified note id with channel  
`<address> 0x69 <channel> <note id> <velocity MSB> <velocity LSB>`

note off for specified note id  
`<address> 0x56 <note id>`

note off for specified note id with channel  
`<address> 0x6A <channel> <note id>`

all notes off  
`<address> 0x57`

---

### Dual Algorithms
  
`<side / parameter index>` is `(side << 4) | parameter index`
  
get current parameter value (returns 1 byte)  
`<address> 0x5A <side / parameter index>`
  
get parameter min (returns 1 byte)  
`<address> 0x5B <side / parameter index>`
  
get parameter max (returns 1 byte)  
`<address> 0x5C <side / parameter index>`
  
set parameter X to value Y (using the actual parameter value)  
`<address> 0x5D <side / parameter index> <value>`
  
set parameter X to value Y (using 0..16384 range, will be scaled to min..max by EX)  
`<address> 0x5E <side / parameter index> <value MSB> <value LSB>`
  
get current algorithm - returns 1 byte  
`<address> 0x5F <side>`
  
load algorithm  
`<address> 0x60 <side> <algorithm number>`
  
get current algorithms (returns 2 bytes)  
`<address> 0x61`
  
load algorithms  
`<address> 0x62 <algorithm number> <algorithm number>`
  
load dual preset  
`<address> 0x63 <side> <preset>`
  
save dual preset  
`<address> 0x64 <side> <preset>`
  
take-over/release Z  
`<address> 0x65 <side> <value 0-127, else release>`
  
read Z pots (returns 2x2 bytes, 15 bit results)  
`<address> 0x66`