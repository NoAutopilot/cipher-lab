#!/usr/bin/env python3
"""Diff our cryptogram-1 transcription (ciphertext.txt) against an independent typed one with its own sign names.

Names differ between transcribers, so the diff is structural: each of our codes is mapped to the other side's
code it shares most positions with (one-to-one, greedy by overlap); a position disagrees when the other side's
sign there is not the mapped image of ours. Also reports pairwise agreement on "same sign / different sign" over
all 70*69/2 position pairs, and repeat-pair agreement (pairs either side calls the same sign).
Usage: transcription_diff.py OTHER.txt OUT.tsv   (OTHER: same row-major layout, '#' comments)
"""
import sys, itertools, collections, os
HERE = os.path.dirname(os.path.abspath(__file__))
def load(p):
    t = []
    for line in open(p):
        line = line.split('#')[0].strip()
        if line: t += line.split()
    return t
ours = load(os.path.join(HERE, '..', 'ciphertext.txt')); his = load(sys.argv[1])
assert len(ours) == len(his) == 70, (len(ours), len(his))
co = collections.Counter(zip(ours, his))
m, used = {}, set()
for (a, b), n in sorted(co.items(), key=lambda x: -x[1]):
    if a not in m and b not in used: m[a] = b; used.add(b)
rows, dis = [], 0
for i, (a, b) in enumerate(zip(ours, his)):
    ok = m.get(a) == b
    dis += not ok
    rows.append((f"r{i//10+1}c{i%10+1}", a, b, 'agree' if ok else 'DIFF'))
pairs = list(itertools.combinations(range(70), 2))
same = lambda t, i, j: t[i] == t[j]
pa = sum(same(ours, i, j) == same(his, i, j) for i, j in pairs) / len(pairs)
ro = {(i, j) for i, j in pairs if same(ours, i, j)}; rh = {(i, j) for i, j in pairs if same(his, i, j)}
with open(sys.argv[2], 'w') as f:
    f.write("position\tours\this\tstatus\n")
    for r in rows: f.write("\t".join(r) + "\n")
print(f"K ours {len(set(ours))} his {len(set(his))}; positions agreeing under best 1-1 map: {70-dis}/70 = {(70-dis)/70:.3f}")
print(f"pairwise same/different agreement {pa:.4f}; repeat pairs ours {len(ro)} his {len(rh)} shared {len(ro & rh)}")
print("DIFF rows:"); [print("  " + "\t".join(r)) for r in rows if r[3] == 'DIFF']
