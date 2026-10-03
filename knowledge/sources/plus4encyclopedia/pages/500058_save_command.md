# SAVE Command

- Source: https://plus4world.powweb.com/plus4encyclopedia/500058
- Category: Reference/Commodore BASIC V3.5

SAVE ["*filename*"[,*device#*[,*EOT flag*] ] ]

This command stores a program in memory onto a tape or disk. Simply entering SAVE will save the program currently in memory onto tape with a null filename. Entering SAVE followed by a filename within double quotes (maximum 16 characters) will save the program to tape with the specified filename.

If saving to disk, a filename is required, followed by the device number (normally device 8).

If saving to tape, the END-OF-TAPE (EOT) flag can be used. If the device is not a tape device (such as device 1), the flag is ignored. This flag has the following settings:
0: No action (default)
1: Save so that the relocate flag on the LOAD command is ignored, and the program always loads into the location it was saved from.
2: Saves the program, and records an END-OF-TAPE marker afterward. If this marker is read when loading from tape, a [?DEVICE NOT PRESENT ERROR](500056_device_not_present_error.md) occurs.
3: Saves in non-relocatable format (1) and writes the EOT marker (2).

Examples
`SAVE`  Saves program onto tape without a name
`SAVE"MYPROG"`  Saves program onto tape with the name "MYPROG"
`SAVE A$`  Saves onto tape with the name stored in A$. A string variable must be used, or a [?TYPE MISMATCH ERROR](500177_type_mismatch_error.md) will occur. If the string variable is empty, then the program is saved without a filename if saving to tape, or a [?MISSING FILE NAME ERROR](500165_missing_file_name_error.md) will occur if saving to disk
`SAVE"MYPROG",8`  Saves to disk with the filename "MYPROG"
`SAVE"MYPROG",1,1`  Saves the program to tape so that the relocate flag in the LOAD command has no effect
`SAVE"MYPROG",1,3`  As above, but adds an EOT marker

Bug
When using KERNAL ROM version 318004-03 in a 64K configuration, the SAVE command contains a bug when saving data from memory locations over $7FFF to tape, because the tape routines do not look at RAM under ROM. Disk operations are not affected. This bug also affects the [VERIFY command](500060_verify_command.md).

Abbreviation
S SHIFT+A

See Also
DSAVE
