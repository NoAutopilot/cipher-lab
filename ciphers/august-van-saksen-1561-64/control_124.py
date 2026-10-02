#!/usr/bin/env python3
"""A2-AVS4 (2 Oct 2026): rule-3 control for align_124.txt before its pairs enter key_98.
Statistic: of 124's sure pairings (unit without '~', sign without '?', unit not '?') on signs that key_98.tsv grades C
from 98 alone, the share whose unit equals key_98's value (u/v merged). Control: the same statistic with the units
shuffled within each line (pairing destroyed, line letter content kept), 1000 seeds. The control CAN differ: the
statistic depends on which unit sits on which sign, which the shuffle changes. Prints both numbers; exit 0."""
import csv, random, os, collections
D = os.path.dirname(os.path.abspath(__file__))
k98 = {}
for r in csv.DictReader(open(f"{D}/key_98_from98.tsv"), delimiter="\t"):
    if r["grade"] == "C": k98[r["sign"]] = r["value"]
norm = lambda u: "u" if u == "v" else u
rows = list(csv.DictReader(open(f"{D}/pairs_124.tsv"), delimiter="\t"))
sure = lambda r: not r["unit"].endswith("~") and not r["sign"].endswith("?") and r["unit"] != "?"
def score(units):
    n = ok = 0
    for r, u in zip(rows, units):
        if not sure(r) or r["sign"] not in k98 or u.endswith("~") or u == "?": continue
        n += 1; ok += norm(u) == norm(k98[r["sign"]])
    return ok, n
real = score([r["unit"] for r in rows])
bylines = collections.defaultdict(list)
for i, r in enumerate(rows): bylines[(r["page"], r["line"])].append(i)
cs = []
for seed in range(1000):
    rnd = random.Random(seed); units = [r["unit"] for r in rows]
    for idx in bylines.values():
        vals = [units[i] for i in idx]; rnd.shuffle(vals)
        for i, v in zip(idx, vals): units[i] = v
    ok, n = score(units); cs.append(ok / n if n else 0)
cs.sort()
print(f"target: {real[0]}/{real[1]} = {real[0]/real[1]:.3f} of 124's sure pairings on key_98 C signs agree with key_98")
print(f"control (units shuffled within line, 1000 seeds): mean {sum(cs)/len(cs):.3f}, p95 {cs[949]:.3f}, max {cs[-1]:.3f}")
bad = [(r['line'], r['idx'], r['sign'], r['unit'], k98[r['sign']]) for r in rows
       if sure(r) and r['sign'] in k98 and norm(r['unit']) != norm(k98[r['sign']])]
print("disagreements:", bad)
