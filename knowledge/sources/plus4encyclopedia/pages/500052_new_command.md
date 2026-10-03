# NEW Command

- Source: https://plus4world.powweb.com/plus4encyclopedia/500052
- Category: Reference/Commodore BASIC V3.5

NEW

This command erases the entire program in memory and removes any variables used. WARNING: Be careful when using this command.

NEW can be used within BASIC programs. When executed within a program, the program is erased and program execution stops.

Notes
The following BASIC line places two zeroes to the BASIC start address (pointed to by $2B/$2C). As long as no further BASIC lines are typed, and no variables are changed, the NEW command is reversible:
`POKE PEEK ( DEC("2B") ) + PEEK ( DEC("2C") ) * 256, 1 : RENUMBER`

Abbreviation
None
