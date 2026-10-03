# CHROUT ($FFD2)

- Source: https://plus4world.powweb.com/plus4encyclopedia/500242
- Category: Programming/Assembly, Reference/KERNAL

Write a byte to the output (default: screen).

Input: A = byte to write

Example:
`LDA #$93  character code of SHIFT+HOME
JSR $FFD2  clear the screen

LDA #$41  character code for letter "A"
JSR $FFD2  print letter "A" on screen`

Notes
On VC-20, C64, etc. writing text to the screen is often achieved by putting this call inside a loop. On C16/Plus4, that's not necessary, it can be done with a single call (see $FF4F).
