# GET Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500076
- Category: Reference/Commodore BASIC V3.5

GET *variable*

The GET statement is used to get data from the keyboard one character at a time. When it is executed, the computer checks the keyboard for any pressed keys. If none are pressed, a null character is returned.

GET is followed by a variable name, which is fed with the returned character. This is usually a string variable. If a numeric variable is used and a non-numeric key is pressed, a [?TYPE MISMATCH ERROR](500177_type_mismatch_error.md) occurs.

The GET statement only checks for keys pressed at the time of execution, it does not wait for a key to be pressed. To do this, use the [GETKEY statement](500159_getkey_statement.md) instead.

This statement can only be used within a program. If it is used in direct mode, an [?ILLEGAL DIRECT ERROR](500160_illegal_direct_error.md) will occur.

Examples
`10 GET A$ : IF A$ <> "Y" THEN 10`  This line waits for the Y key to be pressed before continuing

Abbreviation
G SHIFT+E
