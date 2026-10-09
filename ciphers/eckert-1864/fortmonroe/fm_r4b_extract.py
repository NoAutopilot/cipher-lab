#!/usr/bin/env python3
"""FM-R4b (9 Oct 2026): extract the ten rows' entries from the FM-PRE builder at HEAD, print shares, write fm_r4b_entries.txt.
Rows are pointer/entry_on_page of entries-fm.tsv. Usage: python3 fm_r4b_extract.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import fm_entries as fe
ROWS = [(5787,1),(5629,1),(5741,0),(5812,0),(5610,1),(5822,1),(5609,2),(5790,0),(5742,1),(5775,1)]
_, ents = fe.build(); by = {(e["pointer"], e["entry_on_page"]): e for e in ents}
out = []
for i,(p,n) in enumerate(ROWS,1):
    e = by[(p,n)]
    print(p,n,e["page"],e["date"],e["direction"],e["words"],"s1/s2/s9=",e["s1"],e["s2"],e["s9"],"best",e.get("best_book"),"share_book",e["share_book"],"cont",e.get("cont"))
    out.append(f"### F{i} | row {p}/{n} | FM-R4b, mssEC 25 / obj 5952, pointer {p}\n" + "\n".join(e["lines"]) + "\n")
open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"fm_r4b_entries.txt"),"w").write("\n".join(out))
