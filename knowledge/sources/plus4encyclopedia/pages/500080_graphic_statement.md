# GRAPHIC Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500080
- Category: Reference/Commodore BASIC V3.5

GRAPHIC <*mode* [,*clear option*]/*CLR*>

This statement is used to select one of the 5 graphic modes:
0: normal text
1: high-resolution graphics
2: high-resolution graphics, text split-screen
3: multicolor graphics
4: multicolor graphics, text split-screen

When a hi-res or multicolor graphic mode is selected, a 10K area is allocated for the bitmap area, and the BASIC text area is moved above this area. This occurs on 32K and 64K machines. This area remains allocated even if normal text (GRAPHIC 0) is selected later. To de-allocate the 10K area and restore the BASIC text to it's normal location, use the **GRAPHIC CLR** command. (Note that the GRAPHIC CLR command will **not** deallocate** the memory on 32K machines, this appears to be a bug.)

The clear option determines whether the screen is cleared when the graphic mode is selected. (1: clear screen, 0: do not clear screen). Default is 0. If this flag is used when selecting a hi-res or multicolor mode, the [pixel cursor](500204_pixel_cursor.md) coordinates are reset to 0,0. (This does not occur when selecting normal text.)

To find out which graphics mode is currently being used, see the [RGR function](500128_rgr_function.md).

By default, the F1 key on the C16/C116 issues the GRAPHIC statement. This corresponds to KEY 1.

Examples
`GRAPHIC 0`  Selects normal text mode
`GRAPHIC 3`  Selects multicolor graphics mode
`GRAPHIC 2,1`  Selects split-screen hi-res graphics and text mode, and clears the screen
`GRAPHIC CLR`  De-allocates the 10K area reserved for graphics, and returns to normal text mode

Abbreviation
G SHIFT+R
