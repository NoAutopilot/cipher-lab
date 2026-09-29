#!/usr/bin/env python3
"""H33 (29 Sept 2026): which ids open lines beyond chance? For every id with >= 3 settled tokens (punctuation dropped,
56 lines), line-initial count against 10,000 within-line shuffles (exact per-line probability k/n, simulated as
independent Bernoulli per line), one-sided p; Benjamini-Hochberg at q 0.10 over all ids tested; the same for
line-final. Ids that clear form the candidate 'initial' class; each is tagged with h3's shape class. Writes
h33_initial_class.json."""
import os, json, random, collections, sys
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
sys.path.insert(0, here); from settled_lines import settled_lines
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
def shape(s):
    if s.startswith('PICT-') or s in ('SUN', 'STAR', 'HEART', 'RAM'): return 'pictogram'
    if s.endswith('-LETTER') or s in ('PHI', 'OMEGA', 'LAMBDA', 'DELTA', 'SIGMA', 'PI', 'X'): return 'letter'
    return 'other'
lines = [l for l in ([s for s in v if s not in PUNCT] for v in settled_lines(root, 'c').values()) if len(l) >= 2]
cnt = collections.Counter(s for l in lines for s in l); rng = random.Random(33); T = 10000
def test(pos):
    res = []
    for s, c in cnt.items():
        if c < 3: continue
        ps = [l.count(s) / len(l) for l in lines if s in l]
        obs = sum((l[0] if pos == 0 else l[-1]) == s for l in lines)
        null = [sum(rng.random() < p for p in ps) for _ in range(T)]
        res.append(dict(id=s, n=c, obs=obs, exp=round(sum(ps), 2), p=(sum(x >= obs for x in null) + 1) / (T + 1), shape=shape(s)))
    res.sort(key=lambda r: r['p']); m = len(res)
    k = max([i + 1 for i, r in enumerate(res) if r['p'] <= 0.10 * (i + 1) / m] or [0])
    for i, r in enumerate(res): r['bh_pass'] = i < k
    return res
out = dict(initial=test(0), final=test(-1))
for pos in ('initial', 'final'):
    print(pos, 'ids tested', len(out[pos]), 'BH pass', [(r['id'], r['obs'], r['exp'], round(r['p'], 4)) for r in out[pos] if r['bh_pass']])
    print('  top 8', [(r['id'], r['obs'], r['exp'], round(r['p'], 4), r['shape']) for r in out[pos][:8]])
json.dump(out, open(os.path.join(root, 'h33_initial_class.json'), 'w'), indent=1)
