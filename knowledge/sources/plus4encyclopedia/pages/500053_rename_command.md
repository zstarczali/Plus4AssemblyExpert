# RENAME Command

- Source: https://plus4world.powweb.com/plus4encyclopedia/500053
- Category: Reference/Commodore BASIC V3.5

RENAME [D*drive#*,] "*old name*" TO "*new name*" [,U*unit#*]

Renames a file on disk. As long as the two names are supplied, this command will never cause an error, not even [?DEVICE NOT PRESENT ERROR](500056_device_not_present_error.md) if there's no drive connected. If the rename command fails because the old filename does not exist, the DS$ will return "62, FILE NOT FOUND, 00, 00". Wildcards in the filenames are not valid. If a wildcard is used, DS$ will return "30, SYNTAX ERROR, 00, 00".

Examples
`RENAME "TEST" TO "FINALTEST"`  Changes the name of the file "TEST" to "FINALTEST"
`RENAME D0,"ALPHA" TO "BETA",U9`  Changes "ALPHA" to "BETA" on device 9

Abbreviation
RE SHIFT+N
