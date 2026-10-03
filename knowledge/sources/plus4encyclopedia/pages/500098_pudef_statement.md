# PUDEF Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500098
- Category: Reference/Commodore BASIC V3.5

PUDEF "*characters 1-4*"

The PUDEF statement changes certain characters printed using the [PRINT USING statement](500096_print_using_statement.md). The word PUDEF is followed by a string, either in double quotes or a string variable, which contains between 1 to 4 characters. Each of these characters represents a symbol printed in the PRINT USING statement. The characters specified in this string replace the previous characters. This statement is normally used to represent other currencies in the PRINT USING statement.

The characters are as follows: The first character is the filler character (normally an empty space). The second is the comma. The third is the decimal point, and the fourth is the currency symbol (normally the dollar sign).

If less than 4 characters are in the string, only the ones specified are changed. If there are no characters or more than 4 characters in the string, an [?ILLEGAL QUANTITY ERROR](500171_illegal_quantity_error.md) occurs.

If, for example, only the 3rd character is to be changed, the 1st and 2nd characters must be specified at the same time.

NOTE: Any changes made by the PUDEF statement do not affect the characters used in the format list in the PRINT USING statement. It only affects the printed characters.

Examples
`PUDEF " ,.$"`  The default values
`PUDEF "*"`  Prints * in place of empty spaces
`PUDEF " @"`  Prints @ in place of commas
`PUDEF " .,"`  Prints decimal points instead of commas, and commas instead of decimal points
`PUDEF " ,.£"`  Prints English pound signs instead of dollar signs
`A$ = " ,.£" : PUDEF A$`  As above

Abbreviation
P SHIFT+U
