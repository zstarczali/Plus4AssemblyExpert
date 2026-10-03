# Digi Playback

- Source: https://plus4world.powweb.com/plus4encyclopedia/500201
- Category: Programming/Audio

To play back digital audio on the TED, one has to quickly change the volume register ($FF11). The traditional, simple way of achieving this is setting up the first timer ($FF00/$FF01) for a fixed speed, then changing the volume register each time the timer interrupt occurs.

To calculate the frequency of the playback for a given speed:

PAL: ( 17734475 / 20 ) / speed = freq
NTSC: ( 14318180 / 16 ) / speed = freq

For example, speed $60 is 9237Hz, or $C0 is 4618Hz.

To calculate the playback speed for a given frequency:

PAL: ( 17734475 / 20 ) / freq = speed
NTSC: ( 14318180 / 16 ) / freq = speed

Fox example, freq 11025Hz (which is 44100 / 4) is speed $50.

Digital sound playback evolved with times. In the beginning there was the most naïve implementation where only the 9 natural volume levels (0..8) were used with usually both tone generators turned on. Digitized musics converted from C64 used only 8 of these levels for the ease of conversion. These levels are more or less linear.

Invention of the waveform digital converter brought a new development. While playing samples, the tone generators can be turned on and off independently. That gives some more amplitudes to work with, namely 13 (0..8, 10, 12, 14, 16). These levels have a middle point break in linearity, which results in sample level errors, but have greater dynamic range.

The next discovery was the possibility of locking a tone generator without turning on the sample playback mode of TED. That and the fact that TED can produce ultrasonic frequencies with the usual more or less 50% duty cycle coupled with independently turning on and off the generators results in 18 levels (0, .5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 7.5, 8, 9, 10.5, 12). These levels have more breaking points in linearity, but the scaling is less steep, which means less error and less dynamic range. Combining that with the Sound Reload bit, which can yield an additional 3 levels (10, 14, 16), results in 21 altogether.

Then came a Herculean work of detailed analysis of TED tone generation. That yielded over a hundred distinct levels. The fact that many of those falls very-very close to one another means that the actually usable number of amplitudes is much less. However, that already enabled to select 31 levels which means 5 bit resolution. And the latest attempt resulted in 46 levels. The nature of these levels should be analysed later.
