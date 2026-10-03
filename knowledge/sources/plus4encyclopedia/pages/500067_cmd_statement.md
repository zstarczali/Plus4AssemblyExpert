# CMD Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500067
- Category: Reference/Commodore BASIC V3.5

CMD *file#* [,*string*]

CMD sends the output which would normally go to the screen (from commands such as PRINT, LIST, but not POKEs into the screen) to another device, such as a printer, or a data file on tape or disk. The device or file must be opened first with the [OPEN statement](500089_open_statement.md), otherwise [?FILE NOT OPEN ERROR](500155_file_not_open_error.md) occurs.

The CMD statement must be followed by a file number, or a numeric variable containing the file number. This may be followed by a string or a string variable, the contents of which will be sent immediately to the target device.

Examples
`OPEN 1,4`  Opens device 4 (printer)
`CMD 1,"THIS IS MY PROGRAM"`  All screen output now goes to the printer, and the text "THIS IS MY PROGRAM" is printed
`LIST`  The listing goes to the printer, including the READY prompt at the end
`PRINT#1`  Output returns to the screen
`CLOSE 1`  Closes the file

Abbreviation
C SHIFT+M
