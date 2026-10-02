#!/usr/bin/env python3
"""Search the printed Wellesley editions' OCR text for the D623 despatches never phrase- or date-searched before
(D623/4 3 Jul 1798, D623/5 6 Jul 1798, D623/24 7 Jun 1799) and locate D623/23's printed text (16 May 1799).

Usage: python3 ciphers/mornington-1798/print/grep_editions.py [--context N]
Reads the *_djvu.txt files beside this script (manifest.tsv names their source). Normalises OCR whitespace and
hyphenated line breaks, then prints every match with context so each can be judged by eye. No network.
GAPS-mornington-1798, 2 Oct 2026.
"""
import re, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
EDITIONS = {
    "35304": "Martin, Despatches, Vol. 1 (1836)",
    "117686": "Owen, Selection (1877)",
    "87788": "Wellesley Papers I (1914)",
    "87766": "Wellesley Papers II (1914)",
}
def norm(t):
    t = t.replace("\r", "")
    t = re.sub(r"-\n\s*", "", t)          # re-join hyphenated line breaks
    t = re.sub(r"\s+", " ", t)
    return t
def date_rx(day, month, year):
    ords = r"(?:st|nd|rd|d|th)?"
    m = month[:3] + r"[a-z]*\.?"
    return re.compile(
        rf"(?:\b{day}{ords}\s+(?:of\s+)?{m},?\s+{year}\b|\b{m}\s+(?:the\s+)?{day}{ords},?\s+{year}\b)", re.I)
TARGETS = {
    "D623/4 (3 Jul 1798)": [date_rx(3, "July", 1798)],
    "D623/5 (6 Jul 1798)": [date_rx(6, "July", 1798)],
    "D623/24 (7 Jun 1799)": [date_rx(7, "June", 1799)],
    "D623/23 (16 May 1799, printed)": [date_rx(16, "May", 1799),
                                       re.compile(r"Yesterday I received the enclosed despatch from Lieut", re.I)],
    "phrase: proclamation ... Mauritius": [re.compile(r"proclamation[^.]{0,80}Mauritius|Mauritius[^.]{0,80}proclamation", re.I)],
    "phrase: Malartic took that step": [re.compile(r"Malartic took that step|policy of Monsieur Malartic", re.I)],
    "phrase: re-?distributing": [re.compile(r"re-?\s?distributing", re.I)],
    "phrase: memorandum ... settlement": [re.compile(r"memorandum[^.]{0,80}settlement|settlement[^.]{0,80}memorandum", re.I)],
    "phrase: cipher/cypher": [re.compile(r"\bc[iy]pher", re.I)],
}
ctx = int(sys.argv[sys.argv.index("--context") + 1]) if "--context" in sys.argv else 160
for ident, name in EDITIONS.items():
    p = HERE / f"{ident}_djvu.txt"
    if not p.exists():
        print(f"## {name}: MISSING {p.name}"); continue
    t = norm(p.read_text(errors="replace"))
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
