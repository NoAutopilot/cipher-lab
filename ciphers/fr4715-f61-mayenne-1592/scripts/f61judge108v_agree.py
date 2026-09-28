#!/usr/bin/env python3
"""H85 add-on (28 Sept 2026, runner session_01NQpd6L9ZvLvjU1L7ttFmZs): letter-level agreement of the three independent
judge resolutions of the TARGET set on f.108v (seeds 101-103; each call saw different permutations and a different set
order). Reported, not gated (the gate is rank 1 of 21 in all three). Also the same statistic for the best-scoring
permutation of each call, as a floor. -> scripts/f61judge108v_agree.txt [--check]"""
import csv, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
def get(seed, which):
    k = json.load(open(f"{HERE}/f61judge_f108v_s{seed}_key.json"))["key"]
    rows = {r["label"].strip(): r for r in csv.DictReader((l for l in open(f"{HERE}/f61judge_f108v_s{seed}_verdict.tsv") if not l.startswith("#")), delimiter="\t")}
    tgt = [l for l, m in k.items() if m == 0][0]
    lab = tgt if which == "target" else max((l for l in rows if l != tgt), key=lambda l: float(rows[l]["score_0_10"]))
    return [s.strip().replace(" ", "") for s in rows[lab]["reading"].split("|")]
out = []
for which in ("target", "best_permutation"):
    R = {s: get(s, which) for s in (101, 102, 103)}
    same = tot = allthree = 0; lenok = 0
    for li in range(7):
        a, b, c = (R[s][li] if li < len(R[s]) else "" for s in (101, 102, 103))
        if len(a) == len(b) == len(c): lenok += 1
        n = min(len(a), len(b), len(c)); tot += n
        same += sum(1 for i in range(n) if a[i] == b[i]) + sum(1 for i in range(n) if a[i] == c[i]) + sum(1 for i in range(n) if b[i] == c[i])
        allthree += sum(1 for i in range(n) if a[i] == b[i] == c[i])
    out.append(f"{which}: lines of equal length in all three {lenok}/7; pairwise letter agreement {same / (3 * tot):.3f}; all three agree {allthree}/{tot} = {allthree / tot:.3f}")
txt = "\n".join(out) + "\n"; res = f"{HERE}/f61judge108v_agree.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
