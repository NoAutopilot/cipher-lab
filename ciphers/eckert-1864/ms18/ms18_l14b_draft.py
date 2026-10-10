#!/usr/bin/env python3
"""L14-B draft: append placeholder-description blocks for the 8 rows to ../ciphertext.txt (E610-E617) so decode.py can read them. Idempotent."""
import re
from pathlib import Path
H = Path(__file__).resolve().parent
M = [("ms18_r10_entries.txt","X3","E610",9787,127,"9787/1"),("ms18_r10_entries.txt","X4","E611",9733,73,"9733/1"),("ms18_r10_entries.txt","X5","E612",9883,223,"9883/0"),
     ("ms18_r10_entries.txt","X6","E613",9802,142,"9802/1"),("ms18_r10_entries.txt","X8","E614",9874,214,"9874/2"),("ms18_r10_entries.txt","X9","E615",9779,119,"9779/0"),
     ("ms18_r11_entries.txt","X1","E616",9743,83,"9743/1"),("ms18_r11_entries.txt","X2","E617",9686,26,"9686/2")]
p = H.parent/"ciphertext.txt"; t = p.read_text(encoding="utf-8"); add = []
for f,x,e,ptr,pg,row in M:
    if f"### {e} |" in t: continue
    s = (H/f).read_text(encoding="utf-8")
    m = re.search(rf"### {x} \|[^\n]*\n(.*?)(?=\n### X|\Z)", s, re.S)
    add.append(f"### {e} | Page {pg} | {ptr} | mssEC 18 (obj 10074, pointer {ptr}), DRAFT {row}\n" + "\n".join(l for l in m.group(1).splitlines() if l.strip()) + "\n")
if add: p.write_text(t.rstrip("\n")+"\n\n"+"\n".join(add), encoding="utf-8")
print("added", len(add))
