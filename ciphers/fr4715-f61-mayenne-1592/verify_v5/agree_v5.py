#!/usr/bin/env python3
"""VERIFY-F61-V5: row-by-row agreement of the verifier's blind sign passes (P/Q) with the runner's (A/B) on f.176r L06-L11,
L28-L33, and of the verifier's clear read of fol. 177r with the runner's. Writes agree_v5_result.txt; --check."""
import difflib, os, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.abspath(f"{HERE}/../family")
sys.path.insert(0, F); sys.path.insert(0, os.path.abspath(f"{HERE}/../scripts"))
import h170_gate as g, build_f176_key as b
def mine(tag):
    d = defaultdict(list)
    for sr in ("L06-L11", "L28-L33"):
        for r in g.rd(f"{HERE}/passes/f176r_signs{tag}_{sr}.tsv"):
            s = {"EBR_A": "EBR", "EBR_B": "EBR"}.get(r["sign"].strip(), r["sign"].strip())
            if s != "PLAIN": d[r["line"].strip()].append(s)
    return d
P, Q = mine("P"), mine("Q"); A, B = b.pass_rows("A"), b.pass_rows("B")
out = ["row\tsigns A/B/P/Q\tagree A-B\tagree P-Q\tagree cons(AB)-cons(PQ) (share of AB consensus signs matched to the same code)"]
conf = Counter(); tot = [0, 0]
for k in list(range(6, 12)) + list(range(28, 34)):
    l = f"L{k:02d}"; ab = b.consensus(A[l], B[l]); pq = b.consensus(P[l], Q[l])
    r = lambda x, y: difflib.SequenceMatcher(None, x, y, autojunk=False).ratio()
    sm = difflib.SequenceMatcher(None, ab, pq, autojunk=False); same = 0; n_ab = sum(not s.startswith("?") for s in ab)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal": same += sum(not s.startswith("?") for s in ab[i1:i2]); [conf.update([(s, s)]) for s in ab[i1:i2] if not s.startswith("?")]
        elif op == "replace" and i2 - i1 == j2 - j1:
            for x, y in zip(ab[i1:i2], pq[j1:j2]):
                if not x.startswith("?") and not y.startswith("?"): conf[(x, y)] += 1
    tot[0] += same; tot[1] += n_ab
    out.append(f"{l}\t{len(A[l])}/{len(B[l])}/{len(P[l])}/{len(Q[l])}\t{r(A[l], B[l]):.2f}\t{r(P[l], Q[l]):.2f}\t{same}/{n_ab} = {same/max(1,n_ab):.2f}")
out.append(f"all 12 rows: runner consensus signs matched by the verifier's consensus {tot[0]}/{tot[1]} = {tot[0]/tot[1]:.2f}")
out.append(""); out.append("confusion, runner consensus class -> verifier consensus class (1:1 aligned columns, both sides agreed), key classes only:")
for x in ["VBAR_A", "VBAR_B", "EBR", "HASH4", "4STEM", "DBL", "ZHOOK", "C43", "BETA", "4PI", "4TRI", "PHI", "INF", "CROSS", "SBS"]:
    row = {y: n for (a, y), n in conf.items() if a == x}
    if row: out.append(f"{x}\t" + " ".join(f"{y}{n}" for y, n in sorted(row.items(), key=lambda t: -t[1])))
# clear text agreement
def lines_of(pat):
    d = {}
    import glob
    for f in sorted(glob.glob(pat)):
        for r in g.rd(f): d.setdefault(r["line"].strip(), g.fold(r["text"]))
    return d
R = lines_of(f"{F}/passes/f177r_clearA_*.tsv"); V = lines_of(f"{HERE}/passes/f177r_clearV_*.tsv")
out.append(""); out.append("clear read fol. 177r, folded letters: line\trunner len\tverifier len\tsimilarity (difflib ratio)")
ss = []
for l in sorted(V, key=lambda x: int(x[1:])):
    if l in R: rr = difflib.SequenceMatcher(None, R[l], V[l], autojunk=False).ratio(); ss.append(rr); out.append(f"{l}\t{len(R[l])}\t{len(V[l])}\t{rr:.2f}")
out.append(f"mean similarity {sum(ss)/len(ss):.2f} over {len(ss)} lines")
txt = "\n".join(out) + "\n"; p = f"{HERE}/agree_v5_result.txt"
if "--check" in sys.argv: sys.exit(0 if open(p).read() == txt else "STALE")
open(p, "w").write(txt); print(txt)
