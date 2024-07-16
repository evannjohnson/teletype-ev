## Just Type

More extensively covered in the [Just Friends Documentation](https://github.com/whimsicalraps/Just-Friends/blob/main/Just-Type.md).

Copied below, modified and stripped of crow commands and unimplemented (proposed) teletype commands.

monome's *Teletype* (and since, *crow*) excites us. Writing simple scripts away from a computer; executing tiny morsels of musical composition. Just Type is a suggestion for how these ideas can be extended & deeply integrated with elements of synthesis.

At it's most basic, Just Type is a set of invisible patch cords. But more than a cloaking device, it extends the base functionality of Just Friends into more complex territory. Every output can be driven with varying velocity, and the INTONE relationship can be altered away from the default harmonic structure.

Beyond these general-purpose modifications, Just Type brings two entirely new modalities. *Synthesis* allows explicit or automatic polyphonic control over each channel. *Geode* instead pursues rhythmic manipulation of striated repetitions, creating polymetric bursts with dynamic decay.

Enough! Just. Type.

### Install?

Just Type has shipped on every new module made since late 2017. A substantial update was released in July 2020, opening up a host of new features, and fixing many shortcomings of the original formulation.

Get the [latest release](https://github.com/whimsicalraps/Just-Friends/releases/latest) and you'll be all set to type!

### On reading this doc

Each command has a description of the names & syntax for usage. Both Teletype & crow syntax is displayed and will take the following form:

`JF.COMMAND value` (set)\
`JF.COMMAND` (get)

\needspace{0.2\textheight}
Each command has 1 or 2 forms listed. These can be of 2 types:

- 'setters' tell Just Friends to do something without expecting a response.
- 'getters' ask Just Friends to return a value.

Some commands are 'set' only, while others and 'get' only, but many have both functionalities. What's important is to recognize which option you need in your script.

Furthermore, getters work quite differently on Teletype vs crow. For Teletype, the getter will query the value and return it directly. On crow, the response to a `ii.jf.get()` call will come through the `ii.jf.event( event, value )` function which you must add to your script. For an example, you can call `ii.jf.help()` and crow will show you what this event function should look like.

### The basics: Remote control

These commands allow remote control over Just Friends. Imagine a set of invisible patch cables connected to the TRIGGERS and RUN jacks.

### Triggers

`JF.TR CHANNEL STATE`

Create a TRIGGER event on the `CHANNEL` with the provided `STATE`.

- `CHANNEL`
    - 1 is IDENTITY, and 6 is 6N
    - 0 creates a TRIGGER on all 6 channels (hardware normalization is ignored)
- `STATE`
    - 1 is *high* (5V). All non-zero values are treated as high
    - 0 is *low* (0V)
- Only *sustain* cares about the *low* triggers (the others modes will simply ignore this message).

### Run Mode

`JF.RMODE MODE`

Set the RUN state of Just Friends when no physical jack is present.

- `MODE`
    - 1 activates RUN mode. All non-zero values are treated as high
    - 0 deactivates RUN. If a physical jack is present, RUN stays high.

### Run Voltage

`JF.RUN VOLTS`

Send a virtual voltage to the RUN input.

- `VOLTS`
    - The voltage to be virtually sent to the RUN jack. Adds to the physical state
    - On TT use `JF.RUN V x` to set to x volts.
    - Range is -5 to +5
- *Requires `JF.RMODE 1` to have been executed*.

### Extended behaviour

This collection of commands extend the base capabilities of Just Friends, without totally changing the mode of interaction. They let you interact with the module in subtly different ways, and consider alternative approaches to creating compositional structure.


### Transposition

`JF.SHIFT PITCH`

Shifts the transposition of Just Friends, regardless of speed setting. Shifting by `V 1` doubles the frequency in *sound*, or doubles the rate in *shape*.

- `PITCH`
    - Amount to shift base pitch by
    - Use `N x` for semitones, or `V y` for octaves
    - Microtonal transpositions are allowed (especially useful for tuning)

\needspace{0.3\textheight}
### Velocity

`JF.VTR CHANNEL LEVEL`

Trigger *channel* with velocity set by *level*. Like Trigger but with added volume control. Velocity is scaled with volts, so try `V 5` for an output trigger of 5 volts. Channels remember their latest velocity setting and apply it regardless of whether the TRIGGER comes digitally or via CV.

- `CHANNEL`
    - channel to trigger
    - 0 sets all channels to the same velocity

- `LEVEL`
    - amplitude of output in volts
    - 0 is treated as a 'low' state, and doesn't change the saved velocity (same as `JF.TR CHANNEL 0`)


### Tuning and Intonation

`JF.TUNE CHANNEL n d`

Adjust the tuning ratios used by the INTONE control. The default for this is just the first 6 elements of the harmonic series. Instead you can retune this to your needs or desires. Think a guitar with open-G tuning – lends itself to an entirely different style of play.

Tuning is defined as a pitch ratio: numerator `n` / denominator `d`. 1/1 is IDENTITY, whereas 4/1 would be 4N's default setting. Read a little about just intonation for some ideas how you might utilise this feature.

- `CHANNEL`
    - select which channel's tuning to redefine (1 through 6)
- `n` (numerator)
    - set the multiplier for the tuning ratio
- `d` (denominator)
    - set the divisor for the tuning ratio
- *Reset to default tuning with `JF.TUNE 0 0 0`*
- If you want to retain your custom tuning permanently (across power-cycles), send the special command `JF.TUNE -1 0 0` which will store the setup to memory. When you restart the module, it will automatically recall the custom tuning.


### Address (communicating with two Just Friends simultaneously)

`JF.ADDR index`

This is only useful when configuring an ii network with two Just Friends device. Note that all devices default to index 1.

1. Power down your case
2. Disconnect the Just Friends that will be index #1 from the i2c bus
3. Make sure your second device is connected
4. Power on the case
5. Run the above address command with an index of 2: `JF.ADDR 2`
6. Test you can now talk to the second device: `JF2.TR 1 1`
6. Power down the case
7. Reconnect the Just Friends from step 2.
8. Power on the case

Now you can refer to your two devices like so. Teletype will use the `JF2` prefix instead of `JF`:

```
JF.TR 1 1
JF2.TR 1 1
```


### Panel Queries

The physical panel settings are able to be queried too. With some outside-the-box thinking, you can use the Just Friends panel to manipulate parameters inside your script. This could augment the controls (eg. the *CURVE* value could change `vtrigger` level), or introduce additional dimensions (eg. *FM* could select different `TUNE` ratios).

While the lower 3 jacks (*RAMP*, *FM*, *CURVE*) send only the knob position, *TIME* and *INTONE* send a combination of the knob with any received CV. These signals are also mapped to the same scaling as Just Type in *Synthesis* mode (see below). That means, a value of `V 0` is equal to C3. As such you could rapidly query the *TIME* control and convert it to a control-voltage with Teletype or crow - allowing for Just Friends to control the base pitch of multiple oscillators.

Finally the parameters can be used entirely tangentially to Just Friends' functionality. *RAMP* could control the rate of a METRO, while *sound*/*shape* choose between major and minor arpeggios.


`JF.SPEED`

- Returns the current *shape* (0) or *sound* (1) switch position

`JF.TSC`

- Returns the current *MODE* switch state
    - 1 = *transient*
    - 2 = *sustain*
    - 3 = *cycle*

`JF.RAMP`

- Returns the current state of the *RAMP* knob in volts (-5,5)

`JF.CURVE`

- Returns the current state of the *CURVE* knob in volts (-5,5)

`JF.FM`

- Returns the current state of the *FM* knob in volts (-5,5)

`JF.TIME`

- Returns the current state of the *TIME* knob + cv in volts (-5,5)

`JF.INTONE`

- Returns the current state of the *INTONE* knob + cv in volts
    - 0 = C3
    - 1V/octave scaled

### Modal Personality

Until now, we've only been speaking of modifying or extending the base Just Friends behaviours. Conversely, it is also possible to change some fundamentals of the JF system, leaning more heavily on the Teletype / crow integration for configuration and control.

These alternate personalities are *Synthesis*, a polyphonic synthesizer; and *Geode*, a rhythm machine. `JF.MODE 1` will take you to these modes depending on the *sound*/*shape* setting. Beware that whilst in Just Type's alternate modes, things will behave differently to normal & will remain there until power-cycling or exiting with `JF.MODE 0`.

`JF.MODE STATE`

Activates *Synthesis* or *Geode* modalities.

- `STATE`
    - 1 activates JT alternate modes. Any non-zero value is treated as 1.
    - 0 returns to standard functionality

You'll likely want to put `JF.MODE x` in your INIT script.

### Synthesis

Synthesis is, as its name boringly suggests, a synthesizer. Further, it is a polyphonic synthesizer of six independent voices. Control is either explicitly per voice, or can be dynamically assigned in a traditional polysynth fashion.

Enter *Synthesis* with `JF.MODE 1` and switching to *sound*.

The voices are centered around Just Friends' manifold generators, with pitch controlled digitally rather than with the panel controls. Each generator is shaped by *RAMP* & *CURVE* as per normal, then passed to a Vactrol Low-Pass Gate model to impart dynamics. The Vactrol model implements rudimentary envelope shaping of the velocity, controlled by *TIME*, for envelope speed, and *INTONE*, for attack-release shaping. These envelopes are controlled by the *transient* / *sustain* / *cycle* switch, and may be excited either digitally or via the hardware *TRIGGERS*.

Internally each voice contains a linked sinewave oscillator providing frequency modulation over the function generator. FM index (ie. amount), is controlled with the *FM* knob & CV input. The knob functions as normal with INTONE-style modulation CCW, and uniform modulation CW. *FM* CV input is a traditional CV-offset where positive voltage increases, and negative decreases modulation. The frequency relationship between the modulation & carrier oscillators is set via the *RUN* jack, though is matched at 1:1 with no cable attached. Positive voltages move toward 2:1 at 5V, while negative sweeps down to 1:2 at -5V giving many grumbles.

The `VOX` and `NOTE` commands are designed to create complete notes in the General MIDI sense. They simultaneously set the pitch of a voice & begin / end an envelope cycle. Physical `TRIGGERS` on the other hand, will only trigger the envelope, using whatever pitch & velocity are currently set for that voice, encouraging combinations of digital & voltage control. Pitch can be set directly with `PITCH` to slew between tones without triggering notes.


### Individual voice control (6 monosynth voices)

`JF.VOX CHANNEL PITCH LEVEL`

Play a note on the specified *channel* at the defined *pitch* and *level*.

- `CHANNEL`
    - Assign to channel 1 through 6
    - 0 sets all channels simultaneously.

- `PITCH`
    - set the pitch in 1V/octave
    - `V 0` is C3

- `LEVEL`
    - set the volume as in `VTR`
    - `V 5` gives 5V peak to peak (ie. standard modular level)

Assigning notes with voice control is great if you want to sequence independent synthesizer lines on the different channels. By using the *FM* control in the counter-clockwise direction, you can give each voice its own character, as the higher-numbered voices will have greater frequency modulation applied.


### Dynamic voice allocation (6-voice polysynth)

`JF.NOTE PITCH LEVEL`

Polyphonically allocated note sequencing. Works like `VOX` but with *channel* selected automatically. In *sustain*, free voices will be prioritized. If all voices are currently sustaining, the oldest note will be stolen to play the new note.

- `PITCH`
    - set the pitch in 1V/octave
    - `V 0` is C3

- `LEVEL`
    - set the volume as in `VTR`
    - `V 5` gives 5V peak to peak (ie. standard modular level)

`VOX` and `NOTE` are interactive, meaning you can create interesting splits of mono and poly voices.

Try turning the FM knob counter-clockwise and sequencing a fixed cycle of tones-- The timbre of the voices will cycle through 6 levels of FM depth. This can be great with 6 tones where the note order chooses timbre, but even more interesting if your sequence is 5 or 7 steps long, creating long phasing patterns for movement in a simple arpeggio.


### Pitch Control (portamento)

`JF.PITCH CHANNEL PITCH`

Control the *pitch* of a chosen *channel* without triggering the envelope (like `JF.VOX`).
- `CHANNEL`
    - Assign to channel 1 through 6
    - 0 sets all channels simultaneously.

- `PITCH`
    - set the pitch in volts-per-octave
    - `V 0` is C3

This command is useful along with `VOX` & `NOTE` control to introduce pitch changes while a note is decaying (*transient*), or without retriggering the cyclic envelope (*cycle*). Additionally it can be very useful where you are *TRIGGER*ing the channels with CV pulses, but want to choose scales or chords digitally.


### Attuned Vibrations

`JF.GOD STATE`

Redefines C3 to align with the 'God' note. See: https://attunedvibrations.com/432hz/ or http://www.roelhollander.eu/en/tuning-frequency/goebbels-and-440/.

- `STATE`
    - 0 is A=440Hz
    - 1 is A=432Hz

### Geode

In *shape*, Just Type inherits it's functionality from the standard mode. However, atop it sits a rhythmic engine for polymetric & -phasic patterns. Fundamentally this is a 'clocked' mode, whether internally so or via a continuous *tick*. The TIME & INTONE controls maintain their standard free-running influence, speeding up and slowing down *envelopes*, while the rhythms are controlled remotely.

Notes in Geode are a combination of a standard trigger along with a number of *repeats* & a rhymthic *division*. The former sets the number of envelope events to create, while the latter chooses the rhythmic relation of those repeats to the core timebase. The *MODE* switch selects how the amplitudes of repeated elements change over time. These changes are further modified by the RUN jack for fluid rhythmic variation under voltage control. These undulations are highly interactive with the *TIME* & *INTONE* controls, where the different MODE settings will handle overlapping repeats in drastically different ways. Start with *TIME* set very fast, then dial it back to hear how the repeats entangle.

Once these rhythmic streams are moving, their pattern can be corralled into a set of *quantized* steps. Using odd-subdivisions for notes, with even quantize, will enable patterns to break out of the evenly-spaced-repeats model. Try prime numbers (5/7/11) for divisions, but 4/8/16 for quantize to create traditional syncopated rhythms.

#### Geode: Transient

When set to *transient*, each repeat will have the full velocity (or a reduced one set by `VTR`).

RUN voltages will introduce a rhythmic variation every *n* repeats. At 0V, every note is emphasized (hence sounding static). Increasing a little and every 2nd note is emphasized. Further and a cycle of 3 velocities is introduced, and so on up to a cycle of 10 notes. The velocities decrease in a 'sawtooth' pattern.

With negative voltages, the same cycles are introduced, however the pattern is reversed, dropping the volume at first, then rising up over *n* repeats.

Regular syncopated rhythms are great here. Try 8 *repeats*, triggered every 8 clocks and choose a rhythm with RUN.


#### Geode: Sustain

In *sustain* repeats decay to silence over the duration of *repeats*.

By adding a RUN voltage the rate of decay can be modified. At 0V it takes exactly *repeats* to fade away. As RUN increases the repeats fade more quickly, however they will reflect back up when hitting the minimum. With around 1V the repeats will decay to near zero, then back to full volume by the last repeat, creating a triangle shape. Further increasing this level 'folds' into multiple waves per set of repeats.

Negative values slow the decay rate, making the fade out effect more and more subtle. At -5V the amplitudes are almost uniform.

Creative use of this behaviour can introduce a third temporal element to the Geode equation: *TIME* & *INTONE* set a base envelope rate, *divisions* sets the rhythm of notes, and *RUN* sets the amplitude cycle relative to *repeats*.

This mode is useful for creating pseudo-delay envelopes.


#### Geode: Cycle

*cycle* introduces a complex, *repeats* sensitive amplitude cycling. The rhythm is generated similarly to *transient*, however the variation is applied continuously rather than in single steps of beats.

Applying RUN voltage emphasizes every 2nd then 3rd then 4th event, however all the in-between beats are available too. Subtle CV shifts allow for a variation of *groove* with nothing but volume manipulation.

Negative RUN levels emphasize every fraction of a beat, which is a hard thing to think about, let alone control. As the voltage becomes lower the rhythmic cycles change more rapidly, starting to feel random. This zone is great to explore if you want to introduce some unpredictability into a rhythmic pattern.

This mode is a source of endless subtle movement and works extra well with `QT` active.


### Percussive Timebase

*Geode* needs a timebase from which to calculate the rates for the envelope sequences. This base can be set with a continuous stream of events (ie a clock) useful for when you need to synchronize the events to other elements. Alternatively a simple beats-per-minute value can be used if Just Friends is free running and doesn't need to play in time with others.

`JF.TICK DIVS`

Clock *Geode* with a stream of `DIV` ticks per measure.

- `DIV`
    - Tells Just Type how many `tick` messages will be received per measure, where a measure is 4 beats.
    - 1 to 48 ticks per measure are allowed
    - 4 means 1 tick per beat
    - 0 acts a reset to synchronize to the start of the measure

Typically `JF.TICK` will be called in a METRO. For 60 bpm, you can send `JF.TICK 4` once per second, or `JF.TICK 8` twice per second etc. Once you are comfortable using it in a standard way, the `DIV` value can be modulated to create rhythmically related clock multiplications and divisions of the *repeats*.


`JF.TICK BPM`

Set timebase for *Geode* with a static `BPM`.

- `BPM`
    - Number of beats per minute where a measure is 4 beats.
    - Must be between 49 and 255 bpm.
    - 0 acts a reset to synchronize to the start of the measure

### Individual Rhythms

`JF.VOX CHANNEL DIV REPEATS`

Create a stream of rhythmic envelopes on the named `CHANNEL`. The stream will continue for the count of `REPEATS` at a rhythm defined by `DIV`.

- `CHANNEL`
    - select the channel to assign this rhythmic stream
    - 0 sets all channels

- `DIV`
    - Divides the measure into this many segments
    - 4 creates quarter notes
    - 15 creates 15 equally spaced notes per bar (weird!)

- `REPEATS`
    - Number of times to retrigger the envelope
    - -1 repeats indefinitely
    - 0 will still create the initial trigger but no repeats
    - 1 will make 2 events total (the initial trigger, and 1 repeat)


### Round-Robin Rhythms

`JF.NOTE DIV REPEATS`

Works as `JF.VOX` but with dynamic allocation of channel. Assigns the rhythmic stream to the next channel.

- `DIV`
    - Divides the measure into this many segments
    - 4 creates quarter notes
    - 15 creates 15 equally spaced notes per bar (weird!)

- `REPEATS`
    - Number of times to retrigger the envelope
    - -1 repeats indefinitely
    - 0 will still create the initial trigger but no repeats
    - 1 will make 2 events total (the initial trigger, and 1 repeat)


### Time Quantization

`JF.QT DIV`

Quantize *Geode* events to `DIV` of a measure.

When non-zero, all events are queued & delayed until the next quantize event occurs. Using values that don't align with the division of rhythmic streams will cause irregular patterns to unfold.

- `DIV`
    - delay all events until this division of the timebase
    - 0 deactivates quantization
    - 1 to 32 sets the subdivision & activates quantization

If you need your rhythms to stay on a regular grid, activate that grid with Quantization. By setting a regular quantization (try 8 or 16) you can experiment with irregular `DIV` when triggering `VOX` or `NOTE` (try 7, 11, 13, 15) and those repeats will be locked into the quantized grid. Couple this with dynamic control over RUN and you have a very powerful groove generator with a few high level controls. Instant percussion inspiration!

While it uses a different implementation, this functionality can create [Euclidean rhythms](https://splice.com/blog/euclidean-rhythms/), though 'rotating' the rhythms requires delaying the `VOX` or `NOTE` calls.

### Teletype Reference

#### Set values or call actions:

`JF.TR CHANNEL STATE`: Set trigger `channel` to `STATE`\
`JF.RMODE MODE`: Set RUN state to `MODE`\
`JF.RUN VOLTS`: Set RUN voltage to `VOLTS`\
`JF.SHIFT VOLTS`: Transpose frequency / speed by `VOLTS` (v/8)\
`JF.VTR CHANNEL LEVEL`: Trigger `CHANNEL` with velocity set by `LEVEL`\
`JF.TUNE CHANNEL NUMERATOR DENOMINATOR`: Alter the INTONE relationship to IDENTITY\
`JF.MODE STATE`: Activates *Synthesis* or *Geode*
`JF.ADDR INDEX` Set all connected Just Friends to ii address `INDEX`\

*Synthesis:*

`JF.NOTE PITCH LEVEL`: Play a note, dynamically allocated to a voice\
`JF.VOX CHANNEL PITCH LEVEL`: Play a note on a specific voice\
`JF.GOD STATE`: If `STATE`, retune to A=432Hz (default A=440Hz)
`JF.PITCH CHANNEL PITCH`: Same as `JF.VOX` but doesn't trigger the envelope

*Geode:*

`JF.NOTE DIVS REPEATS`: Play a sequence, dynamically allocated to a channel\
`JF.VOX CHANNEL DIVS REPEATS`: Play a sequence on a specific `CHANNEL`\
`JF.TICK DIVS`: Clock *Geode* with a stream of ticks at `DIVS` per measure\
`JF.TICK BPM`: Set timebase for *Geode* with a static `BPM`\
`JF.QT DIVS`: Quantize *Geode* events to `DIVS` of the timebase

#### Get values from Just Friends:

*Proposed getters, yet to be implemented as of Teletype 3.2*

`JF.TR CHANNEL`: Returns true if the `CHANNEL` is in motion\
`JF.RMODE`: Returns the state of run_mode (ignores the jack)\
`JF.RUN`: Returns the current RUN value (ignores the jack)\
`JF.SHIFT`: Returns the current transpose setting\
`JF.MODE`: Returns 1 if *Synthesis* or *Geode* are active\
`JF.TICK`: Returns the current *Geode* tempo in beats per minute\
`JF.GOD`: Returns 1 if god mode is active\
`JF.QT`: Returns the number of *divisions* quantize is set to\
`JF.SPEED`: Returns the current *shape* (0) or *sound* (1) switch position\
`JF.TSC`: Returns the current *MODE* switch state (1/2/3)\
`JF.RAMP`: Returns the current state of the *RAMP* knob\
`JF.CURVE`: Returns the current state of the *CURVE* knob\
`JF.FM`: Returns the current state of the *FM* knob\
`JF.TIME`: Returns the current state of the *TIME* knob + cv\
`JF.INTONE`: Returns the current state of the *INTONE* knob + cv

## Just Friends reference
