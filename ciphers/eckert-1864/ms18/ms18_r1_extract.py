#!/usr/bin/env python3
"""MS18-R1: write ms18/ms18_r1_entries.txt (decode.load_ciphertext format) for the 12 reader rows, from sources/mssEC18 via the shared segmenter."""
import sys, re
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import entries_mssEC19 as E
ROWS = "9696/0 9819/2 9836/0 9830/2 9875/2 9769/0 9823/2 9730/1 9751/0 9923/3 9703/0 9923/2".split()
pages = E.load_pages("sources/mssEC18")
ents = E.segment(pages, base=9660)
by = {(e["pointer"], e["entry_on_page"]): e for e in ents}
out = []
for r in ROWS:
    p, n = map(int, r.split("/")); e = by[(p, n)]
    out.append(f"### X{ROWS.index(r)+1} | Page {e['page']} | {p} | (MS18-R1, row {r})\n{e['header']}\n" + "\n".join(e["lines"]) + "\n")
Path(HERE/"ms18"/"ms18_r1_entries.txt").write_text("\n".join(out))
print("\n".join(out))
