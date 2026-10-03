# DIRECTORY Command

- Source: https://plus4world.powweb.com/plus4encyclopedia/500044
- Category: Reference/Commodore BASIC V3.5

DIRECTORY [D*drive#*] [,U*unit#*] [,"*filename*"]

Displays a disk directory on the screen. Press CTRL+S to pause the display (any key to restart) or hold the C= button to slow it down. The specified drive (8 by default) must be connected and turned on, otherwise a [?DEVICE NOT PRESENT ERROR](500056_device_not_present_error.md) will occur.

DIRECTORY cannot be used to print the directory on a printer. To do that (for device 8), use the following program (NOTE: this will destroy any BASIC program in memory!):
LOAD"$",8
OPEN4,4:CMD4:LIST
PRINT#4:CLOSE4

By default, the F3 key issues the DIRECTORY command. This corresponds to KEY 3.

Examples
`DIRECTORY`  Lists all files on disk
`DIRECTORY D0,U9,"WORK"`  Lists the file "WORK" on device 9, drive 0
`DIRECTORY "AB*"`  Lists all files starting with "AB", such as "ABOUT", "ABOVE" etc
`DIRECTORY "FILE?.BAK"`  The ? is a wildcard which matches any character in that position, which would match "FILE1.BAK", "FILE2.BAK", "FILE3.BAK" etc

Abbreviation
DI SHIFT+R
