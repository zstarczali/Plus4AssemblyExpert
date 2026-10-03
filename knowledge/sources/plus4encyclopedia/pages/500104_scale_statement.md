# SCALE Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500104
- Category: Reference/Commodore BASIC V3.5

SCALE <*1/0*>

Normally, statements which draw objects onto a graphics screen use coordinates which are based on the graphic screen resolution (320 x 200 on hi-res, 160 x 200 on multicolor). This causes shapes to appear differently depending on whether hi-res or multicolor mode is selected.

The SCALE statement replaces this coordinate system with a scale of 0 to 1023 in both X and Y axis, in both hi-res and multicolor mode.

To convert normal coordinates to scaled coordinates, the following conversions can be used:
Hi-res X axis: coordinate x 3.2
Multicolor X axis: coordinate x 6.4
Hi-res/Multicolor Y axis: coordinate x 5.12

Examples
`SCALE 1`  Turns scaling on
`SCALE 0`  Turns scaling off

Abbreviation
SC SHIFT+A
