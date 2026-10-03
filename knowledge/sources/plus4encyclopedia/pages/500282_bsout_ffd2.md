# BSOUT ($FFD2)

- Source: https://plus4world.powweb.com/plus4encyclopedia/500282
- Category: Programming/Assembly, Reference/KERNAL

To output a character on the screen.

The character stored in the accumulator is output at the current cursor position. The character must be a PETSCII code.

Examples:

```
LDA #$93  Clear the screen by outputting the SHIFT+HOME character
JSR BSOUT
LDA #$41  Output the character "A"
JSR BSOUT
```
