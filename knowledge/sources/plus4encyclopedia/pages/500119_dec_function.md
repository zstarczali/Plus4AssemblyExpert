# DEC Function

- Source: https://plus4world.powweb.com/plus4encyclopedia/500119
- Category: Reference/Commodore BASIC V3.5

DEC(*hexidecimal string*)

This function returns a numeric value.

This function returns the DECimal value of a hexidecimal string, which must be between $0-$FFFF (0-65535). This is the opposite of the [HEX$ function](500139_hex_function.md).

If the hexidecimal number is outside this range, or if the string contains non-hexidecimal characters, an [?ILLEGAL QUANTITY ERROR](500171_illegal_quantity_error.md) occurs.

Abbreviation
None
