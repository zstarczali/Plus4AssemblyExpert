# SOUND Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500106
- Category: Reference/Commodore BASIC V3.5

SOUND *voice#*,*frequency control*,*duration*

This statement produces a sound from one of the three voices (1: tone, 2: tone, 3: white noise). The frequency control is a value from 0-1023, and the duration is a value from 0-65535, measured in 50ths of a second on a PAL machine (a maximum of 21 minutes 50.7 seconds), or 60ths of a second on an NTSC machine (a maximum of 18 minutes 12.25 seconds).

If a sound for a particular voice is requested while that particular voice is still playing, BASIC waits for that voice to finish the current sound before playing the next sound. Else while the sound is played, BASIC continues to execute the next statements. The only exception is when the duration for the next sound is set to 0, in which case the voice stops immediately.

Sounds on voices 1 & 2 or 1 & 3 can be played simultaneously. Voices 2 and 3 are shared, so if a sound is requested on voice 3 while voice 2 is playing (or vice versa), it will wait until voice 2 has finished before playing.

NOTE: Before any sound can be heard, a volume level must be specified with the [VOL statement](500113_vol_statement.md). VOL acts to all the 3 voices at once (this could be a problem in case different volumes are requested for different voices).

Examples
`SOUND 1,800,300`  Plays a sound from voice 1 at a frequency control of 800 for 6 seconds (PAL) or 5 seconds (NTSC)
`SOUND 1,700,100:SOUND 1,500,50`  Plays a sound for 2 seconds, which is followed by a lower sound for 1 second
`SOUND 1,700,100:SOUND 2,500,100`  Plays two different sounds simultaneously
`SOUND 2,600,50:SOUND 3,600,50`  Plays a sound for 1 second, then produces white noise for 1 second
`SOUND 1,500,50:SOUND 1,500,0`  The first sound is cancelled by the second SOUND statement which has a duration of 0

Abbreviation
S SHIFT+O
