#!/usr/bin/env python3
"""MS18-R11: write ms18/ms18_r11_entries.txt (decode.load_ciphertext format) for the 9 reader rows, from sources/mssEC18 via the shared segmenter (same as ms18_r1_extract.py)."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import entries_mssEC19 as E
ROWS = '9743/1 9686/2 9869/4 9730/0 9764/1 9897/1 9862/0 9885/3'.split()
pages = E.load_pages("sources/mssEC18")
ents = E.segment(pages, base=9660)
by = {(e["pointer"], e["entry_on_page"]): e for e in ents}
out = []
for r in ROWS:
    p, n = map(int, r.split("/")); e = by[(p, n)]
    out.append(f"### X{ROWS.index(r)+1} | Page {e['page']} | {p} | (MS18-R11, row {r})\n{e['header']}\n" + "\n".join(e["lines"]) + "\n")
Path(HERE/"ms18"/"ms18_r11_entries.txt").write_text("\n".join(out))
print("\n".join(out))
