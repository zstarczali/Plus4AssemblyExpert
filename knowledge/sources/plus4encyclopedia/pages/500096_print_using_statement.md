# PRINT USING Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500096
- Category: Reference/Commodore BASIC V3.5

PRINT[# *file#*,] USING *format list*;*print list*

This allows any item that is printed on the screen ([PRINT statement](500094_print_statement.md)) or other device/file ([PRINT# statement](500095_print_statement.md)) to be displayed in a specified format.

The word PRINT (followed by # and a file number if printing to a device) is followed by the word USING, followed by the specified format list, which can be within double quotes, or as a string variable.

The specified format list is composed of special symbols, which are explained below:
# : Reserves a space in the output field for any one character. Use as many as required. If the number of #s is lower than the number of characters to be printed, different results occur: if the item is numeric, *s are printed instead of numbers; if the item is a string, it is truncated at the bounds of the field. Truncation occurs on the right.
+ : Places a plus sign next to the printed number. Can be either at the beginning or end of the number (but not both, or a [?SYNTAX ERROR](500168_syntax_error.md) occurs). If the numeric value to be printed is negative, a minus sign is displayed instead.
- : Places a minus sign next to the printed number. Can be either at the beginning or end of the number (but not both, or a [?SYNTAX ERROR](500168_syntax_error.md) occurs). If the numeric value to be printed is positive, no sign is displayed.
. : Specifies the decimal point position in the printed number. Only one can be specified (or a [?SYNTAX ERROR](500168_syntax_error.md) occurs).
, : Places a comma in numeric fields. The position of the comma in the format list indicates where the comma appears in the printed number. A comma is only printed if it is within the printed number.
$ : Prints a dollar (currency) sign. If the sign is to appear right next to the number, place a # before the $ (NOTE: the # before the $ will add an extra character space). Otherwise, it will appear at the boundary of the format field. If a plus or minus sign is to be displayed at the start of the printed number, it will appear before the dollar sign.
^^^^ (up arrows) : Prints the number in scientific notation (eg 2E-04). These must be preceeded by a # sign. If more ^s are added only the first 4 are used. If there are less than 4, a [?SYNTAX ERROR](500168_syntax_error.md) occurs.
= : Normally, text which is shorter than the format field allows is left-justified. Using the = sign centres the text in the output field. The = counts as a character space.
> : The output text is right-justified instead of left-justified. The > counts as a character space.

The # is used for string and numeric output. The = and > are used for string output only. All other symbols are for numeric output only.

To change the output characters for spaces, commas, decimal points and dollar signs (to represent other currencies), see the [PUDEF statement](500098_pudef_statement.md).

A semi-colon follows the format list, which in turn is followed by the items to be printed. However, unlike the PRINT and PRINT# statements, only commas can be used to separate items.

Examples
`PRINT USING "$##.##";2.99`  Prints `$ 2.99` (note the space after the dollar sign)
`PRINT USING "+#$##.##";2.99`  Prints `+ $2.99`
`PRINT USING "#$##.##";2999.99`  Prints ***, as the number is too large for the field
`PRINT USING "####";"HELLO"`  Prints HELL, as the smaller field truncates the output text from the right
`PRINT USING "#########";"HELLO"`  Prints HELLO with four spaces on the right
`PRINT USING "=########";"HELLO"`  Prints HELLO with two spaces on both left and right
`PRINT USING ">########";"HELLO"`  Prints HELLO with four spaces on the left
`PRINT USING "#^^^^";200`  Prints 2E+02
`PRINT# 1, USING "#";X`  Prints to file 1

Special cases
Hit [here](https://plus4world.powweb.com/forum.php?postid=6072&h=print%20using) for special masks to obtain a string like "00:01:23"

Bug (?): if a pattern beginning with a comma (like ",###,###") is used to print a number, result will always contain the first ",". For example: ,__1,234

Numeric values cannot be centered or left justified.

Abbreviation
USING: US SHIFT+I

Credits
? + SVS
