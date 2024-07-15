### Save grid state
Store the states of multiple rows of 16 buttons in pages via binary.

With a row of 16 buttons, it is possible to store each row in one pattern slot as a 16-bit binary number. 6 rows of 16 steps * 8 pages (768 values) may be stored in just 48 Teletype pattern slots. Page 1 stores to pattern slots 0-5 store page 1, page 2 to 6-11, etc.

#### Create buttons
`#I`  
`G.BTX 0 0 0 1 1 1 3 8 16 6`  
`G.FDR 0 0 7 8 1 2 3 8`  

**1** - The 6 rows of 16 toggle buttons. Create 96 buttons, starting at the id `0`, top left (x `0`, y `0`), size of `1` by `1`, latching, `3` brightness when off, triggering script `8`, `16` columns, `6` rows.  

**2** - The page switcher. Create a fader, id `0`, in the bottom left of the grid (x `0`, y `7`), `8` buttons wide, `1` button tall, `2` is the fader type (coarse, horizontal dot), `3` brightness when off, triggering script `8`

#### Manage presses
`#8`  
`J + G.BTNY A; K G.BTNX`  
`IF G.BTNV: P J BSET P J K`  
`ELSE: P J BCLR P J K`  
`A * G.FDRN 6`  
`L 0 95: $ 7`  

**1** - Set the var `J` to the row of the button pressed + the pattern number stored in `A`. Set `K` to the x position of the button pressed.

**2** - If the button pressed is being turned on, set the bit at the x position to `1` for the pattern slot `J` (visible row + the page slot)

**3** - If the button pressed is being turned off, clear the bit to 0.

**4** - Both the buttons and the fader trigger this same script. Set A to the pressed fader value * 6. This is used to offset the patter slot for rows - page 1 to patterns 0-5, page 2 to patterns 6-11.

**5** - Loop 96 times (for each button) and run script 7.

#### Update buttons
`#7`  
`K + A / I 16`  
`G.BTN.V I BGET P K WRP I 0 15`  

**1** - Each time this is run it is being iterated for each of the 96 buttons. Set `K` to the page-pattern offset + current button's row number. `/ I 16` gets the row number because Teletype rounds decimal places values down so `I` with a value less than 16 becomes 0, 16-31 becomes 1, 32-47 becomes 2.

**2** - Set the current button's (`G.BTN.V I`) value to the bit (`WRP I 0 15`) from the number from the pattern for the button's row, offset by the current page (`P K`).
