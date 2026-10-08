#!/usr/bin/env python3
"""BNF-G60R robustness check (8 Oct 2026), registered in .claude/briefs/runs/2026-10-08-ytbiz-bnf-g60r.md.
Uses g60d_instrument.py unchanged. Tags read from ciphertext.tsv, trailing '?' stripped; tags not in key are
skipped by the instrument's Viterbi (as it does for any unkeyed tag).
Null A: 1000 class-preserving shuffled keys (seed 7001). Null B: 200 permutations of tag order (seed 7002), real key."""
import sys, random
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import g60d_instrument as G
J = G.J
T = Path(__file__).resolve().parents[1]
seq = []
for l in (T / "ciphertext.tsv").read_text().splitlines():
    for t in l.split("\t")[1].split():
        seq.append(t.rstrip("?"))
key = G.load_key(); inst = G.Inst()
ra, rb = inst.stats(seq, key)
txt = inst.viterbi(seq, key)
print(f"tags {len(seq)} keyed {sum(t in key for t in seq)} unkeyed {sorted(set(t for t in seq if t not in key))}")
print(f"real (a) {ra:.3f} (b) {rb:.3f}"); print("decode", txt)
if len(sys.argv) > 1 and sys.argv[1] == "real": sys.exit()
rnd = random.Random(7001)
A = [inst.stats(seq, G.make_null(key, rnd)) for _ in range(1000)]
na = sorted(x[0] for x in A); nb = sorted(x[1] for x in A)
print(f"NullA (a) p99 {J.pct(na,.99):.3f} rank {sum(x>=ra for x in na)}/1000 >= real | (b) p99 {J.pct(nb,.99):.3f} rank {sum(x>=rb for x in nb)}/1000 >= real")
rnd = random.Random(7002)
B = []
for _ in range(200):
    s = seq[:]; rnd.shuffle(s); B.append(inst.stats(s, key))
ba = sorted(x[0] for x in B); bb = sorted(x[1] for x in B)
print(f"NullB (a) p95 {J.pct(ba,.95):.3f} p99 {J.pct(ba,.99):.3f} share>=real {sum(x>=ra for x in ba)/200:.3f}")
print(f"NullB (b) p95 {J.pct(bb,.95):.3f} p99 {J.pct(bb,.99):.3f} share>real {sum(x>rb for x in bb)/200:.3f} share>=real {sum(x>=rb for x in bb)/200:.3f}")
