#!/usr/bin/env python3
"""N2R-2: per-entry book assignment over ms18/ms18_n2g_entries.txt: vocabulary share in key.md / key-no2.md / key-no9.md and decode H/C/I/M counts
under No. 1, No. 2, No. 9 and a meaning-shuffled No. 2 (seeds 7, 8, 9). Same shape as ms18_r7.py; machinery of decode.py unchanged. Usage: ms18_n2g.py [--show]"""
import random, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); import decode
keys = {n: decode.load_key(HERE/f) for n, f in [("no1","key.md"),("no2","key-no2.md"),("no9","key-no9.md")]}
def shuffled(key, seed):
    rows = [k for k,v in key.items() if v[2]=="word"]
    meanings = [key[k] for k in rows]; rnd = random.Random(seed); rnd.shuffle(meanings)
    out = dict(key)
    for k,m in zip(rows, meanings): out[k] = m
    return out
SEEDS = (7, 8, 9)
for s in SEEDS: keys[f"no2shuf{s}"] = shuffled(keys["no2"], s)
FUNC = set("the a an of to and in is are was were be been for on at by with that this it as or not but from have has had will would shall should you your i we he his her him them they their there then than so if do does did can could may might must".split())
def toks(t): return [w for w in re.findall(r"[a-z]+", re.sub(r"\s*=\s*","",t.lower())) if w not in FUNC and len(w)>1]
show = "--show" in sys.argv
for header, lines in decode.load_ciphertext(HERE/"ms18"/"ms18_n2g_entries.txt"):
    text = decode.entry_text(lines); tk = toks(text)
    share = {n: sum(1 for w in tk if decode.lookup(w, keys[n])[2] is not None) for n in ("no1","no2","no9")}
    print(f"{header.split('|')[0].strip()} {header.split('|')[3].strip() if header.count('|')>2 else ''} tokens={len(tk)} " + " ".join(f"{n}={share[n]}({share[n]/max(1,len(tk)):.2f})" for n in share))
    cnt = {}
    for n in keys:
        r, c = decode.decode_entry(text, keys[n]); cnt[n] = (c['H'], c['C'], c['I'], c['M'])
        if show and n in ("no1","no2"): print(f"  [{n}]", r.replace("\n"," ")[:600])
    print("  H/C/I/M  " + "  ".join(f"{n}={cnt[n]}" for n in ("no1","no2","no9")) + "  | shuf2 H: " + ",".join(str(cnt[f'no2shuf{s}'][0]) for s in SEEDS))
