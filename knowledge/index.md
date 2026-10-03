# Plus/4 Assembly Expert – Knowledge Index

A Plus/4 / C16 / C116 (264-es család) tudásbázis témaindexe. Gyökér: `knowledge/`.

Források:
- **ENC** = Plus/4 World Encyclopedia offline tükre: `sources/plus4encyclopedia/pages/<fájl>.md` (292 topic; teljes lista: `sources/plus4encyclopedia/INDEX.md`)
- **Könyvek** = `sources/pdfs/<könyv>.txt` (teljes szöveg, `--- PAGE n ---` = PDF-oldal); leírás és fejezettérkép: `sources/pdfs/BOOKS.md`
  - **PRG** = Programmer's Reference Guide for the Commodore Plus/4 · **REF** = C16 and Plus/4 Reference Book · **INTERN** = A Commodore 16-os belső felépítése · **ROM** = Erdős: Commodore ROM lista · **BM** = Bábán–Mása: Gépi kódú programozás kezdőknek és haladóknak · **ZSEB** = C16 programozói zsebkönyv · **GY** = Gyetvai: Assembly és gépi szintű programozás · **BEV/FEJ** = Gudenus két füzete · **ABS** = C16 Machine Language for the Absolute Beginner
- Gyorsreferencia (forráshivatkozásokkal): `../plugin/skills/plus4-expert/references/ted-quick-reference.md`

Az oldalszámok **PDF-oldalak**.

---

## Hardver, CPU

| Téma | ENC | Könyvek |
|---|---|---|
| 7501/8501 CPU, regiszterek | `500149_6502_registers.md` | PRG 251–308 · BM PDF 13 · GY 7 |
| CPU I/O port `$00/$01` | `500290_cpu_i_o_registers.md` | INTERN processzorport (I/O fejezet) |
| CPU sebesség, single/double clock | `500248_cpu_speed.md` | — |
| 6502 utasítások, címzési módok | `500021_6502_opcodes.md`, `500016_6502_addressing_modes.md`, ADC/AND/ASL/LDA/LDX/LDY oldalak | PRG 251–308 · BM 16–42 · INTERN függelék |
| BCD | `500150_bcd.md` | — |
| Hardver általában, hibaelhárítás | Hardware, Hardware/Troubleshooting kategóriák (`INDEX.md`) | INTERN 1. fejezet |

## TED – videó

| Téma | ENC | Könyvek |
|---|---|---|
| TED regiszterek `$FF00–$FF3F` (teljes leírás) | `500024_ted_registers.md` | PRG App. G 437–451 · REF 183 · BM 174 · INTERN 66 |
| Videómódok (text, MCM, ECM, hires, multicolor bitmap) | `500024_ted_registers.md#VideoModes` | REF 9–36 · PRG 198–238 · BM 63 |
| Paletta, színkódok (luma/chroma) | `500024_ted_registers.md#Palette`, `500025_color_codes.md`, `500107_color_codes.md`, `500063_color_sources.md` | — |
| C64 színek → Plus/4 | `500291_converting_commodore_64_colors_to_plus_4_colors.md` | — |
| Bitmap megjelenítés | `500234_how_to_display_a_multicolor_bitmap.md`, `500251_load_hires_multi_bitmap_to_the_screen.md` | REF 13–32 |
| Saját karakterkészlet | `500235_how_to_use_a_selfdefined_charset_in_multicolor_mode.md`, `500250_useful_poke_s_and_custom_charset.md` | REF 10 |
| Képformátumok | `500289_image_file_formats.md` | — |
| Border, kiterjesztett keret, nem szabványos frame | `500152_writing_to_the_border.md`, `500268_extended_vertical_border.md`, `500279_practical_tips_for_non_standard_video_modes.md` | — |
| Szoftveres sprite-ok (TED-nek nincs hardveres) | `500228_sprites.md`, `500266_sprite.md`, `500267_sprite_scroll.md`, `500192_bobs.md` | — |
| Vonalhúzás | `500253_fast_line_draw.md` | — |

## Megszakítások, időzítők

| Téma | ENC | Könyvek |
|---|---|---|
| IRQ flag/enable `$FF09/$FF0A`, raszter `$FF0B` | `500024_ted_registers.md#FF09` | PRG 309–312 (raszter IRQ példa) · REF 38 · BM 84 · INTERN raszter-interrupt · GY 13 |
| TED timerek `$FF00–$FF05` | `500024_ted_registers.md#FF00` | INTERN időzítők (I/O fejezet) |
| Raster split, FLD, FLI, stb. | Glossary/Demos kategória: `500230_raster_split.md`, `500028_fld.md`, `500027_fli.md`, `500216_linecrunch.md`, `500217_agsp.md`, `500215_hsp.md` | — |

## Hang

| Téma | ENC | Könyvek |
|---|---|---|
| TED hangregiszterek, belső működés | `500244_ted_sound_generation_internals.md`, `500024_ted_registers.md#FF0E` | REF 53–54 · BM 98 · PRG 187–197 |
| Frekvenciatábla, decibel | `500243_frequency_table.md`, `500288_decibel_values.md` | BM függelék 191 · PRG App. F 433 |
| Digi lejátszás | `500201_digi_playback.md`, `500270_digimuz_support.md` | — |
| SID kártyák | `500269_sid_support.md` | — |

## Memória, banking, ROM

| Téma | ENC | Könyvek |
|---|---|---|
| Memóriatérkép, zero page | `500237_memory_map.md` | **PRG App. G 437–451** · REF 158–182 · INTERN RAM-térkép 80 · ZSEB 48 · GY 45 |
| ROM/RAM váltás `$FF3E/$FF3F`, bankváltó `$FDD0` | `500255_rom_banking.md` | BM 101 |
| ROM autostart, cartridge fejléc | `500271_rom_autostarting.md` | INTERN cartridge |
| ROM diszasszembláció | — | **ROM 7–223** (`rom_lista_address_index.md`) · INTERN 88– (`c16_intern_address_index.md`) |
| C64 ↔ Plus/4 ROM címek | `500293_c64_to_plus_4_rom_xrefmap.md` | REF 190 (CBM-64 ↔ C-16) |
| KERNAL ugrótábla | `500232_kernal_routines.md`, `500242_chrout_ffd2.md`, `500282_bsout_ffd2.md`, `500285_basin_ffcf.md`, `500284_getin_ffe4.md`, `500283_plot_fff0.md` | REF 82–157, 187 · BM ROM-rutinok 112 · ZSEB 44–46 · GY 28 · INTERN 3. fejezet |
| ROM hibák | `500015_ff28_bug.md`, `500292_ds_bug.md` | — |

## Billentyűzet, joystick, perifériák

| Téma | ENC | Könyvek |
|---|---|---|
| Billentyű/joystick mátrix `$FD30` + `$FF08` | `500012_plus_4_keyboard_joystick_matrix.md` | BM 94 · INTERN 51 · GY 10 · ZSEB 11 · PRG 403 |
| Billentyűzet tiltás, autorepeat, escape | `500031_disabling_keyboard.md`, `500029_how_do_i_disable_keyboard_s_auto_repeat.md`, `500020_escape_key_codes.md`, `500202_disable_c_shift.md` | PRG 169 |
| Lemez, soros busz | `500032_disabling_all_serial_peripherals.md` | PRG 337–372 · INTERN IEC busz |
| Kazetta, TAP formátumok | Reference/TAP files kategória (`500247_tap_files.md`, Novaload, Razorload, …) | PRG 373 |
| RS-232 / modem | — | PRG 393 |

## BASIC 3.5, TEDMON

| Téma | ENC | Könyvek |
|---|---|---|
| BASIC 3.5 parancsok | Reference/Commodore BASIC V3.5 kategória | **PRG 13–109** · ZSEB 6–31 |
| BASIC tárolás, tokenek | `500211_basic_format.md` | PRG App. B 418 · INTERN 7. fejezet · BM 107 |
| BASIC hibaüzenetek | Reference/BASIC Error Messages, `500035_list_of_basic_error_messages.md` | PRG App. A 407 |
| BASIC ↔ gépi kód, SYS, paraméterátadás | — | PRG 329–334 · GY 31 · ZSEB 50 · FEJ |
| TEDMON | `500086_tedmon.md` | PRG 241 · BM 43 · GY 19 · ABS 4. fejezet · ZSEB 55 |

## Demóeffektek, technikák

Glossary/Demos kategória az `INDEX.md`-ben (DYCP, DYPP, tech-tech, plasma, rasterbars, FPP, FPD, shadebobs, tunnel, texture mapping, …).

## Eszközök, történet

- Ajánlott eszközök: `500265_curated_tools_list_what_should_i_use.md`
- History kategória, FAQ kategória (`INDEX.md`)
