### Trigger sequencer
It might seem it would be difficult to create anything more complex than just a few buttons or faders controlling a few things. Let's try something significantly more complex to both prove that it's possible and show that it can be done with just a few lines. Let's build a 6 track 16 step trigger sequencer!

We'll start with the foundation. We'll use the top 6 rows as 6 tracks with 16 steps each. Each step is a separate button. We already know the op to create multiple buttons at once - `G.BTX`. Open the Init script and add the following:

I:  
`G.BTX 0 0 0 1 1 1 4 0 16 6`

As a reminder, the parameters are `id x y w h latch level script columns rows`. We are creating a 16x6 block of 1x1 latching buttons starting with the top left corner (coordinates 0,0), the background level of 4 and no script assigned to them. Execute the Init script (by pressing `F10`) and give it a try with the grid - you should see the top 6 rows dimly lit, and you can press anywhere to turn that step on. The buttons don't do anything yet - we didn't even assign a script to them. That's because for sequencer functionality we don't actually need to trigger any actions when steps are changed, we just need to know their state (if they're "on" or "off") for the current sequencer step. Let's store the current step in variable `Z` and use the Metro script to update the step and update the outputs accordingly:

M:  
`Z WRAP + Z 1 0 15`  
`G.GBTN.L 0 4 4`  
`L 0 5: Y I; SCRIPT 8`

We increment `Z` and use `WRAP` so that it goes back to step 0 after step 15. We will cover `G.GBTN.L` later when we talk about groups, for now let's just say it will change the background level on all the buttons to 4. The last line doesn't do anything yet but it will when we make script 8 update the output for a row indicated by variable `Y`, and then our loop will do it for each of the 6 rows:

8:  
`D + Z * 16 Y`  
`G.BTN.L D 8`  
`TR + Y 1 G.BTN.V D`  

Here we update a trigger output for row `Y` (row 0 corresponds to trigger 1 etc, so we add 1) based on the corresponding button state. To do so we need to find the button id for a given row (`Y`) and a given step (`Z`). As you recall we used `G.BTX` to create 6 rows of 16 buttons. We used id 0 for the first button. `G.BTX` increments ids sequentially, row by row. So in the first row we have buttons 0..15, in the 2nd row we have buttons 16..31 and so on. To find our button we need to add the current step (`Z`) and 16 for each row after the first one. That's exactly what the formula in the first line does.

The next line contains a new op - `G.BTN.L`, which sets the background level to 8 for the specified button, so that we can see which step we are on at the moment. We don't have to change the level of the previous step back to 4 - we already did it in the Metro script (by setting it to 4 for all the buttons).

The last line updates the corresponding output based on the button state. This will work as a gate sequencer as the output will stay on for the whole step duration, if you prefer triggers replace the last line with `IF G.BTN.V D: TR.P + Y 1`. 

Try it now - at this point it's already a fully working 6 track sequencer done in only 7 lines! We could easily make it into an 8 track sequencer by changing the loops above to `L 0 7`, but we're saving the last 2 rows for extra functionality. Let's use row 6 to jump to any step.

But first we need to find ids that haven't been used yet. Since we used 0-95 for the sequencer itself the next available id is 96. Open the Init script and add the following:

`G.BTX 96 0 6 1 1 0 4 1 16 1`  

This creates a row of momentary buttons assigned to script 1, which we edit to contain the following:

1:  
`Z - G.BTNI 97`  

This sets the current step (`Z`) to the position determined by the id of the last pressed button. Since we used buttons 96-111 for this we need to subtract 96 to get the actual step number, but we subtract 97 because we want to be on the previous step before the next clock. If you want the jump to be immediate change it to 96 and add the following (the last 2 lines will update the outputs - they are the same as in the Metro script):

`M.RESET`  
`G.GBTN.L 0 4 4`  
`L 0 5: Y I; SCRIPT 7`  

You can try it now but to save on replugging let's just add the rest, starting with track mutes. We'll use 6 left buttons in row 8 for that. We already used buttons 1-111 so the next available id is 112. Add one more line to the Init script:

`G.BTX 112 0 7 1 1 1 4 0 6 1`  

and change the last line in script 8 to:

`A G.BTN.V + 112 Y`  
`TR + Y 1 * A G.BTN.V D`  

`A` will have the state of the mute button for track `Y`, so if the button is pressed the output will get updated, otherwise it'll be muted (if you're doing the trigger version replace the last line with `IF * A G.BTN.V D: TR.P + Y 1`). Remember, by default newly defined buttons will be off, don't forget to press these buttons, otherwise your tracks will be muted! By the way, button state is saved with the scene (both to flash and USB), so it will remember which tracks were muted. If you prefer to always start with unmuted tracks just add `L 112 117: G.BTN.V I 1` to the Init script.

Finally, let's add a start/stop button. We'll use the rightmost button in row 8 for that. The next available id is 118 but let's use 127 instead. You are free to choose whichever ids work best but it helps having a consistent convention - in our case we've been using sequential ids where ids increment horizontally left to right, row by row:

`0..15`  
`16..31`  
`...`  
`112..127`  

We're not using ids 118-255 yet but if we want to use them later having this consistent identification will help us remember where each button is located and what each button does.

Initialize the start/stop button in the Init script by adding the following (we will enable it by default):

`G.BTN 127 15 7 1 1 1 4 2`  
`G.BTN.V 127 1`  

It's assigned to script 2 which simply updates `M.ACT` based on the button state:

2:  
`M.ACT G.BTNV`

Don't forget to execute the Init script before you reconnect the grid. One last thing - this is driven by Metro clock, we want to be able to change speed without reconnecting the grid. Let's use the knob for that - add this to the Metro:

`M SCALE 0 16383 500 50 PARAM`  

That's it - a 6 track 16 step trigger/gate sequencer with a start/stop button, jump to step and individual track mutes, initialized in 4 lines and functionality taking another 9 lines. That leaves enough room to add more features - as an exercise, try using a trigger input as a reset, add a button to switch direction or clock it externally.  
  
But what about saving the pattern - if you have a good pattern going you probably don't want to lose it when you turn off your modular! Conveniently, you don't need to add any commands to do this - button and fader states are saved with a scene when you save it to flash or a USB stick, and are loaded automatically when you load a scene. Just remember to save your scene.  
  
You do need to add scripts to store your sequences if you have a more complex scene where the same group of buttons is used for multiple pages. Bit operations are very useful for this as they will allow you to store a state of 16 buttons in just one pattern value by using individual bits (all values, variables and pattern values in Teletype have 16 bits). To see a detailed example on how to do it see the next section, 'Saving grid state'.
  
Another improvement that could be made is having a different background level for different sections. This is what groups allow us to do, see the subsequent section 'Groups'.

see the trigger sequencer in action: https://www.instagram.com/p/BXCbE1sgS-D_

grid sequencer scene:

https://raw.githubusercontent.com/scanner-darkly/teletype_lib/main/grid/grid_sequencer.txt

trigger sequencer scene:

https://raw.githubusercontent.com/scanner-darkly/teletype_lib/main/grid/trigger_sequencer.txt

