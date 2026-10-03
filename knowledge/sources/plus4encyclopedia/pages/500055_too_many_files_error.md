# ?TOO MANY FILES ERROR

- Source: https://plus4world.powweb.com/plus4encyclopedia/500055
- Category: Reference/BASIC Error Messages

At any give time only 10 files can be open. This error occurs when you try to open a file after 10 are already open.

Example
`0 FOR I = 1 TO 11:OPEN I,8:NEXT I`  Running this code will cause ?TOO MANY FILES ERROR. Note if you replace 11 to 10 in the FOR loop, the program will execute fine.

ERR$ error number
1
