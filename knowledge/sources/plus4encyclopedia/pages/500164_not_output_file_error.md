# ?NOT OUTPUT FILE ERROR

- Source: https://plus4world.powweb.com/plus4encyclopedia/500164
- Category: Reference/BASIC Error Messages

This occurs when a [PRINT# statement](500095_print_statement.md) or [CMD statement](500067_cmd_statement.md) is used to output data to a file opened with the [OPEN statement](500089_open_statement.md) as an input file.

Example
`10 OPEN 1,1,0,"TEST"`  Opens file 1 on tape as an input (read) file
`20 CMD 1,"HELLO"`  Causes the error by attempting to write to a file specified for reading

ERR$ error number
7

See Also
?NOT INPUT FILE ERROR
