#!/usr/bin/env python3
"""VIV-MSORT (PREREG-VIV-MSORT.md): unsupervised k=2 sort of the 36 ink-40 sorter tiles, image features only.

    python3 tx/ksplit/msort.py --sort     # writes tx/ksplit/msort_frozen.tsv (reads no truth)
    python3 tx/ksplit/msort.py --score    # reads truth.tsv, writes tx/ksplit/msort.json

Report only: nothing here touches the sorter page or its labels.
"""
import csv, json, os, random, sys
import numpy as np
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__))
S = 32


def rows(p):
    return list(csv.DictReader(open(os.path.join(H, p)), delimiter='\t'))


def otsu(a):
    h = np.bincount(a.ravel(), minlength=256).astype(float); w = np.cumsum(h); m = np.cumsum(h * np.arange(256))
    t = w[-1]; best, th = -1, 128
    for i in range(255):
        if w[i] == 0 or w[i] == t:
            continue
        v = w[i] * (t - w[i]) * (m[i] / w[i] - (m[-1] - m[i]) / (t - w[i])) ** 2
        if v > best:
            best, th = v, i
    return th


def feat(i):
    a = 255 - np.asarray(Image.open(os.path.join(H, 'tiles', f'{i}.png')).convert('L'), dtype=np.uint8)
    ink = a > otsu(a)
    ys, xs = np.nonzero(ink)
    c = (a * ink)[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    hh, ww = c.shape; f = S / max(hh, ww)
    im = Image.fromarray(c.astype(np.uint8)).resize((max(1, round(ww * f)), max(1, round(hh * f))), Image.BILINEAR)
    cv = np.zeros((S, S)); y0 = (S - im.size[1]) // 2; x0 = (S - im.size[0]) // 2
    cv[y0:y0 + im.size[1], x0:x0 + im.size[0]] = np.asarray(im, dtype=float)
    p = np.pad(cv, 1); cv = sum(p[dy:dy + S, dx:dx + S] for dy in range(3) for dx in range(3)) / 9
    v = cv.ravel() - cv.mean()
    return v / np.linalg.norm(v)


def cluster(X, k=2):
    Xn = X / np.linalg.norm(X, axis=1, keepdims=True)
    D = 1 - Xn @ Xn.T
    cl = [[i] for i in range(len(X))]
    while len(cl) > k:
        best = None
        for a in range(len(cl)):
            for b in range(a + 1, len(cl)):
                d = D[np.ix_(cl[a], cl[b])].mean()
                if best is None or d < best[0] - 1e-12:
                    best = (d, a, b)
        _, a, b = best
        cl[a] += cl.pop(b)
    lab = [0] * len(X)
    for j, c in enumerate(sorted(cl, key=min)):
        for i in c:
            lab[i] = j
    return lab


def ari(x, y):
    from collections import Counter
    n = len(x); c2 = lambda m: m * (m - 1) / 2
    sij = sum(c2(v) for v in Counter(zip(x, y)).values()); a = sum(c2(v) for v in Counter(x).values())
    b = sum(c2(v) for v in Counter(y).values()); e = a * b / c2(n); mx = (a + b) / 2
    return 0.0 if mx == e else (sij - e) / (mx - e)


def purity(x, y):
    from collections import Counter
    return sum(max(Counter(t for s, t in zip(x, y) if s == c).values()) for c in set(x)) / len(x)


def p95(v):
    return sorted(v)[18]


def gated(lab, truth, X, tag):
    r = ari(lab, truth)
    n1 = []; n2 = []
    for i in range(20):
        t = truth[:]; random.Random(f'VIV-MSORT-{tag}-n1-{i}').shuffle(t); n1.append(ari(lab, t))
        g = np.random.default_rng([i, sum(map(ord, tag))])
        n2.append(ari(cluster(g.normal(size=X.shape)), truth))
    return dict(ari=round(r, 4), purity=round(purity(lab, truth), 4), n1_p95=round(p95(n1), 4), n2_p95=round(p95(n2), 4),
                pass_=r > p95(n1) and r > p95(n2), sizes=sorted([lab.count(0), lab.count(1)]))


def main():
    ids = [r['sid'] for r in rows('sorter/signs.tsv')]
    lab = {r['id']: r['label'] for r in rows('tiles.tsv')}
    if '--sort' in sys.argv:
        X = np.array([feat(i) for i in ids])
        trays = {'A': [i for i in ids if lab[i] == 'c'], 'B': [i for i in ids if lab[i] == '2'], 'P': ids}
        with open(os.path.join(H, 'msort_frozen.tsv'), 'w') as f:
            f.write('run\tid\tcluster\n')
            for run, sub in trays.items():
                for i, c in zip(sub, cluster(X[[ids.index(j) for j in sub]])):
                    f.write(f'{run}\t{i}\t{c}\n')
        return
    fr = rows('msort_frozen.tsv')
    tru = {r['id']: r['clerk_letter'] for r in rows('truth.tsv')}
    X = np.array([feat(i) for i in ids]); ix = {i: k for k, i in enumerate(ids)}
    out = {}
    A = [r for r in fr if r['run'] == 'A']
    out['A'] = gated([int(r['cluster']) for r in A], ['p' if tru[r['id']] == 'p' else 'eq' for r in A], X[[ix[r['id']] for r in A]], 'A')
    out['A']['table'] = {f"{c}": sorted(tru[r['id']] for r in A if r['cluster'] == c) for c in '01'}
    B = [r for r in fr if r['run'] == 'B']
    out['B'] = dict(truth=sorted(set(tru[r['id']] for r in B)), sizes=sorted([sum(r['cluster'] == c for r in B) for c in '01']),
                    verdict='not machine-testable at this material (one truth class)')
    P = [r for r in fr if r['run'] == 'P']
    out['P'] = gated([int(r['cluster']) for r in P], [lab[r['id']] for r in P], X[[ix[r['id']] for r in P]], 'P')
    # power at the target's N: 15 tiles, 12 of one label + 3 of the other, both ways round, 20 draws
    cs = [i for i in ids if lab[i] == 'c']; ts = [i for i in ids if lab[i] == '2']
    pw = []
    for d in range(20):
        rg = random.Random(f'VIV-MSORT-power-{d}')
        big, small = (ts, cs) if d % 2 == 0 else (cs, ts)
        sub = rg.sample(big, 12) + rg.sample(small, 3)
        Xs = X[[ix[i] for i in sub]]
        pw.append(gated(cluster(Xs), [lab[i] for i in sub], Xs, f'pw{d}')['pass_'])
    out['power'] = dict(passed=sum(pw), draws=20, share=sum(pw) / 20)
    ok = out['P']['pass_'] and out['power']['share'] >= 0.5
    out['decision'] = ('non-test at N=15 (positive control or power below gate)' if not ok else
                       'label c splits by shape into p vs e/q (machine lead, M)' if out['A']['pass_'] else
                       'no shape split of label c by this instrument (control-backed negative, this instrument only)')
    json.dump(out, open(os.path.join(H, 'msort.json'), 'w'), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    main()
