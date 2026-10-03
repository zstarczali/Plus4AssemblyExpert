---
name: plus4-debug
description: >
  Debug and review Commodore Plus/4 / C16 assembly code. Activate when the user
  pastes Plus/4, C16, C116 or TED-based 6502/7501/8501 code and asks what is
  wrong, why it crashes, why the raster IRQ fires wrong or only once, why the
  screen or colours look wrong, why the bitmap is garbage, why the timing is off,
  why the sound locks up, or asks for a code review. Also for "hibakeresés",
  "mi a baj ezzel", "miért nem működik" when the code touches $FFxx TED registers.
---

# Plus/4 assembly code debug

Work through the checklist, then report. Load `../plus4-expert/references/ted-quick-reference.md`
for register details; every item below has its source there or in the named encyclopedia page.

## Checklist

### 1. Platform mix-ups (most common when code comes from the C64)
- [ ] Any `$D000–$DFFF` I/O (VIC-II, SID, CIA), `$D020`, `$DC0D`, `$DD00`? None of it exists — TED is at `$FF00–$FF3F`.
- [ ] `$01` used for banking? On the 264 it is only the CPU I/O port (serial bus, datasette) [500290]. Banking = `$FF3E`/`$FF3F` + `$FDD0–$FDDF`.
- [ ] Hardware sprites assumed? TED has none.
- [ ] Load address `$0801`? Plus/4 / C16 BASIC starts at `$1001`.
- [ ] C64 colour indices (0–15) written to colour registers? TED wants `%0LLLCCCC` [500291 for conversion tables].
- [ ] Direct calls into C64 BASIC/KERNAL ROM addresses? Only the `$FF81–$FFF3` jump table is shared; map the rest with [500293].

### 2. Memory / banking
- [ ] Code, data, bitmap or charset placed under ROM (`$8000–$FFFF`) and read while ROM is banked in? Write `$FF3F` first, and remember the KERNAL IRQ expects ROM.
- [ ] RAM-only operation (`$FF3F`) without own vectors at `$FFFA–$FFFF` in RAM → crash on the first IRQ/NMI.
- [ ] Cartridge/function ROM banked in during IRQ: vector comes from that ROM; use `$FCB3` entry / `$FCBE` exit and set ZP `$FB` [500255].
- [ ] C16 target: does everything fit in 16K (`$0000–$3FFF`)? Function ROM banks absent on C16.

### 3. TED video setup
- [ ] Screen block `$FF14` (b7–3, 2K steps): first 1K = attributes/luma, second 1K = character codes.
- [ ] Bitmap `$FF12` b5–3 (8K steps) and `$FF12` b2 = 0 to fetch from RAM; charset `$FF13` b7–2 (1K steps).
- [ ] Read-modify-write used on `$FF12`/`$FF13`? Those registers also hold voice-1 frequency bits and the single-clock bit — don't clobber them.
- [ ] Bitmap mode = `$FF06` bit 5, multicolour = `$FF07` bit 4; ECM+MCM → black screen.
- [ ] Hires bitmap colours come from the 2K attribute block (luma byte + chroma byte), not from `$FF15` alone.

### 4. Interrupts
- [ ] Vector set in `$0314/$0315` (KERNAL path) or `$FFFE/$FFFF` (RAM path) under `SEI`?
- [ ] IRQ acknowledged by writing the handled bits back to `$FF09` (`LDA $FF09 / STA $FF09`, or `LDA #$02 / STA $FF09` for raster only)? Without it the IRQ re-fires immediately.
- [ ] Raster enable is `$FF0A` bit 1; raster compare bit 8 is `$FF0A` bit 0 — a plain `STA $FF0A` of `$02` clears bit 8 and other enables.
- [ ] KERNAL-path exit restores Y, X, A (`PLA/TAY/PLA/TAX/PLA/RTI`) or jumps to the original `$0314` target.
- [ ] Raster line in the visible range (~`$04`–`$CB`) and below the frame length (312 PAL / 262 NTSC)?
- [ ] Writing `$FF1C/$FF1D` (frame tricks): parity kept, written at a fixed position every frame [500279].

### 5. Timing
- [ ] Cycle counts assume one clock speed? CPU runs double clock outside DMA lines and border; `$FF13` bit 1 forces single [500248].
- [ ] Screen blanked (`$FF06` bit 4 = 0) changes the per-frame cycle budget.
- [ ] TED timers: LO written before HI, little delay between them; timers count single-clock cycles; timer 2/3 wrap to `$FFFF`.

### 6. Keyboard / joystick
- [ ] Selector written to `$FD30` **and** `$FF08`, result read from `$FF08`? Write `$FF` to the other latch to read keyboard or joystick alone [500012].
- [ ] Joystick bits: port 2 selector `$FD`, port 1 `$FB`; fire bit 7 (port 2) / bit 6 (port 1).

### 7. Sound
- [ ] Frequency register value `$3FE` locks the voice; formula `1023 - clock/f` [500024#FF0F].
- [ ] Volume in `$FF11` b3–0 (max 8); voice-2 noise and square bits both set → square.

### 8. Generic 6502
- [ ] `CLC`/`SEC` before `ADC`/`SBC`; branch range; `JMP ($xxFF)` page bug; ZP use colliding with KERNAL/BASIC (see Appendix G of the Programmer's Ref. Guide).

## Report format

For each issue: **what** (one sentence), **where** (line/label), **why** (TED/CPU behaviour + source),
**fix** (corrected snippet, named assembler). Then list the checklist sections that were clean.
