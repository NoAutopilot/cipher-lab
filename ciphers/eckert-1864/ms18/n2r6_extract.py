#!/usr/bin/env python3
"""N2R-6 (10 Oct 2026): write ms18/n2r6_entries.txt (decode.load_ciphertext format) for the rows guessed Cipher No. 2, from sources/mssEC18 via the shared segmenter (same as ms18_r7_extract.py)."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import entries_mssEC19 as E
ROWS = '9848/0 9811/0 9688/0 9729/1 9697/0 9850/2 9908/2 9798/1 9832/1'.split()
pages = E.load_pages("sources/mssEC18")
ents = E.segment(pages, base=9660)
by = {(e["pointer"], e["entry_on_page"]): e for e in ents}
out = []
for r in ROWS:
    p, n = map(int, r.split("/")); e = by[(p, n)]
    out.append(f"### Z{ROWS.index(r)+1} | Page {e['page']} | {p} | (N2R-6, row {r})\n{e['header']}\n" + "\n".join(e["lines"]) + "\n")
Path(HERE/"ms18"/"n2r6_entries.txt").write_text("\n".join(out))
print("\n".join(out))
