---
name: plus4-search
description: >
  Search the offline Plus/4 knowledge base: 292 Plus/4 World Encyclopedia topics
  plus the full text of 11 Plus/4 / C16 books (Programmer's Reference Guide,
  Hungarian machine-code books, C16 ROM listing, C16 Intern). Activate when the
  user asks to find or look up a Plus/4 / C16 routine, register, ROM address,
  BASIC 3.5 command, demo effect, tape format or technique, says "keress",
  "nézd meg a könyvekben", "van erről valami", "find in the encyclopedia",
  "what does the ROM do at $xxxx", or names effects like FLI, FLD, DYCP, tech-tech,
  raster split, digi playback on the Plus/4.
---

# Plus/4 knowledge base search

## Where

Knowledge root: `../../knowledge/` relative to this skill's base directory
(fallback: `F:\Development\Plus4AssemblyExpert\knowledge\`).

| Path | Content |
|---|---|
| `sources/plus4encyclopedia/INDEX.md` | Topic list by category (FAQ, Glossary/Demos, Hardware, Programming/Assembly, Audio, BASIC, General, Reference/6502, KERNAL, Memory Map, TAP files, BASIC errors, History) |
| `sources/plus4encyclopedia/pages/NNNNNN_title.md` | One topic per file; first lines give source URL, category, keywords |
| `sources/plus4encyclopedia/files/kb/` | Images referenced by the topics (palettes, effect screenshots, schematics) |
| `sources/pdfs/BOOKS.md` | What each book covers and where (PDF page ranges) |
| `sources/pdfs/<book>.txt` | Full book text, `--- PAGE n ---` markers = PDF page numbers |

## How

1. Grep the encyclopedia first, then the book texts. Try several variants:
   the register (`\$FF0A`, `FF0A`, `65290`), the English and the Hungarian term
   (`raster` / `raszter`, `interrupt` / `megszakítás` / `megszakitas`), and the KERNAL name.
   ```
   Grep pattern="\$FF1D" path="<root>/sources/plus4encyclopedia/pages" output_mode="files_with_matches"
   Grep pattern="(?i)FF[0O]B" path="<root>/sources/pdfs" glob="*.txt" output_mode="count"
   Grep pattern="(?i)megszak" path="<root>/sources/pdfs" glob="*.txt" output_mode="content" -C 2
   ```
   In the OCR'd books `$FF0B` is usually spelled `FFOB`: the exact pattern finds it in 1 book,
   `FF[0O]B` in 7. Always make register searches OCR-tolerant in the book texts.
   For a ROM address, use `sources/pdfs/rom_lista_address_index.md` (Erdős ROM lista) or
   `c16_intern_address_index.md` to get the PDF page directly.
2. The book texts are Windows OCR without Hungarian language support: accented letters are
   often wrong (`ő`→`ö`/`6`, `á`→`é`), and `0/O`, `8/B`, `1/l/I` get swapped. Search with
   accent-free fragments (`megszak`, `regiszt`, `rutin`) and allow for `[0O]`, `[8B]`.
3. Read the best 1–3 hits. For a book hit, note the `--- PAGE n ---` number; when an exact
   value or a code listing matters, open that PDF page in the project copy
   (`F:\Development\Plus4AssemblyExpert\knowledge\sources\pdfs\<book>.pdf`) and read it from the image.
4. Report: the answer, the file name (+ PDF page), the assembler syntax of any code found
   (TEDMON listings, TASS, Kick Assembler), and what to change for Kick Assembler.

## Quick map

| Topic | Start with |
|---|---|
| TED registers, video modes, palette | `500024_ted_registers.md` |
| Raster IRQ, timers | `500024_ted_registers.md#FF09`, Programmer's Ref. Guide PDF p. 309–311 |
| ROM banking, long call/fetch | `500255_rom_banking.md`, `500271_rom_autostarting.md` |
| CPU port `$00/$01` | `500290_cpu_i_o_registers.md` |
| CPU speed / cycle budget | `500248_cpu_speed.md` |
| Keyboard, joystick | `500012_plus_4_keyboard_joystick_matrix.md` |
| KERNAL jump table | `500232_kernal_routines.md`, `500242_chrout_ffd2.md`, `500283_plot_fff0.md` |
| C64 → Plus/4 ROM addresses | `500293_c64_to_plus_4_rom_xrefmap.md` |
| C64 → Plus/4 colours | `500291_converting_commodore_64_colors_to_plus_4_colors.md` |
| Sound, frequency table, digis | `500244_ted_sound_generation_internals.md`, `500243_frequency_table.md`, `500201_digi_playback.md` |
| Demo effects | Glossary/Demos section of `INDEX.md` (FLI, FLD, DYCP, tech-tech, raster split, …) |
| Border tricks, non-standard frames | `500152_writing_to_the_border.md`, `500268_extended_vertical_border.md`, `500279_practical_tips_for_non_standard_video_modes.md` |
| Tape formats / TAP | Reference/TAP files section |
| BASIC 3.5 | Reference/Commodore BASIC V3.5 section, Programmer's Ref. Guide ch. 1 |
| Full memory map | Programmer's Ref. Guide Appendix G (PDF p. 437–451) |
| ROM disassembly | `commodore_rom_lista_c-16_plus4_c-116(1986).txt` |
| Hardware internals | `a_commodore-16-os_belso_felepitese(1986).txt` |
