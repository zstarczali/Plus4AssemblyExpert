# BOX Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500061
- Category: Reference/Commodore BASIC V3.5

BOX [*color source#*],*a1*,*b1*,*a2*,*b2*[ [,*angle*] [,*paint*] ]

A graphics area must be defined with the [GRAPHIC statement](500080_graphic_statement.md) before using this statement, or a [?NO GRAPHICS AREA ERROR](500092_no_graphics_area_error.md) will occur.

To ensure the object has the same appearence in both hi-res and multicolor modes, see the [SCALE statement](500104_scale_statement.md).

The BOX statement is used to draw a rectangle of any size anywhere on the screen.

The [color sources](500063_color_sources.md) are 0-3 (default 1). To change the colors, see the [COLOR statement](500068_color_statement.md). Multicolor sources can only be used when a multicolor mode is active.

a1 and b1 are the corner coordinates in pixels. These can be expressed either as specific values (eg 160,100), values relative to the [pixel cursor](500204_pixel_cursor.md) coordinates (eg +50,-25), or a length and angle relative to the pixel cursor coordinates (eg 50;45 (where 50 is the length, and 45 is the angle, seperated by a semi-colon)).

a2 and b2 are the coordinates for the opposite corner. These can be expressed in the same choice of format as the first corner coordinates. If no value is specified, the pixel cursor coordinates are used. When no value is specified, only one comma is used to seperate from the other parameters, as the default value is for both a2 and b2.

The angle is the clockwise rotation of the box in degrees; default is 0.

The paint flag determines whether the shape is filled with the color source (0: off, 1: on). Default is 0.

Examples
`BOX 1,10,10,60,60`  Draws the outline of a box
`BOX ,10,10,60,60,45,1`  Draws a filled box rotated at 45 degrees (a diamond)
`BOX ,20,30, ,0`  Draws a box with the opposite corner coordinates taken from the position of the pixel cursor
`BOX ,20,30, , ,1`  As above, but the rectangle is filled.
`BOX ,-10,+10,100,100`  Draws a box with the first corner starting 10 pixels left and 10 pixels down from t he pixel cursor position
`BOX ,50;45,100;90`  Draws a box with the first corner starting 50 pixels away from the pixel cursor at an angle of 45 degrees, and the opposite corner 100 pixels away from the pixel cursor at an angle of 90 degrees

Abbreviation
B SHIFT+O
