#!/usr/bin/env python3
"""H54: how coarse must the shorthand glyph inventory be before two blind readers agree? Reads line B's B35 passes
(line-b/b35/, through its own reconcile.py loader; nothing there is edited). Greedy agglomeration on the TRAIN half:
repeatedly merge the pair of current classes the two readers confuse most often (ties: the rarer pair of classes),
down to 2 classes; at every class count, score the HELD-OUT half: positional agreement on crops where both readers
found the same glyph count, the agreement expected by chance from the two readers' own class marginals there, and
Cohen's kappa. Both splits (crops 1-15 / 16-29). B35's gate was 90 pct agreement; a coarse inventory can reach it by
chance alone (two classes, one dominant), so kappa is what says the readers see the same thing.
usage: python3 h54/coarse_curve.py"""
import os, sys
from collections import Counter
B35 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "line-b", "b35")
sys.path.insert(0, B35); cwd = os.getcwd(); os.chdir(B35); sys.argv = ["x"]
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    from reconcile import A, B, glyphs
os.chdir(cwd)
def pairs(crops):
    out = []
    for k in crops:
        ga, gb = glyphs(A[k]), glyphs(B[k])
        if len(ga) == len(gb): out += [(x, y) for x, y in zip(ga, gb) if "??" not in (x, y)]
    return out
def run(train, test):
    tr, te = pairs(train), pairs(test)
    labels = sorted({x for p in tr + te for x in p}); cls = {l: l for l in labels}
    def find(x):
        while cls[x] != x: x = cls[x]
        return x
    freq = Counter(x for p in tr for x in p)
    rows = []
    while True:
        m = lambda x: find(x)
        a = [(m(x), m(y)) for x, y in te]; n = len(a)
        agree = sum(x == y for x, y in a) / n
        ca, cb = Counter(x for x, _ in a), Counter(y for _, y in a)
        pe = sum(ca[c] * cb[c] for c in ca) / (n * n); kappa = (agree - pe) / (1 - pe) if pe < 1 else 0.0
        k = len({m(l) for l in labels}); rows.append((k, agree, pe, kappa))
        if k <= 2: break
        conf = Counter()
        for x, y in tr:
            u, v = m(x), m(y)
            if u != v: conf[tuple(sorted((u, v)))] += 1
        if conf:
            (u, v), _ = max(conf.items(), key=lambda kv: (kv[1], -(freq[kv[0][0]] + freq[kv[0][1]])))
        else:  # no confusion left in train: merge the two rarest classes
            cf = Counter({c: 0 for c in {m(l) for l in labels}})
            for l in labels: cf[m(l)] += freq[l]
            u, v = [c for c, _ in sorted(cf.items(), key=lambda kv: kv[1])[:2]]
        cls[find(u)] = find(v)
    return len(te), rows
for name, train, test in (("train 1-15 / test 16-29", range(1, 16), range(16, 30)), ("train 16-29 / test 1-15", range(16, 30), range(1, 16))):
    n, rows = run(train, test)
    print(f"{name}: {n} held-out aligned glyph pairs")
    for k, ag, pe, ka in rows:
        if k in (38, 35, 30, 25, 20, 15, 12, 10, 8, 6, 5, 4, 3, 2) or ag >= 0.9 or k == rows[0][0]:
            print(f"  classes {k:2d}\tagreement {ag:.3f}\tchance {pe:.3f}\tkappa {ka:+.3f}")
    best = max(rows, key=lambda r: r[3]); gate = [r for r in rows if r[1] >= 0.9]
    print(f"  best kappa {best[3]:+.3f} at {best[0]} classes (agreement {best[1]:.3f}); first class count reaching 90 pct agreement: "
          + (f"{gate[0][0]} (kappa {gate[0][3]:+.3f})" if gate else "none"))
