#!/usr/bin/env python3
"""SUR-POOLPC (9 Oct 2026): SPLIT power at the pooled N (0744 L + 0744 R + 0745 L), PREREG-SUR-POOLPC.md pushed before any draw.
SUR-SPLITPC's planted-split scaffold (splitpc.py: bootstrap gloss lines, real per-letter facing distributions from the steered DP alignment,
real deletion and insertion rates; H1 = every m drawn as [y-fam] written with a sign 'Mx' not in T, so the y-family faces n only) is built
per pass (A, B) from the three held-out units pooled, with each unit loaded by 0745 L's score.py load() unchanged (U set per unit).
The statistic is score.py (b) unchanged: S = n/(m+n) over y-family tokens DP-aligned to gloss m|n with T's [y-fam]={m,n} steer, against K
deranged-gloss C1 draws, LEANS n iff S > p99.5, LEANS m iff S < p0.5, non-test iff m+n < 10, < K/2 usable draws or p0.5 == p99.5.
Speed-up (exact, checked): dp_idx is per line, so a unit's (m, n) count for cipher line i against gloss line j is computed once for every
(i, j) and each derangement draw is a sum over that matrix; --selftest compares it to score.py's stats() on deranged draws and must match.
Ladder: synthetic units of 22 (0745 L's size), 44 and the pooled line count, 200 H1 units per pass scaffold at each; H0 50 units per scaffold
at the pooled N. Gate (pooled N): detection >= 0.80 on both scaffolds. Only on a PASS, --real scores the real pooled units (10,000 draws).
Usage: python3 poolpc.py [--selftest | --real] [--check]   writes poolpc.out (or poolpc_real.out); --check exits 1 if stale."""
import os, sys, random
from collections import Counter
from multiprocessing import Pool
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, '..'); SP = os.path.join(P, 'inv373_0745L_blind')
src = open(os.path.join(SP, 'score.py'), encoding='utf-8').read().split('\nout = []; V = {}')[0]
S = {'__file__': os.path.join(SP, 'score.py'), '__name__': 'poolpc'}; exec(src, S)
T, dp_idx, stats, split, derange = S['T'], S['dp_idx'], S['stats'], S['split'], S['dn']['derange']
UNITS = ['inv373_0744_blind_sb', 'inv373_0744R_blind', 'inv373_0745L_blind']
SEED = 20261010; K = 300; KREAL = 10000; YF = '[y-fam]'
def loadpool(p):
    L, Lab, G, per = [], [], [], []
    for u in UNITS:
        S['U'] = os.path.join(P, u); l, lb, g = S['load'](p); L += l; Lab += lb; G += g
        per.append((u, len(l), stats(l, lb, g)[3]))
    return L, Lab, G, per
def scaffold(L, Lab, G):
    face = {}; unal = []; nal = 0
    for cs, lab, gs in zip(L, Lab, G):
        al = dp_idx(cs, gs, T); used = set()
        for i, x in al:
            face.setdefault(x, Counter())[YF if lab[i] else cs[i]] += 1; used.add(i)
        unal += [YF if lab[i] else cs[i] for i in range(len(cs)) if i not in used]; nal += len(al)
    nlet = sum(map(len, G)); return G, face, unal, 1 - nal / nlet, len(unal) / nlet
def synth(sc, arm, rnd, nl):
    G, face, unal, pdel, pins = sc; L, Lab, GG = [], [], []
    for _ in range(nl):
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
def mnmat(L, Lab, G):
    M = []
    for cs, lab in zip(L, Lab):
        row = []
        for gs in G:
            m = n = 0
            for i, x in dp_idx(cs, gs, T):
                if lab[i]:
                    if x == 'm': m += 1
                    elif x == 'n': n += 1
            row.append((m, n))
        M.append(row)
    return M
def ctrl(L, Lab, G, k, rnd):
    M = mnmat(L, Lab, G); nl = len(G)
    m0 = sum(M[i][i][0] for i in range(nl)); n0 = sum(M[i][i][1] for i in range(nl)); t = m0 + n0
    S0 = n0 / t if t else float('nan'); cP = []
    for _ in range(k):
        q = derange(rnd, nl); m = sum(M[i][q[i]][0] for i in range(nl)); n = sum(M[i][q[i]][1] for i in range(nl))
        if m + n > 0: cP.append(n / (m + n))
    cP.sort(); N = len(cP); lo, hi = (cP[int(0.005 * N)], cP[int(0.995 * N) - 1]) if N else (float('nan'),) * 2
    v = 'non-test' if (t < 10 or N < k // 2 or lo == hi) else 'LEANS n' if S0 > hi else 'LEANS m' if S0 < lo else 'NO SPLIT SHOWN'
    return m0, n0, S0, lo, hi, v, cP
def one(args):
    p, arm, nl, sd = args; rnd = random.Random(sd); L, Lab, G = synth(SC[p], arm, rnd, nl)
    m0, n0, S0, lo, hi, v, _ = ctrl(L, Lab, G, K, rnd); return p, arm, nl, m0, n0, S0, lo, hi, v
POOL = {p: loadpool(p) for p in 'AB'}; SC = {p: scaffold(*POOL[p][:3]) for p in 'AB'}; NP = len(POOL['A'][0])
LADDER = [22, 44, NP]; DRAWS = {'H1': 200, 'H0': 50}
def head():
    out = [f'# SUR-POOLPC: units {", ".join(UNITS)}; K={K} C1 draws per synthetic unit, master seed {SEED}']
    for p in 'AB':
        L, Lab, G, per = POOL[p]; G_, face, unal, pdel, pins = SC[p]
        out.append(f'# pass {p} real m|n-facing y-family tokens: ' + '; '.join(f'{u} lines {n} m {mn["m"]} n {mn["n"]}' for u, n, mn in per)
                   + f'; pooled lines {len(L)} m {sum(x[2]["m"] for x in per)} n {sum(x[2]["n"] for x in per)}')
        out.append(f'# scaffold {p}: lines {len(G)}, gloss letters {sum(map(len, G))}, p_del {pdel:.3f}, p_ins {pins:.3f}; '
                   f'face m {dict(face["m"].most_common(4))}; face n {dict(face["n"].most_common(4))}')
    return out
if __name__ == '__main__':
    if '--selftest' in sys.argv:
        rnd = random.Random(1); L, Lab, G = synth(SC['A'], 'H1', rnd, 22); M = mnmat(L, Lab, G)
        for _ in range(5):
            q = derange(rnd, 22); mn = stats(L, Lab, [G[k] for k in q])[3]
            assert (mn['m'], mn['n']) == (sum(M[i][q[i]][0] for i in range(22)), sum(M[i][q[i]][1] for i in range(22)))
        print('\n'.join(head())); print('selftest OK (matrix sums == stats() on 5 deranged draws)'); sys.exit(0)
    if '--real' in sys.argv:
        out = head() + [f'# REAL pooled SPLIT, C1 {KREAL} deranged-gloss draws, seed {SEED}']; V = {}
        for p in 'AB':
            L, Lab, G, _ = POOL[p]; m0, n0, S0, lo, hi, v, cP = ctrl(L, Lab, G, KREAL, random.Random(SEED))
            mean = sum(cP) / len(cP); out.append(f'  pass {p}: y on m {m0}, n {n0}; S {S0:.3f}; C1 mean {mean:.3f} p0.5 {lo:.3f} p99.5 {hi:.3f} -> {v}'); V[p] = v
        out.append(f'UNIT pooled SPLIT: {V["A"] if V["A"] == V["B"] else "not shown (passes disagree)"}')
        f = os.path.join(H, 'poolpc_real.out')
    else:
        master = random.Random(SEED)
        jobs = [(p, 'H1', nl, master.getrandbits(48)) for nl in LADDER for p in 'AB' for _ in range(DRAWS['H1'])]
        jobs += [(p, 'H0', NP, master.getrandbits(48)) for p in 'AB' for _ in range(DRAWS['H0'])]
        with Pool(4) as pool: res = pool.map(one, jobs, chunksize=4)
        out = head()
        for nl in LADDER:
            for p in 'AB':
                for arm in ('H1', 'H0'):
                    r = [x for x in res if x[0] == p and x[1] == arm and x[2] == nl]
                    if not r: continue
                    n = len(r); c = Counter(x[8] for x in r); mean = lambda k: sum(x[k] for x in r) / n
                    out.append(f'  lines {nl} {p} {arm}: units {n}; y on m mean {mean(3):.1f}, on n mean {mean(4):.1f}; S mean '
                               f'{sum(x[5] for x in r if x[5] == x[5]) / n:.3f}; p99.5 mean {mean(7):.3f}; verdicts {dict(c)}; LEANS n rate {c["LEANS n"] / n:.3f}')
        for nl in LADDER:
            d = [sum(1 for x in res if x[0] == p and x[1] == 'H1' and x[2] == nl and x[8] == 'LEANS n') / DRAWS['H1'] for p in 'AB']
            out.append(f'DETECTION lines {nl}: A {d[0]:.3f} B {d[1]:.3f}' + (f' -> GATE {"PASS" if min(d) >= 0.8 else "FAIL"}' if nl == NP else ''))
        f = os.path.join(H, 'poolpc.out')
    txt = '\n'.join(out) + '\n'
    if '--check' in sys.argv: sys.exit(0 if os.path.exists(f) and open(f, encoding='utf-8').read() == txt else 1)
    open(f, 'w', encoding='utf-8').write(txt); print(txt, end='')
