# Plus/4 Assembly Expert Plugin

Commodore Plus/4 / C16 / C116 (264 family) assembly expert for Claude Code.

## Skills

- `plus4-expert` — TED (`$FF00–$FF3F`), memory map and banking, 7501/8501, IRQ, sound,
  keyboard, KERNAL, BASIC 3.5. Defaults to Kick Assembler with a `$1001` BASIC stub.
  Reference: `skills/plus4-expert/references/ted-quick-reference.md`.
- `plus4-search` — Grep-based search across the bundled encyclopedia and book texts.
- `plus4-debug` — review checklist for Plus/4 code (C64 leftovers, banking, TED setup, IRQ ack, timing).
- `plus4-c64-port` — C64 → Plus/4 translation table and porting workflow.

## Bundled knowledge (`knowledge/`)

- `sources/plus4encyclopedia/` — offline mirror of the Plus/4 World Encyclopedia
  (https://plus4world.powweb.com/plus4encyclopedia): 292 topics as Markdown + images.
- `sources/pdfs/*.txt` — full text of 11 Plus/4 / C16 books (OCR for the scanned ones),
  `BOOKS.md` describes them. The PDFs themselves stay in the project
  (`F:\Development\Plus4AssemblyExpert\knowledge\sources\pdfs\`).
- `index.md` — topic → source map.

No external tools or MCP servers required.
