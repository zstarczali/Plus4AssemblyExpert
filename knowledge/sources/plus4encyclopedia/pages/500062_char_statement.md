# CHAR Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500062
- Category: Reference/Commodore BASIC V3.5

CHAR [*color source#*],*x*,*y*,"*text string*"[,*reverse flag*]

This statement displays text characters in any location in either text or graphic mode.

The [color sources](500063_color_sources.md) are 0-3 (default 1). To change the colors, see the [COLOR statement](500068_color_statement.md). Multicolor sources can only be used when a multicolor mode is active (see [GRAPHIC statement](500080_graphic_statement.md)).

The x coordinate is the character column (0-39).

The y coordinate is the character row (0-24).

The text to be printed can either be text within double quotes, or can be a string variable.

The reverse flag reverses the printed text (0:off, 1:on) in graphic mode. Default is 0. The reverse flag has extra uses in multicolor mode (see below).

In multicolor graphic mode, selecting color 0 displays the character in the foreground color with one of the multicolors for the surrounding background. The choice of multicolor is determined by the reverse flag. (0: multicolor 1, 1:multicolor 2)

Special characters (such as FLASH or CLEAR) may be included in the string when printing to a text screen, but when printing to a graphic screen, the PETSCII character representing the special character will be printed instead.

Examples
`CHAR 1,17,12,"HELLO"`  Prints HELLO in the centre of the screen.
`CHAR ,0,0,"HELLO",1`  Prints HELLO in reversed characters

Abbreviation
CH SHIFT+A

**Warning:
Execution of CHAR statement does reset possible screen windows.**
