#!/usr/bin/env python3
"""V-SUR0744R (verifier, 9 Oct 2026): re-run of SUR-0744R's (a) CLASS gate with fresh C1 master seeds, and one key-blind robustness
variant. Not a gate of its own; score.py and PREREG-SUR0744R.md are unchanged. Loads score.py's own functions (its scoring body is not
executed). Usage: python3 vsur0744r_seeds.py SEED [SEED ...] [--keyblind]
--keyblind: T without '[y-fam]' (the aligner earns nothing for putting a y-family sign on gloss m|n); the statistic is then the raw
share of aligned reader-[ij] tokens whose gloss letter is m or n, real vs the same C1 draws. Descriptive (not pre-registered)."""
import os, sys, random
from multiprocessing import Pool
H = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(H, 'score.py'), encoding='utf-8').read().split('\nout = []; V = {}')[0]
S = {'__file__': os.path.join(H, 'score.py'), '__name__': 'vsur'}; exec(src, S)
KB = '--keyblind' in sys.argv; seeds_m = [int(a) for a in sys.argv[1:] if not a.startswith('--')]
if KB: S['T'].pop('[y-fam]', None)
T, dp_idx, ok = S['T'], S['dp_idx'], S['ok']; N = 10000; MN = {'m', 'n'}
def st(L, Lab, G):
    a = n = 0; d = h = 0
    for cs, lab, gs in zip(L, Lab, G):
        for i, x in dp_idx(cs, gs, T):
            if cs[i] in T: n += 1; a += ok(cs[i], x, T)
            if lab[i] == 'D': d += 1; h += (x in MN) if KB else ok(cs[i], x, T)
    return (a / n if n else 0.0), d, h
CTX = {}
def chunk(args):
    p, sds = args; L, Lab, G = CTX[p]; r = []
    for sd in sds:
        q = S['dn']['derange'](random.Random(sd), len(G)); A_, d, h = st(L, Lab, [G[k] for k in q]); r.append((A_, h / d if d else 0.0))
    return r
for p in ('A', 'B'):
    L, Lab, G, _ = S['load'](p); CTX[p] = (L, Lab, G); A0, d0, h0 = st(L, Lab, G); sh = h0 / d0 if d0 else 0.0
    for m in seeds_m:
        mr = random.Random(m); sds = [mr.getrandbits(48) for _ in range(N)]
        with Pool(4) as pool: c = [x for ch in pool.map(chunk, [(p, sds[i::4]) for i in range(4)]) for x in ch]
        cA = sorted(x[0] for x in c); cS = sorted(x[1] for x in c); p99 = cS[9899]
        same = A0 >= 0.50 and A0 > cA[9899]
        g = 'non-test' if d0 < 10 else 'PASS' if (sh >= 0.60 and sh >= p99 + 2 / d0 and same) else 'FAIL'
        ge = sum(1 for x in cS if x >= sh)
        print(f'{"keyblind " if KB else ""}pass {p} seed {m}: A {A0:.3f} C1 p99 {cA[9899]:.3f}; [ij] n_al {d0} hit {h0} share {sh:.3f}; '
              f'C1 share mean {sum(cS)/N:.3f} p99 {p99:.3f} need {p99 + 2/d0:.3f}; draws >= share {ge}/{N} -> {g}', flush=True)
