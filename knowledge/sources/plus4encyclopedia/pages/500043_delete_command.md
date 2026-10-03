# DELETE Command

- Source: https://plus4world.powweb.com/plus4encyclopedia/500043
- Category: Reference/Commodore BASIC V3.5

DELETE [*first line#*] [- *last line#*]

Deletes BASIC lines. Used in direct mode only. If used in a BASIC program, [?DIRECT MODE ONLY ERROR](500161_direct_mode_only_error.md) occurs. Use with caution, deleted lines cannot be recovered.

Examples
`DELETE 75`  Deletes line 75
`DELETE 10-50`  Deletes all lines from 10 to 50 inclusive
`DELETE -50`  Deletes all lines from the start of the program up to and including line 50
`DELETE 75-`  Deletes all lines from 75 on to the end of the program

Abbreviation
DE SHIFT+L
