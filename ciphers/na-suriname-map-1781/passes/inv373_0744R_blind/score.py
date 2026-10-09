#!/usr/bin/env python3
"""SUR-0744R: score the two blind passes of NA 1.05.03 inv. 373 scan 0744 RIGHT page under PREREG-SUR0744R.md (pushed 94e16aee before
either pass was run or this script existed). R15-SURALIAS alias_run.py's functions (dp_idx, csigns, outside) and R14-SURDP dp_align.py
(table, ok, score, A, derange, rows, gletters) loaded unchanged; T = 0693+0702+0730 + [sh-lig]={h}.
(0) scan A vs C1 (10,000 deranged-gloss draws, seed 7440); (a) CLASS gate: reader [ij] m|n share vs the same C1 draws, p99, +2 token
steps; (b) DOT gate: dotted m|n share among aligned y-family tokens vs 10,000 dot-label permutations (seed 7441), p99; (c) descriptive
m vs n. Scan A is computed from dp_idx's pairs (a line-for-line copy of dp(); asserted equal to dp_align.A on the real gloss).
Writes score.out; `--check` exits 1 if score.out is stale."""
import os, re, sys, random
from math import comb
from multiprocessing import Pool
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, '..')
src = open(os.path.join(P, 'inv373_alias_r15', 'alias_run.py'), encoding='utf-8').read().split('\nout = []; allp = []')[0]
an = {'__file__': os.path.join(P, 'inv373_alias_r15', 'alias_run.py')}; exec(src, an)
dn = an['ns']; dn['SCAN'] = '0744'
TABS = ['inv373_0693_r10', 'inv373_0702_r13', 'inv373_0730_r13']; T = dn['table'](TABS); T['[sh-lig]'] = {'h'}
ok, csigns, outside, dp_idx = dn['ok'], an['csigns'], an['outside'], an['dp_idx']
N = 10000; MN = {'m', 'n'}
def toks(raw, crop):
    s = raw.replace('[ij]', '‹D›'); s = outside(s, lambda p: re.sub(r'(?<!\S)y(?!\S)', '‹U›', p))
    out, lab = [], []
    for p in re.split(r'(‹[DU]›)', s):
        if p in ('‹D›', '‹U›'):
            t = csigns('[ij]', crop); out += t; lab += [p[1]] * len(t)
        elif p:
            t = csigns(p, crop); out += t; lab += [None] * len(t)
    return out, lab
def load(p):
    d = os.path.join(H, p)
    blind = {f[0]: f[2] for f in dn['rows'](os.path.join(d, 'passA_sonnet_blind.tsv')) if len(f) > 2 and f[1] == 'cipher'}
    gloss = {f[0]: f[1] for f in dn['rows'](os.path.join(d, 'gloss_reconciled.tsv')) if f[0] != 'crop'}
    crops = [c for c in sorted(gloss) if c in blind]
    TL = [toks(blind[c], c) for c in crops]; G = [dn['gletters'](gloss[c]) for c in crops]
    keep = [i for i in range(len(crops)) if TL[i][0] and G[i]]
    return [TL[i][0] for i in keep], [TL[i][1] for i in keep], [G[i] for i in keep], blind
def stats(L, Lab, G):
    a = n = 0; st = {'D': [0, 0], 'U': [0, 0]}; recs = []; mn = {'m': 0, 'n': 0}
    for cs, lab, gs in zip(L, Lab, G):
        for i, x in dp_idx(cs, gs, T):
            if cs[i] in T: n += 1; a += ok(cs[i], x, T)
            if lab[i]:
                hit = ok(cs[i], x, T); st[lab[i]][0] += 1; st[lab[i]][1] += hit; recs.append((lab[i], hit))
                if x in mn: mn[x] += 1
    return (a / n if n else 0.0), n, st, recs, mn
CTX = {}
def c1_chunk(args):
    p, seeds = args; L, Lab, G = CTX[p]; res = []
    for sd in seeds:
        rnd = random.Random(sd); q = dn['derange'](rnd, len(G)); A_, _, st, _, _ = stats(L, Lab, [G[k] for k in q])
        res.append((A_, st['D'][1] / st['D'][0] if st['D'][0] else 0.0))
    return res
def fisher(a, b, c, d):
    n1, n2, k, n = a + b, c + d, a + c, a + b + c + d; pr = lambda x: comb(n1, x) * comb(n2, k - x) / comb(n, k)
    p0 = pr(a); return min(1.0, sum(pr(x) for x in range(max(0, k - n2), min(k, n1) + 1) if pr(x) <= p0 * (1 + 1e-9)))
out = []; V = {}
for p in ('A', 'B'):
    L, Lab, G, blind = load(p); CTX[p] = (L, Lab, G)
    A0, n0, st, recs, mn = stats(L, Lab, G)
    Aref, nref = dn['A'](L, G, T); assert abs(Aref - A0) < 1e-12 and nref == n0, (Aref, A0, nref, n0)
    nD = sum(r[2].count('[ij]') for r in [l.split('\t') for l in open(os.path.join(H, p, 'passA_sonnet_blind.tsv'), encoding='utf-8') if l[0] != '#'] if len(r) > 2 and r[1] == 'cipher')
    master = random.Random(7440); seeds = [master.getrandbits(48) for _ in range(N)]
    with Pool(4) as pool: c1 = [x for ch in pool.map(c1_chunk, [(p, seeds[i::4]) for i in range(4)]) for x in ch]
    cA = sorted(x[0] for x in c1); cS = sorted(x[1] for x in c1)
    same = A0 >= 0.50 and A0 > cA[9899]
    out.append(f'# pass {p}: reader [ij] {nD}; pairs {len(L)}, signs {sum(map(len, L))}; keyed aligned {n0}, A {A0:.3f}; C1 (N={N}, seed 7440) '
               f'mean {sum(cA)/N:.3f} p99 {cA[9899]:.3f} max {cA[-1]:.3f} -> {"SAME SYSTEM (DP)" if same else "not shown"}')
    nal, k = st['D']; sh = k / nal if nal else 0.0; p99 = cS[9899]
    ga = 'non-test (n_al < 10)' if nal < 10 else 'PASS' if (sh >= 0.60 and sh >= p99 + 2 / nal and same) else 'FAIL'
    out.append(f'  (a) CLASS [ij] -> m|n: n_al {nal}, agree {k}, share {sh:.3f}; C1 share mean {sum(cS)/N:.3f} p99 {p99:.3f}; '
               f'need >= {p99 + 2/nal if nal else 0:.3f} -> {ga}')
    nU, kU = st['U']
    out.append(f'      undotted y -> m|n (descriptive): n_al {nU}, agree {kU}, share {kU/nU if nU else 0:.3f}')
    flags = [h for _, h in recs]; nd = sum(1 for l, _ in recs if l == 'D')
    rnd = random.Random(7441); perm = []
    for _ in range(N):
        f2 = flags[:]; rnd.shuffle(f2); perm.append(sum(f2[:nd]) / nd if nd else 0.0)
    perm.sort(); pp99, pp95 = perm[9899], perm[9499]
    if nal < 10 or nU < 10 or len(set(flags)) < 2: gb = 'non-test'
    else: gb = 'PASS' if sh > pp99 else 'FAIL'
    out.append(f'  (b) DOT: dotted {k}/{nal} ({sh:.3f}) vs undotted {kU}/{nU} ({kU/nU if nU else 0:.3f}); dot-label permutation (N={N}, seed 7441) '
               f'mean {sum(perm)/N:.3f} p95 {pp95:.3f} p99 {pp99:.3f} -> {gb}; Fisher two-sided p {fisher(k, nal-k, kU, nU-kU):.3f}')
    out.append(f'  (c) descriptive: aligned y-family facing gloss m {mn["m"]}, n {mn["n"]}')
    V[p] = (ga, gb)
def unit(a, b):
    return 'PASS' if (a, b) == ('PASS', 'PASS') else 'FAIL' if (a, b) == ('FAIL', 'FAIL') else 'non-test' if a.startswith('non') and b.startswith('non') else 'not shown (passes disagree)'
out.append(f'UNIT CLASS (a): {unit(V["A"][0], V["B"][0])}  [A {V["A"][0]}; B {V["B"][0]}]')
out.append(f'UNIT DOT (b): {unit(V["A"][1], V["B"][1])}  [A {V["A"][1]}; B {V["B"][1]}]')
txt = '\n'.join(out) + '\n'; f = os.path.join(H, 'score.out')
if '--check' in sys.argv: sys.exit(0 if os.path.exists(f) and open(f, encoding='utf-8').read() == txt else 1)
open(f, 'w', encoding='utf-8').write(txt); print(txt, end='')
