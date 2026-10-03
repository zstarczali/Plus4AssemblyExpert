# OPEN Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500089
- Category: Reference/Commodore BASIC V3.5

OPEN *file#*, *device#* [,*secondary address*] [,"*filename*,*type*,*mode*"]

The OPEN statement allows access to a peripheral device or to a tape or disk file.

The file number can be 0 to 255. Not all devices accept 0 as a file number. File numbers greater than 127 cause a line feed character to be sent after the carriage return at the end of a line, this is required by certain types of printers and RS-232 devices.

The device number identifies the device to be accessed. The default number is 1. The normal device numbers are as follows:
0: keyboard
1: tape
2: RS-232 port
3: screen
4-7: reserved for printers
8-11: reserved for disk drives

The usage of the secondary address depends on the device being accessed.
For the tape, 0: read from tape, 1: write to tape, 2: write to tape with END-OF-TAPE marker.
For printers, this is used to send commands. These vary between make and model of printer.
For disk drives, this indicates the channel being used.

The string following the secondary address may contain a command to a disk drive, or a filename on tape or disk. The *type* and *mode* components of the string are used for disk files only. (*Type*s are: PRG, SEQ, REL and USR; *mode*s are: READ and WRITE)

If an attempt is made to open a file that is already open, a [?FILE OPEN ERROR](500038_file_open_error.md) occurs.

Examples
`OPEN 1,0`  Opens the keyboard as a device
`OPEN 2,2,0,CHR$(22)+CHR$(5)`  Opens RS-232 port: 300 bps, 8 Databits, no parity, 1 Stopbit (=3008N1):
`OPEN 3,3`  Opens the screen as a device
`OPEN 4,4`  Opens a channel to use a printer
`OPEN 1,1,0,"TEST"`  Opens the tape for reading and searches for the file named TEST
`OPEN 15,8,15`  Opens the command channel on a disk drive
`OPEN 8,8,12,"TESTFILE,SEQ,WRITE"`  Creates a sequential disk file named TESTFILE for writing

Reading from RS-232 Port

Configuration of the Port:
`OPEN 2,2,0,CHR$(Control-Register)+CHR$ (Command-Register)`

Example:
300 bps, 8 Databits, 1 Stop-Bit, no parity (=3008nl):
`OPEN 2,2,0,CHR$(22)+CHR$(5)`
`GET #2,a$`
`PRINT A$`

Control-Register
Bit
4 3 2 1 0 Baudrate (bps)
---------------------------------------
1 0 0 0 0 -
1 0 0 0 1 50
1 0 0 1 0 75
1 0 0 1 1 110
1 0 1 0 0 134,5
1 0 1 0 1 150
1 0 1 1 0 300
1 0 1 1 1 600
1 1 0 0 0 1200
1 1 0 0 1 1800
1 1 0 1 0 2400
1 1 0 1 1 3600
1 1 1 0 0 4800
1 1 1 0 1 7200
1 1 1 1 0 9600
1 1 1 1 1 19200

Bit
6 5 Count of Databits
---------------------------------------
0 0 8
0 1 7
1 0 6
1 1 5

Bit
7 Count of Stop-Bits
---------------------------------------
0 1
1 2

Example: 300 bps, 8 Databits, 1 Stop-Bit
Binary 00010110 = 22

Command-Register
Bit
4 3 2 1 0 (always)
---------------------------------------
0 0 1 0 1 (=5 decimal)

Bit
7 6 5 Parity
---------------------------------------
0 0 0 no
0 0 1 odd
0 1 1 even
1 0 1 mark
1 1 1 space

Example:
no Parity
Binary 00000101 = 5

Abbreviation
O SHIFT+P
