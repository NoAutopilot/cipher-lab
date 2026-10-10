#!/usr/bin/env python3
"""MS18-R7: write ms18/ms18_r7_entries.txt (decode.load_ciphertext format) for the 10 reader rows, from sources/mssEC18 via the shared segmenter (same as ms18_r1_extract.py)."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import entries_mssEC19 as E
ROWS = '9842/1 9907/1 9878/1 9673/1 10061/0 10013/0 9774/1 9820/3 9759/1 9732/1 10048/1 10003/2'.split()
pages = E.load_pages("sources/mssEC18")
ents = E.segment(pages, base=9660)
by = {(e["pointer"], e["entry_on_page"]): e for e in ents}
out = []
for r in ROWS:
    p, n = map(int, r.split("/")); e = by[(p, n)]
    out.append(f"### X{ROWS.index(r)+1} | Page {e['page']} | {p} | (MS18-R7, row {r})\n{e['header']}\n" + "\n".join(e["lines"]) + "\n")
Path(HERE/"ms18"/"ms18_r7_entries.txt").write_text("\n".join(out))
print("\n".join(out))
# X13: the mssEC 19 received-ledger row 9258/2 (p.364 of the ledger; leaf 'Page 366' of the volunteer pages), 27 July 1865 (AUD2-LEDGER-33)
pages19 = E.load_pages("sources/mssEC19")
e19 = {(e["pointer"], e["entry_on_page"]): e for e in E.segment(pages19)}[(9258, 2)]
blk = f"### X13 | Page {e19['page']} | 9258 | (MS18-R7, row 9258/2, mssEC 19)\n{e19['header']}\n" + "\n".join(e19["lines"]) + "\n"
with open(HERE/"ms18"/"ms18_r7_entries.txt", "a") as fh: fh.write("\n" + blk)
print(blk)
