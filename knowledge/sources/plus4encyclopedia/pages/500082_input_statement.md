# INPUT Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500082
- Category: Reference/Commodore BASIC V3.5

INPUT [*prompt string*;] *variable list*

The INPUT statement allows the computer to ask for data, which is entered via the keyboard.

INPUT is followed by a one or more variable names seperated by commas. If an input prompt is required, it may be included within double quotes before the variable list, and seperated from the variable list with a semi-colon. NOTE: The prompt string cannot be substituted with a string variable (eg INPUT A$;B$ is not allowed).

When executed, the prompt (if specified) appears, followed by a question mark. Data may then be typed in and entered.

If more than one variable is specified, the data for each variable may be seperated by commas on a single line (eg with INPUT A$,B$,C$:, the data may be entered as YES,NO,MAYBE (where YES goes into A$, NO goes into B$, and MAYBE goes into C$)). If there are insufficient commas for all the variables, there will be additional prompts (with a double question mark) until data is entered for all variables. If there are more commas than needed, an [?EXTRA IGNORED](500191_extra_ignored.md) error appears, and the data following the first excess comma is not used. Therefore, comma characters cannot be entered into variables using the INPUT statement.

Colon characters also cannot be entered into variables. In all cases, if a colon is entered at an INPUT prompt, only the characters (and seperator commas) preceeding the colon are accepted. It will also cause an ?EXTRA IGNORED error if entered in a prompt for a single variable, or (when entering for multiple variables) the last variable.

If the data entered is unsuitable for the variable (eg a string for a numeric variable), a [?REDO FROM START](500190_redo_from_start.md) error occurs, and the computer will display the prompt again, starting with the first variable.

If no data is entered for a variable, that variable's contents are unchanged.

The maximum length of the string supplied to a single INPUT prompt is 88 characters.

This statement can only be used within a program. If it is used in direct mode, an [?ILLEGAL DIRECT ERROR](500160_illegal_direct_error.md) will occur.

Examples
`INPUT A$`  Displays a question mark, and awaits string data
`INPUT B`  Awaits numeric data. If non-numeric data is entered, a ?REDO FROM START error occurs, and the prompt is displayed again
`INPUT "WHAT IS YOUR NAME";A$`  Displays WHAT IS YOUR NAME? (the question mark is added automatically) and awaits string data
`INPUT A$,B,C%`  Prompts and awaits data for multiple variables of different types

Abbreviation
None
