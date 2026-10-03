# RESUME Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500103
- Category: Reference/Commodore BASIC V3.5

RESUME [*line#*/NEXT]

The RESUME statement is only used when a [TRAP statement](500111_trap_statement.md) traps an error and executes a seperate line of a BASIC program.

Without arguments, RESUME attempts to re-execute the line in which the error occured. RESUME NEXT resumes execution immediately following the statement which caused the error. RESUME *line#* will begin execution at the specified line number. When a RESUME statement is executed, the TRAP operation stops.

If a RESUME statement is executed and there is no TRAP in operation, a [?CAN'T RESUME ERROR](500186_can_t_resume_error.md) occurs. NOTE: This error message will be displayed if there is no TRAP statement defined, but if there is a TRAP statement defined, the ?CAN'T RESUME ERROR will be trapped just like any other error.

This statement can only be used within a program. If it is used in direct mode, an [?ILLEGAL DIRECT ERROR](500160_illegal_direct_error.md) will occur.

Examples
`RESUME`  Re-executes the line on which the error occured
`RESUME NEXT`  Resumes execution at the statement immediately following the statement that caused the error
`RESUME 250`  Resumes execution at line 250

Abbreviation
RES SHIFT+U
