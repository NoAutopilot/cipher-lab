#!/usr/bin/env python3
"""FM-UND2 (10 Oct 2026): decode the head of E622 (5614 l.20 'Washington Apr 20 1864' + 5615 + E622 body) under No.1 and a meaning-shuffled No.1 (seeds 1-3, 7)."""
import json, random, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); import decode
sys.path.insert(0, str(HERE/"fortmonroe"))
key = decode.load_key(HERE/"key.md")
def shuffled(key, seed):
    rows = [k for k,v in key.items() if v[2]=="word"]; m=[key[k] for k in rows]; random.Random(seed).shuffle(m)
    o=dict(key); o.update(zip(rows,m)); return o
def page(p): return json.load(open(HERE/f"sources/fortmonroe/p{p}.json"))["transc"].splitlines()
l14 = page(5614); i = [n for n,l in enumerate(l14) if l.startswith("Washington Apr 20 1864")][0]
head = [l for l in l14[i+1:] if l.strip()] + [l for l in page(5615) if l.strip()]
def tail():
    out=[]
    for l in page(5616):
        if not l.strip(): break
        out.append(l)
    return out
if "--head-only" in sys.argv: lines = head
else: lines = head + tail()
open(HERE/"fortmonroe/fmund2_head_lines.txt","w").write("\n".join(lines)+"\n")
text = decode.entry_text(lines)
for name,k in [("no1",key)]+[(f"shuf{s}",shuffled(key,s)) for s in (1,2,3,7)]:
    r,c = decode.decode_entry(text,k)
    print(f"== {name} H{c['H']} C{c['C']} I{c['I']} M{c['M']}"); print(r.replace("\n"," ")[:2600] if name in ("no1","shuf1","shuf7") else r.replace("\n"," ")[:500])
