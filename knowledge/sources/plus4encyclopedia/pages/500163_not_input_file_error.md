# ?NOT INPUT FILE ERROR

- Source: https://plus4world.powweb.com/plus4encyclopedia/500163
- Category: Reference/BASIC Error Messages

This occurs when a [GET# statement](500077_get_statement.md) or [INPUT# statement](500083_input_statement.md) is used to input data from a file opened with the [OPEN statement](500089_open_statement.md) as an output file.

Example
`10 OPEN 1,1,1,"TEST"`  Opens file 1 on tape as an output (write) file
`20 GET# 1,A$`  Causes the error by attempting to read from a file specified for writing

ERR$ error number
6

See Also
?NOT OUTPUT FILE ERROR
