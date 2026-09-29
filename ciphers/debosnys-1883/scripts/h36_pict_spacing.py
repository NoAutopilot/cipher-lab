#!/usr/bin/env python3
"""H36 (29 Sept 2026): spacing of pictograms in the running text. Pages (c1, c2, c3, c4) as continuous sign streams
(settled lines in order, punctuation-class boxes and clear_spans.tsv positions dropped); gaps between consecutive
pictograms within a page (in signs). Statistics: variance-to-mean ratio of the gaps (clumped > random > regular),
share of gaps under 3, and the minimum gap. Null: 10,000 random re-placements of each page's pictogram count over its
positions. Power: a planted stream with one pictogram opening each phrase of 15-25 signs (uniform) at the same total
count, scored against the same null. Writes h36_pict_spacing.json."""
import os, json, random, collections, sys
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
sys.path.insert(0, here); from settled_lines import settled_lines
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
def is_pict(s): return s.startswith('PICT-') or s in ('SUN', 'STAR', 'HEART', 'RAM')
raw = settled_lines(root, 'c', drop_clear=True); pages = collections.OrderedDict()
for k, v in raw.items():
    pg = {'c2a': 'c2', 'c2b': 'c2', 'c4a0': 'c4', 'c4a': 'c4', 'c4b': 'c4'}.get(k.split('_')[0], k.split('_')[0])
    pages.setdefault(pg, []).extend(s for s in v if s not in PUNCT)
def stats(pos_by_page):
    gaps = []
    for pos in pos_by_page:
        pos = sorted(pos); gaps += [b - a for a, b in zip(pos, pos[1:])]
    m = sum(gaps) / len(gaps); var = sum((g - m) ** 2 for g in gaps) / len(gaps)
    return dict(vmr=var / m, short=sum(g < 3 for g in gaps) / len(gaps), n_gaps=len(gaps), mean=m)
obs_pos = [[i for i, s in enumerate(p) if is_pict(s)] for p in pages.values()]
obs = stats(obs_pos); rng = random.Random(36); null = []
for _ in range(10000):
    null.append(stats([rng.sample(range(len(p)), len(op)) for p, op in zip(pages.values(), obs_pos)]))
def band(k, val):
    v = sorted(x[k] for x in null); return dict(obs=round(val, 3), lo=round(v[250], 3), hi=round(v[9749], 3), p_le=sum(x <= val for x in v) / 10000, p_ge=sum(x >= val for x in v) / 10000)
res = dict(pages={k: dict(N=len(p), pict=len(op)) for (k, p), op in zip(pages.items(), obs_pos)}, vmr=band('vmr', obs['vmr']), short=band('short', obs['short']), mean_gap=round(obs['mean'], 1))
plant = []
for p, op in zip(pages.values(), obs_pos):
    pos = []; i = rng.randint(0, 10)
    while i < len(p) and len(pos) < len(op): pos.append(i); i += rng.randint(15, 25)
    plant.append(pos)
ps = stats(plant); res['planted'] = dict(vmr=round(ps['vmr'], 3), short=round(ps['short'], 3), vmr_below_lo=ps['vmr'] < res['vmr']['lo'])
print(res); json.dump(res, open(os.path.join(root, 'h36_pict_spacing.json'), 'w'), indent=1)
