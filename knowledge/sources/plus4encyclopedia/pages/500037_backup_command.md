# BACKUP Command

- Source: https://plus4world.powweb.com/plus4encyclopedia/500037
- Category: Reference/Commodore BASIC V3.5

BACKUP D*drive#* TO D*drive#* [, ON U*unit#*]

Copies all files from one disk to another using a dual disk drive. Automatically HEADERs the destination disk.**This command requires a dual-drive unit such as an MSD SD-2**, and will not function on a single-unit drive such as a 1541, 1551, or 1571.

Examples
`BACKUP D0 TO D1`  Copies all files from drive 0 to drive 1
`BACKUP D0 TO D1, ON U9`  Copies from drive 0 to drive 1 on device 9

Abbreviation
B SHIFT+A
