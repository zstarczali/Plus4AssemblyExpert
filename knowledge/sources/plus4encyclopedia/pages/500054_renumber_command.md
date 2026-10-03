# RENUMBER Command

- Source: https://plus4world.powweb.com/plus4encyclopedia/500054
- Category: Reference/Commodore BASIC V3.5

RENUMBER [*new starting line#*[,*increment*[,*old starting line#*] ] ]

Renumbers the lines in a BASIC program. Normally used to renumber entire programs, but can also partially renumber programs to a limited extent. This command also adjusts line numbers in BASIC statements, such as GOTO, GOSUB, RESTORE etc, so that they point to the new line numbers.

The old starting line is the first line where renumbering will begin. By default, it is the first line in the program. If the line number specified does not exist in the program, renumbering will start from the next valid line number.

The new starting line will be the first line number of the renumbered program. It is set to 10 by default. NOTE: If the old starting line number is not the first line of the program, the new starting line number must not be the same or lower than the line number preceeding the old starting line number. If this happens, an [?ILLEGAL QUANTITY ERROR](500171_illegal_quantity_error.md) will occur.

The increment is the spacing between the new line numbers (10, 20, 30 etc). It is set to 10 by default.

Therefore, simply entering RENUMBER without parameters will renumber an entire program with the lines numbered 10, 20, 30 and so on.

This command can only be used in direct mode. If used in a program, [?DIRECT MODE ONLY ERROR](500161_direct_mode_only_error.md) will occur.

Bug
The RENUMBER command in Basic V3.5 has a bug. If a line in the BASIC program refers to a non-existent line number, that line number will become 65535. For example, if the following program is renumbered:
`10 GOTO 20`
it will become
`10 GOTO 65535`
Issuing another RENUMBER command will cause a [?SYNTAX ERROR](500168_syntax_error.md), since line numbers can only be between 0-63999.
This bug was fixed in Basic V7.0 on the C128 (where it would cause an ?UNRESOLVED REFERENCE error).

Examples
`RENUMBER`  Renumbers a program as line numbers 10, 20, 30 etc.
`RENUMBER 20,20,5`  Starting at line 5, renumbers the program. Line 5 becomes line 20, and the following lines are numbered in increments of 20 (40, 60, 80 etc)

Abbreviation
REN SHIFT+U
