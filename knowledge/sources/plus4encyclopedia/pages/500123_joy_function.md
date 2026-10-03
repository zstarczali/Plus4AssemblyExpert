# JOY Function

- Source: https://plus4world.powweb.com/plus4encyclopedia/500123
- Category: Reference/Commodore BASIC V3.5

JOY(X)

This function returns a numeric value.

This function finds the status of either joystick. X is the port number (1 or 2).

The value returned indicates the direction of the joystick, and whether the fire button is pressed. The values returned are:
0: No movement
1: Up
2: Right-Up
3: Right
4: Right-Down
5: Down
6: Left-Down
7: Left
8: Left-Up
If the fire button is pressed, 128 is added to the above values.

Example
`JOY(1) = 3`  Joystick 1 is pushed to the right
`JOY(2) = 135`  Joystick 2 is pushed to the left with the fire button pressed

Abbreviation
J SHIFT+O
