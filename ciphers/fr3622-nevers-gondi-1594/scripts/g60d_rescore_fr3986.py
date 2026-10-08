#!/usr/bin/env python3
"""BNF-G60D: numbers-only re-score of fr3986's ciphertext_v2.tsv with the g60d instrument (does not touch that folder)."""
import sys, random, statistics
from pathlib import Path
R = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(R / "tools")); sys.path.insert(0, str(Path(__file__).parent))
import decode_key as dk, judge_plaintext as J, g60d_instrument as G
F = R / "ciphers/fr3986-nevers-revol-1593"
k0 = dk.load_keys(str(F), ['../../tools/keys/key60.tsv', 'key_atlas_extra.tsv'])
key = {}
for s, d in k0.items():
    a = [x for x in (J.fold(v) for v in d['value'].split('|')) if x]
    if a: key[s] = a
rows = [l.rstrip('\n').split('\t') for l in open(F / 'ciphertext_v2.tsv') if l.strip() and not l.startswith('#')][1:]
seq = [r[2] for r in rows]; inkey = [s for s in seq if s in key]
print(f"signs {len(seq)} in key {len(inkey)} key tags {len(key)}")
inst = G.Inst(); ra, rb = inst.stats(seq, key); rnd = random.Random(7)
nul = [inst.stats(seq, G.make_null(key, rnd)) for _ in range(200)]
for name, r, xs in (("(a) 4-gram", ra, sorted(x[0] for x in nul)), ("(b) word cover", rb, sorted(x[1] for x in nul))):
    print(f"{name}: real {r:.3f} shuffled mean {statistics.mean(xs):.3f} p95 {J.pct(xs,.95):.3f} p99 {J.pct(xs,.99):.3f} rank {sum(x<r for x in xs)+1}/201")
