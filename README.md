# Plus/4 Assembly Agent Pack

Forrásalapú Commodore Plus/4 / C16 / C116 (264-es család) assembly szakértő csomag Claude-hoz,
a C64AssemblyExpert mintájára.

## Tartalom

| Hely | Mi van benne |
|---|---|
| `SYSTEM_PROMPT.md` | Általános agent prompt |
| `CLAUDE.md` | Claude projektinstrukciók |
| `knowledge/index.md` | Téma → forrás index (itt kezdj) |
| `knowledge/sources/plus4encyclopedia/` | A Plus/4 World Encyclopedia offline tükre: 292 topic Markdownban (`pages/`), 162 kép/fájl (`files/`), kategóriaindex (`INDEX.md`), letöltő szkript |
| `knowledge/sources/pdfs/` | 11 könyv teljes szövege `.txt`-ben (`--- PAGE n ---` = PDF-oldal), `BOOKS.md` könyvleírások oldaltérképpel. A PDF-ek nincsenek a git repóban (530 MB, kettő 100 MB fölött) — másold ide őket a `C:\Users\rlung\iCloudDrive\Plus4` mappából |
| `knowledge/sources/urls/reference-sites.md` | Külső hivatkozások |
| `plugin/` | Claude Code plugin forrása: 4 skill + a tudásbázis másolata (PDF-ek nélkül) |
| `plus4-assembly-expert.plugin` | Telepíthető plugin csomag (zip) |

## Skillek

| Skill | Mire |
|---|---|
| `plus4-expert` | Általános Plus/4 / C16 / TED assembly kérdések, Kick Assembler kód |
| `plus4-search` | Keresés az enciklopédiában és a könyvek szövegében |
| `plus4-debug` | Plus/4 kód hibakeresés, checklist (TED, IRQ, banking, időzítés) |
| `plus4-c64-port` | C64 kód portolása Plus/4-re, VIC-II/SID/CIA → TED megfeleltetés |

## Frissítés / újraépítés

```bash
cd knowledge/sources/plus4encyclopedia
python download_plus4encyclopedia.py all     # új/módosult topicok letöltése, Markdown újragenerálás
cd ../pdfs
python ocr_pdfs.py                           # szkennelt PDF-ek OCR-je (Windows OCR, PowerShell 5.1)
cd ../../..
python build_plugin.py                       # plugin/knowledge frissítése + .plugin csomag
```

- Az enciklopédia `raw/` mappája HTML-cache: egy fájl törlése után az újra letöltődik.
  Az index oldalt minden futás frissíti, így az új topicok automatikusan bekerülnek.
- Az OCR jelenleg en-US nyelvvel fut (a gépen nincs magyar Windows OCR nyelv), ezért a magyar
  ékezetek egy része hibás. Ha a Windows beállításokban telepíted a magyar nyelvhez tartozó
  OCR-t, `OCR_LANG=hu-HU` mellett a `.txt` fájlok törlése után újra lehet futtatni.

## Források

- Plus/4 World Encyclopedia — https://plus4world.powweb.com/plus4encyclopedia (© Plus/4 World Team)
- A felhasználó saját Plus/4 könyvgyűjteménye (`C:\Users\rlung\iCloudDrive\Plus4`), lásd `knowledge/sources/pdfs/BOOKS.md`
