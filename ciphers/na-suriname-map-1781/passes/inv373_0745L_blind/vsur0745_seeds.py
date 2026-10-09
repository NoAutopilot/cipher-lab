#!/usr/bin/env python3
"""V-SUR0745 (verifier, 9 Oct 2026): re-run of SUR-0745's (a) CLASS and (b) SPLIT gates with fresh C1 master seeds, plus two descriptive
variants (not pre-registered, not gates). score.py and PREREG-SUR-0745.md are unchanged; score.py's functions are loaded, its scoring
body is not executed. Usage: python3 vsur0745_seeds.py SEED [SEED ...] [--keyblind | --posctl CODE]
--keyblind: T without '[y-fam]' (the aligner earns nothing for putting a y-family sign on gloss m or n); CLASS statistic = raw share of
  aligned y-family tokens whose gloss letter is m|n; SPLIT S = n/(m+n) over those, so the m-vs-n placement is not steered by T.
--posctl CODE: power check for the SPLIT statistic on a sign whose T value is n only ('h'): CODE is removed from T and its tokens are
  tagged instead of the y-family; S = n/(m+n) against the same C1 draws. Shows whether an n-only sign reads LEANS n unsteered."""
import os, sys, random
from multiprocessing import Pool
H = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(H, 'score.py'), encoding='utf-8').read().split('\nout = []; V = {}')[0]
S = {'__file__': os.path.join(H, 'score.py'), '__name__': 'vsur'}; exec(src, S)
KB = '--keyblind' in sys.argv; PC = sys.argv[sys.argv.index('--posctl') + 1] if '--posctl' in sys.argv else None
seeds_m = [int(a) for a in sys.argv[1:] if a.isdigit()]
if KB: S['T'].pop('[y-fam]', None)
if PC: S['T'].pop(PC, None)
T, dp_idx, ok = S['T'], S['dp_idx'], S['ok']; N = 10000; MN = {'m', 'n'}
def tag(c, l): return (c == PC) if PC else bool(l)
def st(L, Lab, G):
    a = n = 0; d = h = 0; mn = {'m': 0, 'n': 0}
    for cs, lab, gs in zip(L, Lab, G):
        for i, x in dp_idx(cs, gs, T):
            if cs[i] in T: n += 1; a += ok(cs[i], x, T)
            if tag(cs[i], lab[i]):
                d += 1; h += (x in MN) if (KB or PC) else ok(cs[i], x, T)
                if x in MN: mn[x] += 1
    t = mn['m'] + mn['n']
    return (a / n if n else 0.0), d, h, mn, (mn['n'] / t if t else None)
CTX = {}
def chunk(args):
    p, sds = args; L, Lab, G = CTX[p]; r = []
    for sd in sds:
        q = S['dn']['derange'](random.Random(sd), len(G)); A_, d, h, _, s = st(L, Lab, [G[k] for k in q]); r.append((A_, h / d if d else 0.0, s))
    return r
tagname = f'{PC} (posctl)' if PC else 'y-family'
for p in ('A', 'B'):
    L, Lab, G = S['load'](p); CTX[p] = (L, Lab, G); A0, d0, h0, mn0, S0 = st(L, Lab, G); sh = h0 / d0 if d0 else 0.0
    for m in seeds_m:
        mr = random.Random(m); sds = [mr.getrandbits(48) for _ in range(N)]
        with Pool(4) as pool: c = [x for ch in pool.map(chunk, [(p, sds[i::4]) for i in range(4)]) for x in ch]
        cA = sorted(x[0] for x in c); cS = sorted(x[1] for x in c); p99 = cS[9899]; cP = sorted(x[2] for x in c if x[2] is not None)
        same = A0 >= 0.50 and A0 > cA[9899]
        g = 'non-test' if d0 < 10 else 'PASS' if (sh >= 0.60 and sh >= p99 + 2 / d0 and same) else 'FAIL'
        ge = sum(1 for x in cS if x >= sh); M = len(cP); t0 = mn0['m'] + mn0['n']
        lo, hi = cP[int(0.005 * M)], cP[int(0.995 * M) - 1]; mean = sum(cP) / M
        gb = 'non-test' if (t0 < 10 or M < N // 2 or lo == hi) else 'LEANS n' if S0 > hi else 'LEANS m' if S0 < lo else 'NO SPLIT SHOWN'
        print(f'{"keyblind " if KB else ""}pass {p} seed {m}: A {A0:.3f} C1 p99 {cA[9899]:.3f}; {tagname} n_al {d0} m|n {h0} share {sh:.3f}; '
              f'C1 share mean {sum(cS)/N:.3f} p99 {p99:.3f} need {p99 + 2/d0 if d0 else 0:.3f}; draws >= share {ge}/{N} -> CLASS {g} | '
              f'SPLIT m {mn0["m"]} n {mn0["n"]} S {S0 if S0 is None else round(S0, 3)}; C1 ({M}) mean {mean:.3f} p0.5 {lo:.3f} p99.5 {hi:.3f} -> {gb}', flush=True)
