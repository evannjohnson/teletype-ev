Groups are also useful for creating paged interfaces, but before we try that we should talk about enabling and disabling controls. All controls can be enabled and disabled. When a control is disabled it's not shown and it can't receive input, but it keeps its properties. You can enable or disable a control by using `G.BTN.EN` and `G.FDR.EN` ops (when a control is defined with `G.BTN` or `G.FDR` it's automatically enabled). Groups also have a similar op `G.GRP.EN`. When a group is disabled, all the controls assigned to the group are disabled as well, same for enabling. This is a great way to create different pages as you can combine multiple controls and then show/hide them at once.

_to be continued with example_

***

### FADERS

### X/Y PAD

### GAME OF LIFE

### VISUALIZER

### SCENE MANAGEMENT

### TIPS AND TRICKS
control brightness with param knob  
radio buttons