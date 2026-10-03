# MID$ Function

- Source: https://plus4world.powweb.com/plus4encyclopedia/500142
- Category: Reference/Commodore BASIC V3.5

MID$(X$,S[,X])

This function returns string data.

This function returns a string taken from X$, containing X number of characters starting from the Sth character in X$. If X is not specified, all characters starting from the Sth character to the last character are returned.

The MID$ function can also be used to change parts of a string by being used as the left side of a [LET statement](500084_let_statement.md). When used in this way, the value of X (if present) is ignored, and the length of the string on the right-side of the LET statement must not exceed the length of X$ minus the value of S. If this happens, an [?ILLEGAL QUANTITY ERROR](500171_illegal_quantity_error.md) will occur.

Examples
`MID$("THE CAT IN THE HAT",5,3)`  Returns the string 'CAT'
`A$="THE DOG IN THE HAT": MID$(A$,5) = "CAT"`  Changes A$ to 'THE CAT IN THE HAT'

Abbreviation
M SHIFT+I
