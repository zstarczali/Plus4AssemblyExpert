#!/usr/bin/env python3
"""
OCR the scanned (text-less) PDFs with the built-in Windows OCR engine.

  python ocr_pdfs.py [pdf ...]      # default: every PDF here without a text layer

Pages are rendered with pypdfium2 into ocr_work/<pdf-stem>/, OCR'd by ocr_dir.ps1
(Windows PowerShell 5.1, WinRT OCR), then re-assembled into <pdf-stem>.txt with
"--- PAGE n ---" markers. Resumable: already rendered/OCR'd pages are skipped.
Set OCR_LANG (e.g. hu-HU) once that Windows OCR language is installed.
"""

import os
import subprocess
import sys
from pathlib import Path

import pypdfium2 as pdfium

HERE = Path(__file__).parent
WORK = HERE / "ocr_work"
LANG = os.environ.get("OCR_LANG", "en-US")
DPI = {"commodore_rom_lista_c-16_plus4_c-116(1986)": 300}
DEFAULT_DPI = 220


def has_text(doc: pdfium.PdfDocument) -> bool:
    sample = range(0, min(len(doc), 20))
    return sum(len(doc[i].get_textpage().get_text_range().strip()) for i in sample) > 500


def render(pdf: Path, outdir: Path) -> int:
    doc = pdfium.PdfDocument(str(pdf))
    outdir.mkdir(parents=True, exist_ok=True)
    scale = DPI.get(pdf.stem, DEFAULT_DPI) / 72
    for i in range(len(doc)):
        png = outdir / f"p{i + 1:04d}.png"
        if png.exists() or (outdir / f"p{i + 1:04d}.txt").exists():
            continue
        doc[i].render(scale=scale).to_pil().convert("L").save(png)
    return len(doc)


def assemble_page(raw: str) -> str:
    """Merge OCR lines that sit on the same baseline (multi-column tables, listings)."""
    items = []
    for ln in raw.splitlines():
        parts = ln.lstrip("﻿").split("\t", 3)
        if len(parts) != 4:
            continue
        y, x, h, text = float(parts[0]), float(parts[1]), max(float(parts[2]), 1.0), parts[3]
        items.append((y, x, h, text))
    items.sort()
    rows: list[list[tuple]] = []
    for it in items:
        if rows and abs(it[0] - rows[-1][0][0]) < 0.6 * max(it[2], rows[-1][0][2]):
            rows[-1].append(it)
        else:
            rows.append([it])
    out = []
    for row in rows:
        row.sort(key=lambda t: t[1])
        out.append("   ".join(t[3] for t in row))
    return "\n".join(out)


def process(pdf: Path) -> None:
    outdir = WORK / pdf.stem
    n = render(pdf, outdir)
    print(f"{pdf.name}: {n} pages rendered, OCR ({LANG}) ...", flush=True)
    subprocess.run(
        ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(HERE / "ocr_dir.ps1"), str(outdir), LANG],
        check=True, stdout=subprocess.DEVNULL,
    )
    pages = []
    for i in range(1, n + 1):
        txt = outdir / f"p{i:04d}.txt"
        body = assemble_page(txt.read_text(encoding="utf-8-sig")) if txt.exists() else "[OCR missing]"
        pages.append(f"--- PAGE {i} ---\n{body}")
        png = outdir / f"p{i:04d}.png"
        if txt.exists() and png.exists():
            png.unlink()
    header = (
        f"# OCR text of {pdf.name}\n"
        f"# Windows OCR ({LANG}); accents and digits may be misread (0/O, 8/B, 1/l).\n"
        f"# Use it to locate pages, then open the PDF page itself to verify.\n\n"
    )
    (HERE / f"{pdf.stem}.txt").write_text(header + "\n\n".join(pages) + "\n", encoding="utf-8")
    print(f"  -> {pdf.stem}.txt", flush=True)


def main() -> None:
    targets = [HERE / a for a in sys.argv[1:]] or sorted(HERE.glob("*.pdf"))
    for pdf in targets:
        if not sys.argv[1:] and has_text(pdfium.PdfDocument(str(pdf))):
            print(f"{pdf.name}: has a text layer, skipped")
            continue
        process(pdf)


if __name__ == "__main__":
    main()
