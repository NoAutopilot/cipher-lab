#!/usr/bin/env python3
"""UNA-GRAM: score unagram/sort_sonnet.tsv against unagram/occ.tsv under PREREG-UNA-GRAM.md (G0 <= 0.20; G1 word for word from
r12zb2/score.py; G2 reference separation; per-target class). python3 unagram/score.py"""
import sys, collections
from pathlib import Path
if "--help" in sys.argv: print(__doc__); sys.exit()
H = Path(__file__).resolve().parent
occ = {l.split("\t")[0]: l.split("\t") for l in (H / "occ.tsv").read_text().splitlines()[1:]}
cl = {l.split("\t")[0]: l.split("\t")[1] for l in (H / "sort_sonnet.tsv").read_text().splitlines()[1:]}
tab = collections.defaultdict(collections.Counter)
for i, r in occ.items(): tab[(r[1], r[2])][cl[i]] += 1
for k in sorted(tab): print(k, dict(tab[k]))
def on(sets, src=None):
    c = collections.Counter()
    for (s, so), cc in tab.items():
        if s in sets and (src is None or so == src): c.update({k: v for k, v in cc.items() if k != "OFF"})
    return c
def plur(c): k, v = c.most_common(1)[0]; return k, v / sum(c.values()), sum(c.values())
off = sum(1 for i in occ if cl[i] == "OFF"); g0 = off / len(occ) <= 0.20
print(f"G0 OFF {off}/{len(occ)} = {off/len(occ):.2f} -> {'ok' if g0 else 'UNDECIDED'}")
P = plur(on({"P"})); B = plur(on({"B"})); print("P plurality", P, "| B plurality", B)
zfam = on({"X", "P", "B"}); g1 = True; dp = {}
for d in ("fh", "n6"):
    k, f, n = plur(on({d})); dp[d] = k
    per = {s: on({d}, s)[k] / max(1, sum(on({d}, s).values())) for s in ("f30", "fr3040")}
    zshare = zfam[k] / sum(zfam.values())
    ok = f >= .75 and all(v >= .60 for v in per.values()) and k != P[0] and zshare <= .20
    print(f"G1 {d}: plurality {k} {f:.2f} of {n}; per-source {per}; z-family share {zshare:.2f} -> {'pass' if ok else 'FAIL'}"); g1 &= ok
g1 &= dp["fh"] != dp["n6"]; print("G1", "PASS" if g1 else "FAIL (NON-TEST)")
g2 = B[1] >= .60 and P[1] >= .60 and B[0] != P[0] and B[0] not in dp.values() and P[0] not in dp.values()
print("G2", "PASS" if g2 else "FAIL (NON-TEST)")
for i, r in sorted(occ.items(), key=lambda x: x[1][3]):
    if r[1] != "X": continue
    c = cl[i]; v = "barred" if c == B[0] else "plain" if c == P[0] else "unclassed"
    print(f"X #{i} {r[3]}: {c} -> {v if (g0 and g1 and g2) else 'no call (gate failed)'}")
print("OUTCOME", "per-target calls above" if (g0 and g1 and g2) else "NON-TEST" if g0 else "UNDECIDED")
