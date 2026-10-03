#!/usr/bin/env python3
"""
Plus/4 Encyclopedia mirror
==========================
Letölti a https://plus4world.powweb.com/plus4encyclopedia összes topicját
(nyers HTML cache), a kategória-oldalakat, és minden topicban linkelt
fájlt (képek, letölthető anyagok), majd Markdown-ra konvertálja őket.

Futtatás:
  python download_plus4encyclopedia.py fetch     # nyers HTML + fájlok letöltése
  python download_plus4encyclopedia.py convert   # raw/ -> pages/*.md + INDEX.md
  python download_plus4encyclopedia.py all       # mindkettő

Kimenet:
  raw/      nyers HTML (cache, újrafuttatáskor nem tölti le újra)
  files/    a topicokból linkelt fájlok, az eredeti útvonal szerint
  pages/    topiconként egy Markdown fájl
  INDEX.md  kategória szerinti tartalomjegyzék
"""

import html
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

BASE = "https://plus4world.powweb.com"
ENC = BASE + "/plus4encyclopedia"
HERE = Path(__file__).parent
RAW = HERE / "raw"
FILES = HERE / "files"
PAGES = HERE / "pages"
DELAY = 0.4
TIMEOUT = 30
FIRST_TOPIC = 500001
UA = {"User-Agent": "Mozilla/5.0 (compatible; Plus4KnowledgeBot/1.0)"}

# Site chrome that is never content
SKIP_ASSET_RE = re.compile(r"^/(i|images)/|favicon\.ico$")
FILE_EXT_RE = re.compile(
    r"\.(gif|png|jpe?g|bmp|webp|svg|zip|rar|7z|gz|tgz|lha|lzh|prg|p00|d64|d71|d81|t64|tap|"
    r"crt|bin|rom|pdf|txt|asm|s|src|inc|bas|seq|doc|docx|rtf|htm|html|xls|xlsx|csv|mp3|wav|sid|"
    r"ted|tmf|exe|c|h|py|xml|json)$",
    re.I,
)


# ───────────────────────────── fetch ──────────────────────────────

def fetch(url: str) -> tuple[int, bytes]:
    req = urllib.request.Request(url, headers=UA)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            return e.code, b""
        except Exception as e:  # noqa: BLE001 - network flakiness, retry
            print(f"  [retry {attempt + 1}] {url}: {e}")
            time.sleep(2 + attempt * 3)
    return 0, b""


def decode(raw: bytes) -> str:
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("cp1252", errors="replace")


def cached(name: str, url: str) -> str | None:
    p = RAW / name
    if p.exists() and p.stat().st_size > 0:
        return decode(p.read_bytes())
    status, body = fetch(url)
    time.sleep(DELAY)
    if status != 200 or not body:
        print(f"  [{status}] {url}")
        return None
    p.write_bytes(body)
    return decode(body)


def last_topic_id(index_html: str) -> int:
    ids = [int(x) for x in re.findall(r"/plus4encyclopedia/(50\d{4})", index_html)]
    return max(ids) if ids else FIRST_TOPIC


def asset_links(page_html: str) -> set[str]:
    out = set()
    for m in re.finditer(r'(?:href|src)\s*=\s*["\']([^"\'#]+)["\']', page_html, re.I):
        u = html.unescape(m.group(1)).strip()
        if u.startswith("//"):
            u = "https:" + u
        absu = urllib.parse.urljoin(ENC + "/", u)
        pu = urllib.parse.urlparse(absu)
        if "plus4world.powweb.com" not in pu.netloc:
            continue
        if SKIP_ASSET_RE.search(pu.path):
            continue
        is_dl = "download" in pu.path.lower() or pu.path.startswith("/dl/")
        if FILE_EXT_RE.search(pu.path) or is_dl:
            out.add(absu)
    return out


def local_file_path(url: str) -> Path:
    pu = urllib.parse.urlparse(url)
    rel = urllib.parse.unquote(pu.path.lstrip("/"))
    if pu.query:
        rel += "__" + re.sub(r"[^\w.-]+", "_", pu.query)
    return FILES / rel


def download_file(url: str) -> bool:
    dst = local_file_path(url)
    if dst.exists() and dst.stat().st_size > 0:
        return True
    status, body = fetch(url)
    time.sleep(DELAY)
    if status != 200 or not body:
        print(f"  [file {status}] {url}")
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(body)
    return True


def do_fetch() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    FILES.mkdir(parents=True, exist_ok=True)
    (RAW / "index.html").unlink(missing_ok=True)  # always refresh the index
    index = cached("index.html", ENC)
    if index is None:
        sys.exit("Cannot fetch encyclopedia index")
    cats = sorted(set(re.findall(r"/plus4encyclopedia/(49\d{4})", index)))
    print(f"{len(cats)} categories")
    for cid in cats:
        cached(f"cat_{cid}.html", f"{ENC}/{cid}")

    last = last_topic_id(index)
    for name in RAW.glob("cat_*.html"):
        last = max(last, last_topic_id(decode(name.read_bytes())))
    print(f"topics {FIRST_TOPIC}..{last}")

    missing, assets = [], set()
    for tid in range(FIRST_TOPIC, last + 1):
        page = cached(f"{tid}.html", f"{ENC}/{tid}")
        if page is None or "Topic Table Of Contents" not in page and "kbHeader" not in page and "s0_t1" not in page:
            missing.append(tid)
            continue
        assets |= asset_links(page)
        if tid % 25 == 0:
            print(f"  .. {tid}")
    print(f"{len(missing)} missing/empty topics")
    (HERE / "missing_topics.txt").write_text("\n".join(map(str, missing)) + "\n", encoding="utf-8")

    print(f"{len(assets)} linked files")
    failed = [u for u in sorted(assets) if not download_file(u)]
    (HERE / "failed_files.txt").write_text("\n".join(failed) + "\n", encoding="utf-8")
    print(f"done, {len(failed)} file downloads failed")


# ──────────────────────────── convert ─────────────────────────────

BLOCK_TAGS = {"p", "div", "center", "blockquote", "ul", "ol", "table", "h1", "h2", "h3", "h4", "h5", "h6", "hr"}


class MD(HTMLParser):
    """Minimal HTML -> Markdown converter tuned for plus4world KB pages."""

    def __init__(self, page_url: str):
        super().__init__(convert_charrefs=True)
        self.page_url = page_url
        self.out: list[str] = []
        self.pre = 0
        self.code_inline = 0
        self.list_stack: list[str] = []
        self.href_stack: list[str | None] = []
        self.tables: list[dict] = []
        self.skip = 0

    # helpers
    def w(self, s: str) -> None:
        if self.tables and self.tables[-1]["cell"] is not None:
            self.tables[-1]["cell"].append(s)
        else:
            self.out.append(s)

    def nl(self, n: int = 1) -> None:
        if self.tables and self.tables[-1]["cell"] is not None:
            self.tables[-1]["cell"].append(" <br> " if n else "")
            return
        self.out.append("\n" * n)

    def link(self, u: str) -> str:
        u = html.unescape(u).strip()
        if u.startswith("#"):
            return u
        absu = urllib.parse.urljoin(self.page_url, u)
        m = re.match(r"https?://plus4world\.powweb\.com/plus4encyclopedia/(50\d{4})(#.*)?$", absu)
        if m:
            return f"{m.group(1)}.md{m.group(2) or ''}"
        if "plus4world.powweb.com" in absu and FILE_EXT_RE.search(urllib.parse.urlparse(absu).path):
            p = local_file_path(absu)
            if p.exists():
                return "../" + p.relative_to(HERE).as_posix()
        return absu

    # parser callbacks
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self.skip += 1
            return
        if self.skip:
            return
        if tag == "pre":
            self.pre += 1
            self.nl(2)
            self.w("```\n")
        elif tag in ("code", "tt") and not self.pre:
            self.code_inline += 1
            self.w("`")
        elif tag == "br":
            self.w("\n" if self.pre else "")
            if not self.pre:
                self.nl(1)
        elif tag in ("b", "strong") and not self.pre:
            self.w("**")
        elif tag in ("i", "em") and not self.pre:
            self.w("*")
        elif tag == "u" and not self.pre:
            self.w("")
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.nl(2)
            self.w("#" * (int(tag[1]) + 1) + " ")
        elif tag in ("ul", "ol"):
            self.list_stack.append(tag)
            self.nl(1)
        elif tag == "li":
            self.nl(1)
            depth = max(len(self.list_stack) - 1, 0)
            self.w("  " * depth + ("1. " if self.list_stack and self.list_stack[-1] == "ol" else "- "))
        elif tag == "a":
            href = a.get("href")
            name = a.get("name") or a.get("id")
            if self.pre:
                self.href_stack.append(None)
                return
            if name and not href:
                self.w(f'<a id="{name}"></a>')
            self.href_stack.append(self.link(href) if href else None)
            if href:
                self.w("[")
        elif tag == "img":
            src = a.get("src", "")
            if SKIP_ASSET_RE.search(urllib.parse.urlparse(src).path):
                return
            alt = a.get("alt", "") or Path(src).name
            self.w(f"![{alt}]({self.link(src)})")
        elif tag == "table":
            self.tables.append({"rows": [], "row": None, "cell": None})
        elif tag == "tr" and self.tables:
            self.tables[-1]["row"] = []
        elif tag in ("td", "th") and self.tables:
            t = self.tables[-1]
            if t["row"] is None:
                t["row"] = []
            t["cell"] = []
            t["span"] = int(a.get("colspan", "1") or 1) if str(a.get("colspan", "1")).isdigit() else 1
        elif tag in BLOCK_TAGS:
            self.nl(2)

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag == "pre":
            self.pre = max(0, self.pre - 1)
            self.w("\n```")
            self.nl(2)
        elif tag in ("code", "tt") and not self.pre:
            self.code_inline = max(0, self.code_inline - 1)
            self.w("`")
        elif tag in ("b", "strong") and not self.pre:
            self.w("**")
        elif tag in ("i", "em") and not self.pre:
            self.w("*")
        elif tag in ("ul", "ol"):
            if self.list_stack:
                self.list_stack.pop()
            self.nl(2)
        elif tag == "a":
            href = self.href_stack.pop() if self.href_stack else None
            if href:
                self.w(f"]({href})")
        elif tag in ("td", "th") and self.tables:
            t = self.tables[-1]
            if t["cell"] is not None and t["row"] is not None:
                txt = re.sub(r"\s+", " ", "".join(t["cell"])).strip()
                txt = re.sub(r"(\s*<br>\s*)+", " <br> ", txt).strip()
                txt = re.sub(r"^(<br>\s*)+|(\s*<br>)+$", "", txt).strip()
                txt = txt.replace("|", "\\|")
                t["row"].append(txt)
                for _ in range(t.get("span", 1) - 1):
                    t["row"].append("")
            t["cell"] = None
        elif tag == "tr" and self.tables:
            t = self.tables[-1]
            if t["row"]:
                t["rows"].append(t["row"])
            t["row"] = None
        elif tag == "table" and self.tables:
            t = self.tables.pop()
            md = render_table(t["rows"])
            if self.tables and self.tables[-1]["cell"] is not None:
                # nested table inside a cell: flatten
                self.tables[-1]["cell"].append(" " + md.replace("\n", " <br> ") + " ")
            else:
                self.out.append("\n\n" + md + "\n\n")
        elif tag in BLOCK_TAGS:
            self.nl(2)

    def handle_data(self, data):
        if self.skip:
            return
        if self.pre:
            self.w(data)
            return
        data = re.sub(r"[ \t\r\n]+", " ", data)
        self.w(data)

    def markdown(self) -> str:
        s = "".join(self.out).replace("\xa0", " ")
        # tidy: collapse blank lines outside code fences
        parts = re.split(r"(```.*?```)", s, flags=re.S)
        for i in range(0, len(parts), 2):
            p = parts[i]
            p = re.sub(r"[ \t]+\n", "\n", p)
            p = re.sub(r"\n[ \t]+(?=\S)", "\n", p)
            p = re.sub(r"\n{3,}", "\n\n", p)
            p = re.sub(r"\*\*\s*\*\*", "", p)
            parts[i] = p
        return "".join(parts).strip() + "\n"


MNEMONICS = (
    "adc and asl bcc bcs beq bit bmi bne bpl brk bvc bvs clc cld cli clv cmp cpx cpy dec dex dey "
    "eor inc inx iny jmp jsr lda ldx ldy lsr nop ora pha php pla plp rol ror rti rts sbc sec sed "
    "sei sta stx sty tax tay tsx txa txs tya"
).split()
ASM_LINE_RE = re.compile(
    r"^\s*(?:[A-Za-z_@.!][\w.@]*:?\s+)?(?:" + "|".join(MNEMONICS) + r")(?:\s|$)"
    r"|^\s*;"
    r"|^\s*[.!]?(?:byte|word|text|org|fill|res|db|dw|dc\.b|binary|import|include)\b"
    r"|^\s*\*\s*=",
    re.I,
)


def fence_asm(md: str) -> str:
    """Wrap runs of bare assembly lines (no <pre> on the site) in code fences."""
    parts = re.split(r"(```.*?```)", md, flags=re.S)
    for pi in range(0, len(parts), 2):
        lines = parts[pi].split("\n")
        out: list[str] = []
        i = 0
        while i < len(lines):
            if not ASM_LINE_RE.match(lines[i]):
                out.append(lines[i])
                i += 1
                continue
            j, asm_count, last_asm = i, 0, i
            while j < len(lines):
                ln = lines[j]
                if ASM_LINE_RE.match(ln):
                    asm_count += 1
                    last_asm = j
                elif ln.strip() == "" or re.match(r"^\s*[A-Za-z_][\w.]*:?\s*(=.*)?$", ln):
                    pass  # blank, bare label, or symbol assignment inside code
                else:
                    break
                if j - last_asm > 3:
                    break
                j += 1
            if asm_count >= 5:
                out.append("```asm")
                out.extend(lines[i:last_asm + 1])
                out.append("```")
                i = last_asm + 1
            else:
                out.append(lines[i])
                i += 1
        parts[pi] = "\n".join(out)
    return "".join(parts)


def render_table(rows: list[list[str]]) -> str:
    rows = [r for r in rows if any(c.strip() for c in r)]
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    if width == 1:
        return "\n\n".join(r[0] for r in rows)
    lines = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * width]
    for r in rows[1:]:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)


def strip_tags(s: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def parse_topic(tid: int, page: str) -> dict | None:
    m = re.search(r's0_t1\.gif[^>]*>\s*<span class="h">(.*?)</span>', page, re.S)
    title = strip_tags(m.group(1)) if m else ""
    if not title:
        m = re.search(r"<title>(.*?)</title>", page, re.S)
        title = strip_tags(m.group(1)).replace(" - Plus/4 Encyclopedia - Plus/4 World", "") if m else str(tid)
    # content lives in the single <td class="x"> cell after the title row
    hdr = page.find("s0_t2.gif")
    start = page.find('<td class="x">', hdr)
    end = page.find("s0_4.gif", start)
    if hdr < 0 or start < 0 or end < 0:
        return None
    body = page[start + len('<td class="x">'):end]
    end_cell = body.rfind("</td>")
    body = body[:end_cell] if end_cell >= 0 else body
    topic_at = body.find("<u>Topic</u>")
    head_part = body[:topic_at] if topic_at >= 0 else ""
    cats = [(c, strip_tags(n)) for c, n in re.findall(r'href="/plus4encyclopedia/(49\d{4})"[^>]*>(.*?)</a>', head_part, re.S)]
    if topic_at >= 0:
        body = body[topic_at + len("<u>Topic</u>"):]
        body = re.sub(r"^\s*</span>\s*(<br\s*/?>\s*)*", "", body)
    conv = MD(f"{ENC}/{tid}")
    conv.feed(body)
    conv.close()
    md = fence_asm(conv.markdown())
    kw = ""
    km = re.search(r"\*?\*?Keywords\*?\*?\s*\n+(.*)$", md, re.S)
    if km:
        kw = re.sub(r"\s+", " ", km.group(1)).strip()
        md = md[: km.start()].rstrip() + "\n"
    return {"id": tid, "title": title, "cats": cats, "md": md, "keywords": kw}


def slug(s: str) -> str:
    s = re.sub(r"[^\w]+", "_", s.lower()).strip("_")
    return s[:60] or "topic"


def do_convert() -> None:
    PAGES.mkdir(parents=True, exist_ok=True)
    for old in PAGES.glob("*.md"):
        old.unlink()
    cat_names: dict[str, str] = {}
    idx = RAW / "index.html"
    if idx.exists():
        for c, n in re.findall(r'href="/plus4encyclopedia/(49\d{4})"[^>]*>(.*?)</a>', decode(idx.read_bytes()), re.S):
            cat_names[c] = strip_tags(n)
    topics = []
    for f in sorted(RAW.glob("50*.html")):
        tid = int(f.stem)
        t = parse_topic(tid, decode(f.read_bytes()))
        if not t or t["title"].lower() == "topic not found":
            print(f"  skip {tid}")
            continue
        topics.append(t)
    for t in topics:
        t["file"] = f"{t['id']}_{slug(t['title'])}.md"
    by_id = {str(t["id"]): t["file"] for t in topics}
    for t in topics:
        # rewrite NNNNNN.md cross links to real filenames
        md = re.sub(r"\((50\d{4})\.md(#[^)]*)?\)", lambda m: f"({by_id.get(m.group(1), m.group(1) + '.md')}{m.group(2) or ''})", t["md"])
        cats = ", ".join(n for _, n in t["cats"]) or "-"
        head = [
            f"# {t['title']}",
            "",
            f"- Source: {ENC}/{t['id']}",
            f"- Category: {cats}",
        ]
        if t["keywords"]:
            head.append(f"- Keywords: {t['keywords']}")
        (PAGES / t["file"]).write_text("\n".join(head) + "\n\n" + md, encoding="utf-8")
    # index
    groups: dict[str, list] = {}
    for t in topics:
        for _, n in t["cats"] or [("", "Uncategorized")]:
            groups.setdefault(n, []).append(t)
    lines = ["# Plus/4 Encyclopedia – offline index", "", f"Source: {ENC}", f"Topics: {len(topics)}", ""]
    for name in sorted(groups):
        lines.append(f"## {name}")
        lines.append("")
        for t in sorted(groups[name], key=lambda x: x["title"].lower()):
            lines.append(f"- [{t['title']}](pages/{t['file']})")
        lines.append("")
    (HERE / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"converted {len(topics)} topics")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    if cmd in ("fetch", "all"):
        do_fetch()
    if cmd in ("convert", "all"):
        do_convert()
