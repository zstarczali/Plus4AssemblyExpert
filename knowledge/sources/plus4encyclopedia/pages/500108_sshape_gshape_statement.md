# SSHAPE/GSHAPE Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500108
- Category: Reference/Commodore BASIC V3.5

SSHAPE *string variable*,*a1*,*b1* [*a2*,*b2*]
GSHAPE *string variable* [, [*a*, *b*], *mode*]

A graphics area must be defined with the [GRAPHIC statement](500080_graphic_statement.md) before using either of these statements, or a [?NO GRAPHICS AREA ERROR](500092_no_graphics_area_error.md) will occur.

SSHAPE is used to save a rectangular area of a graphics screen. The data is stored in the string variable. GSHAPE is used to display saved areas, and has several different modes of displaying them.

When saving shapes, the word SSHAPE is followed by the string variable name, then followed by a1 and b1, which are the corner coordinates in pixels. These can be expressed either as specific values (eg 160,100), values relative to the [pixel cursor](500204_pixel_cursor.md) coordinates (eg +50,-25), or a length and angle relative to the pixel cursor coordinates (eg 50;45 (where 50 is the length, and 45 is the angle, seperated by a semi-colon)).

a2 and b2 are the second corner coordinates. These are the pixel cursor coordinates by default.

Because a string variable is limited to 255 characters, the size of the saved area is limited. The string size of the area to be saved can be calculated using the following formulas (with the [SCALE statement](500104_scale_statement.md) off):
Hi-res: `INT((ABS(*a1*-*a2*)+1)/8+.99)*(ABS(*b1*-*b2*)+1)+4`
Multicolor: `INT((ABS(*a1*-*a2*)+1)/4+.99)*(ABS(*b1*-*b2*)+1)+4`
If the area is too large, a [?STRING TOO LONG ERROR](500178_string_too_long_error.md) will occur.

Shape's image data is stored in the string variable in the following format:

| Data | Size (chars/bytes) | Description |
|---|---|---|
| ROW 0 | INT(WIDTH/8)+1 | Shape's 1st (top) pixel line from left to right. Array of bytes. |
| ROW 1 | INT(WIDTH/8)+1 | Shape's 2nd pixel line from left to right. Array of bytes. |
| ROW 2 | INT(WIDTH/8)+1 | Shape's 3rd pixel line from left to right. Array of bytes. |
| ... |  |  |
| ROW n | INT(WIDHT/8)+1 | Shape's last (bottom) pixel line from left to right. n = HEIGHT. Array of bytes. |
| WIDTH | 2 | Shape width in pixels minus 1. 16-bit (LOHI) value. |
| HEIGHT | 2 | Shape height in pixels minus 1. 16-bit (LOHI) value. |

To display a saved shape, the word GSHAPE is followed by the string variable which contains the shape. This may be followed by the a1 and b1 coordinates, which is the top left corner of where the shape will be drawn. The default values are the pixel cursor coordinates.

This is followed by the mode, which determines how the shape is displayed:
0: Place shape as is (default)
1: Place shape with inverted colors
2: OR shape with area
3: AND shape with area
4: XOR shape with area

Examples
`SSHAPE A$,10,10`  Saves shape area from specified corner to the pixel cursor corner
`SSHAPE A$,10,10,20,20`  Saves a fully specified area
`GSHAPE A$`  Displays shape with the top left corner at the pixel cursor coordinates
`GSHAPE A$,100,100`  Displays shape at a specified location
`GSHAPE A$,,1`  Displays color-inverted shape

BUG
There is a bug on the end-line saving or restoring. This causes that GSHAPE is not always able to redraw the exact shape of the source box.

Abbreviation
SSHAPE: S SHIFT+S
GSHAPE: G SHIFT+S

Credits
? +SVS
