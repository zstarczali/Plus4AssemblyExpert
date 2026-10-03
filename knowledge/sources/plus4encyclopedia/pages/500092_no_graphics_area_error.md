# ?NO GRAPHICS AREA ERROR

- Source: https://plus4world.powweb.com/plus4encyclopedia/500092
- Category: Reference/BASIC Error Messages

This error message occurs if any graphic statement (example: [CIRCLE statement](500064_circle_statement.md), [BOX statement](500061_box_statement.md), etc.) is issued without allocating the graphics area first. Issuing a GRAPHIC 1, 1 statement for example allocates the graphics area.

Example
`GRAPHIC CLR:CIRCLE ,1,1`  will cause ?NO GRAPHICS AREA ERROR

ERR$ error number
35
