# GETKEY Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500159
- Category: Reference/Commodore BASIC V3.5

GETKEY *variable list*

The GETKEY statement is used to get data from the keyboard one character at a time. When it is executed, program execution is paused until a key is pressed.

GETKEY is followed by a variable name, which is fed with the returned character. This is usually a string variable. If a numeric variable is used and a non-numeric key is pressed, a [?TYPE MISMATCH ERROR](500177_type_mismatch_error.md) occurs. Additional variables may be added, seperated by commas. GETKEY will wait until a key is pressed for each variable in the list.

Because GETKEY pauses a program until a key is pressed, it is not suitable for programs running continuously while awaiting key presses (such as action games). To do this, use the [GET statement](500076_get_statement.md) instead.

Note that GETKEY can also be written as GET KEY.

This statement can only be used within a program. If it is used in direct mode, an [?ILLEGAL DIRECT ERROR](500160_illegal_direct_error.md) will occur.

Examples
`10 GETKEY A$`  Program waits until a key is pressed, whose character is entered into variable A$
`20 GETKEY B$,C$,D$`  Program waits until three keys are pressed, one for each variable.

Bug
In KERNAL versions 4 and earlier, if a function key is pressed in response to GET or GETKEY, and another GETKEY is encountered before all characters of the function key have been processed, the program will crash with a garbled error message. This can also occur if a function key is pressed in response to a GETKEY with multiple variables. This is fixed in the Rev 5 ROM.

Abbreviation
G SHIFT+E K SHIFT+E
