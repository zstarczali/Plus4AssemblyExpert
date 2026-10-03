# Practical Tips For Non-standard Video Modes

- Source: https://plus4world.powweb.com/plus4encyclopedia/500279
- Category: Programming/Assembly, Hardware

Modern devices with digital video signal processing (TVs, monitors, capture devices, scalers) have a problem with a video frame not being exactly 312 rows (for PAL, 262 for NTSC). First of all, we should be happy if the device works at all and does not reject the non-TV standard video timings of the computer. It's not worth using devices that have problems with this as they already display the BASIC screen of the computer badly or not at all.

What will be displayed with incorrect rows/frame:

- in emulators, you won't notice anything (unless you are looking specifically for this) although YAPE has a tolerance setting for this

- old-school CRTs (monitor/TV) either work and you won't notice anything or the picture will be rolling

- for devices with digital processing (flat TV, scaler, capture devices) it depends on what's programmed in the firmware: maybe it works, maybe the picture will be broken, maybe it'll display a "not supported signal". Anything is possible.

Other things to do.
If you have a (n altered) screen (for example an extended screen with more than 25 text rows) with exactly the required number of rows (312 for PAL, 262 for NTSC) the screen mode change should be handled properly too. Usually this trick is achieved by altering the vertical raster position TED registers ($ff1c/$ff1d) by setting them to a lower value in an interrupt so TED will think that drawing the screen is not done yet, and later when it's done setting the registers back to the value it should be in another interrupt.
That means when initializing the new mode and returning to the standard mode the number of raster rows should remain constant in the frame. To achieve that you have to “switch modes” (in and out of extended border) either before the first interrupt so the new mode is not switched on at all or after the second one so the switching back will already be done.
Also, be careful that writing the vertical raster position register requires precise timing so it's written at the same horizontal and vertical raster positions in every frame.

If you fail to do this the result could vary again:

- in emulators, you won't notice anything

- on CRT probably you won't notice anything

- with digital video signal processing devices probably they will lose sync as they can't determine the video standard due to the non-standard number of lines and will resync in 1-2 seconds. Until then you won't see the picture.

When you change the vertical raster position register be careful to always write a value where its lowest bit is the same as the original value (so if it was even the new value should be even if it was odd the new value should also be odd). If you fail to do so an interesting picture artifact (PAL color phase inversion) will appear. Unless that's exactly what you wanted to do.

Credits
Thanks to BSz for compiling the list.
