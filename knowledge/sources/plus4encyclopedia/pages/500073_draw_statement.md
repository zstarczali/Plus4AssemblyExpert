# DRAW Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500073
- Category: Reference/Commodore BASIC V3.5

DRAW [*color source#*] [,*a1*,*b1*] [TO *a2*,*b2*...]

A graphics area must be defined with the [GRAPHIC statement](500080_graphic_statement.md) before using this statement, or a [?NO GRAPHICS AREA ERROR](500092_no_graphics_area_error.md) will occur.

To ensure the object has the same appearence in both hi-res and multicolor modes, see the [SCALE statement](500104_scale_statement.md).

This statement can be used to draw individual dots, lines and shapes.

The [color sources](500063_color_sources.md) are 0-3 (default 1). To change the colors, see the [COLOR statement](500068_color_statement.md). Multicolor sources can only be used when a multicolor mode is active.

a1 and b1 are the starting point coordinates in pixels. These can be expressed either as specific values (eg 160,100), values relative to the [pixel cursor](500204_pixel_cursor.md) coordinates (eg +50,-25), or a length and angle relative to the pixel cursor coordinates (eg 50;45 (where 50 is the length, and 45 is the angle, seperated by a semi-colon)). The default values for these are the pixel cursor coordinates.

If an endpoint is not specified, only a dot is drawn. To specify an endpoint for a line, the starting coordinates must be followed by TO, then followed by another pair of coordinates (which can be expressed in the same choice of format as the starting point coordinates). These can be followed by another TO, followed by yet another pair of coordinates to specify the endpoint a third line starting from the end of the previous line, and so on.

Examples
`DRAW 1 TO 160,100`  Draws a line from the [pixel cursor](500204_pixel_cursor.md) coordinates to the centre of the screen
`DRAW 1,20,20 TO 50,50`  Draws a diagonal line
`DRAW ,160,100 TO 100,100 TO 130,50 TO 160,100`  Draws a triangle
`DRAW ,-10,+10 TO 100,100`  Draws a line starting 10 pixels left and 10 pixels down from the pixel cursor position
`DRAW ,50;45 TO 100,100`  Draws a line starting 50 pixels away from the pixel cursor at an angle of 45 degrees

Abbreviation
D SHIFT+R
