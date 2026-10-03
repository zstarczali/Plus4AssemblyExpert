# KEY Command

- Source: https://plus4world.powweb.com/plus4encyclopedia/500049
- Category: Reference/Commodore BASIC V3.5

KEY [*key#*,*string*]

The KEY command allows for redefining the actions of the 8 function keys. The HELP key is defined under KEY 8.

The KEY command without parameters displays the current definitions of the function keys.

To define special characters, use CHR$ codes (such as CHR$(13) for RETURN, or CHR$(34) for a double quote mark).

The total combined length of all KEY definitions cannot exceed 128 characters. If you try to define a KEY which would exceed this, [?OUT OF MEMORY ERROR](500173_out_of_memory_error.md) will occur. Try this example program:
`10 FOR I = 1 TO 8 : KEY I, "" : NEXT I : REM CLEAR ALL KEY DEFINITIONS
20 FOR I = 1 TO 129 : A$ = A$ + "." : NEXT I : REM BUILD A 129 CHARACTER LONG STRING
30 KEY 1, A$`
Line 30 will display an error. NB: if you change 129 to 128, the program will work.

Examples
`KEY`  Displays current KEY definitions
`KEY 1,""`  'Disable' F1 key, when pressed, nothing will happen.
`KEY 2,"GRAPHIC 0"+CHR$(13)+"LIST"+CHR$(13)`  Redefines F2 so that when pressed, causes the computer to select text mode and list the program in memory

Notes
The KEY data is stored from $055F (1375 decimal) in the memory. The first 8 bytes are key string lengths, followed by the strings.

Abbreviation
K SHIFT+E
