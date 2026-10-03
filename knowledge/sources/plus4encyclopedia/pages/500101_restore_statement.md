# RESTORE Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500101
- Category: Reference/Commodore BASIC V3.5

RESTORE [*line#*]

When executed, the RESTORE statement resets the pointer to the next [DATA statement](500069_data_statement.md) in a program, allowing [READ statement](500099_read_statement.md)s to re-read DATA statements.

If a line number follows RESTORE, the pointer is set to that line. If there is no number, the pointer is reset to the start of the program. If the specified line number does not exist, an [?UNDEF'D STATEMENT ERROR](500174_undef_d_statement_error.md) occurs. If a negative number or a number greater than 65535 is used, an [?ILLEGAL QUANTITY ERROR](500171_illegal_quantity_error.md) occurs. If a string in double quotes is used, a [?TYPE MISMATCH ERROR](500177_type_mismatch_error.md) occurs.

The line number can also be specified with a variable or arithmetic expression. If a fraction is returned, the fraction component is ignored. If a string variable is used, a [?TYPE MISMATCH ERROR](500177_type_mismatch_error.md) occurs.

Examples
`RESTORE 200`  Resets pointer to line 200
`B=200:RESTORE B`  As above, but using a variable
`C=150:RESTORE C+50`  As above, but using variables + arithmetic

Abbreviation
RE SHIFT+S
