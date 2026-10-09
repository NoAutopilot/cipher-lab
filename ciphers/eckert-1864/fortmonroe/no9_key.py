#!/usr/bin/env python3
"""NO9-KEY (9 Oct 2026): controlled key test of Cipher No. 9 (key-no9.md) on five Fort Monroe rows (no9_entries.txt, from no9_dump.py).
Per row: share of non-function tokens each book reads (key.md No. 1, key-no2.md No. 2, key-no9.md No. 9) and the decoded text.
Controls (rule 3):
 (a) SHARE NULL that can differ from the target: the same No. 9 share statistic over every *clear* Fort Monroe entry (entries-fm.tsv
     best_book == 'clear') of 30-70 words -- how many plain words a book "reads" by accident at this length; mean and p99.
 (b) SENSE control: No. 9 with its word meanings shuffled (seeds 1..200); the share is identical by construction (a meaning shuffle keeps
     which words are in the key), so only the decoded text is compared, by eye, against the real No. 9 decode (seed 7 printed).
Usage: python3 no9_key.py [--show]"""
import csv, random, re, statistics, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; PARENT = HERE.parent
sys.path.insert(0, str(PARENT)); sys.path.insert(0, str(HERE)); import decode, fm_entries as F
keys = {n: decode.load_key(PARENT/f) for n, f in [("no1","key.md"),("no2","key-no2.md"),("no9","key-no9.md")]}
def shuffled(key, seed):
    rows = [k for k,v in key.items() if v[2]=="word"]; meanings = [key[k] for k in rows]; random.Random(seed).shuffle(meanings)
    out = dict(key); out.update(zip(rows, meanings)); return out
FUNC = set("the a an of to and in is are was were be been for on at by with that this it as or not but from have has had will would shall should you your i we he his her him them they their there then than so if do does did can could may might must".split())
def toks(t): return [w for w in re.findall(r"[a-z]+", re.sub(r"\s*=\s*","",t.lower())) if w not in FUNC and len(w)>1]
def share(tk, key): return sum(1 for w in tk if decode.lookup(w, key)[2] is not None) / max(1, len(tk))
codes, ents = F.build()
clear = [e for e in ents if e.get('best_book') == 'clear' and 30 <= e['words'] <= 70]
null = sorted(share(toks(" ".join(e['lines'])), keys["no9"]) for e in clear)
p99 = null[min(len(null)-1, int(0.99*len(null)))]
print(f"(a) No.9 share on clear FM entries 30-70 words: n={len(null)} mean {statistics.mean(null):.3f} p99 {p99:.3f}")
show = "--show" in sys.argv
for header, lines in decode.load_ciphertext(HERE/"no9_entries.txt"):
    text = decode.entry_text(lines); tk = toks(text)
    sh = {n: share(tk, keys[n]) for n in ("no1","no2","no9")}
    hits9 = [w for w in tk if decode.lookup(w, keys["no9"])[2] is not None]
    print(f"{header.split('|')[1].strip()} N={len(tk)} " + " ".join(f"{n}={sh[n]:.3f}" for n in sh) + f" | No.9 > null p99: {sh['no9'] > p99} | No.9 hits: {hits9}")
    for n in ("no1","no2","no9"):
        r, c = decode.decode_entry(text, keys[n]); print(f"  {n}: H{c['H']} C{c['C']} I{c['I']} M{c['M']}")
        if show: print("   ", r.replace("\n"," ")[:600])
    r, c = decode.decode_entry(text, shuffled(keys["no9"], 7)); print(f"  no9shuf(seed 7): H{c['H']}")
    if show: print("   ", r.replace("\n"," ")[:600])
