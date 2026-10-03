#!/usr/bin/env python3
"""Code-group overlap of no. 94 f.120r (both blind passes) with the Gran-cifra code list, against a matched control.

  python3 ciphers/esp318-sicilia-1503/code_overlap.py [--check]

Overlap = distinct code groups read by BOTH passes (agreed groups) whose form, after merging the hand's look-alike
letters (u/n, c/k/q, y/i, z/s), equals a Gran-cifra code. Control: 200 random code lists with the key's own length
profile, drawn from the key codes' own letter frequencies (same size, same letters, no key structure); reports how
many agreed groups each random list matches. Writes code_overlap.json; --check exits 1 if it is stale (rule 7).
"""
import csv, json, random, sys, collections
from pathlib import Path
H = Path(__file__).resolve().parent
def norm(c): return c.translate(str.maketrans("ncqyz", "ukkis"))
key = [l.split("\t")[0][2:] for l in open(H / "key/key_gran_cifra.tsv") if l.startswith("g:")]
def groups(p): return collections.Counter(r["token"][2:] for r in csv.DictReader(open(p), delimiter="\t") if r["token"].startswith("g:"))
A, B = groups(H / "passes/f120r_passA.tsv"), groups(H / "passes/f120r_passB.tsv")
agreed = sorted(set(A) & set(B)); tok = {g: min(A[g], B[g]) for g in agreed}
def match(codes):
    s = {norm(c) for c in codes}; m = [g for g in agreed if norm(g) in s]
    return m, sum(tok[g] for g in m)
m, mt = match(key)
letters = "".join(key); rnd = random.Random(94); ctl = []
for _ in range(200):
    fake = ["".join(rnd.choice(letters) for _ in c) for c in key]
    ctl.append(len(match(fake)[0]))
ctl.sort()
res = {"agreed_distinct_groups": len(agreed), "agreed_group_tokens": sum(tok.values()), "key_codes": len(key),
       "matched_distinct": len(m), "matched_tokens": mt, "matched": {g: tok[g] for g in m},
       "control_random_lists": {"n": 200, "mean": round(sum(ctl) / len(ctl), 3), "p50": ctl[100], "p95": ctl[190], "max": ctl[-1]},
       "top_agreed_groups_not_in_key": sorted(((tok[g], g) for g in agreed if g not in m), reverse=True)[:15]}
out = H / "code_overlap.json"; new = json.dumps(res, indent=1) + "\n"
if "--check" in sys.argv:
    ok = out.exists() and out.read_text() == new; print("check:", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
out.write_text(new); print(new)
