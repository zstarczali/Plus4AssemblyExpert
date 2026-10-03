# VERIFY Command

- Source: https://plus4world.powweb.com/plus4encyclopedia/500060
- Category: Reference/Commodore BASIC V3.5

VERIFY "*filename*" [,*device#*] [,*relocate flag*]

Used to check the contents of memory against the contents of a file. Useful for checking for bad disks or tapes.

The filename can be "*". In this case it assumes "last used filename" (and not any filename like wildcard)

VERIFY without arguments will check the next program on tape against the one in memory.

If the contents of the file do not match those in memory, a [?VERIFY ERROR](500183_verify_error.md) indicates this.

Examples
`VERIFY`  Checks the next program on the tape
`VERIFY "HELLO"`  Searches for the program "HELLO" on tape, then checks against memory
`VERIFY A$`  Searches for the program name stored in A$, then checks against memory. A string variable must be used, or a [?TYPE MISMATCH ERROR](500177_type_mismatch_error.md) will occur. If the string variable is empty, then the next program is checked if checking from tape, or a [?MISSING FILE NAME ERROR](500165_missing_file_name_error.md) will occur if checking from disk
`VERIFY "HELLO",8,1`  Searches for "HELLO" on disk, then checks against the memory location it was originally saved from
`VERIFY "*",8`  Searches and verify the last used file

Bug
When using KERNAL ROM version 318004-03 in a 64K configuration, the VERIFY command cannot correctly verify memory locations over $7FFF when checking against tape, because the tape routines do not look at RAM under ROM. Disk operations are not affected. This bug also affects the [SAVE command](500058_save_command.md).

Abbreviation
V SHIFT+E

Credits
? + SVS
