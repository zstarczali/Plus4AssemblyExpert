# FOR/TO/STEP/NEXT Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500075
- Category: Reference/Commodore BASIC V3.5

FOR *loop variable* = *start value* TO *end value* [STEP *increment*] : *statements* : NEXT [*loop variable* [,*loop variable*... ] ]

The FOR and NEXT statements are used to set up a loop that repeats a set number of times.

FOR must be followed by a numeric variable, which is the loop variable. This is followed by the start value, which is placed into the loop variable, then the word TO, followed by the end value.

This may be followed by STEP, which determines the amount that is added/subtracted to the loop variable. This may be either greater than 1 (1 is the default value), a fraction, or (in the case of the end value being lower than the start value) a negative number. NOTE: If the end value is lower than the start value, a negative STEP value (such as -1) must be specified, otherwise the statements within the FOR/NEXT loop will only be executed once.

The NEXT statement adds 1 to the loop variable (or adds/subtracts the amount specified after STEP), and returns execution to the FOR statement. If the value of the loop variable exceeds the end value of the FOR statement, the loop ends and program execution continues after the NEXT statement.

The NEXT statement may be followed by the name of the loop variable, or a list of loop variables separated by commas, to specify the loop to be restarted, this is normally used with nested FOR/NEXT loops. When using multiple loop variable names in a NEXT statement, if the first loop variable has finished, the following loop variable is looped instead, and so on. Without a loop variable name, NEXT statement returns to the last encountered FOR statement (this mode allows a faster exec).

If a program encounters a NEXT statement without a FOR loop in operation, a [?NEXT WITHOUT FOR ERROR](500167_next_without_for_error.md) occurs.

Warnings
-> The control variable cannot be integer type, only FP is allowed (ex.: I is OK, I% causes error)
-> The step value can be negative.
-> A technically possible zero step value causes an infinite loop :)

Examples
`FOR A = 1 TO 5:PRINT A:NEXT`  This prints the numbers 1, 2, 3, 4 and 5
`FOR A = 0 TO 6 STEP 2:PRINT A:NEXT`  This prints the numbers 0, 2, 4 and 6
`FOR A = 1 TO 5:FOR B = 5 TO 1 STEP -1:C(A,B) = 1:NEXT B:NEXT A`  A nested loop
`FOR A = 1 TO 5:FOR B = 5 TO 1 STEP -1:C(A,B) = 1:NEXT B,A`  As above

Abbreviations
FOR: F SHIFT+O
STEP: ST SHIFT+E
NEXT: N SHIFT+E

Credits
? + SVS
