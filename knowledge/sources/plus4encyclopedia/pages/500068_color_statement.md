# COLOR Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500068
- Category: Reference/Commodore BASIC V3.5

COLOR *source#*,*color#* [,*luminance#*]

Assigns a color to one of the 5 [color sources](500063_color_sources.md) (numbered 0-4).

The color number ranges from 1-16:
1: Black
2: White
3: Red
4: Cyan
5: Purple
6: Green
7: Blue
8: Yellow
9: Orange
10: Brown
11: Yellow-Green
12: Pink
13: Blue-Green
14: Light Blue
15: Dark Blue
16: Light Green

The luminance level selects the level of the color brightness. There are 8 luminance levels (0-7, 0: lowest, 7:highest). The default level is 7. All luminance levels of black (color 1) are identical in appearence.

Examples
`COLOR 0,8,5`  Turns the background color to a dull yellow
`COLOR 4,1`  Turns the border color to black

Abbreviation
CO SHIFT+L
