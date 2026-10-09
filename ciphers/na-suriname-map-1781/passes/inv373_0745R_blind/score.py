#!/usr/bin/env python3
"""SUR-0745R (9 Oct 2026): score.py of SUR-0745 (0745 LEFT) copied unchanged in logic for scan 0745 RIGHT page, under PREREG-SUR-0745R.md (pushed before either pass ran).
Same machinery as SUR-0744R score.py: R15-SURALIAS alias_run.py (dp_idx, csigns, outside) and R14-SURDP dp_align.py loaded unchanged;
T = 0693+0702+0730 + [sh-lig]={h}; [ij], y, ÿ all map to [y-fam]={m,n} in dp, so the alignment ignores dot labels.
(0) scan A vs C1 (10,000 deranged-gloss draws, seed 7450); (a) CLASS gate, dot dropped: pooled y-family ([ij]+y) m|n share vs the same
C1 draws, p99, +2 token steps; [ij]-only share descriptive; (b) SPLIT gate: S = n/(m+n) among pooled y-family tokens aligned to gloss m|n,
two-sided against the same C1 draws (p0.5 / p99.5); (c) descriptive: per gloss letter m / n, which cipher codes face it.
`--calib DIR` runs (0)-(b) on another unit's A/ B/ (calibration of the control's spread; writes nothing). Writes score.out; `--check`
exits 1 if score.out is stale."""
import os, re, sys, random
from collections import Counter
from multiprocessing import Pool
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, '..')
src = open(os.path.join(P, 'inv373_alias_r15', 'alias_run.py'), encoding='utf-8').read().split('\nout = []; allp = []')[0]
an = {'__file__': os.path.join(P, 'inv373_alias_r15', 'alias_run.py')}; exec(src, an)
dn = an['ns']; dn['SCAN'] = '0745'
TABS = ['inv373_0693_r10', 'inv373_0702_r13', 'inv373_0730_r13']; T = dn['table'](TABS); T['[sh-lig]'] = {'h'}
ok, csigns, outside, dp_idx = dn['ok'], an['csigns'], an['outside'], an['dp_idx']
N = 10000; MN = {'m', 'n'}; SEED = 7450
CAL = sys.argv[sys.argv.index('--calib') + 1] if '--calib' in sys.argv else None
U = CAL or H
def toks(raw, crop):
    s = raw.replace('[ij]', '‹D›'); s = outside(s, lambda p: re.sub(r'(?<!\S)[yÿ](?!\S)', '‹U›', p))
    out, lab = [], []
    for p in re.split(r'(‹[DU]›)', s):
        if p in ('‹D›', '‹U›'):
            t = csigns('[ij]', crop); out += t; lab += [p[1]] * len(t)
        elif p:
            t = csigns(p, crop); out += t; lab += [None] * len(t)
    return out, lab
def load(p):
    d = os.path.join(U, p)
    blind = {f[0]: f[2] for f in dn['rows'](os.path.join(d, 'passA_sonnet_blind.tsv')) if len(f) > 2 and f[1] == 'cipher'}
    gloss = {f[0]: f[1] for f in dn['rows'](os.path.join(d, 'gloss_reconciled.tsv')) if f[0] != 'crop'}
    crops = [c for c in sorted(gloss) if c in blind]
    TL = [toks(blind[c], c) for c in crops]; G = [dn['gletters'](gloss[c]) for c in crops]
    keep = [i for i in range(len(crops)) if TL[i][0] and G[i]]
    return [TL[i][0] for i in keep], [TL[i][1] for i in keep], [G[i] for i in keep]
def stats(L, Lab, G, cov=False):
    a = n = 0; st = {'D': [0, 0], 'Y': [0, 0]}; mn = {'m': 0, 'n': 0}; face = {'m': Counter(), 'n': Counter()}
    for cs, lab, gs in zip(L, Lab, G):
        for i, x in dp_idx(cs, gs, T):
            if cs[i] in T: n += 1; a += ok(cs[i], x, T)
            if cov and x in MN: face[x]['[y-fam]' if lab[i] else cs[i]] += 1
            if lab[i]:
                hit = ok(cs[i], x, T); st['Y'][0] += 1; st['Y'][1] += hit
                if lab[i] == 'D': st['D'][0] += 1; st['D'][1] += hit
                if x in mn: mn[x] += 1
    return (a / n if n else 0.0), n, st, mn, face
def frac(st): return st[1] / st[0] if st[0] else 0.0
def split(mn): t = mn['m'] + mn['n']; return mn['n'] / t if t else float('nan')
CTX = {}
def c1_chunk(args):
    p, seeds = args; L, Lab, G = CTX[p]; res = []
    for sd in seeds:
        rnd = random.Random(sd); q = dn['derange'](rnd, len(G)); A_, _, st, mn, _ = stats(L, Lab, [G[k] for k in q])
        res.append((A_, frac(st['Y']), split(mn), mn['m'] + mn['n']))
    return res
out = []; V = {}
for p in ('A', 'B'):
    L, Lab, G = load(p); CTX[p] = (L, Lab, G)
    A0, n0, st, mn, face = stats(L, Lab, G, cov=True)
    Aref, nref = dn['A'](L, G, T); assert abs(Aref - A0) < 1e-12 and nref == n0
    master = random.Random(SEED); seeds = [master.getrandbits(48) for _ in range(N)]
    with Pool(4) as pool: c1 = [x for ch in pool.map(c1_chunk, [(p, seeds[i::4]) for i in range(4)]) for x in ch]
    cA = sorted(x[0] for x in c1); cS = sorted(x[1] for x in c1); cP = sorted(x[2] for x in c1 if x[3] > 0)
    same = A0 >= 0.50 and A0 > cA[9899]
    out.append(f'# pass {p}: pairs {len(L)}, signs {sum(map(len, L))}; keyed aligned {n0}, A {A0:.3f}; C1 (N={N}, seed {SEED}) '
               f'mean {sum(cA)/N:.3f} p99 {cA[9899]:.3f} max {cA[-1]:.3f} -> {"SAME SYSTEM (DP)" if same else "not shown"}')
    nal, k = st['Y']; sh = frac(st['Y']); p99 = cS[9899]
    ga = 'non-test (n_al < 10)' if nal < 10 else 'PASS' if (sh >= 0.60 and sh >= p99 + 2 / nal and same) else 'FAIL'
    out.append(f'  (a) CLASS pooled y-family -> m|n: n_al {nal}, agree {k}, share {sh:.3f}; C1 share mean {sum(cS)/N:.3f} p99 {p99:.3f}; '
               f'need >= {p99 + 2/nal if nal else 0:.3f} -> {ga}')
    out.append(f'      [ij]-only (descriptive): n_al {st["D"][0]}, agree {st["D"][1]}, share {frac(st["D"]):.3f}')
    t = mn['m'] + mn['n']; S = split(mn); M = len(cP)
    lo, hi = (cP[int(0.005 * M)], cP[int(0.995 * M) - 1]) if M else (float('nan'),) * 2
    mean = sum(cP) / M if M else float('nan'); sd = (sum((x - mean) ** 2 for x in cP) / M) ** 0.5 if M else 0.0
    if t < 10 or M < N // 2 or lo == hi: gb = 'non-test'
    else: gb = 'LEANS n' if S > hi else 'LEANS m' if S < lo else 'NO SPLIT SHOWN'
    out.append(f'  (b) SPLIT: y-family on gloss m {mn["m"]}, n {mn["n"]}; S = n/(m+n) {S:.3f}; C1 (draws with m+n>0: {M}) mean {mean:.3f} '
               f'sd {sd:.3f} p0.5 {lo:.3f} p99.5 {hi:.3f}; distinct values {len(set(cP))} -> {gb}')
    for x in ('m', 'n'):
        tot = sum(face[x].values())
        out.append(f'  (c) gloss {x} aligned {tot}: ' + ', '.join(f'{c} {v}' for c, v in face[x].most_common(8)))
    V[p] = (ga, gb)
def unit(a, b):
    if a == b: return a
    return 'not shown (passes disagree)'
out.append(f'UNIT CLASS (a): {unit(V["A"][0], V["B"][0])}  [A {V["A"][0]}; B {V["B"][0]}]')
out.append(f'UNIT SPLIT (b): {unit(V["A"][1], V["B"][1])}  [A {V["A"][1]}; B {V["B"][1]}]')
txt = '\n'.join(out) + '\n'
if CAL: print(f'# CALIBRATION on {os.path.relpath(CAL, P)} (not the target)\n' + txt, end=''); sys.exit(0)
f = os.path.join(H, 'score.out')
if '--check' in sys.argv: sys.exit(0 if os.path.exists(f) and open(f, encoding='utf-8').read() == txt else 1)
open(f, 'w', encoding='utf-8').write(txt); print(txt, end='')
