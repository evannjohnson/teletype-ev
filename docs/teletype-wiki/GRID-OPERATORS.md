## Grid operators
### Usage

Controls are referenced by ids. Buttons can use ids from `0` to `255`, faders can use ids from `0` to `63`. Controls can overlap, and presses are processed by all the controls that include that grid button. `G.LED` and `G.REC` will be applied on top of everything else. 

Defining a control enables it. Disabling a control will hide it. Disabling a group disables all controls within that group. `G.LED` and `G.REC` cannot be disabled, instead they have to be cleared.

`x` and `y` specify the top left corner, `x` is the horizontal coordinate between `0` (left) and `15` (right),`y` is the vertical coordinate between `0` (top) and `15` (bottom). `w` and `h` are width and height. `level` is the brightness level between `0` (completely dark) and `15` (the brightest). There are two special brightness levels: `-1` (dim) and `-2` (brighten). Level -3 clears (makes it transparent again).

A control can only belong to one group at a time. Operators that don't take groups as a parameter will use the currently selected group which is set with `G.GRP`. There are 64 groups available (ids: `0` to `63`).

For script parameter possible values can be `1-10`, where `9` is Metro and `10` is Init. Same script can be shared by multiple controls, in which case take advantage of the ops that give you the value or the id of the last control pressed.

Also see [[STARTING SIMPLE]]

***

### General

`G.RST`  
full reset (reset all controls to defaults, clear all LEDs, reset dim level)

`G.CLR`  
clear all LEDs

`G.DIM level`  
set dim level `0..14` (higher values dim more). to remove set to `0`

`G.ROTATE 1/0`  
rotate grid `180` degrees

`G.KEY x y action`  
emulate grid key press (set action to `1` for press, `0` for release)

***

### Groups

there are also button and fader specific group ops - see BUTTONS/FADERS sections below

`G.GRP` `G.GRP id`    
get or set the current group

`G.GRP.EN id` `G.GRP.EN id 1/0`  
check if a group is enabled or enable/disable a group

`G.GRP.RST id`  
reset all controls within a group to defaults

`G.GRP.SW id`  
switch a group (enable specified group, disable all others)

`G.GRP.SC id` `G.GRP.SC id script`  
get assigned script or assign a script to a group

`G.GRPI`  
get id of the last group that received input

***

### LEDS / Rectangles

_to dim set level to -1_  
_to brighten set level to -2_  
_to clear set level to -3_  

`G.LED x y` `G.LED x y level`  
get LED level or set LED to level

`G.LED.C x y`  
clear LED (same as using `G.LED` with level `-3`)

`G.REC x y w h fill border`  
draw a rectangle (use width or height of `1` for lines)

`G.RCT x1 y1 x2 y2 fill border`  
draw a rectangle using start/end coordinates

***

### Buttons

`G.BTN id x y w h latch level script`  
initialize a button in the current group and assign a script (`0` for no script)  
set `latch` to `0` for momentary, any other value for latching

`G.GBT group id x y w h latch level script`  
same as above but with group specified

`G.BTX id x y w h latch level script columns rows`  
create a block of buttons with the specified number of columns and rows  
ids are incremented sequentially

`G.GBX group id x y w h latch level script columns rows`  
same as above but with group specified

`G.BTN.EN id` `G.BTN.EN id 1/0`  
check if a button is enabled or enable/disable a button

`G.BTN.X id` `G.BTN.X id x`  
get or set x coordinate

`G.BTN.Y id` `G.BTN.Y id y`  
get or set y coordinate

`G.BTN.V id` `G.BTN.V id value`  
get or set value. `1` means the button is pressed, `0` not pressed

`G.BTN.L id` `G.BTN.L id level`  
get or set brightness level

`G.BTNI`  
get id of the last pressed

`G.BTNX` `G.BTNX x`  
get or set x coordinate of the last pressed

`G.BTNY` `G.BTNY y`  
get or set y coordinate of the last pressed

`G.BTNV` `G.BTNV value`  
get or set value of the last pressed

`G.BTNL` `G.BTNL level`  
get or set brightness level of the last pressed

`G.BTN.SW id`  
set value for specified button to `1`, set it to `0` for all others within the same group

`G.BTN.PR id action`  
emulate button press. set `action` to 1 for press, 0 for release  
(`action` is ignored for latching buttons)

`G.GBTN.V group value`  
set value for all buttons in a group

`G.GBTN.L group odd_level even_level`  
set brightness level for all buttons in a group

`G.GBTN.C group`  
get the count of all currently pressed buttons in a group

`G.GBTN.I group index`  
get the id of a currently pressed button by index (index is 0-based)

`G.GBTN.W group`  
get the width of a block represented by currently pressed buttons in a group

`G.GBTN.H group`  
get the height of a block represented by currently pressed buttons in a group

`G.GBTN.X1 group`  
get x coordinate for the leftmost pressed button in a group

`G.GBTN.X2 group`  
get x coordinate for the rightmost pressed button in a group

`G.GBTN.Y1 group`  
get y coordinate for the highest pressed button in a group

`G.GBTN.Y2 group`  
get y coordinate for the lowest pressed button in a group

***

### Faders

`G.FDR id x y w h type level script`  
initialize fader in the current group and assign a script (`0` for no script)  
`type` selects fader type:  
0 - coarse, horizontal bar  
1 - coarse, vertical bar  
2 - coarse, horizontal dot  
3 - coarse, vertical dot  
4 - fine, horizontal bar  
5 - fine, vertical bar  
6 - fine, horizontal dot  
7 - fine, vertical dot  
`level` is brightness level for coarse faders, max value level for fine faders  
  
`G.GFD group id x y w h type level script`  
same as above but with group specified

`G.FDX id x y w h type level script columns rows`  
create a block of faders with the specified number of columns and rows  
ids are incremented sequentially

`G.GFX group id x y w h type level script columns rows`  
same as above but with group specified

`G.FDR.EN id` `G.FDR.EN id 1/0`  
check if a fader is enabled or enable/disable a fader

`G.FDR.X id` `G.FDR.X id x`  
get/set x coordinate

`G.FDR.Y id` `G.FDR.Y id y`  
get/set y coordinate

`G.FDR.V id` `G.FDR.V id value`  
get/set value scaled to fader min max (set range with `G.GFDR.RN`)

`G.FDR.N id` `G.FDR.N id value`  
get/set value in grid units

`G.FDR.L id` `G.FDR.L id level`  
get or set level (brightness level for coarse faders, max value level for fine faders)

`G.FDRI`  
get id of the last pressed

`G.FDRX` `G.FDRX x`  
get or set x coordinate of the last pressed

`G.FDRY` `G.FDRY y`  
get or set y coordinate of the last pressed

`G.FDRV` `G.FDRV value`  
get or set value of the last pressed scaled to fader min max

`G.FDRN` `G.FDRN value`  
get or set value of the last pressed

`G.FDRL` `G.FDRL level`  
get or set level of the last pressed

`G.FDR.PR id value`  
emulate fader press

`G.GFDR.V group value`  
set value for all faders in group

`G.GFDR.N group value`  
set value for all faders in group

`G.GFDR.L group odd_level even_level`  
set level for all faders in group

`G.GFDR.RN group min max`  
set range for fader values (by default `0..16383`)  
applies to all faders within that group

***

### X/Y Pad (work in progress)

`G.XYP`  
`G.GXYP`  
`G.XYPX`  
  
`G.XYP.EN`  
`G.XYP.LAT`  
`G.XYP.L`  
  
`G.XYP.X id index`  
`G.XYP.Y id index`  
  
`G.XYPI`  
`G.XYPN`  
`G.XYPX`  
`G.XYPY`  
`G.XYPL`  
  
***
 
### Game of Life (work in progress)

`G.GOL`  
`G.GGOL`  
`G.GOLX`  
  
`G.GOL.EN`  
`G.GOL.L`  
`G.GOL.V`  
`G.GOL.DENS`  
  
`G.GOL.CLK`  
`G.GOL.RND`  
`G.GOL.NEW`  
`G.GOL.RULES`  
`G.GOL.SHF`  
