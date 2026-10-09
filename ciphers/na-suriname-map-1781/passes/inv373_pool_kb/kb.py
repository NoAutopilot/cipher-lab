#!/usr/bin/env python3
"""SUR-KB (9 Oct 2026): key-blind SPLIT statistic at the pooled N (65 lines; 0744 L + 0744 R + 0745 L), PREREG-SURKB.md pushed in its own
commit before any draw. poolpc.py is imported unchanged (loader, scaffold builder, synthetic generator logic, matrix speed-up, verdict rule,
K=300 deranged-gloss C1 per synthetic unit); the change is V-SUR0745's key-blind T: '[y-fam]' is removed from T before ANY alignment used
here, so the DP aligner earns nothing for putting a y-family sign on gloss m or n. S = n/(m+n) over y-family tokens aligned to gloss m|n.
Scaffolds are rebuilt per pass from the KEY-BLIND alignment (facing distributions, deletion and insertion rates), so neither the generator
nor the statistic carries the steer. Planted arm: each gloss m drawn as [y-fam] is written 'Mx' with probability f; under the key-blind T
'Mx' and '[y-fam]' are both outside T, so the plant changes only the y-family label, never the alignment. Levels f = 0 (H0), 0.25, 0.50,
0.75, 1.00; 100 units per level per pass scaffold at 65 lines; master seed 20261009.
Usage: python3 kb.py --selftest | (power curve, writes kb.out) | --real (writes kb_real.out, 10,000 draws) ; --check exits 1 if stale."""
import os, sys, random
from collections import Counter
from multiprocessing import Pool
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, '..', 'inv373_pool_poolpc'))
import poolpc as PC
YF = PC.YF; PC.T.pop(YF, None); T = PC.T          # key-blind: shared dict, so PC.ctrl / PC.mnmat / dp_idx all run without the steer
assert YF not in PC.S['T']
SEED = 20261009; K = PC.K; KREAL = 10000; NU = 100; LEVELS = [0.0, 0.25, 0.50, 0.75, 1.00]
POOL = {p: PC.POOL[p] for p in 'AB'}; SCK = {p: PC.scaffold(*POOL[p][:3]) for p in 'AB'}; NP = PC.NP
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
    p, f, sd = args; rnd = random.Random(sd); L, Lab, G, pl, kp = synth(SCK[p], f, rnd, NP)
    m0, n0, S0, lo, hi, v, _ = PC.ctrl(L, Lab, G, K, rnd); return p, f, m0, n0, S0, lo, hi, v, pl, kp
def write(fo, out):
    txt = '\n'.join(out) + '\n'
    if '--check' in sys.argv: sys.exit(0 if os.path.exists(fo) and open(fo, encoding='utf-8').read() == txt else 1)
    open(fo, 'w', encoding='utf-8').write(txt); print(txt, end='')
if __name__ == '__main__':
    if '--selftest' in sys.argv:   # planted share and matrix == stats() under the key-blind T; prints no real statistic
        rnd = random.Random(1); L, Lab, G, _, _ = synth(SCK['A'], 1.0, rnd, 22); M = PC.mnmat(L, Lab, G)
        for _ in range(5):
            q = PC.derange(rnd, 22); mn = PC.stats(L, Lab, [G[k] for k in q])[3]
            assert (mn['m'], mn['n']) == (sum(M[i][q[i]][0] for i in range(22)), sum(M[i][q[i]][1] for i in range(22)))
        for f in LEVELS[1:]:
            r = [synth(SCK['A'], f, random.Random(i), NP)[3:] for i in range(20)]
            print(f'selftest f {f}: planted share {sum(a for a, b in r) / max(1, sum(a + b for a, b in r)):.3f}')
        print('selftest OK (key-blind matrix sums == stats() on 5 deranged draws)'); sys.exit(0)
    hd = [f'# SUR-KB: key-blind T (no {YF}); scaffolds from the key-blind alignment; pooled lines {NP}; K={K}; master seed {SEED}']
    for p in 'AB':
        G, face, unal, pdel, pins = SCK[p]
        hd.append(f'# scaffold {p}: lines {len(G)}, p_del {pdel:.3f}, p_ins {pins:.3f}; face m {dict(face["m"].most_common(4))}; '
                  f'face n {dict(face["n"].most_common(4))}')
    if '--real' in sys.argv:
        out = hd + [f'# REAL pooled key-blind SPLIT, C1 {KREAL} deranged-gloss draws, seed {SEED}']; V = {}
        for p in 'AB':
            L, Lab, G, _ = POOL[p]; m0, n0, S0, lo, hi, v, cP = PC.ctrl(L, Lab, G, KREAL, random.Random(SEED))
            out.append(f'  pass {p}: y on m {m0}, n {n0}; S {S0:.3f}; C1 ({len(cP)}) mean {sum(cP) / len(cP):.3f} p0.5 {lo:.3f} '
                       f'p99.5 {hi:.3f} -> {v}'); V[p] = v
        out.append(f'UNIT pooled key-blind SPLIT: {V["A"] if V["A"] == V["B"] else "not shown (passes disagree)"}')
        write(os.path.join(H, 'kb_real.out'), out); sys.exit(0)
    master = random.Random(SEED)
    jobs = [(p, f, master.getrandbits(48)) for f in LEVELS for p in 'AB' for _ in range(NU)]
    with Pool(4) as pool: res = pool.map(one, jobs, chunksize=4)
    out = hd; det = {}
    for f in LEVELS:
        for p in 'AB':
            r = [x for x in res if x[0] == p and x[1] == f]; n = len(r); c = Counter(x[7] for x in r); mean = lambda k: sum(x[k] for x in r) / n
            det[f, p] = c['LEANS n'] / n
            out.append(f'  f {f:.2f} {p}: units {n}; planted share {sum(x[8] for x in r) / max(1, sum(x[8] + x[9] for x in r)):.3f}; '
                       f'y on m mean {mean(2):.1f}, on n mean {mean(3):.1f}; S mean {sum(x[4] for x in r if x[4] == x[4]) / n:.3f}; '
                       f'p99.5 mean {sum(x[6] for x in r if x[6] == x[6]) / n:.3f}; verdicts {dict(c)}; LEANS n rate {det[f, p]:.3f}')
    for f in LEVELS:
        tag = 'false-LEANS-n (H0)' if f == 0 else 'DETECTION'
        out.append(f'{tag} f {f:.2f}: A {det[f, "A"]:.3f} B {det[f, "B"]:.3f}' + (' -> power >= 0.80 both' if f and min(det[f, 'A'], det[f, 'B']) >= 0.8 else ''))
    ok = [f for f in LEVELS if f and min(det[f, 'A'], det[f, 'B']) >= 0.8]
    out.append(f'SMALLEST f with power >= 0.80 on both scaffolds: {min(ok) if ok else "none (the key-blind statistic is a non-test at every f)"}')
    write(os.path.join(H, 'kb.out'), out)
