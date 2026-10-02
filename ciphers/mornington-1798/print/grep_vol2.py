#!/usr/bin/env python3
"""Martin, Despatches ... of the Marquess Wellesley, Vol. 2 (1836; IA india.history.resource.35315), read as OCR text
for the three dates named by the 1 Oct 2026 "Remaining gaps" Verdict line: 21 Jun 1800 (D623/35; Ingram 1970's
footnote "Add. MSS. 13751, f. 77. Wellesley, ii, 311"), 7 Jun 1799 (D623/24) and 13 Jul 1800 (Dundas's 30 Dec 1800
reply names an "overland despatch in cypher, dated 13th July last"). Also locates the running heads for pp. 305-316
and p. 361 so the page the footnote cites can be read by eye. The same dates are run against the 1914 Wellesley
Papers Vol. II OCR (87766_djvu.txt, on disk) in case "Wellesley, ii, 311" means that edition.

Usage: python3 ciphers/mornington-1798/print/grep_vol2.py [--context N]
No network: reads the *_djvu.txt files beside this script (manifest.tsv names their source).
GAPS2-mornington-1798, 2 Oct 2026.
"""
import re, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
def norm(t):
    t = t.replace("\r", "")
    t = re.sub(r"-\n\s*", "", t)
    t = re.sub(r"\s+", " ", t)
    return t
def date_rx(day, month, year):
    ords = r"(?:st|nd|rd|d|th)?"
    m = month[:3] + r"[a-z]*\.?"
    return re.compile(
        rf"(?:\b{day}{ords}\s+(?:of\s+)?{m},?\s+{year}\b|\b{m}\s+(?:the\s+)?{day}{ords},?\s+{year}\b)", re.I)
TARGETS = {
    "D623/35 (21 Jun 1800)": [date_rx(21, "June", 1800)],
    "D623/24 (7 Jun 1799)": [date_rx(7, "June", 1799)],
    "13 Jul 1800 (Dundas's 'despatch in cypher dated 13th July')": [date_rx(13, "July", 1800)],
    "phrase: cipher/cypher": [re.compile(r"\bc[iy]pher", re.I)],
}
EDITIONS = {"35315": "Martin, Despatches, Vol. 2 (1836)", "87766": "Wellesley Papers II (1914)"}
ctx = int(sys.argv[sys.argv.index("--context") + 1]) if "--context" in sys.argv else 160
for ident, name in EDITIONS.items():
    p = HERE / f"{ident}_djvu.txt"
    if not p.exists():
        print(f"## {name}: MISSING {p.name}"); continue
    raw = p.read_text(errors="replace")
    t = norm(raw)
    print(f"## {name} ({p.name}, {len(t):,} chars normalised)")
    for label, rxs in TARGETS.items():
        n = 0
        for rx in rxs:
            for m in rx.finditer(t):
                n += 1
                if n <= 12:
                    s, e = max(0, m.start() - ctx), min(len(t), m.end() + ctx)
                    print(f"  [{label}] @{m.start()}: ...{t[s:e]}...")
        print(f"  {label}: {n} match(es)")
    # running heads carrying a page number in 305-316 or 361 (raw text, one per line)
    for m in re.finditer(r"\n([^\n]{0,70}\b(?:30[5-9]|31[0-6]|36[01])\b[^\n]{0,70})\n", raw):
        line = m.group(1).strip()
        if re.search(r"WELLESLEY|GOVERNOR|COURT|KOEHLER|DUNDAS|1800|1799", line):
            print(f"  [running head] line {raw.count(chr(10), 0, m.start())+2}: {line}")
