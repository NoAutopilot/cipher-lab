#!/usr/bin/env python3
"""FM-R7a (9 Oct 2026): H-word counts for each entry under No.1/No.2/No.9 vs 30 meaning-shuffled copies of each book (seeds 1-30): mean, p99 (max of 30), true count.
Machinery of decode.py unchanged (as fm_r7a.py). Usage: python3 fm_r7a_multi.py"""
import random, re, sys, statistics as st
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); import decode
keys = {n: decode.load_key(HERE/f) for n, f in [("no1","key.md"),("no2","key-no2.md"),("no9","key-no9.md")]}
def shuf(key, seed):
    rows=[k for k,v in key.items() if v[2]=="word"]; m=[key[k] for k in rows]; random.Random(seed).shuffle(m)
    o=dict(key)
    for k,x in zip(rows,m): o[k]=x
    return o
sh = {n:[shuf(keys[n],s) for s in range(1,31)] for n in keys}
for header, lines in decode.load_ciphertext(HERE/"fortmonroe"/"fm_r7a_entries.txt"):
    text = decode.entry_text(lines); out=[header.split('|')[1].strip()]
    for n in ("no1","no2","no9"):
        t = decode.decode_entry(text, keys[n])[1]['H']
        c = [decode.decode_entry(text, k)[1]['H'] for k in sh[n]]
        out.append(f"{n} H={t} shuf mean {st.mean(c):.1f} max {max(c)}")
    print(" | ".join(out), flush=True)
