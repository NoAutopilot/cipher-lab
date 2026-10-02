#!/usr/bin/env python3
"""Score the WVO 58 trial decode (NEXT-AVS, 2 Oct 2026): what fraction of the letter-words a key produces from
ciphertext_58_sample.tsv is a word of the f.272 decipherment (plaintext_58_f272.txt)? Word signs (NEWn, U-graded) are
skipped. Normalisation: lower case, u/v -> u, ai/ei -> ei, ss -> s, umlauts stripped, non-letters dropped.
Control (rule 3): the same score for key_53 and for 200 random value-permutations of key_74 (a key of the right sign
inventory with the wrong values), reported as mean / max. Exit 0 always; numbers go to NOTES.md.
  python3 trial58/score_trial58.py   (run from ciphers/august-van-saksen-1561-64)"""
import csv, random, re, sys, unicodedata
from collections import defaultdict

def norm(w):
    w = unicodedata.normalize("NFKD", w.lower()); w = "".join(c for c in w if c.isalpha())
    return w.replace("v","u").replace("ai","ei").replace("ss","s")

def load_key(p):
    k = {}
    for r in csv.DictReader((l for l in open(p) if not l.startswith("#")), delimiter="\t"):
        k[r["sign"]] = r["value"]
    return k

rows = [r for r in csv.DictReader((l for l in open("ciphertext_58_sample.tsv") if not l.startswith("#")), delimiter="\t")]
# rebuild word units from the source '|' boundaries: a NEWn or DOT ends a unit; positions are contiguous otherwise, so we
# take the unit boundaries from the sign stream the same way decode_key.py --style words did (gap = non-letter).
# word boundaries are the '|' layout of the builder (not stored in the TSV), one list of unit sizes per line:
LAYOUT = {
 "58_L01": [2,3,4,2,1,4,2,6,1,4], "58_L02": [4,2,1,8,7,3,3,1], "58_L03": [6,6,3,7,6],
 "58_L08": [3,1,1,11,6,3,4], "58_L09": [12,2,5,5,1,6], "58_L10": [2,1,4,8,8,3,5],
 "58_L11": [7,2,5,3,2,6,1,9], "58_L13": [6,2,1,4,9,1,5,5], "58_L14": [3,1,3,4,2,8,10], "58_L15": [4,1,6,8,6],
}
by_line = defaultdict(list)
for r in rows: by_line[r["line"]].append(r["sign"])
units = []
for ln, sizes in LAYOUT.items():
    signs = by_line[ln]; assert sum(sizes) == len(signs), (ln, sum(sizes), len(signs))
    i = 0
    for n in sizes:
        u = signs[i:i+n]; i += n
        if all(not s.startswith("NEW") and s != "DOT" for s in u): units.append(u)
plain = set()
for l in open("trial58/plaintext_58_f272.txt"):
    if l.startswith("#"): continue
    for w in l.split()[1:]: plain.add(norm(w.strip("?,.()")))
plain.discard("")

def score(key):
    hit = 0; out = []
    for u in units:
        w = norm("".join(key.get(s, "?") for s in u))
        ok = w in plain; hit += ok; out.append((w, ok))
    return hit, len(units), out

k74 = load_key("key_74.tsv"); k53 = load_key("key_53.tsv")
h, n, out = score(k74); print(f"key_74: {h}/{n} letter-words of the sample are words of f.272 ({100*h/n:.1f}%)")
print("  misses:", [w for w, ok in out if not ok])
h53, n, out53 = score(k53); print(f"key_53: {h53}/{n} ({100*h53/n:.1f}%)"); print("  hits:", [w for w, ok in out53 if ok])
random.seed(1); letters = [s for s in k74 if len(k74[s]) == 1]; vals = [k74[s] for s in letters]; sc = []
for _ in range(200):
    random.shuffle(vals); kk = dict(k74); kk.update(zip(letters, vals)); sc.append(score(kk)[0])
print(f"shuffled key_74 values (200 draws, same sign inventory): mean {sum(sc)/len(sc):.2f}/{n}, max {max(sc)}/{n}")
