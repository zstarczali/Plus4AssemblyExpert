# IF/THEN/ELSE Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500081
- Category: Reference/Commodore BASIC V3.5

IF *expression* THEN *then-clause* [:ELSE *else-clause*]

The IF/THEN statement analyses a BASIC expression, and takes different actions depending on whether the expression is true or false.

IF is followed by the expression, which can use any comparison operators (=, <, >, <>, <=, >=), and by using the AND, OR and NOT arguments, additional comparisons can be added.

The expression is followed by THEN. If the expression is true, the statements following THEN are executed, up to the end of that BASIC line. NOTE: If THEN is to be immediately followed by the [GOTO statement](500079_goto_statement.md), this can be expressed as either THEN *line#*, or GOTO *line#* (with the word GOTO in place of THEN).

If the IF expression is false, the statements following ELSE (if present) are executed instead. The ELSE clause must be in the same line as the IF statement. If there is no ELSE clause and the IF expression is false, program execution continues on the next line. If ELSE is to be immediately followed by GOTO *line#*, ELSE *line#* can be used instead.

Examples
`IF A$="N" THEN PRINT"BYE":END`  Checks the value of A$. If A$ is "N" (making the expression true) then the statements following THEN are executed. Otherwise program execution continues on the next line
`IF B=0 THEN 10`
`IF B=0 GOTO 10`  Alternative ways of stating THEN GOTO 10
`10 IF X>0 AND X<9 THEN PRINT X:GOTO 50:ELSE 5`  If the expression is false, the statements following ELSE are executed. In this case, ELSE 5 is a shortened version of ELSE GOTO 5

Abbreviations
IF: None
THEN: T SHIFT+H
ELSE: E SHIFT+L
