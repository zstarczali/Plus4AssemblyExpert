# GET# Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500077
- Category: Reference/Commodore BASIC V3.5

GET# *file number*,*variable*

This is similar to the [GET statement](500076_get_statement.md), but instead of getting a character from the keyboard, it is taken from a device or file opened with the [OPEN statement](500089_open_statement.md).

This statement can only be used within a program. If it is used in direct mode, an [?ILLEGAL DIRECT ERROR](500160_illegal_direct_error.md) will occur.

Examples
`10 GET# 1,A$`  Gets a character from file 1

*** Note: Due some problems with drive' sync, it is a good habit to check if the received character is null (""). In this way the GET statement should be redone:

`10 GET# 1,A$: IF A$="" THEN 10`  Gets a valid character from file 1

Abbreviation
G SHIFT+E #
