#!/usr/bin/env python3
"""MS18-R9: per-entry book assignment (vocabulary share in key.md / key-no2.md / key-no9.md) and a matched control
(decode with each of the three books and with a meaning-shuffled copy of the chosen book, seed 7) over fortmonroe/ms18_r9_entries.txt.
Usage: python3 ms18/ms18_r9.py [--show]   Machinery of decode.py reused unchanged (same shape as ls3_r9.py)."""
import random, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent)); import decode
HERE = Path(__file__).resolve().parent.parent
keys = {n: decode.load_key(HERE/f) for n, f in [("no1","key.md"),("no2","key-no2.md"),("no9","key-no9.md")]}
def shuffled(key, seed=7):
    rows = [k for k,v in key.items() if v[2]=="word"]
    meanings = [key[k] for k in rows]; rnd = random.Random(seed); rnd.shuffle(meanings)
    out = dict(key)
    for k,m in zip(rows, meanings): out[k] = m
    return out
keys["no1shuf"] = shuffled(keys["no1"]); keys["no2shuf"] = shuffled(keys["no2"])
FUNC = set("the a an of to and in is are was were be been for on at by with that this it as or not but from have has had will would shall should you your i we he his her him them they their there then than so if do does did can could may might must".split())
def toks(t): return [w for w in re.findall(r"[a-z]+", re.sub(r"\s*=\s*","",t.lower())) if w not in FUNC and len(w)>1]
show = "--show" in sys.argv
for header, lines in decode.load_ciphertext(HERE/"ms18"/"ms18_r9_entries.txt"):
    text = decode.entry_text(lines); tk = toks(text)
    share = {n: sum(1 for w in tk if decode.lookup(w, keys[n])[2] is not None) for n in ("no1","no2","no9")}
    print(f"{header.split('|')[0].strip()} tokens={len(tk)} " + " ".join(f"{n}={share[n]}({share[n]/max(1,len(tk)):.2f})" for n in share))
    for n in ("no1","no2","no9","no1shuf","no2shuf"):
        r, c = decode.decode_entry(text, keys[n])
        print(f"  {n}: H{c['H']} C{c['C']} I{c['I']} M{c['M']}")
        if show: print("   ", r.replace("\n"," ")[:520])
