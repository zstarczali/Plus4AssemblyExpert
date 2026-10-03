# AUTO Command

- Source: https://plus4world.powweb.com/plus4encyclopedia/500026
- Category: Reference/Commodore BASIC V3.5

AUTO [*line#*]

Turns on automatic line numbering. When auto line numbering is turned on, after typing a BASIC line and pressing RETURN, a new line number is printed automatically, making it easier to type BASIC programs. The [line #] parameter refers to the increment. If it's omitted, auto line numbering is turned off.

This command can only be used in direct mode. If used in a program, [?DIRECT MODE ONLY ERROR](500161_direct_mode_only_error.md) will occur.

Examples
`AUTO 10`  Line numbers will increment by 10
`AUTO`  Turns automatic line numbering off.

Abbreviation
A SHIFT+U
