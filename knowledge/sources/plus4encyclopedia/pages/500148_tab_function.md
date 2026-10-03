# TAB Function

- Source: https://plus4world.powweb.com/plus4encyclopedia/500148
- Category: Reference/Commodore BASIC V3.5

TAB(X)

This function is used by the [PRINT statement](500094_print_statement.md) to move cursor to position (x) by printing how many [Cursor-right] are needed, to achieve the position x in the current text screen line. X can have a value from 0-255, then cursor could perform a newline is needed.
If output is a printer, then the TAB(x) works like SPC(X).

This is similar to the [SPC function](500147_spc_function.md), but only counts spaces from the left side of the screen.

The TAB function cannot be used as part of a variable expression. Otherwise a [?SYNTAX ERROR](500168_syntax_error.md) will occur.

Abbreviation
T SHIFT+A

Credits
?+SVS
