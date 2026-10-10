#!/usr/bin/env python3
"""SUR-MRICH (10 Oct 2026): power of the pooled SPLIT at f = 0.50 if m-rich glossed lines were added to the 88-line pool (PREREG-SURMRICH.md,
pushed before any draw). Loads ../inv373_0745R_blind/pool4.py's source (everything before `if __name__`) unchanged: POOL, SC (per-pass
scaffolds from the real 4-unit pool), ctrl (score.py (b) statistic + K=300 deranged-gloss C1, verdict rule). The only change is the gloss
draw: a synthetic unit is NP (88) lines bootstrapped from the pass's pool gloss, as pool4, PLUS nx lines bootstrapped from an extra gloss set
EG (on-disk out-of-pool gloss lines, counts.tsv), enciphered with the same pool facing/deletion/insertion; each gloss m drawn as [y-fam] is
written 'Mx' with probability f (SUR-PARTIAL's planted partial split). Levels (PREREG): L1 = 23 m-richest lines (EG = those 23, nx 23);
L2 = all 117 out-of-pool lines (EG = all, nx 117); L3 (only if L2 < 0.80 on either pass) = nx 234 from all 117. 30 units per pass at L1 and L2, 20 at L3 (CPU),
f = 0.50, master seed 20261012. --selftest times one L2 unit (no verdict shown); --check exits 1 if mrich_power.out is stale."""
import os, sys, random
from collections import Counter
from multiprocessing import Pool
H = os.path.dirname(os.path.abspath(__file__)); PP = os.path.join(H, '..', 'inv373_0745R_blind', 'pool4.py')
src = open(PP, encoding='utf-8').read().split("\nif __name__ == '__main__':")[0]
Q = {'__file__': PP, '__name__': 'mrich'}; exec(src, Q); PC = Q
T, YF, SC, NP, ctrl, gl = PC['T'], PC['YF'], PC['SC'], PC['NP'], PC['ctrl'], Q['PC']['S']['dn']['gletters']
F = 0.50; NU = 30; NUL = {'L1': 30, 'L2': 30, 'L3': 20}; SEED = 20261012
rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(H, 'counts.tsv'), encoding='utf-8')][1:]
EXTRA = [(r[0], r[3], int(r[4]), int(r[5]), r[7]) for r in rows if r[1] == 'out' and int(r[4]) > 0]
RANK = sorted(range(len(EXTRA)), key=lambda i: (-EXTRA[i][3], -EXTRA[i][3] / EXTRA[i][2], i))
TOP = [EXTRA[i] for i in RANK[:23]]
LEVELS = {'L1': (TOP, 23), 'L2': (EXTRA, 117), 'L3': (EXTRA, 234)}
def synth(sc, f, rnd, eg, nx):
    G, face, unal, pdel, pins = sc; L, Lab, GG = [], [], []
    src_ = [G[rnd.randrange(len(G))] for _ in range(NP)] + [eg[rnd.randrange(len(eg))] for _ in range(nx)]
    for g in src_:
        cs = []
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
    lv, p, sd = a; eg, nx = LEVELS[lv]; rnd = random.Random(sd); L, Lab, G = synth(SC[p], F, rnd, [gl(e[4]) for e in eg], nx)
    m0, n0, S0, lo, hi, v, _ = ctrl(L, Lab, G, PC['K'], rnd); return lv, p, m0, n0, S0, hi, v
def head():
    out = [f'# SUR-MRICH: pool {NP} lines (pool4.py scaffolds), f {F}, {NU} units per pass per level, K={PC["K"]}, master seed {SEED}']
    for lv, (eg, nx) in LEVELS.items():
        out.append(f'# {lv}: extra set {len(eg)} lines, gloss m {sum(e[3] for e in eg)}, letters {sum(e[2] for e in eg)}; nx {nx} drawn; '
                   f'expected added gloss m {nx * sum(e[3] for e in eg) / len(eg):.1f}')
    out.append('# L1 lines: ' + '; '.join(f'{e[0]} {e[1]} m{e[3]}' for e in TOP))
    return out
if __name__ == '__main__':
    if '--selftest' in sys.argv:
        import time; t = time.time(); one(('L2', 'A', 1)); print('\n'.join(head())); print(f'selftest: one L2 unit {time.time()-t:.1f} s (verdict not printed)'); sys.exit(0)
    master = random.Random(SEED); out = head(); det = {}
    run = ['L1', 'L2', 'L3']
    for lv in run:
        if lv == 'L3' and min(det['L2', 'A'], det['L2', 'B']) >= 0.8: out.append('# L3 not run (L2 >= 0.80 on both passes)'); continue
        jobs = [(lv, p, master.getrandbits(48)) for p in 'AB' for _ in range(NUL[lv])]
        with Pool(4) as pool: res = pool.map(one, jobs, chunksize=1)
        for p in 'AB':
            r = [x for x in res if x[1] == p]; n = len(r); c = Counter(x[6] for x in r); det[lv, p] = c['LEANS n'] / n
            out.append(f'  {lv} {p}: units {n}; lines {NP + LEVELS[lv][1]}; y on m mean {sum(x[2] for x in r)/n:.1f}, on n mean {sum(x[3] for x in r)/n:.1f}; '
                       f'S mean {sum(x[4] for x in r)/n:.3f}; p99.5 mean {sum(x[5] for x in r)/n:.3f}; verdicts {dict(c)}; LEANS n {det[lv, p]:.3f}')
        print(out[-2]); print(out[-1]); sys.stdout.flush()
    out.append(f'GATE (L1 power >= 0.80 on both passes at f 0.50): {"PASS -> step 2" if min(det["L1", "A"], det["L1", "B"]) >= 0.8 else "FAIL -> stop after step 1"}')
    txt = '\n'.join(out) + '\n'; fo = os.path.join(H, 'mrich_power.out')
    if '--check' in sys.argv: sys.exit(0 if os.path.exists(fo) and open(fo, encoding='utf-8').read() == txt else 1)
    open(fo, 'w', encoding='utf-8').write(txt); print(txt, end='')
