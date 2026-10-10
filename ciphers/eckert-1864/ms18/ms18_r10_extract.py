#!/usr/bin/env python3
"""MS18-R10: write ms18/ms18_r10_entries.txt (decode.load_ciphertext format) for the 9 reader rows, from sources/mssEC18 via the shared segmenter (same as ms18_r1_extract.py)."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import entries_mssEC19 as E
ROWS = '9823/3 9865/1 9787/1 9733/1 9883/0 9802/1 9790/1 9874/2 9779/0'.split()
pages = E.load_pages("sources/mssEC18")
ents = E.segment(pages, base=9660)
by = {(e["pointer"], e["entry_on_page"]): e for e in ents}
out = []
for r in ROWS:
    p, n = map(int, r.split("/")); e = by[(p, n)]
    out.append(f"### X{ROWS.index(r)+1} | Page {e['page']} | {p} | (MS18-R10, row {r})\n{e['header']}\n" + "\n".join(e["lines"]) + "\n")
Path(HERE/"ms18"/"ms18_r10_entries.txt").write_text("\n".join(out))
print("\n".join(out))
