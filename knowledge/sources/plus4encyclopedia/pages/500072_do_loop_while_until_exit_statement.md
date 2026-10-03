# DO/LOOP/WHILE/UNTIL/EXIT Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500072
- Category: Reference/Commodore BASIC V3.5

DO [UNTIL *boolean argument* / WHILE *boolean argument*] : *statements* [: EXIT]
LOOP [UNTIL *boolean argument* / WHILE *boolean argument*]

Performs the statements between the DO statement and the LOOP statement. If no UNTIL or WHILE modifies either the DO or LOOP statement, the loop continues indefinitely. If an EXIT statement is encountered within a DO loop, program execution moves to the first command/statement following the LOOP statement. DO loops may be nested within other DO loops.

If the UNTIL parameter is used, the loop continues until the boolean argument becomes true. The WHILE parameter is the opposite: the loop contiues until the boolean argument becomes false. Only one of these parameters may be used in a DO or LOOP statement.

The EXIT statement cannot be used if a DO-LOOP is not running. Otherwise, a [?LOOP NOT FOUND ERROR](500187_loop_not_found_error.md) or a [?LOOP WITHOUT DO ERROR](500188_loop_without_do_error.md) will occur.

Examples
`DO UNTIL A$="X":GET A$:LOOP`
`DO:GETKEY A$:LOOP WHILE A$<>"Y"`

Abbreviations
DO: None
LOOP: LO SHIFT+O
WHILE: W SHIFT+H
UNTIL: U SHIFT+N
EXIT: EX SHIFT+I
