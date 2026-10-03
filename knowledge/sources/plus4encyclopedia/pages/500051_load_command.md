# LOAD Command

- Source: https://plus4world.powweb.com/plus4encyclopedia/500051
- Category: Reference/Commodore BASIC V3.5

LOAD ["*filename*"] [,*device#*[,*relocate flag*] ]

This command loads a program from tape or disk.

Simply entering LOAD will start searching for a program found on tape. When a program is found, the C= key may be pressed to load the program. Otherwise loading will commence automatically after a few seconds.?

If a program name is specified, the computer will search for and load the specified program. If other programs are found, the program name will be displayed briefly, then searching will continue.

To use the LOAD command with a disk drive, the device number must be specified (normally device 8), as well as a filename of at least 1 character. The filename "*" will load the first program on the disk. The filename "$" will load the directory or the disk, enter LIST to display it. (WARNING: Loading a directory using this method will destroy any BASIC programs in memory. To avoid this, use the [DIRECTORY](https://plus4world.powweb.com/kb.php?id=500044) command instead.)

The relocate flag is used to determine where in memory a program is loaded. A flag of 0 will load the program at the start of the BASIC program memory ($1000 by default), and a flag of 1 will load the program at the location it was originally saved.

Examples
`LOAD`  Searches for and loads the first program on tape
`LOAD"HELLO"`  Searches tape for a program called "HELLO", and then loads it if found
`LOAD A$`  Searches tape for a program with the name contained in the variable A$. A string variable must be used, or a [?TYPE MISMATCH ERROR](500177_type_mismatch_error.md) will occur. If the string variable is empty, then it will act as a normal LOAD if loading from tape, or a [?MISSING FILE NAME ERROR](500165_missing_file_name_error.md) will occur if loading from disk
`LOAD"HELLO",8`  Searches for and loads the program "HELLO" on disk
`LOAD"",1,1`  Searches for the first program on tape (device 1), then loads it into the memory location it was originally saved from
`LOAD"HELLO",8,1`  Searches for and loads the program "HELLO" from disk, into the memory location it was originally saved from

Abbreviations
L SHIFT+O
