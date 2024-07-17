### Groups
One of the most common tasks when programming a grid interface is updating a group of controls at once. In some cases this could be done with a loop, but loops are not always efficient or even possible. This is where groups can be very helpful. Every grid control belongs to one of the 8 groups. Whenever you initiate a control it will be assigned to the current group. We haven't used groups so far, but that simply means that all our controls where assigned to group 0 - this is the default group for each new scene. To change the current group we use `G.GRP` op:

`G.BTN 0 1 1 1 1 1 0 0`  
`G.GRP 1`  
`G.BTN 1 2 1 1 1 1 0 0`  

In this example button 0 will be assigned to group 0, and button 1 will be assigned to group 1.

To demonstrate how groups can be useful let's create a group of radio buttons. Whenever one button is pressed whichever button was "on" before should be switch to "off" so that only one button is "on" at any given time. We could program it like this:

I:  
`G.BTX 0 0 0 1 1 1 4 1 8 1`

1:  
`L 0 7: G.BTN.V I 0`  
`G.BTN.V G.BTNI 1`

We defined 8 buttons and assigned them to script 1. The script will set the value for each button to 0 (so that it's "off") and then set it to 1 for the last pressed button. Not too bad, but instead we could simply do:

1:  
`G.BTN.SW G.BTNI`  

`G.BTN.SW` (`SW` is short for 'switch') is a convenient op that sets the value to 0 for all the buttons in a group except the specified button (in our case, the last pressed button) which gets its value set to 1. This works well for our radio buttons but we don't want it affecting any other buttons. To avoid that we can simply put the radio buttons into their own group.

Let's look at another example. In the [[trigger sequencer]] study we highlighted the current step by changing the background level for the corresponding buttons to a higher one. We also needed to change the previous step back to a lower level. The easiest way to do this is by resetting the background level for all the buttons first, then setting it to a higher level for the current step. `G.GBTN.L` op lets us set the background level for all the buttons in a group. But what if we want to use a different level for the mute/start/stop buttons? Then we can simply place them in a different group.

You can also assign scripts to groups, and they will get executed whenever any control within that group is pressed. Another useful feature is `G.GRP.RST` which resets all the controls within a group - this is a good way to experiment with some new elements without affecting anything else. Just remember to move them into a proper group if needed. There is no separate op to reassign controls to a different group - simply select the group you need and execute the control ops again.

But perhaps the most useful purpose for groups is being able to create paged UIs.

\addtocontents{toc}{\protect\setcounter{tocdepth}{1}}

