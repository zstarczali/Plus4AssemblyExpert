---
name: plus4-c64-port
description: >
  Port Commodore 64 assembly code, effects or games to the Plus/4 / C16, or
  explain the differences between the two machines. Activate when the user wants
  to convert, port, átírni, portolni C64 code to Plus/4, asks "how is this done on
  the Plus/4", compares VIC-II with TED, SID with TED sound, CIA with TED timers,
  or needs C64 ROM addresses, colours or memory locations translated to the 264 family.
---

# C64 → Plus/4 porting

Use the `plus4-expert` knowledge base (`../../knowledge/`, fallback
`F:\Development\Plus4AssemblyExpert\knowledge\`) and `../plus4-expert/references/ted-quick-reference.md`.

## Translation table (sources in brackets)

| C64 | Plus/4 / C16 | Notes |
|---|---|---|
| Load / BASIC start `$0801` | `$1001` | Kick Assembler: `*=$1001` + `BasicUpstart(start)` |
| `$01` banking | `$FF3E` ROM / `$FF3F` RAM, ROM bank latch `$FDD0–$FDDF` | `$00/$01` is the CPU I/O port only [500290, 500255] |
| VIC-II `$D011` | `$FF06` | same idea: ECM, BMM, DEN, RSEL, YSCROLL [500024] |
| VIC-II `$D016` | `$FF07` | + RVSDIS, NTSC/PAL, TEDOFF |
| `$D012` raster compare | `$FF0B` + `$FF0A` bit 0 | current line readable/writable at `$FF1C/$FF1D` |
| `$D019` / `$D01A` | `$FF09` / `$FF0A` | ack = write 1 bits back to `$FF09` |
| `$D018` + `$DD00` bank | `$FF12` (bitmap), `$FF13` (charset), `$FF14` (screen) | no 16K VIC banks; TED addresses all 64K |
| Screen `$0400` + colour RAM `$D800` | 2K block at `$FF14` (default `$0800` attributes + `$0C00` chars) | attribute byte holds luma + flash |
| `$D020` / `$D021` | `$FF19` / `$FF15` | colour format `%0LLLCCCC` |
| `$D022–$D024` | `$FF16–$FF18` | |
| Colour codes 0–15 | 121-colour luma/chroma | conversion tables [500291] |
| Sprites `$D000–$D02E` | none | software sprites / bobs [500228, 500266, 500192] |
| SID `$D400–$D418` | TED: 2 voices `$FF0E–$FF12`, volume `$FF11` | voice 2 can be noise; no ADSR/filter [500244, 500243, 500269 for SID cards] |
| CIA timers | TED timers `$FF00–$FF05` | single-clock, timer 1 auto-reload [500024] |
| Keyboard `$DC00/$DC01` | `$FD30` + `$FF08` latch | [500012] |
| Joystick `$DC00/$DC01` | `$FF08` selector `$FD` (port 2) / `$FB` (port 1) | |
| KERNAL `$FF81–$FFF3` | same jump table | + `PRIMM $FF4F` etc. [500232] |
| BASIC/KERNAL internals | see xref map | [500293] (page numbers refer to the C64 Intern / "A Commodore 64-es belső felépítése" book) |
| ~985 kHz PAL CPU | 1.15 MHz average, double clock outside DMA | cycle-exact code must be re-timed [500248] |
| Character ROM `$D000` | Character ROM `$D000–$D7FF` (in ROM map) | Programmer's Ref. Guide App. G |

## Porting workflow

1. Inventory every hardware access in the C64 code (grep `\$D[0-9A-F]{3}`, `\$DC`, `\$DD`, `\$01`, `$0314`).
2. Re-place memory: no VIC bank limits, but ROM covers `$8000–$FFFF` unless `$FF3F` is written;
   C16 has only 16K.
3. Translate registers with the table; re-derive colour values; drop or emulate sprites and SID features.
4. Re-time raster code for the TED (two DMA lines per char row, double/single clock).
5. Replace direct ROM calls using [500293] and check their ZP inputs/outputs.
6. Review the result with the `plus4-debug` checklist.
