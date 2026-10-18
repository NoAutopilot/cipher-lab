#!/usr/bin/env python3
"""Locate headwords in an Internet Archive book by scan index and running head.

Downloads <id>_djvu.xml (per-page OCR), and for each word reports the first scan whose
text has the word at the start of a line (optionally preceded by "To "), with the first
two OCR lines of that scan, which normally carry the printed page number and the
running head (e.g. "268 MOR"). Long s is tolerated (s matches s or f). Running heads
are OCR and must be checked by eye where they matter.

Usage: ia_djvu_headwords.py IA_IDENTIFIER [Word ...]   (default word list is for the
Wellington-Maitland 1812 dictionary code). Written 19 Sept 2026.

--anchors FILE mode (SHERWOOD-BOOK, 18 Oct 2026): FILE is a TSV of word<TAB>page (the
cipher's own anchor page for that headword). For each word, restrict the search to a
window of scans centred on the word's own alphabetical-fraction estimate (first letters
only, not the anchor page -- the anchor page must not bias where we look for the
headword, or the "fit" is circular) and report the earliest in-window match, its scan
index, the book's own printed-page number nearest that scan (recovered by a robust
mode-offset over OCR'd digit tokens at page edges, since OCR of 18th-century type is
noisy), and the absolute error against the anchor page. Prints a TSV to stdout:
word, anchor_page, scan, est_printed_page, abs_error.
"""
import html, os, re, subprocess, sys
from collections import Counter

WORDS = ["Alphabet", "And", "At", "Be", "Can", "Cipher", "Cypher", "Day", "Early", "Head", "Morrow",
         "Occupy", "Period", "Provision", "Quarter", "Sea", "South", "Supply", "Theft", "Use",
         "Westward", "Which", "Will", "You"]


def fetch(iid):
    fn = f"{iid}_djvu.xml"
    if not os.path.exists(fn) or os.path.getsize(fn) < 1000:
        subprocess.run(["curl", "-sS", "-L", "-A", "Mozilla/5.0", "-o", fn,
                        f"https://archive.org/download/{iid}/{iid}_djvu.xml"], check=False)
    return open(fn, encoding="utf-8", errors="ignore").read()


def fetch_page_numbers(iid):
    """IA's own archive-hocr-tools leafNum -> printed pageNumber map, when the item has one
    (far less noisy than scraping digit tokens out of the OCR line text ourselves)."""
    import json
    fn = f"{iid}_page_numbers.json"
    if not os.path.exists(fn) or os.path.getsize(fn) < 50:
        r = subprocess.run(["curl", "-sS", "-L", "-A", "Mozilla/5.0", "-o", fn,
                            f"https://archive.org/download/{iid}/{iid}_page_numbers.json"], check=False)
    try:
        d = json.load(open(fn, encoding="utf-8", errors="ignore"))
    except Exception:
        return {}
    out = {}
    for p in d.get("pages", []):
        s = str(p.get("pageNumber") or "").strip()
        if re.fullmatch(r"\d{1,4}", s):
            out[p["leafNum"]] = int(s)
    return out


def pages(xml):
    out = []
    for obj in re.findall(r"<OBJECT.*?</OBJECT>", xml, re.S):
        lines = []
        for ln in re.findall(r"<LINE>(.*?)</LINE>", obj, re.S):
            lines.append(html.unescape(" ".join(re.findall(r"<WORD[^>]*>(.*?)</WORD>", ln))))
        out.append(lines)
    return out


def alpha_frac(word):
    """Fractional position of word in a uniform a..z ordering, from its first 4 letters."""
    w = re.sub(r"[^a-z]", "", word.lower()) or "a"
    frac, scale = 0.0, 1.0
    for c in w[:4]:
        scale /= 26.0
        frac += (ord(c) - ord("a")) * scale
    return frac


NUMTOK = re.compile(r"(?<!\d)(\d{1,4})(?!\d)")


def edge_numbers(lines):
    """Standalone digit tokens (1-4 digits) in the first 2 and last 2 OCR lines of a scan."""
    out = []
    for ln in (lines[:2] + lines[-2:]):
        out += [int(m.group(1)) for m in NUMTOK.finditer(ln)]
    return out


def scan_to_page_offset(pg):
    """Robust scan-index -> printed-page offset: the modal (scan - number) over every
    scan with exactly one plausible edge-number candidate, each vote weighted 1."""
    diffs = Counter()
    for i, lines in enumerate(pg):
        nums = [n for n in edge_numbers(lines) if 1 <= n <= len(pg) + 50]
        if len(nums) == 1:
            diffs[i - nums[0]] += 1
    if not diffs:
        return None, 0
    offset, votes = diffs.most_common(1)[0]
    return offset, votes


def find_headword_scan(pg, word, window):
    """1780s dictionary OCR often inserts a stray apostrophe/accent mark between two
    letters to mark a stressed syllable (e.g. "Reduc'tion", "Cégency"); tolerate one
    optional [’'] between any pair of letters, and long s (s/f)."""
    letters = [c.replace("s", "[sf]").replace("S", "[SF]") for c in re.escape(word)]
    pat = r"[’']?".join(letters)
    lo, hi = window
    for i, lines in enumerate(pg):
        if i < lo or i > hi:
            continue
        txt = "\n".join(lines)
        if re.search(r"(^|\n)\s*(To\s+)?" + pat + r"[,.'’]\s", txt, re.I):
            return i
    return None


def nearest_known_page(pagemap, leaf, n):
    """Printed page at `leaf`, by IA's own map if present else linear interpolation
    between the nearest leaves on either side that the map does cover."""
    if leaf in pagemap:
        return pagemap[leaf], "exact"
    lo = max((l for l in pagemap if l < leaf), default=None)
    hi = min((l for l in pagemap if l > leaf), default=None)
    if lo is not None and hi is not None and hi > lo:
        frac = (leaf - lo) / (hi - lo)
        return round(pagemap[lo] + frac * (pagemap[hi] - pagemap[lo])), "interp"
    if lo is not None:
        return pagemap[lo] + (leaf - lo), "extrap"
    if hi is not None:
        return pagemap[hi] - (hi - leaf), "extrap"
    return None, "no-data"


def run_anchors(iid, anchors_file, margin=0.15):
    pg = pages(fetch(iid))
    n = len(pg)
    pagemap = fetch_page_numbers(iid)
    offset, votes = (None, 0)
    if not pagemap:
        offset, votes = scan_to_page_offset(pg)
    print(f"# {iid} scans={n} page_numbers.json entries={len(pagemap)} "
          f"fallback_offset={offset} fallback_votes={votes}", file=sys.stderr)
    rows = []
    with open(anchors_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            word, page = line.split("\t")[:2]
            page = int(page)
            frac = alpha_frac(word)
            center = frac * n
            lo, hi = max(0, int(center - margin * n)), min(n - 1, int(center + margin * n))
            scan = find_headword_scan(pg, word, (lo, hi))
            if scan is None:
                scan = find_headword_scan(pg, word, (0, n - 1))
                flag = "outside-window" if scan is not None else "not-found"
            else:
                flag = "ok"
            if scan is None:
                rows.append((word, page, scan, None, None, flag, ""))
                continue
            if pagemap:
                est_page, src = nearest_known_page(pagemap, scan, n)
            elif offset is not None:
                est_page, src = scan - offset, "ocr-offset"
            else:
                est_page, src = None, "no-data"
            err = None if est_page is None else abs(est_page - page)
            rows.append((word, page, scan, est_page, err, flag, src))
    print("word\tanchor_page\tscan\test_page\tabs_error\tflag\tsrc")
    for r in rows:
        print("\t".join("" if x is None else str(x) for x in r))
    return rows


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    iid = sys.argv[1]
    if len(sys.argv) >= 4 and sys.argv[2] == "--anchors":
        run_anchors(iid, sys.argv[3])
        return
    words = sys.argv[2:] or WORDS
    pg = pages(fetch(iid))
    print("==", iid, len(pg), "scans")
    found = {}
    for i, lines in enumerate(pg):
        txt = "\n".join(lines)
        for w in words:
            if w in found:
                continue
            pat = w.replace("s", "[sf]")
            if re.search(r"(^|\n)\s*(To\s+)?" + pat + r"[,.'’]\s", txt):
                found[w] = (i, " | ".join(lines[:2])[:60])
    for w in words:
        print(f"  {w:10s}", found.get(w))


if __name__ == "__main__":
    main()
