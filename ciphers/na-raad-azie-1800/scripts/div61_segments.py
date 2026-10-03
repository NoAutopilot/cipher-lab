#!/usr/bin/env python3
"""A2-RAA5 (3 Oct 2026): is cell 6/1 a word divider? Segment statistics of the 370 leaf-2 cells split at 61,
against 200 order shuffles (same line lengths) and 200 nl20 Dutch windows of 285 letters (word lengths).
Also writes data/div61/cells_no61.txt (61 removed, N=285). Run from the repo root."""
import gzip, glob, re, random, statistics, collections
D = 'ciphers/na-raad-azie-1800/'
lines = [l.split() for l in open(D + 'data/masc/cells_370.txt') if l.strip()]
open(D + 'data/div61/cells_no61.txt', 'w').write(
    '\n'.join(' '.join(t for t in l if t != '61') for l in lines) + '\n')
def per(ls):
    dd, S = 0, []
    for l in ls:
        s, c = [], 0
        for t in l:
            if t == '61': s.append(c); c = 0
            else: c += 1
        s.append(c); S += s[1:-1]  # interior segments only
        dd += sum(1 for a, b in zip(l, l[1:]) if a == b == '61')
    return dd, S
dd, S = per(lines)
nz = [x for x in S if x > 0]
print('target: 61-61', dd, 'segs', len(S), 'empty', S.count(0), 'one-cell', S.count(1),
      'mean nonzero %.2f' % statistics.mean(nz), 'max', max(S))
flat = [t for l in lines for t in l]; R = []
for seed in range(200):
    random.seed(seed); f = flat[:]; random.shuffle(f); it = iter(f)
    d, s = per([[next(it) for _ in l] for l in lines]); n = [x for x in s if x > 0]
    R.append((d, s.count(1), statistics.mean(n), max(s)))
for i, k in enumerate(['61-61', 'one-cell', 'mean', 'max']):
    v = sorted(r[i] for r in R); print('shuffle', k, 'p05', round(v[10], 2), 'med', round(v[100], 2), 'p95', round(v[190], 2))
txt = ''.join(gzip.open(f, 'rt', errors='ignore').read()[20000:220000] for f in sorted(glob.glob('tools/data/nl20/*.txt.gz')))
words = re.findall(r'[a-z]+', txt.lower().replace('ij', 'y')); R = []
for seed in range(200):
    random.seed(seed); i = random.randrange(len(words) - 200); w = []; n = 0
    while n < 285: w.append(len(words[i])); n += len(words[i]); i += 1
    R.append((len(w), statistics.mean(w), w.count(1), max(w)))
for i, k in enumerate(['nwords', 'mean', 'one-letter', 'max']):
    v = sorted(r[i] for r in R); print('dutch', k, 'p05', round(v[10], 2), 'med', round(v[100], 2), 'p95', round(v[190], 2))
