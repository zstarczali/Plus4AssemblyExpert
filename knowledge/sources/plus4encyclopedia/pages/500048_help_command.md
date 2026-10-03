# HELP Command

- Source: https://plus4world.powweb.com/plus4encyclopedia/500048
- Category: Reference/Commodore BASIC V3.5

HELP

The HELP command is used after an error occurs in a BASIC program. When used, the line in which the error occured is listed, and the component causing the error is shown flashing. Useful in both direct mode, or in a BASIC program to help debugging.

By default, the HELP key issues the HELP command. This corresponds to KEY 8.

Example
`10 TRAP 100 : REM ENABLE ERROR TRAPPING`
`20 BUG : REM THIS CAUSES A SYNTAX ERROR`
`100 HELP`
When you RUN this program, 20 BUG is displayed with the word BUG flashing.

Abbreviation
HE SHIFT+L
