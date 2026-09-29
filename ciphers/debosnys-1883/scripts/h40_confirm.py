#!/usr/bin/env python3
"""H40 (29 Sept 2026): confirm the H39 fits (X removed) with fresh seeds. Every H39 condition at 7 of 9 or better is
re-run with 200 samples on a new seed, at invented-type share f 0.5 (as H39) and f 1.0 (the hapax miss), pooled; and
the pooled-best conditions on c2 alone and c4 alone (X removed, their own N and K, same nine statistics). A condition
counts as confirmed at 9/9 only on the fresh seed. Writes h40_confirm.json; --drop-clear (H43) leaves out the
clear_spans.tsv positions and writes h43_confirm_noclear.json."""
import os, json, sys, collections
CLEAR = '--drop-clear' in sys.argv
sys.argv = [sys.argv[0], '--drop-x'] + (['--drop-clear'] if CLEAR else [])
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here); sys.path.insert(0, here)
import h38_homophonic_fit as h38
from settled_lines import settled_lines
prev = json.load(open(os.path.join(root, 'h39_homophonic_noX.json')))['conditions']
conds = [k for k, v in prev.items() if v['inside'] >= 7]
def parse(k):
    q, h, c, z, p = k.split(':'); return float(q[1:]), int(h[1:]), int(c[1:]), z == 'zipf', float(p[1:])
out = dict(pooled={}, per_page={}); PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
for f in (0.5, 1.0):
    h38.F = f
    for i, k in enumerate(conds):
        K0, band = h38.run(*parse(k), 200, 40000 + 100 * i + int(f * 10)); ins = sum(b['inside'] for b in band.values())
        out['pooled'][f'{k}:f{f}'] = dict(K0=K0, inside=ins, band=band)
        print('pooled', k, 'f', f, 'K0', K0, f'{ins}/9', ' '.join(f"{s}={b['side']}" for s, b in band.items()), flush=True)
# per page: swap the module's target
raw = settled_lines(root, 'c', drop_clear=CLEAR); best = sorted(out['pooled'], key=lambda k: -out['pooled'][k]['inside'])[:3]
for pg in ('c2', 'c4'):
    ks = [k for k in raw if k.startswith(pg)]
    s7 = [s for k in ks for s in raw[k] if s not in ('_', 'MULTI', 'X')]; sR = [s for k in ks for s in raw[k] if s not in PUNCT and s != 'X']
    T = dict(h38.h3.stats(s7)); T.update(h38.repeats(sR)); h38.T = T; h38.N = len(s7); h38.KT = T['K']
    for k in best:
        h38.F = float(k.split(':f')[1]); K0, band = h38.run(*parse(k.split(':f')[0]), 200, 50000 + len(out['per_page']))
        ins = sum(b['inside'] for b in band.values()); out['per_page'][f'{pg}:{k}'] = dict(N=len(s7), K0=K0, inside=ins, band=band)
        print(pg, 'N', len(s7), k, 'K0', K0, f'{ins}/9', ' '.join(f"{s}={b['side']}" for s, b in band.items()), flush=True)
json.dump(out, open(os.path.join(root, 'h43_confirm_noclear.json' if CLEAR else 'h40_confirm.json'), 'w'), indent=1)
