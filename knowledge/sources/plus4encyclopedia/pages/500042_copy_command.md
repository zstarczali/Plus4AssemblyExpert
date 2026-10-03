# COPY Command

- Source: https://plus4world.powweb.com/plus4encyclopedia/500042
- Category: Reference/Commodore BASIC V3.5

COPY [D*drive#*,] "*source file*" TO [D*drive#*,] "*other file*" [,ON U*unit#*]

Copies a file from one disk to another on a dual drive only, or creates a copy of a file on the same disk with a different filename.

Examples
`COPY D0,"STUFF" TO D1,"STUFF"`  Copies "STUFF" from drive 0 to drive 1
`COPY D0,"TEST" TO D1,"TEST.PROG"`  Copies "TEST" from drive 0 and saves it as "TEST.PROG" on drive 1
`COPY D0 TO D1`  Copies all files from drive 0 to drive 1
`COPY "WORK.PROG" TO "BACKUP"`  Copies "WORK.PROG" and saves the copy as "BACKUP" on the same disk

Abbreviation
CO SHIFT+P
