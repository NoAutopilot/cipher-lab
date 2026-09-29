#!/usr/bin/env python3
"""Post hoc (NOT pre-registered; written after result.json was read, 29 Sept 2026): a genre-matched null for R2-3.
Permute c4's 10 couplets as units (line lengths and finals move together, internal order kept), rescore every
candidate-pool window, record the pool maximum S and each named window's S. If the pool maximum under shuffled
couplet order often reaches the real best (1.359), the real best is a property of couplet verse, not of this poem.
Usage: couplet_null.py --texts DIR [--n 200]. Writes couplet_null.json."""
import argparse, json, os, random, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crib_length import *
ap = argparse.ArgumentParser(); ap.add_argument('--texts', required=True); ap.add_argument('--n', type=int, default=200); a = ap.parse_args()
keys, lens, fin = c4_profile()
pool = {}
for p in sorted(glob.glob(os.path.join(a.texts, 'pool', '*.txt'))):
    vl = verse_lines(p); fr = is_fr(p); pool[os.path.basename(p)] = window_feats(vl, fr)
named = {'moore_8187_1647': ('pg8187.txt', 1647), 'hugo_76396_1011': ('pg76396.txt', 1011), 'hugo_29844_5413': ('pg29844.txt', 5413)}
def run(l, f):
    sc = {k: score_text(v, l, f) for k, v in pool.items()}
    return max(float(s[:, 0].max()) for s in sc.values()), {n: float(sc[t][i, 0]) for n, (t, i) in named.items()}, max(float(s[:, 1].max()) for s in sc.values())
real_max, real_named, real_maxR = run(lens, fin)
rng = random.Random(7); mx = []; nm = {n: [] for n in named}; mxR = []
for _ in range(a.n):
    order = list(range(10)); rng.shuffle(order)
    if order == list(range(10)): continue
    l = [lens[2 * c + j] for c in order for j in (0, 1)]; f = [fin[2 * c + j] for c in order for j in (0, 1)]
    m, d, mr = run(l, f); mx.append(m); mxR.append(mr)
    for n in named: nm[n].append(d[n])
res = dict(n=len(mx), real_pool_max_S=real_max, real_named_S=real_named,
           p_poolmax_ge_real=sum(x >= real_max for x in mx) / len(mx),
           null_poolmax_S_pctiles={q: float(np.percentile(mx, q)) for q in (50, 95, 99)},
           real_pool_max_R=real_maxR, p_poolmaxR_ge_real=sum(x >= real_maxR for x in mxR) / len(mxR),
           named_p={n: sum(x >= real_named[n] for x in nm[n]) / len(nm[n]) for n in named},
           named_null_max={n: max(nm[n]) for n in named})
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'couplet_null.json'), 'w'), indent=1)
print(json.dumps(res, indent=1))
