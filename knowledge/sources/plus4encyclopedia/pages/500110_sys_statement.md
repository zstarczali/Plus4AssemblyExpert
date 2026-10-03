# SYS Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500110
- Category: Reference/Commodore BASIC V3.5

SYS *address*

The SYS statement starts executing a machine language program at the specified address (in decimal format). If the BASIC program is to continue, an RTS instruction (outside of a JSR subroutine) must be executed in the machine language program.

This is similar to the [USR function](500135_usr_function.md), but the starting point is directly specified by the SYS statement, and no data is directly transferred between the machine language program and the BASIC program.

Examples
`SYS 4112`  Starts machine language program execution at memory location 4112 ($1010)

Abbreviation
S SHIFT+Y
