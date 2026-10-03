# PAINT Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500090
- Category: Reference/Commodore BASIC V3.5

PAINT [*color source#*] [,[*a*,*b*] [,*mode*] ]

A graphics area must be defined with the [GRAPHIC statement](500080_graphic_statement.md) before using this statement, or a [?NO GRAPHICS AREA ERROR](500092_no_graphics_area_error.md) will occur.

The PAINT statement is used to fill an area with color.

The [color sources](500063_color_sources.md) are 0-3 (default 1). To change the colors, see the [COLOR statement](500068_color_statement.md). Multicolor sources can only be used when a multicolor mode is active.

a and b are the starting point coordinates in pixels. These can be expressed either as specific values (eg 160,100), values relative to the [pixel cursor](500204_pixel_cursor.md) coordinates (eg +50,-25), or a length and angle relative to the pixel cursor coordinates (eg 50;45 (where 50 is the length, and 45 is the angle, seperated by a semi-colon)). The default values for these are the pixel cursor coordinates.

The mode flag determines the boundary type for the fill operation. If it is 0, the boundary will be of the same color as the selected color source. If it is 1, the boundary will be any non-background color, regardless of the color source.

NOTE: If the starting point is already the same color as the color source (or any non-background color if mode 1 is used), there is no action taken.

Examples
`10 CIRCLE 1,80,100,50,50`  Draws outline of a circle
`20 PAINT 1,80,100`  Fills circle with the same color as the outline
*or*
`20 PAINT 2,80,100,1`  Fills circle with a different color than the outline (in multicolor graphics mode)
`PAINT ,-10,+10`  Fills area starting 10 pixels left and 10 pixels down from the pixel cursor position
`PAINT ,50;45`  Fills area starting 50 pixels away from the pixel cursor at an angle of 45 degrees

Abbreviation
P SHIFT+A
