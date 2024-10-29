## Grid visualizer
As you may have discovered by now, when developing a grid scene you have to often switch between the grid and the keyboard, especially if something is not working as expected. This is where Grid Visualizer will be helpful. It allows you to not only see a visual grid representation but also emulate grid presses, so you might not even have to plug the grid until you complete your scene. As a matter of fact, Grid Visualizer allows you to use grid scenes without the actual grid!  

![](./teletype-wiki/images/20240709_2332283932.png)
  
Grid Visualizer is located on Live screen. To enable it, navigate to Live view and press `Alt-G`. You should now see a visual grid representation along with some additional information. Pressing `Alt-G` again will switch to the full grid mode. Press it again to get back to the default Live screen. You can still enter and execute commands while Grid Visualizer is on - this is a great way to test grid ops, as you can immediately see what it will look like. A good way to build up a grid interface is trying your ops in Live screen and then using history (`arrow up`) to get back to the command and copy it to an appropriate script. Don't forget you can execute `G.RST` to reset grid back to the initial clean state. If you're setting up your init script you can use `G.RST` and then execute the init script with `F10` to make sure it contains everything you need.  
  
The highlighted square shows the current grid "cursor" position. If you press `Alt-Space` it will emulate pressing the corresponding grid button. You can move the cursor with `Alt-arrows`. If you additionally hold `Shift` you can expand the cursor to a bigger area. The 4 numbers on the right show you the current X/Y position and width/height of the currently selected area. `G` shows the currently selected group.  
  
If you select an area bigger than 1x1 and use `Alt-Space` it will emulate a press and hold - it will "press" the starting area point, hold it, then press the ending point, then release both. This is useful for fader slides and for scenes that use "press and hold" for defining loops and such. Being able to define a bigger area has one more purpose - if you press `Alt-PrtSc` it will insert the current x/y/width/height into the command line - very useful for defining faders and buttons.  
  
You might notice you are able to move cursor outside of the visible area (Y will be 8 or higher). This is so that Grid Visualizer can be used with grids 256. As you can only see one half of grid 256 you will need to switch between the upper and the lower halves. This is done with `Alt-/` shortcut.  
  
By default Grid Visualizer shows LEDs exactly as they would be on a varibright grid. It can still be difficult to remember where your grid controls are exactly (especially while you're still making changes to your grid UI). Grid control preview helps with that by showing the outlines of all defined grid controls. Toggle it with `Alt-\`. Grid control preview can be really helpful even after you finish developing a scene - it helps you identify at a glance what controls you have and where.  
  
When you are in full Grid Visualizer mode you don't need to use `Alt` for any of the shortcuts (although it will still work if you do) - this is a great way to use grid scenes without a grid.  
  
### Keyboard shortcuts
  
`Alt-G` switch between visualizer off/on/full view  
`Alt-Arrows` move the grid cursor  
`Alt-Shift-Arrows` select an area  
`Alt-Space` emulate a button press  
`Alt-/` switch between upper and lower half (for grid 256)  
`Alt-\` toggle the control view (shows controls outlines)  
`Alt-PrtSc` insert the current x/y/width/height (useful for creating controls)  
  
`Alt` is not needed when in full grid visualizer mode.
  
