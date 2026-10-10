#!/usr/bin/env python3
"""N2R-3 (10 Oct 2026): write ms18/n2r3_entries.txt (decode.load_ciphertext format) for the rows guessed Cipher No. 2, from sources/mssEC18 via the shared segmenter (same as ms18_r7_extract.py)."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import entries_mssEC19 as E
ROWS = '9791/1 9839/0 9807/1 9888/1 9873/3 9813/0 9840/0 9774/3 9687/0 9848/1 9876/1 9691/0'.split()
pages = E.load_pages("sources/mssEC18")
ents = E.segment(pages, base=9660)
by = {(e["pointer"], e["entry_on_page"]): e for e in ents}
out = []
for r in ROWS:
    p, n = map(int, r.split("/")); e = by[(p, n)]
    out.append(f"### Z{ROWS.index(r)+1} | Page {e['page']} | {p} | (N2R-3, row {r})\n{e['header']}\n" + "\n".join(e["lines"]) + "\n")
Path(HERE/"ms18"/"n2r3_entries.txt").write_text("\n".join(out))
print("\n".join(out))
