#!/usr/bin/env python3
"""N2R-1 (10 Oct 2026): decode ms18/n2r1_entries.txt under No. 1, No. 2, No. 9 and under No. 2 with meanings shuffled (seeds 1,2,3; same token counts, values permuted).
Coherence = H count (words resolved through the key) and plain-English function-word-adjacent share is not used; see NOTES. Usage: python3 ms18/n2r1.py [--show]"""
import random, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); import decode
keys = {n: decode.load_key(HERE/f) for n, f in [("no1","key.md"),("no2","key-no2.md"),("no9","key-no9.md")]}
def shuffled(key, seed):
    rows = [k for k,v in key.items() if v[2]=="word"]; m = [key[k] for k in rows]; random.Random(seed).shuffle(m)
    out = dict(key); out.update(zip(rows, m)); return out
for s in (1,2,3): keys[f"no2s{s}"] = shuffled(keys["no2"], s)
show = "--show" in sys.argv
for header, lines in decode.load_ciphertext(HERE/"ms18"/"n2r1_entries.txt"):
    text = decode.entry_text(lines); res = {}
    for n in keys:
        r, c = decode.decode_entry(text, keys[n]); res[n] = (c['H'], r)
    sh = [res[f"no2s{s}"][0] for s in (1,2,3)]
    print(f"{header.split('|')[0].strip()} {header.split('|')[3].strip()}: H no1={res['no1'][0]} no2={res['no2'][0]} no9={res['no9'][0]} | no2-shuffled(3 seeds)={sh}")
    if show:
        for n in ("no2","no1"): print(f"  {n}: {res[n][1].replace(chr(10),' ')[:700]}")
