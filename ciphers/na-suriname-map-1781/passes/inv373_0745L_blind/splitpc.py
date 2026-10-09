#!/usr/bin/env python3
"""SUR-SPLITPC (9 Oct 2026): positive control for SUR-0745's (b) SPLIT statistic (PREREG-SUR-SPLITPC.md, pushed before this ran).
score.py's functions are loaded unchanged (its scoring body is not run). Synthetic units of 0745 LEFT's size are built per pass scaffold
(A, B): 22 gloss lines bootstrapped from that pass's own gloss lines; each gloss letter is enciphered by a code drawn from the codes that
face that letter in the real DP alignment of that pass (its own reader/aligner noise), deleted with the real unaligned-letter rate, and
followed by an inserted sign (drawn from the real unaligned signs) at the real insertion rate.
Arms: H1 (planted full split, the 'y-family = n only' alternative): every m whose drawn code is [y-fam] is written with a sign 'Mx' not in
T, so the y-family faces n only before alignment; H0 (no split): m and n both keep their real facing distributions.
Each synthetic unit is scored with the same SPLIT statistic (S = n/(m+n) over y-family tokens aligned to gloss m|n, T with the
[y-fam]={m,n} steer) against K deranged-gloss C1 draws, same verdict rule (LEANS n > p99.5, LEANS m < p0.5, non-test rules as score.py).
Usage: python3 splitpc.py [--check]   writes splitpc.out; --check exits 1 if splitpc.out is stale."""
import os, sys, random
from collections import Counter
from multiprocessing import Pool
H = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(H, 'score.py'), encoding='utf-8').read().split('\nout = []; V = {}')[0]
S = {'__file__': os.path.join(H, 'score.py'), '__name__': 'splitpc'}; exec(src, S)
T, dp_idx, stats, split, derange = S['T'], S['dp_idx'], S['stats'], S['split'], S['dn']['derange']
SEED = 20261009; K = 300; DRAWS = {'H1': 200, 'H0': 50}; YF = '[y-fam]'
def scaffold(p):
    L, Lab, G = S['load'](p); face = {}; unal = []; nal = 0
    for cs, lab, gs in zip(L, Lab, G):
        al = dp_idx(cs, gs, T); used = set()
        for i, x in al:
            face.setdefault(x, Counter())[YF if lab[i] else cs[i]] += 1; used.add(i)
        unal += [YF if lab[i] else cs[i] for i in range(len(cs)) if i not in used]; nal += len(al)
    nlet = sum(map(len, G)); return G, face, unal, 1 - nal / nlet, len(unal) / nlet
def synth(sc, arm, rnd):
    G, face, unal, pdel, pins = sc; L, Lab, GG = [], [], []
    for _ in range(len(G)):
        g = G[rnd.randrange(len(G))]; cs = []
        for x in g:
            if rnd.random() >= pdel:
                f = face.get(x)
                c = rnd.choices(list(f), weights=list(f.values()))[0] if f else rnd.choice([k for k, v in T.items() if x in v] or ['?'])
                if arm == 'H1' and x == 'm' and c == YF: c = 'Mx'
                cs.append(c)
            if rnd.random() < pins: cs.append(rnd.choice(unal))
        L.append(cs); Lab.append(['U' if c == YF else None for c in cs]); GG.append(list(g))
    return L, Lab, GG
def one(args):
    p, arm, sd = args; rnd = random.Random(sd); L, Lab, G = synth(SC[p], arm, rnd)
    A0, _, _, mn, _ = stats(L, Lab, G); S0 = split(mn); t = mn['m'] + mn['n']; cP = []
    for _ in range(K):
        q = derange(rnd, len(G)); _, _, _, m2, _ = stats(L, Lab, [G[k] for k in q])
        if m2['m'] + m2['n'] > 0: cP.append(split(m2))
    cP.sort(); M = len(cP); lo, hi = (cP[int(0.005 * M)], cP[int(0.995 * M) - 1]) if M else (float('nan'),) * 2
    v = 'non-test' if (t < 10 or M < K // 2 or lo == hi) else 'LEANS n' if S0 > hi else 'LEANS m' if S0 < lo else 'NO SPLIT SHOWN'
    return p, arm, A0, mn['m'], mn['n'], S0, lo, hi, v
SC = {p: scaffold(p) for p in 'AB'}
if __name__ == '__main__':
    master = random.Random(SEED); jobs = [(p, arm, master.getrandbits(48)) for p in 'AB' for arm in ('H1', 'H0') for _ in range(DRAWS[arm])]
    with Pool(4) as pool: res = pool.map(one, jobs, chunksize=5)
    out = [f'# SUR-SPLITPC: K={K} C1 draws per synthetic unit, master seed {SEED}; synthetic units bootstrapped per pass scaffold']
    for p in 'AB':
        G, face, unal, pdel, pins = SC[p]
        out.append(f'# scaffold {p}: lines {len(G)}, gloss letters {sum(map(len, G))}, p_del {pdel:.3f}, p_ins {pins:.3f}; '
                   f'face m {dict(face["m"].most_common(4))}; face n {dict(face["n"].most_common(4))}')
        for arm in ('H1', 'H0'):
            r = [x for x in res if x[0] == p and x[1] == arm]; n = len(r); c = Counter(x[8] for x in r)
            mean = lambda k: sum(x[k] for x in r) / n
            out.append(f'  {p} {arm}: draws {n}; synth A mean {mean(2):.3f}; y on m mean {mean(3):.1f}, on n mean {mean(4):.1f}; S mean '
                       f'{sum(x[5] for x in r if x[5] == x[5]) / n:.3f}; p99.5 mean {mean(7):.3f}; verdicts {dict(c)}; '
                       f'LEANS n rate {c["LEANS n"] / n:.3f}')
    for p in 'AB':
        d = sum(1 for x in res if x[0] == p and x[1] == 'H1' and x[8] == 'LEANS n') / DRAWS['H1']
        out.append(f'DETECTION {p} (H1, LEANS n): {d:.3f} -> {"power >= 0.8" if d >= 0.8 else "power < 0.8"}')
    txt = '\n'.join(out) + '\n'; f = os.path.join(H, 'splitpc.out')
    if '--check' in sys.argv: sys.exit(0 if os.path.exists(f) and open(f, encoding='utf-8').read() == txt else 1)
    open(f, 'w', encoding='utf-8').write(txt); print(txt, end='')
