# Plus/4 Keyboard/Joystick Matrix

- Source: https://plus4world.powweb.com/plus4encyclopedia/500012
- Category: Programming/Assembly
- Keywords: Keyboard Joystick Matrix

To read keyboard/joystick inputs, a selector value must be written to both the keyboard latch at $FD30 and the joystick latch at $FF08, with the resulting answer being read from $FF08.

The keyboard matrix is arranged in 8 groups of 8 keys, as shown in the table below:

| **The Plus/4 Keyboard controller** |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  | $FD30 selector value |  |  |  |  |  |  |  |
| $FE | $FD | $FB | $F7 | $EF | $DF | $BF | $7F |  |  |
| $FF08 answer value | $FE($01) | Ins/Del | 3 | 5 | 7 | 9 | Down | Left | 1 (one) |
| $FD($02) | Return | W | R | Y | I | P | * | Clr/Home |  |
| $FB($04) | Pound | A | D | G | J | L | ; / ] | Controls |  |
| $F7($08) | Help/F7 | 4 | 6 | 8 | 0 (zero) | Up | Right | 2 |  |
| $EF($10) | F1/F4 | Z | C | B | M | . / > | Escape | Space |  |
| $DF($20) | F2/F5 | S | F | H | K | : / [ | = | Commodore |  |
| $BF($40) | F3/F6 | E | T | U | O | - | + | Q |  |
| $7F($80) | @ sign | Shift keys | X | V | N | , / < | / | Run/Stop |  |

Each bit in the selector value represents a group of 8 keys. For example, bit 0 represents keys Inst/Del, Return, Pound, the Function keys and the @ key, bit 1 represents keys 3, W, A, 4, Z, S, E and Shift, and so on.

To read a group of keys, the corresponding bit must be zero in the selector value. The answer value read from $FF08 indicate which of the keys in that group was pressed. If a key was pressed, it's corresponding bit in the answer value will be zero.

For example, to check if the Space bar was pressed, the selector value would be $7F (zero in bit 7), and if Space is pressed, the answer value read from $FF08 will be $EF (zero in bit 4).

Multiple groups of keys can be checked by clearing multiple bits in the selector value. To check if any key on the keyboard was pressed, use $00 as the selector value. If no keys were pressed, the answer value will be $FF, if it is not $FF, then at least one key was pressed.

For joystick inputs, bit 1 of the selector value reads Port 2, and bit 2 reads Port 1. The selector and answer values for the joysticks are as follows:

| **Joystick controller** |  |  |  |
|---|---|---|---|
|  |  | $FF08 selector value |  |
| $FD | $FB |  |  |
| $FF08 answer value | $FE($01) | Joy2 Up | Joy1 Up |
| $FD($02) | Joy2 Down | Joy1 Down |  |
| $FB($04) | Joy2 Left | Joy1 Left |  |
| $F7($08) | Joy2 Right | Joy1 Right |  |
| $EF($10) |  |  |  |
| $DF($20) |  |  |  |
| $BF($40) |  | Joy1 Fire |  |
| $7F($80) | Joy2 Fire |  |  |

If the same selector value is written to both $FD30 and $FF08, then both keyboard and joystick will be read simultaneously. For example, if the selector value written to both $FD30 and $FF08 is $FB, and the answer is $FD, then either key R was pressed, or Joystick 1 was pushed down.

To read keyboard inputs separately from the joysticks, write the desired selector value to the $FD30 keyboard latch, and write $FF to the $FF08 joystick latch.
Likewise, to read the joysticks separately from the keyboard, write $FF to the $FD30 keyboard latch, and the desired selector value to the $FF08 joystick latch.

Examples
Check if space key is pressed

```
LDA #$7F	 Check column 7
STA $FD30	 Write to Keyboard Latch
STA $FF08	 Write to Joystick Latch
LDA $FF08	 Read answer
AND #$10	 Query for "Space" bit
BNE not_pressed
 space is pressed
not_pressed
```

Check if 'T' is pressed, but **not** checking if Joystick 1 Fire is pressed:

```
LDA #$FB	 Check bit 2
STA $FD30	 Write to Keyboard Latch
LDA #$FF
STA $FF08	 Write $FF to Joystick Latch
LDA $FF08	 Read answer
AND #$40	 Query for "T" bit
BNE not_pressed
 'T' is pressed, but not J1 Fire
not_pressed
```

Check if Joystick 2 Up is pressed, but **not** checking if key '3' is pressed

```
LDA #$FF
STA $FD30	 Write $FF to Keyboard Latch
LDA #$FD	 Check bit 1
STA $FF08	 Write to Joystick Latch
LDA $FF08	 Read answer
AND #$01	 Query for J2 Up bit
BNE not_pressed
 J2 Up is pressed, but not '3'
not_pressed
```

[BSZ](https://plus4world.powweb.com/members/BSZ) and [TLC](https://plus4world.powweb.com/members/TLC) conducted analyses in early 2021 regarding the role of joystick readings in relation to other TED locations and how this affects malfunctioning TED ICs. Please refer to the [forum thread](https://plus4world.powweb.com/forum/42748#42810) for more details.
