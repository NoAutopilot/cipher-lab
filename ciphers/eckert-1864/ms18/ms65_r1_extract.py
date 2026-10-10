#!/usr/bin/env python3
"""MS65-R1: write ms18/ms65_r1_entries.txt (decode.load_ciphertext format) for the 10 reader rows, from sources/mssEC18 via the shared segmenter (same as ms18_r1_extract.py)."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import entries_mssEC19 as E
ROWS = '10019/1 10060/0 10039/0 10030/2 10062/0 10008/0 10046/1 10065/1 10058/0'.split()
pages = E.load_pages("sources/mssEC18")
ents = E.segment(pages, base=9660)
by = {(e["pointer"], e["entry_on_page"]): e for e in ents}
out = []
for r in ROWS:
    p, n = map(int, r.split("/")); e = by[(p, n)]
    out.append(f"### Y{ROWS.index(r)+1} | Page {e['page']} | {p} | (MS65-R1, row {r})\n{e['header']}\n" + "\n".join(e["lines"]) + "\n")
Path(HERE/"ms18"/"ms65_r1_entries.txt").write_text("\n".join(out))
print("\n".join(out))
