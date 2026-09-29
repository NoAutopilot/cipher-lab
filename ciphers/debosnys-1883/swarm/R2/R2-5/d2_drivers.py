#!/usr/bin/env python3
"""R2-5 D2 follow-up (diagnostic): which split-level adjacent pairs exceed their box-shuffle expectation in real-N /
real-T (c1+c2 pooled), and the same for the NULL-SPLIT mean. Prints the top pairs by excess (obs - mean) / sd."""
import sys, random, collections, json
import r25, dcore
def pairs(lines): return collections.Counter((a, b) for l in lines for a, b in zip(l, l[1:]))
for tid in ('real-N', 'real-T'):
    M = r25.REAL_MAPS[tid]; R = r25.R1 + r25.R2; obs = pairs(r25.apply_split(R, M)); rng = random.Random(7); sh = collections.defaultdict(list)
    T = 400
    for _ in range(T):
        s = [];
        for l in R: c = l[:]; rng.shuffle(c); s.append(c)
        p = pairs(r25.apply_split(s, M))
        for k in set(obs) | set(p): sh[k].append(p.get(k, 0))
    rows = []
    for k, v in sh.items():
        v = v + [0] * (T - len(v)); m = sum(v) / T; sd = (sum((x - m) ** 2 for x in v) / T) ** 0.5
        if sd > 0: rows.append(((obs.get(k, 0) - m) / sd, k, obs.get(k, 0), round(m, 2)))
    rows.sort(reverse=True); print(tid, 'top 12 pairs by z (obs, box-shuffle mean):')
    for z, k, o, m in rows[:12]: print('  ', round(z, 1), k, o, m)
