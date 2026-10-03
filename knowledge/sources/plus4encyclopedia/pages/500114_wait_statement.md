# WAIT Statement

- Source: https://plus4world.powweb.com/plus4encyclopedia/500114
- Category: Reference/Commodore BASIC V3.5

WAIT *address*,*value1* [,*value2*]

The WAIT statement halts the program until the contents of a specific memory location changes in a specific way.

The word WAIT is followed by the memory location (in decimal format), then followed by value1, which is a value between 0-255, and optionally followed by value2, also 0-255.

The contents of the memory location is firstly XORed with value2 (if present), then ANDed with value1. If the result is 0, the memory location is checked again. If the result is not 0, program execution continues with the next statement.

The memory location must be changed by an external event, such as the value of the system clock.

Examples
`WAIT 165,128`  Waits until bit 7 of location 165 is 1
`WAIT 165,144,128`  Waits until either bit 4 is 1 or bit 7 is 0
`WAIT 1347,1`  Waits until shift key is pressed

Abbreviation
W SHIFT+A
