# DATA Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500069
- Category: Reference/Commodore BASIC V3.5

DATA *list of constants seperated by commas*

DATA statements are followed by a list of items to be read by [READ statement](500099_read_statement.md)s. The items may be strings or numeric values. If strings are to contain colons or commas, they must be enclosed within double quotes (this can also include special characters, such as FLASH or CLEAR). If two commas have nothing between them, the value will be read as either a zero number or an empty string.

DATA statements can be re-read using the [RESTORE statement](500101_restore_statement.md).

Although the DATA statement can be entered in direct mode, it has no functional purpose, as READ statements can only read DATA items in program lines.

Examples
`100 DATA 100,200,TEST ME,"TEST:ME,NOW",,ABC123`  A variety of data types

Abbreviation
D SHIFT+A
