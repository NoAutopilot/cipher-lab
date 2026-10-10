#!/usr/bin/env python3
"""MS65-R2: write ms18/ms65_r2_entries.txt (decode.load_ciphertext format) for the 10 reader rows, from sources/mssEC18 via the shared segmenter (same as ms18_r1_extract.py)."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import entries_mssEC19 as E
ROWS = '10014/1 10012/1 10023/1 10006/0 10040/0 10034/2 10028/2 10007/1 10006/1 10040/1'.split()
pages = E.load_pages("sources/mssEC18")
ents = E.segment(pages, base=9660)
by = {(e["pointer"], e["entry_on_page"]): e for e in ents}
out = []
for r in ROWS:
    p, n = map(int, r.split("/")); e = by[(p, n)]
    if r == "10023/1":  # cut the Fuller 28 May entry out of the Sullivan segment (BOOK-65)
        i = [j for j, l in enumerate(e["lines"]) if l.startswith("W. G. Fuller")][0]
        e = dict(e, header=e["lines"][i], lines=e["lines"][i+1:])
    out.append(f"### Z{ROWS.index(r)+1} | Page {e['page']} | {p} | (MS65-R2, row {r})\n{e['header']}\n" + "\n".join(e["lines"]) + "\n")
Path(HERE/"ms18"/"ms65_r2_entries.txt").write_text("\n".join(out))
print("\n".join(out))
