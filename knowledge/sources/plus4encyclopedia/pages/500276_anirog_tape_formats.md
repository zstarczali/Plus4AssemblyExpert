# Anirog Tape Formats

- Source: https://plus4world.powweb.com/plus4encyclopedia/500276
- Category: Reference/TAP files, Programming/General

Description of two similar tape formats mostly used for [Anirog](https://plus4world.powweb.com/groups/Anirog) releases.

First Tape Format
This version was used for most Anirog releases.

Bits are encoded using long (bit 0) and short (bit 1) wave cycles, which is opposite to most turbo loaders. Wave cycles are of normal (lo-hi) polarity. The timer value used to determine cycle length is derived from the calibrated KERNAL timer value for short half-cycles. The KERNAL timer value is multiplied by 1.5, then $0160 is added to make the final timer start point. When the falling edge of a cycle is detected, the timer value is checked and reloaded (12 CPU cycles). If the timer was between $0100-$01FF, bit 1 is returned. If it was between $0000-$00FF, bit 0 is returned. Any other timer value is flagged as a bad read. Bits are loaded in LSb->MSb order.

Load addresses are preset in the loader routine.

The block starts with the sync section, which begins with a continuous repetition of seven long cycles and one short cycle, synchronized to bit pattern %00010000 ($10). This is followed by a series of countdown bytes, counting down from $0F to $00, which completes the sync section.

The program data follows. Each byte is added in succession to the check digit, initialized as $00. If the addition to the check digit sets the carry flag, then the carry is added as well. A check digit verification byte is loaded after the end of the program data, which is added to the check digit in the aforementioned manner, then the check digit is shifted right by 1. If the result is zero, then verification is complete. The check digit verification byte is written to memory after the program data.

There were three minor versions of the loader routine, with the first two XORing the current border colour with $11 for the border effect, and the third XORing the border colour with $25. The first would only work on 16K machines, and is found on some copies of [Skramble](https://plus4world.powweb.com/software/Skramble). The second and third variations fixed this bug.

Second Tape Format
This version was used on later Anirog releases, and also on [Magnificent 7](https://plus4world.powweb.com/groups/Magnificent_7_Software) releases and a few [Anco](https://plus4world.powweb.com/groups/Anco) releases.

This second version has the following differences from the first:
The timer start point is no longer derived from the KERNAL timer. Instead, it has a fixed start point of $0322.
Each byte of the program data loaded from the tape is XORed with $2A before storing in memory.
Bad bit reads are no longer flagged, and there is no check digit.
