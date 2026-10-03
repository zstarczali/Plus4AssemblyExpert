# POKE Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500091
- Category: Reference/Commodore BASIC V3.5

POKE *address*,*value*

The POKE statement is used to modify the value of any memory location in RAM, and is also used to modify I/O registers.

The address (in decimal format) is the memory location to be modified, from 0 to 65535. The value is the number (also in decimal format) to be placed in the memory location, from 0 to 255. These numbers can be expressed as variables or formulas.

Any numbers outside the ranges specified above will cause an [?ILLEGAL QUANTITY ERROR](500171_illegal_quantity_error.md).

To read the contents of memory locations, use the [PEEK function](500125_peek_function.md).

Examples
`POKE 28000,8`  Places the value 8 in memory location 28000
`POKE 8000+192,9*8`  Places the value 72 in memory location 8192
`POKE DEC("FF19"),DEC("32")`  Changes the border color to dark red, equivalent to COLOR 4, 3, 3

Abbreviation
P SHIFT+O

See Also
PEEK function
