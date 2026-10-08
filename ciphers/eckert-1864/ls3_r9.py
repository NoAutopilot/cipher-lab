#!/usr/bin/env python3
"""LS3-R9: per-entry book assignment (vocabulary share in key.md / key-no2.md / key-no9.md) and a matched control
(decode with each book, and with a meaning-shuffled copy of key-no9, seed 7) over ls3_r9_entries.txt.
Usage: python3 ls3_r9.py [--file F] [--show]   Counts only unless --show. Machinery of decode.py reused unchanged."""
import random, re, sys
from pathlib import Path
import decode
HERE = Path(__file__).resolve().parent
FILE = HERE / "ls3_r9_entries.txt"
if "--file" in sys.argv: FILE = Path(sys.argv[sys.argv.index("--file")+1])
keys = {n: decode.load_key(HERE/f) for n, f in [("no1","key.md"),("no2","key-no2.md"),("no9","key-no9.md")]}
def shuffled(key, seed=7):  # meanings permuted among the book's own word-kind rows, seed fixed
    rows = [k for k,v in key.items() if v[2]=="word"]
    meanings = [key[k] for k in rows]; rnd = random.Random(seed); rnd.shuffle(meanings)
    out = dict(key)
    for k,m in zip(rows, meanings): out[k] = m
    return out
keys["no9shuf"] = shuffled(keys["no9"]); keys["no1shuf"] = shuffled(keys["no1"])
FUNC = set("the a an of to and in is are was were be been for on at by with that this it as or not but from have has had will would shall should you your i we he his her their they them there which who what if so no any all can may must do did".split())
def toks(t): return [w for w in re.findall(r"[a-z]+", re.sub(r"\s*=\s*","",t.lower())) if w not in FUNC and len(w)>1]
show = "--show" in sys.argv
blocks = decode.load_ciphertext(FILE)
for header, lines in blocks:
    text = decode.entry_text(lines)
    tk = toks(text)
    share = {n: sum(1 for w in tk if decode.lookup(w, keys[n])[2] is not None) for n in ("no1","no2","no9")}
    print(f"{header.split('|')[0].strip()} tokens={len(tk)} " + " ".join(f"{n}={share[n]}({share[n]/max(1,len(tk)):.2f})" for n in share))
    for n in ("no9","no1","no2","no9shuf","no1shuf"):
        r, c = decode.decode_entry(text, keys[n])
        print(f"  {n}: H{c['H']} C{c['C']} I{c['I']} M{c['M']}")
        if show: print("   ", r.replace("\n"," "))
