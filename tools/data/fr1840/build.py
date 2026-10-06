#!/usr/bin/env python3
"""Build tools/data/fr1840 from Internet Archive OCR (_djvu.txt) of five printed volumes of 1835-1850 diplomatic French.

Fetched once by R11-ZESCORP (6 Oct 2026) into a scratch folder; this script only trims and gzips, it makes no network call.
Per file: keep raw lines [start, end) (front matter and the volume's own end index cut), drop running heads (a line that is
mostly capitals or is only a page number), join hyphenated line breaks, write <id>.txt.gz. MANIFEST.tsv records the cuts.
Usage: python3 tools/data/fr1840/build.py RAW_DIR   (RAW_DIR holds <id>.txt as downloaded)
"""
import gzip, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CUTS = {  # id: (first kept line, first dropped line), 1-based raw line numbers
    "lettresetpapiers08ness": (120, 13140),   # Nesselrode, Lettres et papiers VIII (1840-1846); end: 'TABLE DES NOMS CITES'
    "lettresetpapiers09ness": (120, 11690),   # tome IX (1847-1850); end: 'TABLE DES NOMS CITES'
    "memoiresdocume06mett": (382, 32238),     # Metternich, Memoires VI (1835-1848); front: table des matieres to 381
    "mmoirespourse06guiz": (120, 18873),      # Guizot, Memoires VI (1840-41); end: 'TABLE DES MATIERES'
    "mmoirespourse07guiz": (120, 19504),      # Guizot, Memoires VII (1841-47); end: 'TABLE DES MATIERES'
}
HEAD = re.compile(r"ARCHIVES\s+DU\s+COMTE|M[ÉE]MOIRES\s+(POUR|DE\s+METT)|^\s*\d{1,4}\s*$")


def is_head(line):
    s = line.strip()
    if not s or HEAD.search(s):
        return True
    letters = [c for c in s if c.isalpha()]
    return len(letters) >= 6 and sum(c.isupper() for c in letters) / len(letters) > 0.7


def clean(lines):
    out = []
    for l in lines:
        if is_head(l):
            continue
        l = re.sub(r"\s+", " ", l).strip()
        if out and out[-1].endswith("-"):
            out[-1] = out[-1][:-1] + l
        else:
            out.append(l)
    return "\n".join(out) + "\n"


def main():
    raw = Path(sys.argv[1])
    for i, (a, b) in CUTS.items():
        lines = (raw / f"{i}.txt").read_text(encoding="utf-8", errors="replace").splitlines()
        txt = clean(lines[a - 1:b - 1])
        with gzip.open(HERE / f"{i}.txt.gz", "wt", encoding="utf-8") as f:
            f.write(txt)
        print(i, len(lines), len(txt), sum(c.isalpha() for c in txt))


if __name__ == "__main__":
    main()
