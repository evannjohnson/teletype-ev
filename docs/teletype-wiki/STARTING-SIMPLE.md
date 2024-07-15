There are many different ways to use a grid with a teletype. Let's try some simple examples to show the range of things possible.
  
But first let's review the conventions behind grid ops that should make it easier to memorize them. As you've noticed all grid ops start with `G.`. This is followed by 3 letters signifying a control: `G.BTN` for buttons, `G.FDR` for faders etc. 

  
To define a control you use the main ops `G.BTN`, `G.FDR`  
To define multiple controls replace the last letter with X: `G.BTX`, `G.FDX`

When defining controls the first 4 parameters are always the same: `id, coordinates, width, height`. For buttons this is followed by `latching/level/script`, for faders - `direction/level/script`. When creating multiple controls the last 2 parameters are the number of columns and the number of rows.  
  
Controls are created in the current group (set with `G.GRP`). To specify a different group use group versions of the 4 above ops - `G.GBT`, `G.GFD`, `G.GBX`, `G.GFX` and add the desired group as the first parameter.
  
All controls share some common properties, referenced by adding a `.` and:  
`EN`: `G.BTN.EN`, `G.FDR.EN` - **en**ables or disables a control  
`V`: `G.BTN.V`, `G.FDR.V` - **v**alue, simply 1/0 for buttons, range value for faders  
`L`: `G.BTN.L`, `G.FDR.L` - background brightness **l**evel  
`X`: `G.BTN.X`, `G.FDR.X` - **x** coordinate  
`Y`: `G.BTN.Y`, `G.FDR.Y` - **y** coordinate  

Group ops `G.GBTN.#` and `G.GFDR.#` allow you to get/set properties for a group of controls. To get/set properties for individual controls you normally specify the control id as the first parameter: `G.FDR.V 5` will return the value of fader 5. Quite often the actual id is not important, you just need to get or set a property on the last control pressed. As these are likely the ops to be used most often they are offered as shortcuts without a `.`: `G.BTNV` returns the state of the last button pressed, `G.FDRL` will set the background level of the last fader pressed etc etc.
  
All ops can be roughly grouped as follows: general use, groups, drawing, buttons, faders and area ops. There are some specialized ops as well that will be handy for some specific use cases (and make sure to take advantage of being able to rotate and dim grid!). And now let's see them in action...
  
### TRIGGER VISUALIZER

It can be useful to have some visual feedback about what's going on with your scene. The most obvious candidate is tracking incoming triggers. We could use `G.REC` but it's actually easier to use buttons for this since we won't have to calculate the coordinates. We'll use 4x4 buttons, 2 rows with 4 buttons each:

`I:`  
`G.BTX 1 0 0 4 4 0 0 0 4 2`  

As a reminder, the first 4 parameters are id, coordinates, width, height. These are buttons, so next is latching/level/script: 0 for momentary, 0 for level, 0 for script (no script assigned), 4 buttons in 2 rows.

Now add 2 lines to each of the trigger scripts 1-8 as follows:

1:  
`G.BTN.L 1 15`  
`DEL 50: G.BTN.L 1 0`  
  
2:  
`G.BTN.L 2 15`  
`DEL 50: G.BTN.L 2 0`  

Each trigger script will set the corresponding button's brightness level to 15. We display it for 50 ms and then set it to 0. Now whenever a trigger is received the corresponding button will blink.

Since we already have buttons defined let's make them trigger scripts as well. Since all our scripts are used for triggers we'll use the Metro script to process button presses. Change I to:

I:  
`G.BTX 1 0 0 4 4 0 0 9 4 2`  
`M.ACT 0`  

This will stop M from autotriggering and assign it to button presses (9 is for Metro script). Make sure to execute the Init script by pressing F10. Add this to the Metro:

M:  
`SCRIPT G.BTNI`

Now when a button is pressed the corresponding script will execute. This scene can be further expanded by having each button's brightness level correspond to a value of some variable.

[download the scene](https://raw.githubusercontent.com/scanner-darkly/teletype_lib/main/grid/trigger_visualizer.txt)

### SIMPLE SEQUENCER

A really simple 16 step sequencer:

I:
`G.FDX 0 0 0 1 8 1 0 0 16 1`  

We create 1 row of 16 vertical faders, each 8 LEDs high.

1:
`A WRAP + A 1 0 15`  
`CV 1 N G.FDR.N A; TR.P 1`  
`G.CLR; G.REC A 0 1 8 -3 -2`  

Script 1 increments the step (we store it in variable `A`), updates CV 1 with a note based on the value of the fader located on that step and sends a trigger to TR 1. The last line highlights the current step. Instead of using the fader value as a note number you could store notes in a pattern  bank and then do something like `CV 1 PN 0 G.FDR.N A`. Or change `CV 1 N` to `CV 1 V` and use it to modulate something.

Trigger 1 serves as the clock input. If you want teletype to be the main clock update the Metro script to:

`M SCALE 0 16383 500 50 PARAM`  
`SCRIPT 1`  

This makes the knob control the clock rate and then it calls script 1 to advance the sequencer. We can use another trigger input for reset:

2:
`A 15`  

[download the scene](https://raw.githubusercontent.com/scanner-darkly/teletype_lib/main/grid/simple_sequencer.txt)

### LOFI OSCILLOSCOPE

This is a very low res oscilloscope but can be fun as a way to visualize your patch. 

M:
`A WRAP + A 1 0 15`  
`B SCALE 0 V 5 0 7 IN`  
`G.REC A 0 1 8 0 0`  
`G.LED A B 8`  
`M! SCALE 0 16383 200 10 PRM`

`A` is the current step again, `B` is the input voltage scaled to 0..7. It will scale the incoming voltage from a 0..5V range to 8 available vertical pixels. Change `V 5` to desired range. Just remember the input is unipolar, so to see full cycle of an LFO you will need to offset it.

We clear the whole column first and then draw a dot at `A,B` coordinates. The last line is your time resolution - it'll adjust the Metro rate based on the knob.

[download the scene](https://raw.githubusercontent.com/scanner-darkly/teletype_lib/main/grid/lofi_oscilloscope.txt)

[video demo](https://www.instagram.com/p/BZ9dcUKAAw4)

Next we'll try something a bit more complex...

**next: [[TRIGGER SEQUENCER]]**