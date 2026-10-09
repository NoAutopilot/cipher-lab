#!/usr/bin/env python3
"""MS18-R5: write ms18/ms18_r5_entries.txt (decode.load_ciphertext format) for the 10 reader rows, from sources/mssEC18 via the shared segmenter (same as ms18_r1_extract.py)."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import entries_mssEC19 as E
ROWS = '10065/2 9821/1 10004/1 9791/0 9863/0 9729/2 9825/1 10043/1 9753/1 9770/1 9674/0 9886/1'.split()
pages = E.load_pages("sources/mssEC18")
ents = E.segment(pages, base=9660)
by = {(e["pointer"], e["entry_on_page"]): e for e in ents}
out = []
for r in ROWS:
    p, n = map(int, r.split("/")); e = by[(p, n)]
    out.append(f"### X{ROWS.index(r)+1} | Page {e['page']} | {p} | (MS18-R5, row {r})\n{e['header']}\n" + "\n".join(e["lines"]) + "\n")
Path(HERE/"ms18"/"ms18_r5_entries.txt").write_text("\n".join(out))
print("\n".join(out))
