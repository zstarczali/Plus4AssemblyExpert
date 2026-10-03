# ?ILLEGAL DIRECT ERROR

- Source: https://plus4world.powweb.com/plus4encyclopedia/500160
- Category: Reference/BASIC Error Messages

This error occurs if a statement (for example: [GETKEY statement](500159_getkey_statement.md)) is used in direct mode. While most statements work in both direct mode and program mode, some of them must be inside a program.

Example
`GETKEY A$`  issuing the command in direct mode will cause this error.

ERR$ error number
21

See Also
?DIRECT MODE ONLY ERROR
