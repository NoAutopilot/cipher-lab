#!/usr/bin/env python3
"""LS4-R2a: per-entry book assignment (vocabulary share key.md / key-no2.md / key-no9.md) and matched control:
decode with each book plus a meaning-shuffled copy of key-no2 (seeds 7, 11, 13), counting H and the mean word-length plausibility.
Usage: python3 ls4_r2a_controls.py [--file F] [--show]   Machinery of decode.py reused; same shuffling as ls3_r9.py."""
import random, re, sys
from pathlib import Path
import decode
HERE = Path(__file__).resolve().parent
FILE = HERE / "ls4_r2a_entries.txt"
if "--file" in sys.argv: FILE = Path(sys.argv[sys.argv.index("--file")+1])
keys = {n: decode.load_key(HERE/f) for n, f in [("no1","key.md"),("no2","key-no2.md"),("no9","key-no9.md")]}
def shuffled(key, seed):
    rows = [k for k,v in key.items() if v[2]=="word"]
    meanings = [key[k] for k in rows]; random.Random(seed).shuffle(meanings)
    out = dict(key)
    for k,m in zip(rows, meanings): out[k] = m
    return out
for s in (7,11,13): keys[f"no2shuf{s}"] = shuffled(keys["no2"], s)
FUNC = set("the a an of to and in is are was were be been for on at by with that this it as or not but from have has had will would shall should you your i we he his her their they them there which what who whom if so no all any can may must do does did me my our us".split())
def toks(t): return [w for w in re.findall(r"[a-z]+", re.sub(r"\s*=\s*","",t.lower())) if w not in FUNC and len(w)>1]
show = "--show" in sys.argv
for header, lines in decode.load_ciphertext(FILE):
    text = decode.entry_text(lines); tk = toks(text)
    share = {n: sum(1 for w in tk if decode.lookup(w, keys[n])[2] is not None) for n in ("no1","no2","no9")}
    print(f"{header.split('|')[0].strip()} tokens={len(tk)} " + " ".join(f"{n}={share[n]}({share[n]/max(1,len(tk)):.2f})" for n in share))
    for n in ("no2","no1","no9","no2shuf7","no2shuf11","no2shuf13"):
        r, c = decode.decode_entry(text, keys[n])
        print(f"  {n}: H{c['H']} C{c['C']} I{c['I']} M{c['M']}")
        if show: print("   ", r.replace("\n"," "))
