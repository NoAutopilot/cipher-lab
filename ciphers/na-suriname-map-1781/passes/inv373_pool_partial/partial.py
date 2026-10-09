#!/usr/bin/env python3
"""SUR-PARTIAL (9 Oct 2026): partial-split power curve for score.py (b)'s SPLIT statistic at the pooled N (65 lines; 0744 L + 0744 R +
0745 L), PREREG-SUR-PARTIAL.md pushed in its own commit before any draw. Everything is SUR-POOLPC's poolpc.py imported unchanged (loader,
per-pass scaffolds, statistic, K=300 deranged-gloss C1 per synthetic unit, verdict rule, matrix speed-up); the one change is the planted
arm: each gloss m that the scaffold draws as [y-fam] is written 'Mx' (a sign not in T) with probability f, else stays [y-fam]
(f = 1.0 is SUR-POOLPC's H1). Levels f = 0.25, 0.50, 0.75; 200 units per level per pass scaffold at 65 lines; master seed 20261010.
Usage: python3 partial.py [--selftest] [--check]   writes partial.out; --check exits 1 if stale."""
import os, sys, random
from collections import Counter
from multiprocessing import Pool
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, '..', 'inv373_pool_poolpc'))
import poolpc as PC
T, YF, SC, NP, K, SEED = PC.T, PC.YF, PC.SC, PC.NP, PC.K, PC.SEED
LEVELS = [0.25, 0.50, 0.75]; NU = 200
def synth(sc, f, rnd, nl):
    G, face, unal, pdel, pins = sc; L, Lab, GG = [], [], []; planted = kept = 0
    for _ in range(nl):
        g = G[rnd.randrange(len(G))]; cs = []
        for x in g:
            if rnd.random() >= pdel:
                fa = face.get(x)
                c = rnd.choices(list(fa), weights=list(fa.values()))[0] if fa else rnd.choice([k for k, v in T.items() if x in v] or ['?'])
                if x == 'm' and c == YF:
                    if rnd.random() < f: c = 'Mx'; planted += 1
                    else: kept += 1
                cs.append(c)
            if rnd.random() < pins: cs.append(rnd.choice(unal))
        L.append(cs); Lab.append(['U' if c == YF else None for c in cs]); GG.append(list(g))
    return L, Lab, GG, planted, kept
def one(args):
    p, f, sd = args; rnd = random.Random(sd); L, Lab, G, pl, kp = synth(SC[p], f, rnd, NP)
    m0, n0, S0, lo, hi, v, _ = PC.ctrl(L, Lab, G, K, rnd); return p, f, m0, n0, S0, lo, hi, v, pl, kp
if __name__ == '__main__':
    if '--selftest' in sys.argv:
        for f in LEVELS:
            r = [synth(SC['A'], f, random.Random(i), NP)[3:] for i in range(20)]
            print(f'selftest f {f}: planted share {sum(a for a, b in r) / max(1, sum(a + b for a, b in r)):.3f}')
        sys.exit(0)
    master = random.Random(SEED)
    jobs = [(p, f, master.getrandbits(48)) for f in LEVELS for p in 'AB' for _ in range(NU)]
    with Pool(4) as pool: res = pool.map(one, jobs, chunksize=4)
    out = [f'# SUR-PARTIAL: poolpc.py scaffolds (pooled lines {NP}), K={K} C1 per unit, {NU} units per level per pass, master seed {SEED}']
    det = {}
    for f in LEVELS:
        for p in 'AB':
            r = [x for x in res if x[0] == p and x[1] == f]; n = len(r); c = Counter(x[7] for x in r); mean = lambda k: sum(x[k] for x in r) / n
            det[f, p] = c['LEANS n'] / n
            out.append(f'  f {f:.2f} {p}: units {n}; planted share {sum(x[8] for x in r) / max(1, sum(x[8] + x[9] for x in r)):.3f}; '
                       f'y on m mean {mean(2):.1f}, on n mean {mean(3):.1f}; S mean {sum(x[4] for x in r if x[4] == x[4]) / n:.3f}; '
                       f'p99.5 mean {mean(6):.3f}; verdicts {dict(c)}; LEANS n rate {det[f, p]:.3f}')
    for f in LEVELS: out.append(f'DETECTION f {f:.2f}: A {det[f, "A"]:.3f} B {det[f, "B"]:.3f}' + (' -> power >= 0.80 both' if min(det[f, 'A'], det[f, 'B']) >= 0.8 else ''))
    ok = [f for f in LEVELS if min(det[f, 'A'], det[f, 'B']) >= 0.8]
    out.append(f'SMALLEST f with power >= 0.80 on both scaffolds: {min(ok) if ok else "none of 0.25/0.50/0.75 (1.00 per SUR-POOLPC)"}')
    txt = '\n'.join(out) + '\n'; fo = os.path.join(H, 'partial.out')
    if '--check' in sys.argv: sys.exit(0 if os.path.exists(fo) and open(fo, encoding='utf-8').read() == txt else 1)
    open(fo, 'w', encoding='utf-8').write(txt); print(txt, end='')
