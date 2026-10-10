#!/usr/bin/env python3
"""N2R-4 (10 Oct 2026): write ms18/n2r4_entries.txt (decode.load_ciphertext format) for the rows guessed Cipher No. 2, from sources/mssEC18 via the shared segmenter (same as ms18_r7_extract.py)."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import entries_mssEC19 as E
ROWS = '9701/0 9850/1 9755/0 9898/2 9759/0 9685/1 9906/0 9739/2 9782/0 9880/0'.split()
pages = E.load_pages("sources/mssEC18")
ents = E.segment(pages, base=9660)
by = {(e["pointer"], e["entry_on_page"]): e for e in ents}
out = []
for r in ROWS:
    p, n = map(int, r.split("/")); e = by[(p, n)]
    out.append(f"### Z{ROWS.index(r)+1} | Page {e['page']} | {p} | (N2R-4, row {r})\n{e['header']}\n" + "\n".join(e["lines"]) + "\n")
Path(HERE/"ms18"/"n2r4_entries.txt").write_text("\n".join(out))
print("\n".join(out))
