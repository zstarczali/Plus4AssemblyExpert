#!/usr/bin/env python3
"""Copy the knowledge base into plugin/knowledge and pack plugin/ into plus4-assembly-expert.plugin (zip)."""

import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent
PLUGIN = ROOT / "plugin"
KB_SRC = ROOT / "knowledge"
KB_DST = PLUGIN / "knowledge"
OUT = ROOT / "plus4-assembly-expert.plugin"

# Big or regenerable material stays in the project only.
EXCLUDE_DIRS = {"raw", "ocr_work", "__pycache__"}
EXCLUDE_SUFFIXES = {".pdf", ".py", ".ps1", ".log", ".png"}


def wanted(p: Path) -> bool:
    rel = p.relative_to(KB_SRC)
    if any(part in EXCLUDE_DIRS for part in rel.parts):
        return False
    if p.suffix.lower() in EXCLUDE_SUFFIXES and "files" not in rel.parts:
        return False
    return p.is_file()


def main() -> None:
    if KB_DST.exists():
        # a directory may be locked as some process's cwd on Windows; stale files are removed regardless
        shutil.rmtree(KB_DST, ignore_errors=True)
    n = 0
    for p in sorted(KB_SRC.rglob("*")):
        if wanted(p):
            dst = KB_DST / p.relative_to(KB_SRC)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, dst)
            n += 1
    print(f"knowledge: {n} files copied")

    OUT.unlink(missing_ok=True)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(PLUGIN.rglob("*")):
            if p.is_file():
                z.write(p, p.relative_to(PLUGIN).as_posix())
    print(f"{OUT.name}: {OUT.stat().st_size / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
