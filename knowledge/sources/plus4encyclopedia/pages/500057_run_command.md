# RUN Command

- Source: https://plus4world.powweb.com/plus4encyclopedia/500057
- Category: Reference/Commodore BASIC V3.5

RUN [*line#*]

The RUN command clears all variables and starts execution of a program, normally starting at the first line. If a line number is specified, the program starts at that line. If the specified line number does not exist, an [?UNDEF'D STATEMENT ERROR](500174_undef_d_statement_error.md) occurs.

RUN can also be used within a BASIC program to restart the program (all variables will be erased)

By default, the F6 (SHIFT+F3) key issues the RUN command.

Examples
`RUN`  Clears variables and starts program from the first line number
`RUN 100`  Clears variables and starts program from line 100

Machine Language
To perform the equivalent of the RUN command, use this code:
`JSR $8BBE
JMP $8BDC`

- To catch the RUN command in an emulator (e.g. when a program is auto-loaded from a TAP file), set a breakpoint to `$8BDC`.
- Difference between `RUN 0` and `GOTO 0` is that GOTO does not erase the variables in memory.

Abbreviation
R SHIFT+U
