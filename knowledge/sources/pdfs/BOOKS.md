# Plus/4 / C16 könyvek

Minden könyvhöz tartozik egy `.txt` (azonos névvel), benne `--- PAGE n ---` jelölők, ahol **n = PDF-oldal**.
A könyvben nyomtatott oldalszámból a PDF-oldal: **PDF = könyvoldal + eltolás**.

Szövegforrás: a *Programmer's Reference Guide* saját szövegrétegéből, a többi Windows OCR-rel (en-US,
mert a gépen nincs magyar OCR-nyelv): a magyar ékezetek, valamint `0/O`, `8/B`, `5/S`, `1/l/I` gyakran
hibásak, a táblázatok oszlopai elcsúszhatnak. Pontos értékhez nyisd meg a PDF-oldalt (csak a projektben:
`F:\Development\Plus4AssemblyExpert\knowledge\sources\pdfs\`).

---

## 1. Programmer's Reference Guide for the Commodore Plus/4 (Merten – Meyer, 1986) — angol
- **Fájl:** `programmers_reference_guide_for_the_commodore_plus_4.pdf` / `.txt` (465 oldal, szövegréteg)
- **Eltolás:** +12 (könyv 1. oldal = PDF 13)
- **Fejezetek (PDF-oldal):** 1. BASIC 3.5 parancsok 13 · 2. Beépített szoftver (3-plus-1) 110 · 3. Programozási technikák 164 (Escape-billentyűk 169, funkcióbillentyűk 181, hang és zene 187) · 4. Grafika 198 (memória-összefoglaló 237) · 5. Gépi kód a Plus/4-en 239 (TEDMON parancsok 241, 6502 utasításkészlet 251–308, **megszakítások / raszter IRQ 309–312**, operációs rendszer 315, BASIC-kapcsolat 329) · 6. Perifériák 335 (lemez 337, datasette 373, nyomtató 383, modem/RS-232 393, joystick 403) · A: hibaüzenetek 407 · B: BASIC tokenek 418 · C/D/E: CHR$, ASCII, képernyőkódok 420–432 · F: hangjegytáblák 433 · **G: memória- és regisztertérkép 437–451** · tárgymutató 452
- **Használd ha:** hivatalos BASIC 3.5 szintaxis, KERNAL/OS működés, IRQ, teljes zero page / memóriatérkép, TED regiszter-összefoglaló, perifériák gépi kódból.

## 2. Commodore C16 and Plus/4 Reference Book — angol
- **Fájl:** `Commodore_C16_Plus4_Reference_Book.pdf` / `.txt` (213 oldal, OCR)
- **Eltolás:** +3
- **Fejezetek (könyvoldal):** 2. Grafika: TED grafikus lehetőségei 6, saját karakterkészlet 7, hires 10, multicolor 17, extended colour 30, soft scroll 33, **raster interrupt 35**, TED technikai részletek 44 · 3. Hang: BASIC 47, **TED hangregiszterek 50**, IRQ-vezérelt zene 51 · 4. Gépi kód: bevezetés 55, 7501 utasítások 70, **KERNAL rutinok használata 79**, **memóriatérkép 155**, **TED memóriatérkép 180**, KERNAL ugrótábla 184, **CBM-64 ↔ C-16 összehasonlító táblázat 187** · 5. Segédprogramok: véletlenszám 196, joystick 199, **C-16 turbo mód 200**, OLD 201, MERGE 203, VARLIST 205, CROSS 206 · 6. Függelék: BASIC tokenek 208
- **Használd ha:** angol nyelvű, példakódos TED grafika/hang/IRQ, C64 ↔ C16 különbségek.

## 3. A Commodore 16-os belső felépítése (1986) — magyar (a „64 Intern” megfelelője)
- **Fájl:** `a_commodore-16-os_belso_felepitese(1986).pdf` / `.txt` (424 oldal, OCR; a tartalomjegyzék a PDF 422. oldalán)
- **Eltolás:** kb. −7 (pl. RAM-térkép: könyv 87 → PDF 80)
- **Tartalom (könyvoldal):** 1. A gépről, ROM működése 13 · 2. Processzor: architektúra, utasításkészlet, címzési módok 20, interrupt 23, RESET 24 · 3. KERNAL: felhasználói gépi kódú szubrutinok 25–35 · 4. Videó: karakteres módok 37, multicolor, extended color, kurzor, hires/multicolor bitmap, képméret-csökkentés/soft scroll, BLANK 43, PAL/NTSC, FREEZE (TED leállítása), fényceruza 44, **raszter-interrupt** · 5. Hang · 6. I/O: billentyűzet 51, joystick 51, időzítők 52, processzorport 53, magnetofon, IEC busz 54–56, cartridge · 7. BASIC interpreter működése 59–65 (tokenek, tárkezelés, változók, lebegőpont, kifejezés-kiértékelés, SYS/USR, BASIC-bővítés) · Függelék: 6502 opkódok 68, végrehajtási idők 70, **TED regisztertérkép 73**, idegen kifejezések 77, MONITOR utasítások, **C16 RAM-térkép 87**, **C16 ROM-lista 95–** (BASIC és KERNAL, kommentezett) · irodalom 429
- **ROM-cím → oldal:** `c16_intern_address_index.md`
- **Használd ha:** mély hardver-/ROM-működés magyarul, KERNAL és BASIC belső rutinok.

## 4. Erdős Iván: Commodore ROM lista — Plus/4, C-16, C-116 (LSI, 1986) — magyar
- **Fájl:** `commodore_rom_lista_c-16_plus4_c-116(1986).pdf` / `.txt` (284 oldal, OCR 300 dpi)
- **Eltolás:** +1
- **Tartalom:** bevezetés (PDF 5–6) · **teljes, magyarul kommentezett ROM-diszasszembláció `$8000`–`$FFFF` (PDF 7–223)** · Műhelytitkok (könyv 223 → PDF 224) · keresztreferencia-táblázat (könyv 235 → PDF 236) · tartalom PDF 283
- **ROM-cím → oldal:** `rom_lista_address_index.md`
- **Használd ha:** egy ROM-cím pontos kódja/kommentje kell, ROM-rutin bemenetei-kimenetei, C64 → Plus/4 ROM-portolás (együtt az enciklopédia `500293_c64_to_plus_4_rom_xrefmap.md` oldalával).

## 5. Bábán Gábor – Mása István: Gépi kódú programozás kezdőknek és haladóknak (C 16 és Plus/4, Novotrade) — magyar
- **Fájlok (ugyanaz a könyv két szkennben):**
  `gepi_kodu_programozas_kezdoknek_es_haladoknak.pdf` / `.txt` (212 oldal, eltolás 0) és
  `Gepi kodu programozas kezdoknek es haladoknak.pdf` / `.txt` (213 oldal, eltolás +1). Ha az egyik OCR-je rossz egy oldalon, nézd a másikat.
- **Fejezetek (könyvoldal):** 1. Kezdőknek: BASIC vs gépi kód 7, számrendszerek 9, **8501 regiszterei 13**, utasítások és címzési módok 16, **TEDMON 43**, assembler 49 · 2. Haladóknak: gépi rutinok 61, **grafikus üzemmódok 63**, aritmetika 74, **megszakítások 84**, billentyűzet 94, **hanggenerálás 98**, **tárfelosztás, memórialapozás 101**, BASIC programok/változók tárolása 107, **ROM-rutinok jegyzéke 112**, rendszerváltozók 133, I/O programozás 144, **TED regisztertérkép 174** · Függelék: képernyőmemória, szín/fényerő-memória 180, képernyőkódok 181, ASCII 183, BASIC tokenek 188, frekvenciatáblázat 191, átváltás 193, gépi utasítások összefoglalója 200
- **Használd ha:** magyar nyelvű, rendszerezett tankönyv; ROM-rutinok leírása belépési ponttal; IRQ, hang, banking.

## 6. Gudenus László: Bevezetés a Commodore Plus/4-es gépi kódú programozásba (PMPI, 1989) — magyar
- **Fájl:** `bevezetes_a_commodore_plus_4-es_gepi_kodu_programozasba_i.pdf` / `.txt` (84 oldal, OCR)
- **Eltolás:** +3
- **Fejezetek (könyvoldal):** bevezetés 2 · előismeretek 4 · a processzor 7 · írjunk a képernyőre 12 · aritmetika 25 · csillagok, villogás 37 · számoljunk tovább 48 · mire használhatjuk 63 · utasítástáblázat 74 · JCL-segédlet (assembler) PDF 82–83
- **Használd ha:** kezdő szintű, lépésenkénti Plus/4 gépi kód példák.

## 7. Gudenus László: Fejezetek a Commodore Plus/4-es gépi kódú programozásából (PMPI, 1990) — magyar
- **Fájl:** `fejezetek_a_commodore_plus_4-es_gepi_kodu_programozasabol.pdf` / `.txt` (154 oldal, OCR)
- **Eltolás:** +1. A 6. kötet folytatása; feladatgyűjtemény BASIC-keretprogramokkal és gépi kódú rutinokkal.
- **Fejezetek (PDF):** tartalom/programlista 4 · 1. titkosírás 7 · 2. monitor 15 · 3. tükrözés 25 · 4. prímek 32 · 5. két képernyő 38 · 7. hangsebesség 55 · 8. pulzálás 60 · 9. sorok 65 · 10–11. színezés 68–71 · 12. fényújság 75 · forráslisták a végén
- **Használd ha:** kidolgozott grafikai/hang/aritmetikai gépi kódú példák, paraméterátadás BASIC-ből.

## 8. Commodore 16 programozói zsebkönyv — magyar
- **Fájl:** `commodore_16_programozoi_zsebkonyv.pdf` / `.txt` (81 oldal, OCR; tartalomjegyzék PDF 3–4)
- **Eltolás:** kb. +2
- **Tartalom (könyvoldal):** BASIC rész: szintaktikus elemek és tárolásuk 4, BASIC 3.5 utasítások 6, függvények, rendszerváltozók 8, perifériák és I/O 9–10, billentyűzet és mátrix 11, képernyő, escape-szekvenciák 12–14, grafikus képernyő 15 · Gépi kód rész: TED grafikus regiszterei 32, karakteres módok 34, nagyfelbontás 36, scroll, TED 39, NTSC · utasítások 41, párhuzamos port 43, **KERNAL táblázatok és rutinok 44–46**, BASIC-kapcsolatos memóriacímek, szabad területek 48, interpreter belépési pontok 49, paraméterátadás 50–52, kazetta 53, TEDMON 55 · függelék
- **Használd ha:** gyors magyar referencia (cím, rutin, escape-kód).

## 9. Gyetvai Károly: Assembly és gépi szintű programozás Commodore 16, Plus/4 számítógépen (1991) — magyar
- **Fájl:** `assembly_es_gepi_szintu_programozas_commodore_16_plus_4_szamitogepen.pdf` / `.txt` (47 oldal, OCR)
- **Eltolás:** +1
- **Fejezetek (PDF):** bevezetés 6 · regiszterek 7 · I/O eszközök, billentyűmátrix 10 · megszakítások 13 · utasításkészlet 14 · TEDMON parancsok 19–20 · assembly alapfeladatok 24 · lebegőpontos aritmetika gépi kódban 27 · gyakori KERNAL rutinok 28 · gépi kód BASIC-be építése 31 · képernyőkódok 42 · fontosabb memóriacímek 45 · aritmetikai rutinok belépési címei 46
- **Használd ha:** tömör magyar összefoglaló, lebegőpontos ROM-rutinok címei.

## 10. C16 Machine Language for the Absolute Beginner — angol
- **Fájl:** `c16_machine_language_for_the_absolute_beginner_002.pdf` / `.txt` (172 oldal, OCR)
- **Eltolás:** +8
- **Fejezetek (könyvoldal):** 1. bevezetés 3 · 2. alapok, regiszterek, címzési módok, képernyőmemória 7 · 3. hexadecimális 17 · 4. TEDMON 25 · 5. számok, carry, összeadás/kivonás 33 · 6. programvezérlés, elágazások 41 · 7. ciklusok, indexelés 47 · 8. táblázatok, grafikus karakterek, indirekt címzés 57 · 9. státuszflagek 63 · további fejezetek a PDF 5–7. oldali tartalomjegyzékben
- **Használd ha:** angol nyelvű kezdő tankönyv C16-ra.
