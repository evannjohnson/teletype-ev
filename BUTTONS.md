Visualizing things is great, but we want to use grid to control things too. This is easy to do by using operators for grid controls. Grid controls are typical user interface elements such as buttons and faders.

The simplest way to understand how a control works is to try it. But first let's clear the Metro script and 
clear everything we painted in the previous study by executing `G.CLR`. Open the live edit page and execute the following:

`G.BTN 1 0 0 2 2 1 5 0`

That's a lot of parameters! Let's plug in the grid and see what this op does. You should see a dimly lit 2x2 square in the top left corner. Press on any buttons within that square - it will light up and stay lit until you press it again. You now have a button!

The button reacts to presses, but other than that it doesn't do anything. Let's change that. Execute the previous command but change the last parameter to 1:

`G.BTN 1 0 0 2 2 1 5 1`

Open script 1 and enter the following:

`TR 1 G.BTN.V 1`

Plug in the grid again and press on the button. Now when the button is on the trigger output 1 should go high, and when it's off it should go low. You can now generate gates from grid!

Let's examine the command:

`G.BTN id x y w h latch level script`

Some of these should look familiar, `x` and `y` are the coordinates and `w` and `h` are width and height. There is only one parameter for level - this is the level that will be used when the button is not pressed (for pressed it will always use the brightest level, 15). `latch` parameter controls the button behavior - when set to 0 it'll create a momentary button, any other value will make it a latching one.

But the most interesting parameter is `script` - this is the script that will get called whenever the button is pressed. This is how we can make scripts react to grid presses.

There is also `id` parameter - this is the button identifier. You have 256 buttons in total, numbered from 0 to 255. You will need this number if you want to change the button's parameters or if you need to get the button's current state. Let's take a look at the script again:

`TR 1 G.BTN.V 1`

We are setting the trigger output 1 to the current value of button 1 (we could use id 0 but in this case it's easier to remember if the id of the button matches the id of the trigger output). For buttons value is 1 when they're pressed and 0 when they are not pressed.

What if we want to add more buttons so that we can control all 4 trigger outputs? We could create 3 more buttons and assign them to scripts 2-4, which is not very efficient. Instead, let's assign them all to the same script. First, let's add the buttons:

`G.BTN 2 2 0 2 2 1 5 1`  
`G.BTN 3 4 0 2 2 1 5 1`  
`G.BTN 4 6 0 2 2 1 5 1`

Now change script 1 to this:

`TR G.BTNI G.BTNV`

If you try it with the grid now you should have 4 buttons controlling 4 outputs with one script. This is possible due to special shortcut ops: `G.BTNI` gives you the id of the last pressed button, and `G.BTNV` gives you its value (you could also use `G.BTN.V G.BTNI` for the latter but `G.BTNV` is shorter and easier to remember).

This is great, but we still had to use 4 commands to create 4 buttons. Since this is something we'd want to put in the Init script we want this to be as short as possible as well. This is where `G.BTX` op will be handy - it creates multiple buttons with one op. So we can replace this:

`G.BTN 1 0 0 2 2 1 5 1`  
`G.BTN 2 2 0 2 2 1 5 1`  
`G.BTN 3 4 0 2 2 1 5 1`  
`G.BTN 4 6 0 2 2 1 5 1`

with this:

`G.BTX 1 0 0 2 2 1 5 1 4 1`

The first 8 parameters are the same as used by `G.BTN`: `id x y w h latch level script`. There are 2 extra parameters which specify how many columns and rows we need. Here we're telling teletype to create a 4x1 block of buttons. Buttons created this way are placed next to each other and share the same width, height, background level, latch option and script assignment (the ids will be incremented sequentially). We will take advantage of this op when we build a [[trigger sequencer]].

As a final exercise for this study, try changing button type to momentary.

**next: [[STARTING SIMPLE]]**