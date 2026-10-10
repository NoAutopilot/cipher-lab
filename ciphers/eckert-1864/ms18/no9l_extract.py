#!/usr/bin/env python3
"""NO9-L (10 Oct 2026): write ms18/no9l_entries.txt (decode.load_ciphertext format) for the 10 reader rows + 2 spares, from sources/mssEC18 (same segmenter as ms18_r7_extract.py)."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import entries_mssEC19 as E
ROWS = "9699/0 9694/2 9845/0 9679/0 9725/1 9762/1 9761/0 9862/1 9770/2".split()
pages = E.load_pages("sources/mssEC18")
by = {(e["pointer"], e["entry_on_page"]): e for e in E.segment(pages, base=9660)}
out = []
for i, r in enumerate(ROWS, 1):
    rr = r[:-1] if r.endswith("b") else r
    p, n = map(int, rr.split("/")); e = by[(p, n)]
    lines = list(e["lines"])
    if r == "9725/1":  # "(over)": the entry continues on pointer 9726 up to the signature "sig Applause"
        import json
        for l in json.load(open(HERE/"sources"/"mssEC18"/"p9726.json"))["transc"].split("\n"):
            if l.strip(): lines.append(l.strip())
            if "sig Applause" in l: break
    out.append(f"### G{i} | Page {e['page']} | {p} | (NO9-L, row {r})\n{e['header']}\n" + "\n".join(lines) + "\n")
Path(HERE/"ms18"/"no9l_entries.txt").write_text("\n".join(out))
print("\n".join(out))
