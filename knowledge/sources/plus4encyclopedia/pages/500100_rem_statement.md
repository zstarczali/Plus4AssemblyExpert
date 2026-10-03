# REM Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500100
- Category: Reference/Commodore BASIC V3.5

REM [*message*]

AKA REMark. The REM statement is used to make notes within a BASIC program, such as explaning what a section of a program does, or give information about the author, or anything. It has no effect on the operation of a program.

Although the REM statement has no effect on a program, it can be used to alter the screen appearence of a BASIC listing. This is done by following the word REM with an opening double quote, which allows use of special characters such as the cursor and delete characters. When done correctly, this can be used to alter the appearence of BASIC lines. An example of this can be seen in the Berks games prior to RUNning, where the SYS line is hidden by the game title and author name when LISTed.

A REM statement should always be the last statement in a line. Any statements following the REM statement in the same line will be ignored.

NOTE: If shifted characters are not enclosed within double quotes, they will be interpreted as BASIC tokens when the program is listed, causing the listing to display BASIC keywords.

Examples
`50 NEXT A:REM THIS LINE IS NOT NEEDED`

Abbreviation
None
