in order to control disting ex from teletype you will need to do the following:
- update firmware for both (find them [here](https://llllllll.co/t/teletype-disting-ex-integration/33929))
- connect i2c ports (refer to the [i2c guide](https://llllllll.co/t/a-users-guide-to-i2c/19219))
- typically you would want to disable i2c pullups on the disting but if it's not working try enabling them
- set the i2c address on the disting to 65 (if you have multiple distings set them to 65, 66, 67 and 68) (check the [manual](https://www.expert-sleepers.co.uk/distingEXfirmwareupdates.html)) 
- test by executing `EX.ALG` on teletype - you should get the current algorithm number.

for developers: [[DISTING-EX-I2C-SPECIFICATION]]

### General ops

**`EX`**  
get currently selected unit

**`EX unit`**  
select current unit (1-4)

**`EX1:`**  
**`EX2:`**  
**`EX3:`**  
**`EX4:`**  
any EX ops placed after these modifiers will use the unit in the modifier instead of the unit selected with `EX` -  
good for sending messages to a different unit without having to switch and then switch back

### Presets and Algorithms

**`EX.PRESET`**  
**`EX.PRE`**  
get current preset

**`EX.PRESET preset`**  
**`EX.PRE preset`**  
load preset

**`EX.SAVE preset`**  
save as preset

**`EX.RESET`**  
reset preset

**`EX.ALG`**  
**`EX.A`**  
get current algorithm

**`EX.ALG algorithm`**  
**`EX.A algorithm`**  
select algorithm

### Parameters

**`EX.CTRL controller value`**  
**`EX.C controller value`**  
set controller value (used with mappings)

**`EX.PARAM param`**  
**`EX.P param`**  
get current parameter value

**`EX.PARAM param value`**  
**`EX.P param value`**  
set parameter value - this will set parameter to the actual value

**`EX.PV param value`**  
set parameter value scaled to 0..16384 range  
this op expects value in 0..16384 and will map it to the actual min..max parameter range

**`EX.MIN parameter`**  
get min possible value for parameter

**`EX.MAX parameter`**  
get max possible value for parameter

### Algorithm specific ops

**`EX.REC value`**  
WAV recorder: non zero value will start recording, 0 will stop it

**`EX.PLAY value`**  
WAV recorder: non zero value will start playback, 0 will stop it

**`EX.AL.P pitch`**  
Augustus Loop: set pitch  
set the Pitch CV Input (parameter 32) to None for this to work

**`EX.AL.CLK`**  
August Loop: send clock

**`EX.LP loop`**  
Looper: get current loop state  
0 - initial state  
1 - recording  
2 - recording extra material for crossfade  
3 - playback  
4 - overdub  
5 - paused / muted  
6 - fading out towards pause  

**`EX.LP.REC loop`**  
Looper: toggle recording

**`EX.LP.PLAY loop`**  
Looper: toggle playback

**`EX.LP.CLR loop`**  
Looper: clear loop

**`EX.LP.REV loop`**  
Looper: toggle reverse

**`EX.LP.REV? loop`**  
Looper: check if reversed (1 - reversed, 0 otherwise)

**`EX.LP.DOWN loop`**  
Looper: toggle octave down

**`EX.LP.DOWN? loop`**  
Looper: check if octave down (1 - down, 0 otherwise)

### MIDI ops
require a MIDI breakout

**`EX.M.CH`**  
get currently selected MIDI channel

**`EX.M.CH channel`**  
select MIDI channel

**`EX.M.N note velocity`**  
send Note On message - this op uses MIDI values for note and velocity (0..127)!

**`EX.M.NO note`**  
send Note Off message

**`EX.M.PB pitchbend`**  
send Pitchbend message

**`EX.M.CC controller value`**  
send Controller Change message

**`EX.M.PRG program`**  
send Program Change message

**`EX.M.CLK`**  
send Clock message

**`EX.M.START`**  
send Start message

**`EX.M.STOP`**  
send Stop message

**`EX.M.CONT`**  
send Continue message

### Select Bus ops
these ops will send MIDI messages to Select Bus  
to execute specific SB operations refer to the [doc](https://docs.google.com/document/d/1YhPvAI6oliwLYSHhDholdAUym-TfBDGlxST-zDCP-qw/edit#heading=h.y65ejul6x231)

**`EX.SB.CH`**  
get currently selected SB channel

**`EX.SB.CH channel`**  
select SB channel

**`EX.SB.N note velocity`**  
send Note On message - this op uses MIDI values for note and velocity (0..127)!

**`EX.SB.NO note`**  
send Note Off message

**`EX.SB.PB pitchbend`**  
send Pitchbend message

**`EX.SB.CC controller value`**  
send Controller Change message

**`EX.SB.PRG program`**  
send Program Change message

**`EX.SB.CLK`**  
send Clock message

**`EX.SB.START`**  
send Start message

**`EX.SB.STOP`**  
send Stop message

**`EX.SB.CONT`**  
send Continue message

### Note ops
please note that chord/arpeggio functionality is only available for `EX.NOTE`/`EX.N` ops!

**`EX.VOX voice pitch velocity`**  
**`EX.V voice pitch velocity`**  
send a note to specified voice with specified pitch and velocity (using teletype values)

**`EX.VOX.P voice pitch`**  
**`EX.VP voice pitch`**  
set pitch for specified voice without retriggering

**`EX.VOX.O voice`**  
**`EX.VO voice`**  
send a note off to specified voice

**`EX.NOTE pitch velocity`**  
**`EX.N pitch velocity`**  
send note on with specified pitch and velocity (voice allocated by the disting)

**`EX.NOTE.O pitch`**  
**`EX.NO pitch`**  
send note off for specified pitch (voice allocated by the disting)

**`EX.ALLOFF`**  
**`EX.AO`**  
all notes off

**`EX.T voice`**  
trigger a note using the last pitch with velocity of 8192 (`V 5`)  
use this with SD Triggers algo

**`EX.TV voice velocity`**  
trigger a note using the last pitch and specified velocity
use this with SD Triggers algo
