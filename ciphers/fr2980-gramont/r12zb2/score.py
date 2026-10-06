#!/usr/bin/env python3
"""R12D-GRAZB2 (copy of r12zb/score.py, only the sort path changed): score r12zb2/sort_sonnet.tsv against r12zb/occ.tsv under PREREG-R12D-GRAZB.md's gate. python3 r12zb2/score.py"""
import sys, collections
from pathlib import Path
if "--help" in sys.argv: print(__doc__); sys.exit()
H = Path(__file__).resolve().parent.parent / "r12zb"; H2 = Path(__file__).resolve().parent
occ = {l.split("\t")[0]: l.split("\t") for l in (H / "occ.tsv").read_text().splitlines()[1:]}
cl = {l.split("\t")[0]: l.split("\t")[1] for l in (H2 / "sort_sonnet.tsv").read_text().splitlines()[1:]}
tab = collections.defaultdict(collections.Counter)
for i, r in occ.items(): tab[(r[1], r[2])][cl[i]] += 1
for k in sorted(tab): print(k, dict(tab[k]))
def on(sets, src=None):
    c = collections.Counter()
    for (s, so), cc in tab.items():
        if s in sets and (src is None or so == src): c.update({k: v for k, v in cc.items() if k != "OFF"})
    return c
def plur(c): k, v = c.most_common(1)[0]; return k, v / sum(c.values()), sum(c.values())
off = sum(1 for i in occ if cl[i] == "OFF"); print(f"G0 OFF {off}/{len(occ)} = {off/len(occ):.2f} -> {'ok' if off/len(occ) <= 0.30 else 'UNDECIDED'}")
P = plur(on({"P"})); print("P plurality", P)
zfam = on({"T1", "T2a", "T2b", "P"}); g1 = True; dp = {}
for d in ("fh", "n6"):
    k, f, n = plur(on({d})); dp[d] = k
    per = {s: on({d}, s)[k] / max(1, sum(on({d}, s).values())) for s in ("f30", "fr3040")}
    zshare = zfam[k] / sum(zfam.values())
    ok = f >= .75 and all(v >= .60 for v in per.values()) and k != P[0] and zshare <= .20
    print(f"G1 {d}: plurality {k} {f:.2f} of {n}; per-source {per}; z-family share {zshare:.2f} -> {'pass' if ok else 'FAIL'}"); g1 &= ok
g1 &= dp["fh"] != dp["n6"]; print("G1", "PASS" if g1 else "FAIL (NON-TEST)")
T1 = plur(on({"T1"})); T2 = plur(on({"T2a", "T2b"})); print("T1", T1, "T2", T2, "T2a", plur(on({"T2a"})), "T2b", plur(on({"T2b"})))
if not g1: print("OUTCOME NON-TEST")
elif T1[1] >= .70 and T2[1] >= .70 and T1[0] == T2[0] and T1[0] != P[0]: print("OUTCOME SAME")
elif T1[0] != T2[0] and T1[1] >= .60 and T2[1] >= .60: print("OUTCOME DIFFERENT")
else: print("OUTCOME UNDECIDED")
