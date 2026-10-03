# GOTO Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500079
- Category: Reference/Commodore BASIC V3.5

GOTO *line#*

This statement can be entered as GOTO or GO TO.

When a GOTO statement is executed in a program, program execution jumps to the line number specified after the GOTO statement.

GOTO can also be used in direct mode to start a program from a specific line number, similar to the [RUN command](500057_run_command.md), except that variables are not cleared when using GOTO in this manner.

When used within an [IF/THEN/ELSE statement](500081_if_then_else_statement.md), the GOTO keyword may be optional, see the [IF/THEN/ELSE statement](500081_if_then_else_statement.md) for more information.

If a line number is not specified after a GOTO statement, it assumes line 0. If the specified line number does not exist in the program, an [?UNDEF'D STATEMENT ERROR](500174_undef_d_statement_error.md) occurs.

Examples
`10 PRINT "HELLO":GOTO 10`  The GOTO 10 causes line 10 to be repeated indefinitely until RUN/STOP is pressed
`GOTO 20`  Used in direct mode, starts program execution at line 20 with all variables left intact

Abbreviation
G SHIFT+O
