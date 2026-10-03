# ?TYPE MISMATCH ERROR

- Source: https://plus4world.powweb.com/plus4encyclopedia/500177
- Category: Reference/BASIC Error Messages

This error occurs if a numeric value is used in place of a string, or vice-versa. The only exception is when using the [INPUT statement](500082_input_statement.md), where [?REDO FROM START](500190_redo_from_start.md) occurs instead.

Examples
`A = 2 + B$`  String and numeric variables cannot be directly combined in expressions
`A = "TEXT"`  A numeric variable cannot hold string data
`B$ = 123`  String variables do not hold actual numbers, they must be entered as text (within quotes)
`LOAD B`  A numeric variable cannot be used for a filename, only string variables are allowed

ERR$ error number
22
