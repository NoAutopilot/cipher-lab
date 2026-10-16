#!/usr/bin/env python3
"""HEID-1623A positive control (added after the target run, descriptive, not a PREREG gate): can tools/interlinear_align.py pass
its own shuffle gate at THIS N? Same 5 plain spans, same token count per pair as the real pairs; the cipher is generated from a known
one-code-per-chunk table (chunks of 1-3 letters, length mix drawn so each pair has its real token count), codes drawn from the real
code alphabet (numbers 1-99 and letters). usage: python3 poscontrol.py SEED OUT_PAIRS.tsv"""
import sys, csv, random, re
seed, out = int(sys.argv[1]), sys.argv[2]; R = random.Random(seed)
rows = list(csv.DictReader(open("pairs_1623.tsv"), delimiter="\t"))
pool = [str(i) for i in range(1, 100)] + list("abcdefghmprsxyzH"); R.shuffle(pool); table = {}
def code(ch):
    if ch not in table: table[ch] = pool.pop()
    return table[ch]
with open(out, "w") as f:
    f.write("plain_line\tplain_raw\tcipher_line\tcipher_raw\n")
    for r in rows:
        letters = re.sub(r"[^a-z]", "", r["plain_raw"].lower()); n = len(r["cipher_raw"].split())
        n = max(1, min(n, len(letters)))
        cuts = sorted(R.sample(range(1, len(letters)), n - 1)) if n > 1 else []
        chunks = [letters[a:b] for a, b in zip([0] + cuts, cuts + [len(letters)])]
        f.write(f"{r['plain_line']}\t{r['plain_raw']}\t{r['cipher_line']}\t{' '.join('@' + code(c) for c in chunks)}\n")
