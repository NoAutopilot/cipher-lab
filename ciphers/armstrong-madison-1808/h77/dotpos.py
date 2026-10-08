"""H77 dot-position statistic (PREREGISTRATION.md). Usage: python3 h77/dotpos.py  (control, then target only if gate passes)."""
import glob, json, random, sys
import numpy as np
from PIL import Image
from collections import deque

def threshold_otsu(g):
    h, e = np.histogram(g, bins=256, range=(0, 256)); h = h.astype(float); c = (e[:-1] + e[1:]) / 2
    w0 = np.cumsum(h); w1 = w0[-1] - w0; m0 = np.cumsum(h * c); mt = m0[-1]
    with np.errstate(divide='ignore', invalid='ignore'):
        v = (mt * w0 - m0 * w0[-1]) ** 2 / (w0 * w1)
    return c[np.nanargmax(v)]

def components(ink):  # 8-connected; returns (top, left, h, w, area)
    H, W = ink.shape; seen = np.zeros_like(ink, bool); out = []
    for y, x in zip(*np.nonzero(ink)):
        if seen[y, x]: continue
        q = deque([(y, x)]); seen[y, x] = True; ys = []; xs = []
        while q:
            a, b = q.popleft(); ys.append(a); xs.append(b)
            for da in (-1, 0, 1):
                for db in (-1, 0, 1):
                    u, v = a + da, b + db
                    if 0 <= u < H and 0 <= v < W and ink[u, v] and not seen[u, v]:
                        seen[u, v] = True; q.append((u, v))
        out.append((min(ys), min(xs), max(ys) - min(ys) + 1, max(xs) - min(xs) + 1, len(ys)))
    return out

def feats(path):
    g = np.asarray(Image.open(path).convert('L'), dtype=float)
    ink = g < threshold_otsu(g)
    comps = [c for c in components(ink) if c[4] >= 3]
    if not comps: return [], 0, 0
    med = float(np.median([c[4] for c in comps]))
    dots = [c for c in comps if c[4] < 0.15 * med and max(c[2], c[3]) / max(1, min(c[2], c[3])) < 2.5]
    strokes = [c for c in comps if c[4] >= 0.5 * med]
    if not strokes: return [], len(dots), 0
    mh = float(np.median([s[2] for s in strokes]))
    cells = []
    for d in dots:
        cy, cx = d[0] + d[2] / 2, d[1] + d[3] / 2
        best = None
        for s in strokes:
            sy, sx = s[0] + s[2] / 2, s[1] + s[3] / 2
            dist = ((cy - sy) ** 2 + (cx - sx) ** 2) ** .5
            if best is None or dist < best[0]: best = (dist, s)
        if best[0] > 3 * mh: continue
        s = best[1]
        top, bot = s[0], s[0] + s[2]
        v = 0 if cy < top + 0.25 * s[2] else (2 if cy > bot - 0.25 * s[2] else 1)
        rel = (cx - s[1]) / max(1, s[3]); hc = 0 if rel < 1 / 3 else (2 if rel > 2 / 3 else 1)
        cells.append(v * 3 + hc)
    return cells, len(dots), len(strokes)

def hist(cells):
    h = np.bincount(cells, minlength=9).astype(float) + 0.5
    return h / h.sum()

def jsd(p, q):
    m = (p + q) / 2
    kl = lambda a, b: float((a * np.log2(a / b)).sum())
    return (kl(p, m) + kl(q, m)) / 2

def stat(lines):  # lines: dict name -> (system, half, cells)
    pool = {}
    for sysn, half, c in lines.values(): pool.setdefault((sysn, half), []).extend(c)
    H = {k: hist(v) for k, v in pool.items()}
    within = (jsd(H['M', 'A'], H['M', 'B']) + jsd(H['B', 'A'], H['B', 'B'])) / 2
    cross = np.mean([jsd(H['M', a], H['B', b]) for a in 'AB' for b in 'AB'])
    return cross, within

lines, out = {}, {}
for sysn, pat in (('M', 'h24/specimens/mavor_plateV_line%d.jpg'), ('B', 'h24/specimens/byrom_plateI_line%d.jpg')):
    for i in range(1, 5):
        c, nd, ns = feats(pat % i)
        lines['%s%d' % (sysn, i)] = (sysn, 'A' if i <= 2 else 'B', c)
        out['%s%d' % (sysn, i)] = {'dots_used': len(c), 'dots': nd, 'strokes': ns}
cross, within = stat(lines)
obs = cross - within
rng = random.Random(20261008); ge = 0
names = list(lines)
for _ in range(2000):
    labs = [lines[n][0] for n in names]; rng.shuffle(labs)
    perm = {}
    for n, l in zip(names, labs):
        # keep half membership by line order within the permuted system
        perm[n] = [l, None, lines[n][2]]
    for s in 'MB':
        ms = [n for n in names if perm[n][0] == s]
        for j, n in enumerate(ms): perm[n][1] = 'A' if j < 2 else 'B'
    c2, w2 = stat({k: tuple(v) for k, v in perm.items()})
    ge += (c2 - w2) >= obs
p = (ge + 1) / 2001
nM = sum(len(lines[n][2]) for n in names if n[0] == 'M'); nB = sum(len(lines[n][2]) for n in names if n[0] == 'B')
gate = cross > within and p <= 0.01 and nM >= 40 and nB >= 40
res = {'control': {'cross': cross, 'within': within, 'perm_p': p, 'dots_mavor': nM, 'dots_byrom': nB, 'gate': gate, 'lines': out}}
if gate:
    HM = hist([x for n in names if n[0] == 'M' for x in lines[n][2]]); HB = hist([x for n in names if n[0] == 'B' for x in lines[n][2]])
    tl = [feats(p)[0] for p in sorted(glob.glob('images/shorthand/page*_L*.jpg'))]
    tl = [c for c in tl if c]
    allc = [x for c in tl for x in c]; HT = hist(allc)
    boots = []
    r2 = random.Random(1)
    for _ in range(1000):
        s = [x for c in (r2.choice(tl) for _ in tl) for x in c]; h = hist(s); boots.append((jsd(h, HM), jsd(h, HB)))
    b = np.array(boots)
    res['target'] = {'lines': len(tl), 'dots': len(allc), 'jsd_mavor': jsd(HT, HM), 'jsd_byrom': jsd(HT, HB),
                     'ci_mavor': list(np.percentile(b[:, 0], [2.5, 97.5])), 'ci_byrom': list(np.percentile(b[:, 1], [2.5, 97.5]))}
json.dump(res, open('h77/results.json', 'w'), indent=1, default=float)
print(json.dumps(res, indent=1, default=float))
