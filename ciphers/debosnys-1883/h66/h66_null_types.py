#!/usr/bin/env python3
"""H66 (DEB-RUN, 7 Oct 2026): null-TYPE selection search on c2.

Question: is c2 a homophonic language text padded with nulls drawn from their OWN sign types (the classic nomenclator
null, disjoint from the text signs)? DEB-SWARM-D's escape route NULLS-q (escape.py) drew its nulls from the same sign
curve as the text, so it left this design untested: there, no type removal can restore order; here, removing the
null types should. Instrument: greedy backward elimination of sign types (count >= MINC), each step dropping the type
whose removal (tokens deleted, neighbours re-joined) most raises the order score S = z(mi1) + z(bg2) + z(rep3) against
the text's own within-line shuffles; S_max = best S along the path while the dropped share stays <= MAXQ.
Selection inflation is priced by running the identical greedy on within-line shuffles of the same text (the
search-null). Matched control (rule 3, design-matched, can fail differently): FR homophonic letters at c2's line
lengths and sign curve, a disjoint set of null types carrying share q of the tokens, 15 pct type noise; the control
must beat its own search-null's 95th percentile in >= 8 of 10 seeds at q, or q is logged as 'no passable control'.
Target verdict at q only where the control passed: real c2 S_max above the 95th pct of its search-null -> lead
(next: read which types were dropped); else fail for this design at this N and noise.
Usage: h66_null_types.py {real|realnull|ctl|ctlnull} SEED [q]   -> one JSON line on stdout."""
import sys, os, random, math, collections, json
HERE = os.path.dirname(os.path.abspath(__file__)); GD = os.path.join(os.path.dirname(HERE), 'swarm', 'G-D')
sys.path.insert(0, GD); import dcore
MINC, MAXQ, T = 3, 0.65, 24

def stats(lines):
    bg = collections.Counter(); L = collections.Counter(); R = collections.Counter(); tri = collections.Counter()
    for l in lines:
        for a, b in zip(l, l[1:]): bg[(a, b)] += 1; L[a] += 1; R[b] += 1
        for i in range(len(l) - 2): tri[(l[i], l[i + 1], l[i + 2])] += 1
    n = sum(bg.values())
    mi = sum(c / n * math.log2(c * n / (L[a] * R[b])) for (a, b), c in bg.items()) if n else 0.0
    return (mi, sum(1 for c in bg.values() if c >= 2), sum(1 for c in tri.values() if c >= 2))

def S(lines, rng):
    obs = stats(lines); sh = []
    for _ in range(T):
        s = []
        for l in lines: c = l[:]; rng.shuffle(c); s.append(c)
        sh.append(stats(s))
    z = 0.0
    for k in range(3):
        v = [x[k] for x in sh]; m = sum(v) / T; sd = (sum((x - m) ** 2 for x in v) / T) ** 0.5
        z += (obs[k] - m) / sd if sd > 0 else 0.0
    return z

def greedy(lines, rng):
    N = sum(map(len, lines)); cnt = collections.Counter(s for l in lines for s in l)
    removed = set(); dropped = 0; path = [(0.0, S(lines, rng), None)]
    while True:
        cands = [t for t, c in cnt.items() if c >= MINC and t not in removed and (dropped + c) / N <= MAXQ]
        if not cands: break
        best = None
        for t in cands:
            r = removed | {t}; ls = [[s for s in l if s not in r] for l in lines]; ls = [l for l in ls if len(l) > 1]
            v = S(ls, rng)
            if best is None or v > best[0]: best = (v, t)
        removed.add(best[1]); dropped += cnt[best[1]]; path.append((round(dropped / N, 3), round(best[0], 2), best[1]))
    smax = max(p[1] for p in path)
    return dict(S0=round(path[0][1], 2), Smax=round(smax, 2), path=path)

def shuffled(lines, rng):
    out = []
    for l in lines: c = l[:]; rng.shuffle(c); out.append(c)
    return out

def control(q, rng):
    t2 = dcore.target('c2'); lens = [len(l) for l in t2]; N = sum(lens); cv = dcore.curve_of(t2)
    idx = list(range(len(cv))); rng.shuffle(idx); null_idx = []; tot = 0
    for i in idx:                       # disjoint null types until their share reaches q
        if tot >= q * N: break
        null_idx.append(i); tot += cv[i]
    text_curve = [cv[i] for i in range(len(cv)) if i not in set(null_idx)]
    nq = tot / N; nt = N - tot
    text = dcore.encode(dcore.units('fr', nt, rng, 'letters'), text_curve, rng)
    nulls = rng.choices([f'Z{i}' for i in null_idx], [cv[i] for i in null_idx], k=tot)
    pos = sorted(rng.sample(range(N), tot)); seq = []; ti = ni = 0; ps = set(pos)
    for k in range(N):
        if k in ps: seq.append(nulls[ni]); ni += 1
        else: seq.append(text[ti]); ti += 1
    return dcore.cut(dcore.noise(seq, 0.15, rng), lens), round(nq, 3), sorted({f'Z{i}' for i in null_idx})

if __name__ == '__main__':
    mode, seed = sys.argv[1], int(sys.argv[2]); q = float(sys.argv[3]) if len(sys.argv) > 3 else None
    rng = random.Random(6600 + seed)
    if mode in ('real', 'realnull'):
        lines = dcore.target('c2'); lines = shuffled(lines, rng) if mode == 'realnull' else lines; extra = {}
    else:
        lines, nq, nulls = control(q, rng); extra = dict(q=q, q_actual=nq, n_null_types=len(nulls))
        if mode == 'ctlnull': lines = shuffled(lines, rng)
    r = greedy(lines, rng)
    if mode == 'ctl':
        dropped = [p[2] for p in r['path'][1:]]; best_i = max(range(len(r['path'])), key=lambda i: r['path'][i][1])
        sel = set(dropped[:best_i]); nul = set(nulls)
        extra.update(sel_n=len(sel), sel_null_precision=round(len(sel & nul) / len(sel), 3) if sel else None)
    print(json.dumps(dict(mode=mode, seed=seed, **extra, S0=r['S0'], Smax=r['Smax'],
                          path=r['path'] if mode in ('real', 'ctl') else None)), flush=True)
