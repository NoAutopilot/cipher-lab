#!/usr/bin/env python3
"""N2R-1 (10 Oct 2026): write ms18/n2r1_entries.txt (decode.load_ciphertext format) for the 10 reader rows + 2 spares, from sources/mssEC18 (same segmenter as ms18_r7_extract.py)."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import entries_mssEC19 as E
ROWS = '9879/0 9767/1 9690/0 9680/1 9905/1 9807/0 9782/2 9916/2 9690/2 9798/0 9871/2 9874/1'.split()
pages = E.load_pages("sources/mssEC18")
by = {(e["pointer"], e["entry_on_page"]): e for e in E.segment(pages, base=9660)}
out = []
for i, r in enumerate(ROWS, 1):
    p, n = map(int, r.split("/")); e = by[(p, n)]
    out.append(f"### F{i} | Page {e['page']} | {p} | (N2R-1, row {r})\n{e['header']}\n" + "\n".join(e["lines"]) + "\n")
Path(HERE/"ms18"/"n2r1_entries.txt").write_text("\n".join(out))
print("\n".join(out))
