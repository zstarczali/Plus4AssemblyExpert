# ?NEXT WITHOUT FOR ERROR

- Source: https://plus4world.powweb.com/plus4encyclopedia/500167
- Category: Reference/BASIC Error Messages

A NEXT statement was executed outside of an appropriate FOR loop. This can occur when there is no FOR loops in operation, or a variable name was specified in the NEXT statement which does not correspond to a FOR loop currently in operation.

Example
`10 FOR A = 1 TO 10:PRINT"HI"`
`20 NEXT A,B`  Causes the error, as there is no FOR B loop in operation

ERR$ error number
10
