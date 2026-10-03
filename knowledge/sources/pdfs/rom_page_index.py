"""Build an address -> PDF page index for the OCR'd ROM listings (listings are in address order)."""
import re, sys, statistics
FIX = str.maketrans({"S": "5", "s": "5", "B": "8", "O": "0", "o": "0", "I": "1", "l": "1", "i": "1", "D": "0", "G": "6", "Z": "2", "z": "2"})

def page_addrs(body, lower_listing):
    out = []
    for ln in body.splitlines():
        m = re.match(r"\s*\$?([0-9A-Za-z]{4})\b", ln)
        if not m:
            continue
        tok = m.group(1)
        if lower_listing:
            tok = "".join(c if c in "abcdef" else c.translate(FIX) for c in tok)
        else:
            tok = tok.translate(FIX)
        if re.fullmatch(r"[0-9a-fA-F]{4}", tok):
            out.append(int(tok, 16))
    return out

def build(path, first, last, lower):
    t = open(path, encoding="utf-8").read()
    parts = re.split(r"^--- PAGE (\d+) ---$", t, flags=re.M)
    rows = []
    for i in range(1, len(parts), 2):
        n = int(parts[i])
        if not (first <= n <= last):
            continue
        a = [x for x in page_addrs(parts[i + 1], lower) if x >= 0x8000]
        if len(a) < 5:
            continue
        med = statistics.median(a)
        a = [x for x in a if abs(x - med) < 0x400]
        if a:
            rows.append((n, min(a), max(a)))
    # enforce monotonic order: drop pages whose range jumps backwards
    clean, last_lo = [], 0
    for n, lo, hi in rows:
        if lo >= last_lo - 0x40:
            clean.append((n, lo, hi)); last_lo = lo
    return clean

if __name__ == "__main__":
    path, first, last, lower, title = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4] == "lower", sys.argv[5]
    rows = build(path, first, last, lower)
    print(f"# {title} – ROM address → PDF page\n")
    print(f"Source text: `{path}` (OCR). Ranges are approximate (OCR noise); open the PDF page to read the exact listing.\n")
    print("| PDF page | from | to |\n|---|---|---|")
    for n, lo, hi in rows:
        print(f"| {n} | ${lo:04X} | ${hi:04X} |")
