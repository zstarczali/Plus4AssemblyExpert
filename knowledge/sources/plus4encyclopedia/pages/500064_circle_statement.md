# CIRCLE Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500064
- Category: Reference/Commodore BASIC V3.5

CIRCLE [*cs*], [*a*,*b*], *xr*[, [*yr*] [, [*sa*] [, [*ea*] [, [*inc*] [,*angle*] ] ] ] ]

A graphics area must be defined with the [GRAPHIC statement](500080_graphic_statement.md) before using this statement, or a [?NO GRAPHICS AREA ERROR](500092_no_graphics_area_error.md) will occur.

To ensure the object has the same appearance in both hi-res and multicolor modes, see the [SCALE statement](500104_scale_statement.md).

The CIRCLE statement, in addition to circles, can also draw ellipses, arcs, octagons, triangles etc.

The [color sources](500063_color_sources.md) (cs) are 0-3 (default 1). To change the colors, see the [COLOR statement](500068_color_statement.md). Multicolor sources can only be used when a multicolor mode is active.

a and b are the centre coordinates in pixels. These can be expressed either as specific values (eg 160,100), values relative to the [pixel cursor](500204_pixel_cursor.md) coordinates (eg +50,-25), or a length and angle relative to the pixel cursor coordinates (eg 50;45 (where 50 is the length, and 45 is the angle, separated by a semi-colon)). The default values are the pixel cursor coordinates.

xr is the X radius, measured horizontally from the centre in pixels; and yr is the Y radius, measured vertically from the centre in pixels. If yr is not specified, it is the same as xr.

sa is the starting arc angle, and ea is the ending arc angle. By default, these are 0 and 359 respectively, allowing for a complete shape to be formed. These values can be changed so that a shape is only partially drawn.

The inc value specifies the clockwise rotation of the shape in degrees. Default is 0.

Angle specifies the degrees between segments. Default is 2.

NOTE: As PAL and NTSC TV systems have different vertical display resolutions, adjustments may be needed to create a perfect circle on different types of display.

Examples
`CIRCLE 1,160,100,50,50`  Draws a circle in the centre of the screen
`CIRCLE ,160,100,50,10`  Draws an ellipse
`CIRCLE ,160,100,50,10, , ,45`  Draws an ellipse rotated at 45 degrees
`CIRCLE ,160,100,40,40, , , ,120`  Draws a triangle
`CIRCLE ,-10,+10,50,50`  Draws a circle with the centre 10 pixels left and 10 pixels down from the pixel cursor position
`CIRCLE ,50;45,50,50`  Draws a circle with the centre 50 pixels away from the pixel cursor at an angle of 45 degrees

BUG
Although yr is a 16 bit number, If yr > 255 then only the low-order byte is stored and used in drawing the circle, arc or other shape. There is a workaround for circles and circular arcs, if yr is not entered then it will be set equal to xr and used as a 16 bit number.

Abbreviation
C SHIFT+I
