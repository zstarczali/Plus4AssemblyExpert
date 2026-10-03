# DLOAD Command

- Source: https://plus4world.powweb.com/plus4encyclopedia/500045
- Category: Reference/Commodore BASIC V3.5

DLOAD "*filename*" [,D*drive#*] [,U*unit#*]

Loads a program from disk into the start of the BASIC memory area.

DLOAD can only load into the start of BASIC memory ($1000 by default). If a program was originally saved from a different area in memory, DLOAD cannot load the program into its original location. The [LOAD](https://plus4world.powweb.com/kb.php?id=500051) command with the relocate flag must be used instead.

By default, the F2 key displays the DLOAD command together with an opening quotation mark. This corresponds to KEY 2. The SHIFT + RUN/STOP key combination issues a DLOAD"* and a RUN command.

Wildcards are valid. One may use the "?" character to allow *any character in that location of the filename*, or the "*" to allow *any characters after the one(s) specified*.

It should be noted here that Commodore DOS only allows for filename lengths of 16 characters. Specifying a longer filename (such as "START LOOKING INSIDE", 20 characters including spaces) would generate a ?FILE NOT FOUND error.

Examples
`DLOAD "BANKRECS"`  Searches for and loads "BANKRECS"
`DLOAD "PROG3",D0,U9`  Loads "PROG3" from device 9
`DLOAD (A$)`  Loads a program with the filename contained in the variable A$. A string variable must be used, or a [?TYPE MISMATCH ERROR](500177_type_mismatch_error.md) will occur. If the string variable is empty, an [?ILLEGAL QUANTITY ERROR](500171_illegal_quantity_error.md) will occur
`DLOAD "STAR?"`  Loads the first file in the directory that is 5 characters long and starts with "STAR", such as "START", "STARA", or "STAR9"
`DLOAD "ST?RT"`  Loads the first file in the directory that is 5 characters long, starting with "ST", and ending with "RT", such as "START", "ST-RT", or "ST5RT"
`DLOAD "STAR*"`  Loads the first file in the directory that is 5 or more characters long and starts with "STAR", such as "START", "STARTHERE", or "START ME UP"
`DLOAD "ST?R*"`  Combining the wildcards. This example would load the first file found that starts with "ST", then any character, then an "R", than anything afterward, such as "ST-RING", "STRRUS", or "STARS IN SKY"

Abbreviation
D SHIFT+L

See Also
LOAD
