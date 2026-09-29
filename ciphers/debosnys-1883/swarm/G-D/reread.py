#!/usr/bin/env python3
"""DEB-SWARM-D test R (29 Sept 2026): is the language there but in another reading order? The text read in line order
is re-read (a) down columns (sign j of every line, then j+1: the text written in columns), (b) by undoing a columnar
transposition of column height R for every R in 2..60 (the text written in rows of ceil(N/R), taken down columns),
and each reading gets the frozen single-text score (dcore.score 'c2' parts: z mi1 + z bigram types>=2 + z repeated
3-grams - z doubled, 60 within-line shuffles, lines = the original line lengths). Scan statistic: the largest score
over the 60 readings (the multiple readings are paid for by applying the same scan to the nulls). Nulls: NULL-IID at
c2 shape. Power: FR-HOMO letters written by columnar transposition (R 7, 19, 33) and written in columns, 15 pct noise.
Writes reread.json."""
import dcore, escape, random, math, json, statistics as st
rng = random.Random(6262); L2 = escape.L2; N2 = escape.N2; cv = escape.cv
def score1(lines, trials=60):
    z = dcore.zstats(lines, rng, trials); return z['mi1']['z'] + z['bg2']['z'] + z['rep3']['z'] - z['dbl']['z']
def readings(lines):
    seq = [s for l in lines for s in l]; lens = [len(l) for l in lines]; out = {}
    col = [lines[i][j] for j in range(max(lens)) for i in range(len(lines)) if j < lens[i]]; out['columns'] = col
    for R in range(2, 61):
        C = math.ceil(N2 / R); cols = []; k = 0
        # inverse of: rows of length C written, read down columns of height R
        full = R * C - N2  # last row short by `full` cells
        colh = [R if j < C - full else R - 1 for j in range(C)]
        grid = [[None] * C for _ in range(R)]
        for j in range(C):
            for i in range(colh[j]):
                if k < len(seq): grid[i][j] = seq[k]; k += 1
        out[f'R{R}'] = [x for row in grid for x in row if x is not None]
    return {k: dcore.cut(v, lens) for k, v in out.items()}
def scan(lines):
    sc = {k: score1(v) for k, v in readings(lines).items()}; b = max(sc, key=sc.get); return b, round(sc[b], 2), sc
res = {}
b, s, sc = scan(escape.t2); res['target'] = dict(best=b, score=s, line_order=round(score1(escape.t2), 2), all={k: round(v, 2) for k, v in sc.items()})
print('target', b, s, 'line order', res['target']['line_order'], flush=True)
for name, gen in (('NULL-IID', lambda: dcore.make('NULL-IID', L2, cv, rng)), ('TRANS-7', lambda: escape.trans(7)),
                  ('TRANS-19', lambda: escape.trans(19)), ('TRANS-33', lambda: escape.trans(33)), ('VERTICAL', escape.vertical_ctrl)):
    v = [scan(gen())[:2] for _ in range(12)]; sv = sorted(x[1] for x in v)
    res[name] = dict(best_readings=[x[0] for x in v], median=st.median(sv), min=sv[0], max=sv[-1], share_ge_target=sum(x >= s for x in sv) / len(sv))
    print(name, res[name], flush=True)
json.dump(res, open('reread.json', 'w'), indent=1)
