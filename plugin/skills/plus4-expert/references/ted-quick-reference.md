# TED / Plus/4 hardware quick reference

Every line below is taken from the bundled sources; the file in brackets is the place to read the full text.
Encyclopedia pages live in `knowledge/sources/plus4encyclopedia/pages/`.

## TED registers `$FF00–$FF3F`  [500024_ted_registers.md]

Unused bits always read back as 1 (write `$12` to `$FF15`, read `$92`). Almost all registers are read/write.

| Addr | Function | Notes |
|---|---|---|
| `$FF00/01` | Timer 1 lo/hi | Interval timer: reloads the written value. Write LO first (timer stops), then HI (timer starts). Keep < ~110 single-clock cycles between the two writes. |
| `$FF02/03` | Timer 2 lo/hi | Counts to 0, sets flag, wraps to `$FFFF` and keeps counting. |
| `$FF04/05` | Timer 3 lo/hi | Same as timer 2. All timers run from the **single clock**. |
| `$FF06` | CR1: TEST, ECM, BMM, DEN, RSEL, YSCROLL | Default `$1B` (like VIC-II `$D011`). BMM = bit 5 = bitmap mode. DEN = bit 4. |
| `$FF07` | CR2: RVSDIS, NTSC/PAL, TEDOFF, MCM, CSEL, XSCROLL | Default `$08` PAL / `$48` NTSC (like `$D016`). Bit 7 = 256-char mode (no reverse). |
| `$FF08` | Keyboard/joystick latch | Write selector, read answer. See keyboard section. |
| `$FF09` | IRQ flags | b7 IRQ occurred, b6 T3, b4 T2, b3 T1, b1 raster. Writing 1 to a bit clears it: `LDA $FF09 / STA $FF09` acks everything pending; `LDA #$02 / STA $FF09` acks raster only. Flags are set even if the source is disabled. |
| `$FF0A` | IRQ enable + raster compare bit 8 | b6 T3, b4 T2, b3 T1, b1 raster, **b0 = bit 8 of the raster compare**. Default `$A2`. |
| `$FF0B` | Raster compare bits 7–0 | Like `$D012` on write. |
| `$FF0C/0D` | Hardware cursor position (10 bit) | ≥ 1000 = invisible. |
| `$FF0E`, `$FF12` b1–0 | Voice 1 frequency (10 bit) | |
| `$FF0F`, `$FF10` b1–0 | Voice 2 frequency (10 bit) | `reg = 1023 - 110840.46875/f` (PAL), `1023 - 111860.78125/f` (NTSC). `$3FE` locks the voice. |
| `$FF11` | Sound control | b7 D/A mode, b6 voice 2 noise, b5 voice 2 square, b4 voice 1, b3–0 volume (max 8). |
| `$FF12` | b5–3 bitmap address (A15–A13, 8K steps), b2 char/bitmap fetch from ROM(1)/RAM(0), b1–0 voice 1 freq hi | Default `$C4`. |
| `$FF13` | b7–2 charset address (1K steps), **b1 force single clock**, b0 ROM/RAM status (read only) | Default `$D1`. |
| `$FF14` | b7–3 screen (attribute+char) memory address, 2K steps | Default `$0F` → `$0800`. The 2K block = 1K luma/attribute + 1K char codes. |
| `$FF15` | Background colour 0 | colour byte = `%0LLLCCCC` (luma b6–4, chroma b3–0) |
| `$FF16/17` | Multicolour / ECM colour 1, 2 | |
| `$FF18` | ECM colour 3 | |
| `$FF19` | Border colour | |
| `$FF1A/1B` | Character position counter (bitmap reload) | |
| `$FF1C/1D` | Current raster line (9 bit), **writable** | Writing it is how FLD-like/extended-border tricks work — keep the parity of the line (see 500279). |
| `$FF1E` | Horizontal position (writable) | Increases by 4 per character. |
| `$FF1F` | b6–3 flash counter, b2–0 line inside character row (writable) | |
| `$FF3E` | Any write → ROM visible at `$8000–$FFFF` | |
| `$FF3F` | Any write → RAM visible at `$8000–$FFFF` | `$FF20–$FF3D` follows the ROM/RAM switch. |

Colours: 15 chroma × 8 luma + black = 121 colours. `$71` = brightest colour 1 ("white"). [500024, 500025_color_codes.md, 500107_color_codes.md]

## Video modes  [500024_ted_registers.md#VideoModes, 500234, 500235, 500251]

- Text: screen memory 2K at `$FF14` (first 1K = luma/attribute, second 1K = character codes).
- Hires bitmap (BMM=1, MCM=0): pixel 0 = luma byte b6–4 + chroma byte b3–0, pixel 1 = luma b2–0 + chroma b7–4.
- Multicolour bitmap (BMM=1, MCM=1): `00`=`$FF15`, `01`=luma b2–0+chroma b7–4, `10`=luma b6–4+chroma b3–0, `11`=`$FF16`.
- ECM + MCM together → black screen (as on VIC-II).
- DEN=0 (screen off) gives the CPU ~10000 extra cycles per frame and makes the speed non-constant; set `$FF13` bit 1 for constant (single) speed.
- Two DMA ("bad") lines per character row; CPU is halted while TED fetches.
- The TED has **no sprites** (Programmer's Reference Guide preface); "sprites" on the Plus/4 are software sprites [500228_sprites.md, 500266_sprite.md].

## CPU speed  [500248_cpu_speed.md]

| Machine/mode | CPU Hz |
|---|---|
| PAL, screen on, double clock allowed | 1,147,196 (≈116 % of a PAL C64) |
| PAL, screen on, `$FF13` b1=1 (single) | 779,523 |
| PAL, screen off, double clock | 1,695,665 |
| NTSC, screen on, double clock | 1,052,124 |

PAL frame 49.86 Hz, NTSC 59.92 Hz. 1 cycle ≈ 0.5 µs (double) / 1.0 µs (single).

## Memory and banking  [500255_rom_banking.md, 500271_rom_autostarting.md, Programmer's Reference Guide Appendix G (PDF p. 437–451)]

- `$0000/$0001`: 7501/8501 on-chip I/O port (serial bus, datasette) — **not** a banking register as on the C64 [500290_cpu_i_o_registers.md].
- `$FF3E` / `$FF3F`: ROM / RAM at `$8000–$FFFF` (TED registers stay visible).
- `$FDD0–$FDDF`: ROM bank latch; address bits 1–0 = low ROM (`$8000–$BFFF`), bits 3–2 = high ROM (`$C000–$FFFF`). `$FDD0` = BASIC + KERNAL. `$FC00–$FCFF` is always KERNAL.
- Interrupts with a foreign ROM banked in: the IRQ vector comes from that ROM; KERNAL IRQ entry `$FCB3`, exit `$FCBE` restores the bank from ZP `$FB`.
- KERNAL long fetch `$FCF7` (and the other helpers in 500255).
- I/O at `$FD00`: ACIA (RS-232) `$FD00–$FD0F`, 6529 parallel port `$FD10–$FD1F`, keyboard latch `$FD30`, ROM bank latch `$FDD0–$FDDF` (checked against the page image of Appendix G, PDF p. 439 — the text layer of that table has shifted columns).
- ROM cartridge header: `$8000 JMP cold`, `$8003 JMP warm`, `$8006` module number (1 = autostart), `$8007` `"CBM"`.
- BASIC program text starts at `$1001` (pointer `$2B/$2C`).

## Interrupts  [Programmer's Reference Guide p. 297–299 (PDF 309–311), 500024]

- Hardware vector `$FFFE/$FFFF` is in ROM → KERNAL pushes A, X, Y and jumps through **`$0314/$0315`** (same as C64).
- Exit with `PLA / TAY / PLA / TAX / PLA / RTI`, or jump to the original `$0314` target.
- Raster IRQ: set `$FF0B` (+ `$FF0A` bit 0 for line ≥ 256), enable `$FF0A` bit 1, ack bit 1 in `$FF09`. Visible screen ≈ raster `$04`–`$CB`.
- Fully RAM-based IRQ (`$FF3F`, own `$FFFE/$FFFF` vector in RAM) needs your own register save.

## Keyboard / joystick  [500012_plus_4_keyboard_joystick_matrix.md]

- Write the column selector to **both** `$FD30` (keyboard) and `$FF08` (joystick), read `$FF08`. 0 bit = selected / pressed.
- Keyboard only: selector → `$FD30`, `$FF` → `$FF08`. Joystick only: `$FF` → `$FD30`, selector → `$FF08`.
- Joystick selector bit 1 (`$FD`) = port 2, bit 2 (`$FB`) = port 1. Fire: port 2 = bit 7, port 1 = bit 6.

## KERNAL jump table  [500232_kernal_routines.md]

Same table as the C64 from `$FF81` (`CHROUT $FFD2`, `GETIN $FFE4`, `PLOT $FFF0`, …) plus 264-only `DEFKEY $FF49`, `PRINT $FF4C`, `PRIMM $FF4F`, `MONITOR $FF52`.
C64 → Plus/4 ROM address cross reference: [500293_c64_to_plus_4_rom_xrefmap.md].

## Known ROM bugs

- `$FF28` bug: TEDMON + `DS$` writes `$28,$FF` into RAM (often `$304C`/`$3058`) [500015_ff28_bug.md].
- `DS` / `DS$` string-heap bug [500292_ds_bug.md].
