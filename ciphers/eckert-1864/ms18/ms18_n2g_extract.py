#!/usr/bin/env python3
"""N2R-2 (10 Oct 2026): write ms18/ms18_n2g_entries.txt (decode.load_ciphertext format) for the rows guessed Cipher No. 2, from sources/mssEC18 via the shared segmenter (same as ms18_r7_extract.py)."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import entries_mssEC19 as E
ROWS = '9871/2 9874/1 9761/1 9913/0 9800/2 9871/1 9916/1 9722/1 9680/0 9725/0 9914/1 9681/0'.split()
pages = E.load_pages("sources/mssEC18")
ents = E.segment(pages, base=9660)
by = {(e["pointer"], e["entry_on_page"]): e for e in ents}
out = []
for r in ROWS:
    p, n = map(int, r.split("/")); e = by[(p, n)]
    out.append(f"### Y{ROWS.index(r)+1} | Page {e['page']} | {p} | (N2R-2, row {r})\n{e['header']}\n" + "\n".join(e["lines"]) + "\n")
Path(HERE/"ms18"/"ms18_n2g_entries.txt").write_text("\n".join(out))
print("\n".join(out))
