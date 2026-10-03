# INPUT# Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500083
- Category: Reference/Commodore BASIC V3.5

INPUT# *file number*,*variable list*

This is similar to the [INPUT statement](500082_input_statement.md), but instead of getting data from the keyboard, it is taken from a device or file opened with the [OPEN statement](500089_open_statement.md).

No prompt string is allowed with INPUT#.

This statement can only be used within a program. If it is used in direct mode, an [?ILLEGAL DIRECT ERROR](500160_illegal_direct_error.md) will occur.

Examples
`INPUT# 2,A$,B,C%`  Gets data from file 2

Abbreviation
I SHIFT+N
