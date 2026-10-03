# LOCATE Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500085
- Category: Reference/Commodore BASIC V3.5

LOCATE *x-coordinate*,*y-coordinate*

The LOCATE statement is used to place the [pixel cursor](500204_pixel_cursor.md) anywhere on the screen.

The x and y coordinates can be expressed either as specific values (eg 160,100), values relative to the current pixel cursor coordinates (eg +50,-25), or a length and angle relative to the current pixel cursor coordinates (eg 50;45 (where 50 is the length, and 45 is the angle, seperated by a semi-colon)).

To find the current location of the pixel cursor, the [RDOT function](500127_rdot_function.md) is used. RDOT(0) contains the x coordinate and RDOT(1) conatins the y coordinate. The color source (see [color sources](500063_color_sources.md)) of the pixel cursor dot can be found by printing RDOT(2).

Examples
`LOCATE 160,100`  Places the pixel cursor in the centre of the screen
`LOCATE -10,+10`  Places the pixel cursor 10 pixels left and 10 pixels down from its current position
`LOCATE 50;45`  Places the pixel cursor 50 pixels away from its current position at an angle of 45 degrees

Abbreviation
LO SHIFT+C
