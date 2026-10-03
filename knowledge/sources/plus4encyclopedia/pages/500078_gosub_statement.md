# GOSUB Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500078
- Category: Reference/Commodore BASIC V3.5

GOSUB *line#*

AKA GO to SUBroutine. This is similar to the [GOTO statement](500079_goto_statement.md), but remembers where it was executed from. When a [RETURN statement](500102_return_statement.md) is encountered, the program resumes execution following the last encountered GOSUB statement.

This is normally used for accessing sections of a program (subroutine) that are kept isolated from the main program.

Multiple GOSUBs may be executed concurrently. A RETURN statement returns to the last executed GOSUB statement, therefore multiple RETURN statements will be required to end all GOSUB statements.

If a RETURN statement is encountered and there is no GOSUB in operation, a [?RETURN WITHOUT GOSUB ERROR](500169_return_without_gosub_error.md) will occur.

If a line number is not specified after a GOSUB statement, it assumes line 0. If the specified line number does not exist in the program, an [?UNDEF'D STATEMENT ERROR](500174_undef_d_statement_error.md) occurs.

Examples
`20 GOSUB 300`  Goes to line 300 and executes the program from there
`:
:`
`300 PRINT "HELLO" : RETURN`  The [RETURN statement](500102_return_statement.md) returns program execution to the point immediately following the GOSUB statement

Abbreviation
GO SHIFT+S
