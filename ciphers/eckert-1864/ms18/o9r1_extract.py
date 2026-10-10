#!/usr/bin/env python3
"""O9R-1 (10 Oct 2026): write ms18/o9r1_entries.txt (decode.load_ciphertext format) for the 10 reader rows + 2 spares, from sources/mssEC18 (same segmenter as ms18_r7_extract.py)."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import entries_mssEC19 as E
ROWS = '9709/1 9808/2 9673/0 9687/1 9684/1 9699/1 9803/0 9684/0 9684/0b 9735/0 9686/1'.split()
pages = E.load_pages("sources/mssEC18")
by = {(e["pointer"], e["entry_on_page"]): e for e in E.segment(pages, base=9660)}
out = []
for i, r in enumerate(ROWS, 1):
    rr = r[:-1] if r.endswith("b") else r
    p, n = map(int, rr.split("/")); e = by[(p, n)]
    lines = list(e["lines"])
    if rr == "9684/0":  # two telegrams of 9 March on one leaf: the second has its own header ("Wash. D. C." / John Horner N. Y. "No 9")
        k = next(j for j, l in enumerate(lines) if l.strip() == "Wash. D. C.")
        if r.endswith("b"): e = dict(e, header="Wash. D. C.  John Horner N. Y. \" No 9 \"  mar. 9th 1864"); lines = lines[k + 2:]
        else: lines = lines[:k]
    if r == "9699/1":  # the volunteer page break falls inside the entry: continue from pointer 9700 up to the signature
        import json
        cont = json.load(open(HERE/"sources"/"mssEC18"/"p9700.json"))["transc"].split("\n")
        for l in cont:
            if l.strip(): lines.append(l.strip())
            if "sig M C Meigs" in l: break
    out.append(f"### G{i} | Page {e['page']} | {p} | (O9R-1, row {r})\n{e['header']}\n" + "\n".join(lines) + "\n")
Path(HERE/"ms18"/"o9r1_entries.txt").write_text("\n".join(out))
print("\n".join(out))
