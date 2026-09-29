#!/usr/bin/env python3
"""DEB-SWARM-D test S (29 Sept 2026): does any frequent sign behave like a word space (the Copiale spacing-mark
shape)? For each of the six commonest signs of c2, the gaps (signs between two of its occurrences within a line):
share of zero gaps (doubling) and the gap dispersion (variance/mean). A space sign has almost no zero gaps and
under-dispersed gaps (word lengths have a mode); an iid sign gives geometric gaps. Null: 2,000 within-line shuffles.
Power: FR letters with the space written as its own sign (plus 15 pct type noise) at c2 shape. Writes xgap.json."""
import dcore, escape, random, json, collections, statistics as st
rng = random.Random(7373)
def gaps(lines, s):
    g = []
    for l in lines:
        idx = [i for i, x in enumerate(l) if x == s]; g += [b - a - 1 for a, b in zip(idx, idx[1:])]
    return g
def stat(lines, s):
    g = gaps(lines, s)
    if len(g) < 5: return None
    m = st.mean(g); return dict(zero=sum(x == 0 for x in g) / len(g), disp=st.pvariance(g) / m if m else 0, n=len(g))
def test(lines, s, trials=2000):
    o = stat(lines, s); sh = collections.defaultdict(list)
    if o is None: return None
    for _ in range(trials):
        q = [rng.sample(l, len(l)) for l in lines]; r = stat(q, s)
        if r is None: continue
        for k in ('zero', 'disp'): sh[k].append(r[k])
    return {k: dict(obs=round(o[k], 3), p_le=round(sum(x <= o[k] for x in sh[k]) / len(sh[k]), 4)) for k in ('zero', 'disp')} | {'n': o['n']}
res = {}
t2 = escape.t2; top = [s for s, _ in collections.Counter(x for l in t2 for x in l).most_common(6)]
for s in top: res[s] = test(t2, s) or 'under 5 gaps'; print('c2', s, res[s], flush=True)
pw = []
for _ in range(10):
    W = dcore.words('fr'); o = rng.randrange(len(W) - 3000); us = []
    for w in W[o:]:
        us += list(w) + [' ']
        if len(us) >= escape.N2: break
    seq = escape.homo_seq([u for u in us[:escape.N2] if u != ' '], escape.cv[1:], rng)  # letters on the rest of the curve
    it = iter(seq); full = ['SPACE' if u == ' ' else next(it) for u in us[:escape.N2]]
    lines = dcore.cut(dcore.noise(full, 0.15, rng), escape.L2); pw.append(test(lines, 'SPACE', 500))
res['power_space_sign'] = dict(zero_p_le_median=st.median(x['zero']['p_le'] for x in pw), disp_p_le_median=st.median(x['disp']['p_le'] for x in pw),
                               zero_obs_median=st.median(x['zero']['obs'] for x in pw), disp_obs_median=st.median(x['disp']['obs'] for x in pw))
print('power', res['power_space_sign'])
json.dump(res, open('xgap.json', 'w'), indent=1)
