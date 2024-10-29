## Grid control mode
Grid ops give you the ability to build your own grid UI. But sometimes you just want to use grid to perform basic tasks, such as triggering scripts, editing pattern values etc. You could create a scene for that but instead you can just use the  built in Grid Control Mode. Essentially, it turns grid into a Teletype controller.  
  
It's not an alternative to grid scenes - as it happens, it can be especially useful when used together with a grid scene. By delegating some tasks to Grid Control Mode you can pack more functionality into your scene, and you can switch between different Teletype views and save and load scenes without having to reconnect the keyboard.  
  
To turn it on simply press the front panel button (next to the USB port) while grid is connected (remember you shouldn't connect grid directly to teletype - make sure to power it externally!). The right side of grid will change to display the Grid Control UI, assuming you use grid 128. Grid control will also work on grids 64 but it will take over the whole grid (and on grids 256 it will use the right bottom quadrant). To exit Grid Control Mode press the front panel button again.  
  
Grid Control Mode has pages that correspond to Teletype views - Live with variables, Live with Grid Visualizer, Presets, Tracker and 10 scripts. When you turn it on it will automatically go to the page that corresponds to the page Teletype is currently on. Switching pages in Grid Control will switch pages on Teletype as well.  
  
The top 2 rows is where you select a page. These 2 rows stay the same on all pages with the exception of Tracker. Script and Live pages also share other common controls:  
  
  
![live/script screens shared layput](./teletype-wiki/images/20240709_0025503239.png)
  
The bottom row allows you to manually trigger scripts (you can do this even if a script is muted). The row above toggles script mutes. You can also trigger Metro and Init scripts, mute Metro and kill delays and slews.
  
The rest of the controls depends on the page selected.  
  
### Script Pages
![script pages](./teletype-wiki/images/20240709_0025511881.png)
  
When you select one of the script pages you will see the screen above. Here you can toggle comments on individual lines. You can also enable or disable all lines at once.  
  
### Live Page with Variables
![live page with variables](./teletype-wiki/images/20240709_0025513422.png)
  
Live page with Variables allows you to monitor and edit variables. This could be used for debugging purposes or controlling a scene via variables (for instance, you could use a variable for sequencer position - editing this variable will give you the ability to jump to different positions). To edit a variable press on the corresponding button and hold it. While holding, if you press the button directly to the left it will decrement the value by 1. Pressing the button on the right will increment by 1. You can also increment/decrement by 10 by pressing buttons that are two to the left / two to the right.  
  
The value is also shown on the bottom row (if it's within 0..16 range, or 0..8 on grid 64). Pressing in this row will set the value to that position. If you press and release a variable button without changing its value it will toggle the value between 0 and whatever it was before.  
  
This Live page also allows you to scroll through the live command history and execute commands. This is a good way to have some extra commands available, just remember to enter them while you still have the keyboard plugged in.  
  
### Live Grid page
![live page with grid visualizer](./teletype-wiki/images/20240709_0025521710.png)
  
Live page with Grid Visualizer has grid specific controls. You can select the upper/lower grid page, change grid rotation and toggle the grid control view.  
  
### Presets page
![preset page](./teletype-wiki/images/20240709_0025527911.png)
  
Presets page keeps the top 2 rows but uses the rest of space to display the 32 available presets. Press on one of the preset buttons to select a preset - this will not load it but simply select it for loading/saving. You can scroll through a preset description with the buttons on the right. The remaining two buttons will load or save the currently selected preset. When you save it will display `WRITE` on the Teletype screen - press it again to confirm save (or press elsewhere if you want to exit without saving). Once you load or save a preset it will go back to whatever page you were on before switching to Presets.  
  
### Tracker page
![tracker page](./teletype-wiki/images/20240709_0025524826.png)
  
Finally, the Tracker page utilizes the full 8x8 block. To exit, press the Tracker page button again, and it will go back to the previous page.  
  
The Tracker page controls 8 rows of 4 pattern banks, mirroring what you see on Teletype. You can select a pattern page with the left column, or you can scroll with the 2 buttons in the right lower corner.  
  
Editing tracker values is similar to editing variables - pressing and releasing will toggle the value (useful for trigger sequencers), pressing, holding and then pressing buttons to the left / to the right will increment/decrement by 1 or 10. If you press and hold and then press in a different row it will select pattern start and end for one or more pattern banks - useful for defining loops. If you need to select a loop that is longer than 8 steps you can set start/end points separately by using "set start" / "set end" buttons on the right - press and hold and then press where you want the position to be.  
  
The remaining 2 buttons allow you to select the current pattern position and the turtle position. Pressing and releasing the turtle button will toggle the turtle on and off.
