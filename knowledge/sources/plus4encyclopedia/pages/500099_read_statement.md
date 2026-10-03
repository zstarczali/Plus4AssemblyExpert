# READ Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500099
- Category: Reference/Commodore BASIC V3.5

READ *variable list*

This statement is used to get information from [DATA statement](500069_data_statement.md)s into variables. The variables can be strings or numeric, so care must be taken to ensure that the item in the DATA statement is suitable for the variable.

READ statements normally get their data starting from the first DATA line in a program, and each successive READ statement gets its data from the next DATA item. If there are no more DATA lines, and a READ statement is encountered, an [?OUT OF DATA ERROR](500170_out_of_data_error.md) occurs. If DATA lines are to be re-read, or if READ statements should start from a specific line, see the [RESTORE statement](500101_restore_statement.md).

READ statements are often placed in [FOR/TO/STEP/NEXT statement](500075_for_to_step_next_statement.md) loops for large scale DATA reading.

Examples
`READ A,B$,C$`  This expects a numeric value first in the DATA statement, then the following values are placed into string variables.
`FOR A = 1 TO 10:READ B(A):NEXT`  Reads 10 numeric items from DATA statements, and each item is placed into successive elements of the B variable

Abbreviation
R SHIFT+E
