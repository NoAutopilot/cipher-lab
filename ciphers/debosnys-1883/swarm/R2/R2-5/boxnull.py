#!/usr/bin/env python3
"""R2-5 diagnostic D2 (PREREG.md addendum, registered before it was run on the real text). D's order features
(dcore.raw_stats: mi1, bg2, rep3, dbl), but each measured against shuffles made at BOX level (boxes permuted within
their line, then split), so a composite's own internal pairs are in the null and only order BETWEEN boxes counts.
Score = sum over the two texts of z(mi1) + z(bg2) + z(rep3) - z(dbl), D's own combination without the transfer terms.
Usage: boxnull.py TEXT N OUT   TEXT in real-T real-N planted folger null-T null-N (null = NULL-SPLIT at 0.20)"""
import os, sys, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import r25, dcore

def zscore(lines, M, rng, trials):
    obs = dcore.raw_stats(r25.apply_split(lines, M)); sh = collections.defaultdict(list)
    for _ in range(trials):
        s = []
        for l in lines: c = l[:]; rng.shuffle(c); s.append(c)
        for k, v in dcore.raw_stats(r25.apply_split(s, M)).items(): sh[k].append(v)
    z = {}
    for k, v in obs.items():
        m = sum(sh[k]) / trials; sd = (sum((x - m) ** 2 for x in sh[k]) / trials) ** 0.5
        z[k] = (v - m) / sd if sd > 0 else 0.0
    return z['mi1'] + z['bg2'] + z['rep3'] - z['dbl'], z

def pair(u1, u2, M, rng, trials):
    a, za = zscore(u1, M, rng, trials); b, zb = zscore(u2, M, rng, trials)
    return dict(score=round(a + b, 3), c1=round(a, 3), c2=round(b, 3), z1={k: round(v, 2) for k, v in za.items()},
                z2={k: round(v, 2) for k, v in zb.items()})

if __name__ == '__main__':
    tid, n, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]; rows = []
    for i in range(n):
        if tid.startswith('real'):
            rng = random.Random(3000 + i); rows.append(pair(r25.R1, r25.R2, r25.REAL_MAPS[tid], rng, 400))
        elif tid.startswith('null'):
            m = 'real-' + tid[-1]; _, _, _, ids, M = r25.shape(m); rng = random.Random(f'r25-d2-{tid}-{i}')
            names = list(ids); w = [ids[x] for x in names]; N1, N2 = sum(r25.L1), sum(r25.L2)
            a = rng.choices(names, w, k=int(N1 * 1.12) + 3); b = rng.choices(names, w, k=int(N2 * 1.12) + 3)
            u1 = dcore.cut(r25.r21.mixnoise(a, 0.20, rng, N1), r25.L1); u2 = dcore.cut(r25.r21.mixnoise(b, 0.20, rng, N2), r25.L2)
            rows.append(pair(u1, u2, M, rng, 100))
        else:
            rng = random.Random(f'r25-ctrl-{tid}-0.2-{i}'); boxes, M = r25.text_source(tid, rng)
            u1, u2 = r25.noisy_pair(boxes, {}, rng, 0.20); rows.append(pair(u1, u2, M, rng, 100))
    json.dump(dict(text=tid, rows=rows), open(out, 'w')); print(tid, sorted(r['score'] for r in rows)[len(rows) // 2])
