#!/usr/bin/env python3
"""SUR-0745R (9 Oct 2026): pooled SPLIT with 0745 R added, PREREG-SUR-0745R.md (amendment of PREREG-SUR-POOLPC.md) pushed before any draw.
Loads ../inv373_pool_poolpc/poolpc.py's source (everything before `if __name__`) unchanged except the UNITS list, which gains
'inv373_0745R_blind' (0744 L + 0744 R + 0745 L + 0745 R). Statistic, scaffold, K=300 per synthetic unit, verdict rule, matrix speed-up:
poolpc.py's own functions. Power arm: SUR-PARTIAL's planted partial split (each gloss m drawn as [y-fam] written 'Mx' with prob. f),
f = 0 (H0), 0.50, 0.75, 1.00; NU units per level per pass scaffold at the pooled line count; master seed 20261011.
--real: the real pooled SPLIT, 10,000 deranged-gloss draws, seed 20261010 (poolpc --real's seed), unit verdict needs both passes.
Usage: python3 pool4.py [--selftest | --real] [--check]   writes pool4.out / pool4_real.out; --check exits 1 if stale."""
import os, sys, random
from collections import Counter
from multiprocessing import Pool
H = os.path.dirname(os.path.abspath(__file__)); PP = os.path.join(H, '..', 'inv373_pool_poolpc', 'poolpc.py')
src = open(PP, encoding='utf-8').read().split("\nif __name__ == '__main__':")[0]
OLD = "UNITS = ['inv373_0744_blind_sb', 'inv373_0744R_blind', 'inv373_0745L_blind']"
assert src.count(OLD) == 1; src = src.replace(OLD, OLD[:-1] + ", 'inv373_0745R_blind']")
PC = {'__file__': PP, '__name__': 'pool4'}; exec(src, PC)
T, YF, SC, NP, K, POOL, ctrl, head = PC['T'], PC['YF'], PC['SC'], PC['NP'], PC['K'], PC['POOL'], PC['ctrl'], PC['head']
LEVELS = [0.0, 0.50, 0.75, 1.00]; NU = 60; SEEDP = 20261011; KREAL = 10000; SEEDR = 20261010
def synth(sc, f, rnd, nl):
    G, face, unal, pdel, pins = sc; L, Lab, GG = [], [], []
    for _ in range(nl):
        g = G[rnd.randrange(len(G))]; cs = []
        for x in g:
            if rnd.random() >= pdel:
                fa = face.get(x)
                c = rnd.choices(list(fa), weights=list(fa.values()))[0] if fa else rnd.choice([k for k, v in T.items() if x in v] or ['?'])
                if x == 'm' and c == YF and rnd.random() < f: c = 'Mx'
                cs.append(c)
            if rnd.random() < pins: cs.append(rnd.choice(unal))
        L.append(cs); Lab.append(['U' if c == YF else None for c in cs]); GG.append(list(g))
    return L, Lab, GG
def one(a):
    p, f, sd = a; rnd = random.Random(sd); L, Lab, G = synth(SC[p], f, rnd, NP)
    m0, n0, S0, lo, hi, v, _ = ctrl(L, Lab, G, K, rnd); return p, f, m0, n0, S0, hi, v
if __name__ == '__main__':
    if '--selftest' in sys.argv: print('\n'.join(head())); sys.exit(0)
    if '--real' in sys.argv:
        out = head() + [f'# REAL pooled SPLIT (4 units), C1 {KREAL} deranged-gloss draws, seed {SEEDR}']; V = {}
        for p in 'AB':
            L, Lab, G, _ = POOL[p]; m0, n0, S0, lo, hi, v, cP = ctrl(L, Lab, G, KREAL, random.Random(SEEDR))
            out.append(f'  pass {p}: lines {len(L)}; y on m {m0}, n {n0}; S {S0:.3f}; C1 mean {sum(cP)/len(cP):.3f} p0.5 {lo:.3f} p99.5 {hi:.3f} -> {v}'); V[p] = v
        out.append(f'UNIT pooled SPLIT (4 units): {V["A"] if V["A"] == V["B"] else "not shown (passes disagree)"}'); fo = os.path.join(H, 'pool4_real.out')
    else:
        master = random.Random(SEEDP); jobs = [(p, f, master.getrandbits(48)) for f in LEVELS for p in 'AB' for _ in range(NU)]
        with Pool(4) as pool: res = pool.map(one, jobs, chunksize=2)
        out = head() + [f'# SUR-0745R power curve: pooled lines {NP}, K={K} C1 per unit, {NU} units per level per pass, master seed {SEEDP}']; det = {}
        for f in LEVELS:
            for p in 'AB':
                r = [x for x in res if x[0] == p and x[1] == f]; n = len(r); c = Counter(x[6] for x in r); det[f, p] = c['LEANS n'] / n
                out.append(f'  f {f:.2f} {p}: units {n}; y on m mean {sum(x[2] for x in r)/n:.1f}, on n mean {sum(x[3] for x in r)/n:.1f}; '
                           f'S mean {sum(x[4] for x in r if x[4] == x[4])/n:.3f}; p99.5 mean {sum(x[5] for x in r)/n:.3f}; verdicts {dict(c)}; LEANS n {det[f, p]:.3f}')
        for f in LEVELS: out.append(f'DETECTION f {f:.2f}: A {det[f, "A"]:.3f} B {det[f, "B"]:.3f}' + (' (false LEANS n, gate <= 0.05)' if f == 0 else ' -> power >= 0.80 both' if min(det[f, 'A'], det[f, 'B']) >= 0.8 else ''))
        ok = [f for f in LEVELS[1:] if min(det[f, 'A'], det[f, 'B']) >= 0.8]
        out.append(f'GATE (f = 1.00 power >= 0.80 both and H0 false LEANS n <= 0.05 both): {"PASS" if 1.0 in ok and max(det[0.0, "A"], det[0.0, "B"]) <= 0.05 else "FAIL"}; smallest tested f with power >= 0.80: {min(ok) if ok else "none"}')
        fo = os.path.join(H, 'pool4.out')
    txt = '\n'.join(out) + '\n'
    if '--check' in sys.argv: sys.exit(0 if os.path.exists(fo) and open(fo, encoding='utf-8').read() == txt else 1)
    open(fo, 'w', encoding='utf-8').write(txt); print(txt, end='')
