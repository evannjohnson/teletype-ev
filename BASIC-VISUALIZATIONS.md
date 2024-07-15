Let's start with some basic drawing. Open the Metro script and enter the following command:

`G.REC 3 3 4 4 0 RRAND 1 15`

Make sure Metro is enabled (execute `M.ACT 1`), unplug the keyboard and connect the grid. You should see a 4x4 rectangle with a border that changes brightness on each metro tick.

Let's reconnect the keyboard (at this point you are realizing you'll be doing this a lot - not to worry, the grid visualization page which we'll cover in a bit will help to minimize the amount of switching). Edit the line and change it to the following:

`G.REC 1 1 4 4 0 RRAND 1 15`

If you plug in the grid again you should see another 4x4 rectangle partially covering the previous one. Even though we edited the first command the first rectangle is still there. That's because using `G.REC` is like painting on grid canvas - whatever was previously painted will remain until something is painted over, or until we clear the canvas.

Let's examine all the parameters of `G.REC`:

`G.REC x y w h fill border`

`x` and `y` are the coordinates for the rectangle's top left corner. `x` is the horizontal coordinate, starting with the leftmost column, and `y` is the vertical coordinate, starting with the top row. coordinates are 0-based, so the top left corner is 0 0. `w` and `h` are width and height. `fill` and `border` specify the brightness levels. As you can tell by the range we used for `RRAND` the possible range for brightness starts with 1 (the dimmest) and extends to 15 (the brightest). 0 will turn the corresponding LED completely off. 

How can we erase the first rectangle now? We could paint a couple of rectangles with the brightness level of 0 over the parts that are still visible, but sometimes it's just easier to clear everything and draw what you need again. To clear the canvas use `G.CLR` op. Please note that what you draw will not be saved with the scene - whenever a scene is loaded it starts with a blank canvas.

You can also draw individual LEDs:

`G.LED x y level`

There is no separate operator for lines - just use a rectangle with width or height of 1 (fill level is not used in this case).

Just by using these 3 operators you can now visualize your scene with the grid. For instance, you could make an LED blink whenever a script is executed, or draw rectangles with the size reflecting the value of a variable (`SCALE` op will be useful here to make sure it's scaled to the appropriate range).

Or you could do something more interesting - how about drawing rectangles with random coordinates and random size where each script uses a different brightness level?

**next: [[BUTTONS]]**