# PRINT Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500094
- Category: Reference/Commodore BASIC V3.5

PRINT [*print list*]

The PRINT statement is the primary output statement in BASIC. It is used to display characters on the screen from either text inside double quotes ("HELLO"), from variables (A, A$) or from functions (VAL(A$), CHR$(34)). It is also used to display the results of mathematical equations.

The word PRINT is followed by the item(s) to be printed. Multiple strings/string variables can be joined together in a single PRINT statement simply by stating each item in turn (PRINT"I AM " K "YEARS OLD"). Multiple strings can be separated by a plus (+) sign (PRINT"HELLO"+" WORLD"). Multiple numbers or numeric variables by a semicolon ";" (PRINT 3;F;0.5).
Numbers and numeric variables may be joined with any mathematical operators (PRINT 3*4/5). In this case PRINT will show the result.

The comma and semi-colon marks are used for formatting the output of a PRINT statement. The comma divides the screen into 4 columns, and a semi-colon, if present at end of PRINT statement, will prevent the use of a carriage return, causing the next item to be printed immediately after the end of the last item. Either mark can be used as the last symbol in the statement, affecting the output of the next PRINT statement.

Examples
`PRINT "HELLO"`  Prints HELLO on the screen
`A$ = "THERE"`  PRINT "HELLO,"A$ : Prints HELLO, THERE

`PRINT 6 * 2`  Prints 12
`A = 15 : B = 3 : PRINT A / B`  Prints 5
`PRINT "HELLO"; : PRINT "THERE"`  Prints HELLOTHERE
`PRINT "HELLO","THERE`  Prints HELLO, then prints THERE at 1/4 screen across

Abbreviation
? (question-mark character)
