# Pixel Cursor

- Source: https://plus4world.powweb.com/plus4encyclopedia/500204
- Category: Programming/BASIC

When a high-resolution or multicolor graphic mode is active, the pixel cursor can be used to position objects drawn in the graphic screen area.

The various statements used to draw objects is the graphic area ([BOX statement](500061_box_statement.md), [CIRCLE statement](500064_circle_statement.md), [DRAW statement](500073_draw_statement.md), [PAINT statement](500090_paint_statement.md), [SSHAPE/GSHAPE statement](500108_sshape_gshape_statement.md)) can specify certain drawing positions using the location of the pixel cursor, or a position relative to the pixel cursor. The exact usage varies between the different graphic statements.

The pixel cursor is not shown on screen, but its position can be determined using the [RDOT function](500127_rdot_function.md).

The default X,Y location of the pixel cursor is 0,0 (top left of the screen). Whenever an object is drawn on the graphic screen, the pixel cursor is automatically relocated to the position of the last pixel rendered.

To relocate the pixel cursor without drawing an object, use the [LOCATE statement](500085_locate_statement.md).

If the clear flag is set when using the [GRAPHIC statement](500080_graphic_statement.md) to select a hi-res/multicolor mode, the pixel cursor coordinates are reset to 0,0. (This does not occur if the clear flag is set when selecting text-only mode)
