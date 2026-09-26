#!/usr/bin/env python3
"""AX-NAMES step 3: hold out 5811. Map built without 5811 (build_names.build(exclude=['5811'])) predicts
5811's codes > 120; truth is 5811's own observations (build with every other letter excluded, manual rows
for 5811 kept). Reports hit rates by class (NULL / word) and the same for 20 shuffles (seeds 1-20) of the
map's code->value assignment. Writes axnames/control_5811.tsv."""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_names as B

ALL = ["5810", "5811", "4503", "5549", "5550", "5557", "5797"]


def table(rows):
    return {r[0]: r[1] for r in rows if r[6] in ("C", "M") and " | " not in r[1] and not r[1].startswith("?")}


train = table(B.build(exclude=["5811"]))
truth = table(B.build(exclude=[l for l in ALL if l != "5811"]))
pred = sorted(c for c in truth if c in train)


def hit(p, t):
    return int(p == t or (p != "NULL" and t != "NULL" and (t.startswith(p) or p.startswith(t))))


def score(m):
    res = {"NULL": [0, 0], "word": [0, 0]}
    for c in pred:
        k = "NULL" if m[c] == "NULL" else "word"
        res[k][1] += 1
        res[k][0] += hit(m[c], truth[c])
    return res


real = score(train)
codes, vals = list(train), list(train.values())
sh = []
for seed in range(1, 21):
    v = vals[:]; random.Random(seed).shuffle(v)
    sh.append(score(dict(zip(codes, v))))
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "control_5811.tsv")
with open(out, "w") as f:
    f.write("code\tpredicted\t5811_observed\thit\n")
    for c in pred:
        f.write(f"{c}\t{train[c]}\t{truth[c]}\t{hit(train[c], truth[c])}\n")
def pct(a): return 100.0 * a[0] / a[1] if a[1] else float("nan")
for k in ("NULL", "word"):
    s = [pct(x[k]) for x in sh if x[k][1]]
    print(f"{k}: held-out {real[k][0]}/{real[k][1]} = {pct(real[k]):.1f}%; shuffles mean {sum(s)/len(s) if s else float('nan'):.1f}% (min {min(s) if s else float('nan'):.1f}, max {max(s) if s else float('nan'):.1f}, n={len(s)})")
allr = [real['NULL'][0]+real['word'][0], real['NULL'][1]+real['word'][1]]
alls = [100.0*(x['NULL'][0]+x['word'][0])/max(1,x['NULL'][1]+x['word'][1]) for x in sh]
print(f"all: held-out {allr[0]}/{allr[1]} = {pct(allr):.1f}%; shuffles mean {sum(alls)/20:.1f}% (min {min(alls):.1f}, max {max(alls):.1f})")
print("5811 codes with no prediction:", sorted(set(truth) - set(train), key=int))
