#!/usr/bin/env python3
"""Pre-registered replication of the R34 re-reading (LOG.md, 03:30 UTC). (a) scan + 200-scan own-shuffle null on c2 in
the harness reading (only '_'/MULTI and clear spans dropped) and on this group's reading with a fresh seed; (b) the
R34 reading's two halves (grid rows 1-17, 18-34) scored separately at 1,000 shuffles."""
import sys, json, random, math, dcore
def load(harness):
    raw = dcore.settled_lines(dcore.DEB, 'c2', drop_clear=True); drop = {'_', 'MULTI'} if harness else dcore.PUNCT
    return [l for l in ([s for s in v if s not in drop] for v in raw.values()) if l]
def score1(lines, rng, trials=60):
    z = dcore.zstats(lines, rng, trials); return z['mi1']['z'] + z['bg2']['z'] + z['rep3']['z'] - z['dbl']['z']
def grid(seq, R):
    N = len(seq); C = math.ceil(N / R); full = R * C - N; colh = [R if j < C - full else R - 1 for j in range(C)]
    g = [[None] * C for _ in range(R)]; k = 0
    for j in range(C):
        for i in range(colh[j]):
            if k < N: g[i][j] = seq[k]; k += 1
    return [[x for x in row if x is not None] for row in g]
def readings(lines):
    seq = [s for l in lines for s in l]; lens = [len(l) for l in lines]
    o = {'columns': [lines[i][j] for j in range(max(lens)) for i in range(len(lines)) if j < lens[i]]}
    for R in range(2, 61): o[f'R{R}'] = [x for row in grid(seq, R) for x in row]
    return {k: dcore.cut(v, lens) for k, v in o.items()}
def scan(lines, rng):
    sc = {k: score1(v, rng) for k, v in readings(lines).items()}; b = max(sc, key=sc.get); return b, sc[b]
mode = sys.argv[1]; res = {}
if mode in ('harness', 'fresh'):
    rng = random.Random(31337 if mode == 'fresh' else 4711); T = load(mode == 'harness')
    b, s = scan(T, rng); nul = sorted(scan([rng.sample(l, len(l)) for l in T], rng)[1] for _ in range(int(sys.argv[2])))
    res = dict(mode=mode, N=sum(map(len, T)), best=b, score=round(s, 2), null_median=nul[len(nul) // 2], null_p95=nul[int(.95 * len(nul))], p_ge=sum(x >= s for x in nul) / len(nul))
else:
    rng = random.Random(99); T = load(False); seq = [s for l in T for s in l]; rows = grid(seq, 34)
    for name, rr in (('rows1-17', rows[:17]), ('rows18-34', rows[17:])):
        z = dcore.zstats(rr, rng, 1000); res[name] = dict(score=round(z['mi1']['z'] + z['bg2']['z'] + z['rep3']['z'] - z['dbl']['z'], 2), **{k: z[k]['z'] for k in ('mi1', 'bg2', 'rep3', 'dbl')})
print(res); json.dump(res, open(f'r34_rep_{mode}.json', 'w'), indent=1)
