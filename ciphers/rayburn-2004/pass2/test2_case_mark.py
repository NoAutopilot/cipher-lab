#!/usr/bin/env python3
"""Test 2 (PREREG-test2.md): is the underline/strike mark predicted by letter case? Blind pass B, permutation control."""
import csv, random, os
HERE = os.path.dirname(os.path.abspath(__file__))
BLEED = {(1, 6), (4, 8), (5, 8), (6, 6), (7, 1), (6, 1)}
AMBIG = set("ckosuvwxyz")

def tokens(drop_ambig=False):
    out = []
    for r in csv.DictReader(open(os.path.join(HERE, "passB_raw.tsv")), delimiter="\t"):
        if r["group"] != "main" or (int(r["row"]), int(r["pos"])) in BLEED or r["mark"] not in ("U", "S"):
            continue
        c = r["symbol"][0]
        if not c.isascii() or not c.isalpha() or (drop_ambig and c.lower() in AMBIG):
            continue
        out.append((c.isupper(), r["mark"]))
    return out

def agree(toks):
    return sum((up and m == "U") or (not up and m == "S") for up, m in toks) / len(toks)

def run(drop_ambig, seed=20261006, n=10000):
    t = tokens(drop_ambig); a = agree(t); rng = random.Random(seed)
    cases = [u for u, _ in t]; marks = [m for _, m in t]; perm = []
    for _ in range(n):
        rng.shuffle(marks); perm.append(agree(list(zip(cases, marks))))
    perm.sort()
    p = sum(x >= a for x in perm) / n
    return len(t), sum(cases), a, sum(perm) / n, perm[int(0.95 * n)], p

for label, d in (("primary (all letters)", False), ("secondary (case not size-only)", True)):
    N, up, a, mu, p95, p = run(d)
    print(f"{label}: N={N} upper={up} lower={N-up} A={a:.3f} control mean={mu:.3f} p95={p95:.3f} p={p:.4f}")
