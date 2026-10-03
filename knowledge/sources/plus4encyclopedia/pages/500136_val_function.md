# VAL Function

- Source: https://plus4world.powweb.com/plus4encyclopedia/500136
- Category: Reference/Commodore BASIC V3.5

VAL(X$)

This function returns a numeric value.

This function converts strings containing numeric characters into numeric values. It is the opposite of the [STR$ function](500144_str_function.md).

It can also convert strings which represent numbers in scientific notation.

If there are any illegal characters in the string, only the portion of the string from the left up to the first illegal character is converted.

Examples
`VAL("123.456")`  Returns the number 123.456
`VAL("3E03")`  Returns the number 3000
`VAL("12A13B")`  Returns the number 12

Abbreviation
V SHIFT+A
