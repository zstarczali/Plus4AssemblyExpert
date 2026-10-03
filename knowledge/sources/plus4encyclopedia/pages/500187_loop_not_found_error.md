# ?LOOP NOT FOUND ERROR

- Source: https://plus4world.powweb.com/plus4encyclopedia/500187
- Category: Reference/BASIC Error Messages

This error occurs when an EXIT statement is encountered within a DO loop, and there is no LOOP statement in the program lines below it.

Also see the [DO/LOOP/WHILE/UNTIL/EXIT statement](500072_do_loop_while_until_exit_statement.md).

Example
`10 DO:PRINT"TEST"
20 EXIT`  The LOOP statement signals the end of the DO loop. Without it, program execution cannot continue after the EXIT statement

ERR$ error number
32
