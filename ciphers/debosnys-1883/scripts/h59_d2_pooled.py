#!/usr/bin/env python3
"""H59 (29 Sept 2026): R2-5's D2 split lead replicated on the pooled c1-c4 text with power, per h59/PREREG.md
(pushed 11f9ba94 before any score). Usage: h59_d2_pooled.py control|nulls MAP N|real|all. Outputs in h59/."""
import os, sys, json, random, collections, statistics as st
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
R25 = os.path.join(root, 'swarm/R2/R2-5'); sys.path.insert(0, R25); sys.path.insert(0, os.path.join(root, 'swarm/G-D')); sys.path.insert(0, here)
_argv = sys.argv; sys.argv = [sys.argv[0]]
import r25, dcore, boxnull
sys.argv = _argv
from settled_lines import settled_lines
MARKS = {'BLOB', 'BAR-SOLID', 'HOOK-L', 'DASH-V', '_', 'MULTI', 'MARK'}; FOLDS = {'PCT-SLASH': 'PCT', 'X-DOT': 'X', 'X-CURL': 'X'}
NOISE = {'c1': 0.16, 'c2': 0.155, 'c3': 0.09, 'c4': 0.09}; PAGES = ('c1', 'c2', 'c3', 'c4')
raw = settled_lines(root, 'c', drop_clear=True)
pg = lambda k: {'c2a': 'c2', 'c2b': 'c2', 'c4a0': 'c4', 'c4a': 'c4', 'c4b': 'c4'}.get(k.split('_')[0], k.split('_')[0])
TEXT = {p: [] for p in PAGES}
for k, v in raw.items():
    l = [FOLDS.get(s, s) for s in v if s not in MARKS]
    if l: TEXT[pg(k)].append(l)
LENS = {p: [len(l) for l in TEXT[p]] for p in PAGES}
IDS = collections.Counter(s for p in PAGES for l in TEXT[p] for s in l)
def score(texts, M, rng, trials):
    tot = 0.0; parts = {}
    for p in PAGES:
        a, _ = boxnull.zscore(texts[p], M, rng, trials); parts[p] = round(a, 3); tot += a
    return round(tot, 3), parts
def draw_iid(rng, habit=False):
    names = list(IDS); w = [IDS[n] for n in names]; out = {}
    fav = {s: rng.choices(names, w, k=2) for s in names} if habit else None
    for p in PAGES:
        n = sum(LENS[p]); k = int(n * 1.12) + 3; seq = [rng.choices(names, w)[0]]
        while len(seq) < k:
            seq.append(rng.choice(fav[seq[-1]]) if habit and rng.random() < 0.25 else rng.choices(names, w)[0])
        out[p] = dcore.cut(r25.r21.mixnoise(seq, NOISE[p], rng, n), LENS[p])
    return out
def planted_texts(rng):
    L1 = [x for p in ('c1', 'c3') for x in LENS[p]]; L2 = [x for p in ('c2', 'c4') for x in LENS[p]]
    boxes, M = r25.planted(rng, L1, L2, 0.24); out = {}; off = 0
    for p in PAGES:
        n = sum(LENS[p]); k = int(n * 1.12) + 3; seg = boxes[off:off + k]; off += k
        if len(seg) < k: seg = (seg + boxes)[:k]
        out[p] = dcore.cut(r25.r21.mixnoise(seg, NOISE[p], rng, n), LENS[p])
    return out, M
if __name__ == '__main__':
    mode = sys.argv[1]; os.makedirs(os.path.join(root, 'h59'), exist_ok=True)
    if mode == 'nulls':
        m, kind, n, seed = sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5]); M = r25.REAL_MAPS[m]; rows = []
        for i in range(n):
            rng = random.Random(f'h59-{m}-{kind}-{seed}-{i}'); rows.append(score(draw_iid(rng, kind == 'habit'), M, rng, 100)[0])
        json.dump(rows, open(os.path.join(root, 'h59', f'null_{m}_{kind}_{seed}.json'), 'w'))
    elif mode == 'control':
        n, seed = int(sys.argv[2]), int(sys.argv[3]); rows = []
        for i in range(n):
            rng = random.Random(f'h59-planted-{seed}-{i}'); t, M = planted_texts(rng); rows.append(score(t, M, rng, 100)[0])
        json.dump(rows, open(os.path.join(root, 'h59', f'planted_{seed}.json'), 'w'))
    elif mode == 'real':
        out = {}
        for m in ('real-T', 'real-N'):
            v = [score(TEXT, r25.REAL_MAPS[m], random.Random(3000 + i), 400) for i in range(5)]
            out[m] = dict(median=st.median(x[0] for x in v), seeds=[x[0] for x in v], parts=v[0][1])
        json.dump(out, open(os.path.join(root, 'h59', 'real.json'), 'w'), indent=1); print(out)
