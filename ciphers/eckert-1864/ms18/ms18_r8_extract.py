#!/usr/bin/env python3
"""MS18-R8: write ms18/ms18_r8_entries.txt (decode.load_ciphertext format) for the 10 reader rows, from sources/mssEC18 via the shared segmenter (same as ms18_r1_extract.py)."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import entries_mssEC19 as E
ROWS = '10003/2 10048/1 9885/1 9887/0 9841/0 10055/0 9694/1 9903/1 9880/2 9772/0'.split()
pages = E.load_pages("sources/mssEC18")
ents = E.segment(pages, base=9660)
by = {(e["pointer"], e["entry_on_page"]): e for e in ents}
out = []
for r in ROWS:
    p, n = map(int, r.split("/")); e = by[(p, n)]
    out.append(f"### X{ROWS.index(r)+1} | Page {e['page']} | {p} | (MS18-R8, row {r})\n{e['header']}\n" + "\n".join(e["lines"]) + "\n")
Path(HERE/"ms18"/"ms18_r8_entries.txt").write_text("\n".join(out))
print("\n".join(out))
