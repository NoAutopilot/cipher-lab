#!/usr/bin/env python3
"""MS65-R2 (10 Oct 2026): coherence control for the guessed-book decode. H counts cannot separate a key from a meaning-shuffled copy of it (the same codes resolve),
so score each decode by mean per-bigram log-probability under an interpolated bigram model of period text (OR djvu volumes, letters only), trained WITHOUT the volumes
that print any of these rows (OR I/32 pt 2, I/33, I/34 pt 2, I/37 pt 2). Compared: No. 1, No. 2, No. 9, No. 2 shuffled (seeds 1-3), No. 1 shuffled (seeds 1-3).
Usage: python3 ms18/n2r6_coherence.py ENTRIES.txt VOLDIR [more *.txt]   (train on sources/ia-fulltext/print-check OR gz + VOLDIR/*.txt, minus the excluded ids)."""
import glob, gzip, math, os, random, re, sys
from collections import Counter
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); import decode
EXCL = {"warofrebellion014703rootrich"}
PC = HERE/".."/".."/"sources"/"ia-fulltext"/"print-check"
words = lambda s: re.findall(r"[a-z]+", s.lower())
big, uni = Counter(), Counter(); used = []
def feed(txt):
    w = words(txt); uni.update(w); big.update(zip(w, w[1:]))
for p in sorted(glob.glob(str(PC/"warofrebellion*_djvu.txt.gz"))):
    v = os.path.basename(p)[:-12]
    if v in EXCL: continue
    feed(gzip.open(p, "rt", errors="ignore").read()); used.append(v)
for p in sorted(glob.glob(sys.argv[2]+"/*.txt")):
    v = os.path.basename(p)[:-4]
    if v in EXCL or v in used: continue
    feed(open(p, errors="ignore").read()); used.append(v)
N = sum(uni.values()); V = len(uni)
def lp(a, b):
    pu = (uni[b]+0.5)/(N+0.5*V); pb = big[(a, b)]/uni[a] if uni[a] else 0.0
    return math.log(0.7*pb + 0.3*pu)
def score(text):
    t = re.sub(r"\{[^}]*\}", " ", text); t = re.sub(r"[\[\]]", " ", t)
    w = words(t); return sum(lp(a, b) for a, b in zip(w, w[1:]))/max(1, len(w)-1)
keys = {n: decode.load_key(HERE/f) for n, f in [("no1","key.md"),("no2","key-no2.md"),("no9","key-no9.md")]}
def shuffled(key, seed):
    rows = [k for k,v in key.items() if v[2]=="word"]; m = [key[k] for k in rows]; random.Random(seed).shuffle(m)
    out = dict(key); out.update(zip(rows, m)); return out
print(f"trained on {len(used)} OR volumes, {N} words, vocab {V}; excluded {sorted(EXCL)}")
print("row\tno1\tno2\tno9\tno2shuf(1,2,3)\tno1shuf(1,2,3)\tno2_beats_all")
for header, lines in decode.load_ciphertext(Path(sys.argv[1])):
    text = decode.entry_text(lines); r = {}
    for n in ("no1","no2","no9"): r[n] = score(decode.decode_entry(text, keys[n])[0])
    s2 = [score(decode.decode_entry(text, shuffled(keys["no2"], s))[0]) for s in (1,2,3)]
    s1 = [score(decode.decode_entry(text, shuffled(keys["no1"], s))[0]) for s in (1,2,3)]
    ok = r["no2"] > max(r["no1"], r["no9"], *s2, *s1)
    print(f"{header.split('|')[0].strip()}\t{r['no1']:.3f}\t{r['no2']:.3f}\t{r['no9']:.3f}\t{'/'.join(f'{x:.3f}' for x in s2)}\t{'/'.join(f'{x:.3f}' for x in s1)}\t{ok}")
