# DSAVE Command

- Source: https://plus4world.powweb.com/plus4encyclopedia/500046
- Category: Reference/Commodore BASIC V3.5

DSAVE "*filename*" [,D*drive#*] [,U*unit#*]

Saves a BASIC program to disk. A program name is required (maximum of 16 characters).

By default, the F5 key displays the DSAVE command together with an opening double quote mark.

Examples
`DSAVE "BANKRECS"`  Saves "BANKRECS" to disk
`DSAVE "PROG3",D0,U9`  Saves "PROG3" to device 9
`DSAVE (A$)`  Saves the program with the filename contained in the variable A$. A string variable must be used, or a [?TYPE MISMATCH ERROR](500177_type_mismatch_error.md) will occur. If the string variable is empty, an [?ILLEGAL QUANTITY ERROR](500171_illegal_quantity_error.md) will occur

Abbreviation
D SHIFT+S
