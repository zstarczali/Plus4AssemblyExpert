# How Do I Enable Automatic Character Insertion?

- Source: https://plus4world.powweb.com/plus4encyclopedia/500030
- Category: Programming/BASIC
- Keywords: keys,keyboard,insert

With POKE 2026,255 you can automatically insert characters into rows. Disable it with POKE 2026,0.

This is equivalent to pressing ESC+A (enable) and ESC+C (disable).

Machine code equivalent:
LDA #$FF
STA $07EA (enable)

LDA #$00
sta $07EA (disable)
