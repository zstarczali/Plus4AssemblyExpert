# INSTR Function

- Source: https://plus4world.powweb.com/plus4encyclopedia/500121
- Category: Reference/Commodore BASIC V3.5

INSTR(*main string*,*search string* [,*start position*])

This function returns a numeric value.

This function searches a string for the contents of another string. When calling this function, the main string is the string to be searched, followed by the string to search for. The start position is a numeric value indicating from which character in the main string to start searching for. If the start position is not specified, searching starts from the beginning of the string. The start position is normally used to find multiple instances of the string.

If the string is found, the function returns the position of the first found character in the main string. If it is not found, the value returned is 0.

Examples
`INSTR("THE CAT IN THE HAT","CAT")`  The value returned is 5, as 'CAT' starts at the 5th character
`INSTR("THE CAT IN THE HAT","THE",4)`  The value returned is 12, as the start position is after the first instance of 'THE'

Abbreviation
IN SHIFT+S
