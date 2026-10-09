#!/usr/bin/env python3
"""FM-R7b (9 Oct 2026): extract the ten rows' entries from the FM-PRE builder at HEAD, print shares, write fm_r7b_entries.txt.
Rows are pointer/entry_on_page of entries-fm.tsv. Usage: python3 fm_r7b_extract.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import fm_entries as fe
ROWS = [(5639,2),(5709,1),(5648,2),(5695,2),(5702,0),(5782,0)]
_, ents = fe.build(); by = {(e["pointer"], e["entry_on_page"]): e for e in ents}
out = []
for i,(p,n) in enumerate(ROWS,1):
    e = by[(p,n)]
    print(p,n,e["page"],e["date"],e["direction"],e["words"],"s1/s2/s9=",e["s1"],e["s2"],e["s9"],"best",e.get("best_book"),"share_book",e["share_book"],"cont",e.get("cont"))
    out.append(f"### F{i} | row {p}/{n} | FM-R7b, mssEC 25 / obj 5952, pointer {p}\n" + "\n".join(e["lines"]) + "\n")
open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"fm_r7b_entries.txt"),"w").write("\n".join(out))
