# ON Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500088
- Category: Reference/Commodore BASIC V3.5

ON *expression* <**GOTO/GOSUB> *line#1* [,*line#2* [,*line#3*... ] ]

The ON statement is a variation of the [IF/THEN/ELSE statement](500081_if_then_else_statement.md), which is used in combination with the [GOTO statement](500079_goto_statement.md) and the [GOSUB statement](500078_gosub_statement.md).

The word ON is followed by an expression which must return an integer value. If a fraction is returned, the fraction component is ignored, using the integer value instead (without rounding). If a string is returned, a [?TYPE MISMATCH ERROR](500177_type_mismatch_error.md) occurs. If a negative value is returned, an [?ILLEGAL QUANTITY ERROR](500171_illegal_quantity_error.md) occurs.

Following the expression is a GOTO or GOSUB statement with one or more line numbers seperated by commas. If the number returned by the expression is 1, the first line number in the list is executed. If it is 2, the second line number in the list is executed, and so on. If the number is 0, or is larger than the number of line numbers in the list, program execution continues after the ON statement. If GOSUB is used, program execution continues after the ON statement when a [RETURN statement](500102_return_statement.md) is encountered.

Examples
`ON X GOTO 20,30,40,50`  If the value of X is 1, 2, 3 or 4, program execution jumps to line 20,30,40 and 50 respectively. If X is 0 or higher than the number of specified lines, program execution continues after the ON statement.
`ON X+2 GOSUB 300,400,500,600`

Abbreviation
None
