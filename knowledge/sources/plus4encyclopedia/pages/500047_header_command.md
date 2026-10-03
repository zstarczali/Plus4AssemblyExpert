# HEADER Command

- Source: https://plus4world.powweb.com/plus4encyclopedia/500047
- Category: Reference/Commodore BASIC V3.5

HEADER "*diskname*" [I*id#*] ,D*drive#* [,U*unit#*]

Formats a disk. A disk name is required (maximum of 16 characters). Specifying an ID number (any 2 characters) performs a full format, otherwise a quick format (clearing the directory) is performed, and the disk's previous ID number retained. A quick format can only be done only on a disk that was previously fully formatted.

WARNING: This command will destroy all files on disk. When entering this command, an ARE YOU SURE? prompt will appear. Entering Y will proceed with the format, any other key will quit.

Examples
`HEADER "MYDISK",D0`  Performs a quick format, and labels the disk "MYDISK"
`HEADER "MYDISK",I1A,D0,U9`  Performs a full format on the disk in device 9, and gives the disk an ID number of 1A

Abbreviation
HE SHIFT+A
