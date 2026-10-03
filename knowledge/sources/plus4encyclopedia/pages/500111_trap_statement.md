# TRAP Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500111
- Category: Reference/Commodore BASIC V3.5

TRAP [*line#*]

The TRAP statement, when active, intercepts all error conditions (including the STOP key), except [?UNDEF'D STATEMENT ERROR](500174_undef_d_statement_error.md) and the [STOP statement](500109_stop_statement.md). It is normally placed at the start of a BASIC program.

The word TRAP is followed by the line number where program execution occurs after an error. TRAP without a line number turns off error trapping.

If the specified line number does not exist in the program, an [?UNDEF'D STATEMENT ERROR](500174_undef_d_statement_error.md) will occur whenever an error of any type occurs in the program, showing the line number of where the error occured.

When an error occurs, the error flag is set, and program execution is transferred to the line specified by the TRAP statement. The system variables EL and ER are updated with the error information, which may be used by the TRAP routine. To clear the error flag and resume normal program execution, the [RESUME statement](500103_resume_statement.md) must be used.

NOTE: If there is an error in the TRAP routine, it cannot be trapped.

This statement can only be used within a program. If it is used in direct mode, an [?ILLEGAL DIRECT ERROR](500160_illegal_direct_error.md) will occur.

Examples
`TRAP 200`  When an error occurs, program execution starts at line 200
`TRAP`  Turns off error trapping

Abbreviation
T SHIFT+R
