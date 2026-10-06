#!/usr/bin/env python3
"""FER126-ALIGN2 candidates and decoys (PREREG-ALIGN2.md): agreed numerals of LANE-PRIV1's two passes -> Fig. 4 syllables
(unbracketed only); decoys = another line's list, not same/adjacent, closest length. python3 align2_candidates.py KEY.tsv OUT.tsv"""
import difflib, os, sys, collections
key = {}
for l in open(sys.argv[1]).read().split('\n')[1:]:
    if l:
        c, v, g = l.split('\t')[:3]
        if g == 'H':
            key[c] = v
here = os.path.dirname(os.path.abspath(__file__))
rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(here, 'item126_passes.tsv')) if not l.startswith('#')][1:]
C = collections.defaultdict(lambda: collections.defaultdict(list))
for p, ln, seg, kind, txt in rows:
    if kind == 'C' and ln != 'V12':
        C[ln][p].append((seg, txt.split()))
def numerals(segs):
    out = []
    for i, (seg, t) in enumerate(sorted(segs)):
        t = [x for x in t if x.isdigit()]
        if out and i:   # drop the s1/s2 overlap: longest suffix/prefix match
            k = max([k for k in range(0, min(6, len(out), len(t)) + 1) if out[len(out) - k:] == t[:k]] or [0])
            t = t[k:]
        out += t
    return out
cand = {}
for ln in sorted(C):
    a, b = numerals(C[ln]['A']), numerals(C[ln]['B'])
    agreed = []
    for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
        agreed += a[blk.a:blk.a + blk.size]
    cand[ln] = [key[t] for t in agreed if t in key]
order = sorted(cand)
tested = [ln for ln in order if len(cand[ln]) >= 3]
decoy = {}
for ln in tested:
    i = order.index(ln)
    pool = [m for m in tested if abs(order.index(m) - i) > 1]
    decoy[ln] = min(pool, key=lambda m: (abs(len(cand[m]) - len(cand[ln])), m))
with open(sys.argv[2], 'w') as f:
    f.write('line\tn\tcandidate\tdecoy_from\tdecoy\n')
    for ln in tested:
        f.write(f'{ln}\t{len(cand[ln])}\t{" ".join(cand[ln])}\t{decoy[ln]}\t{" ".join(cand[decoy[ln]])}\n')
print(f'lines {len(order)}, tested (>=3 syllables) {len(tested)}, dropped {len(order) - len(tested)}; syllables {sum(len(cand[l]) for l in tested)}')
