#!/usr/bin/env python3
"""R7-MATSORT (6 Oct 2026): sign-sorter inputs for fr.15572 f.110 lines 1-6 (Gallica btv1b9061879d canvas 116), built the
same way as ../../birago-fr3252-1571-72/sorter/build_inputs.py, from the line crops D2B-MATF110 already cut
(images/f110/, manifest.json; no network).

Pages: each image line is its two overlapping crops (s1 x 4780-7180, s2 x 5710-8110 in canvas pixels) joined into one
3330 px strip, sorter/pages/f110_L<nn>.jpg. Strips are only ~52 px tall (the native band), so a tall sign can be cut at
the top or bottom; the sorter's context view shows the neighbouring strips.
Tiles: a column ink profile over the strip splits it into blobs, fitted to the matched ciphertext.txt line's token count
by merging the narrowest blob into its nearer neighbour or halving the widest (Birago's fit()); per line the
profile setting (gap, min width, ink threshold) is the one whose blob count is the smallest at or above the token count
(fit.tsv), so the fit merges rather than halves. Image lines map to
ciphertext lines as f110crops/score.json found for both passes: L01 -> f110-1, L02 -> f110-2, L04 -> f110-3,
L05 -> f110-4, L06 -> f110-5. Image line L03 straddles two rows and matches no line: its blobs are cut unfitted into pile
L03-unplaced. Boxes are APPROXIMATE (one position off where signs touch); a bad cut goes to BAD-CUT, not a pile.
Labels: pile = the ciphertext.txt shape label (Bourdeau's transcription) at that position, family = the same. No sign
values or plaintext appear in sorter/.
focus.tsv: every tile whose label is one of BOX, z, T, U, w, 4 (the labels D2B-MATF110's two blind passes split on or kept
apart from keyed shapes), with what pass A and pass B wrote at that position (f110crops/pass*_L*.tsv, aligned by the same
edit-distance alignment as f110crops/score.py).

  python3 sorter/build_inputs.py      (from ciphers/matignon-mayenne-1586; needs pillow, numpy)
"""
import csv, glob, json
from pathlib import Path
from PIL import Image
import numpy as np
T = Path(__file__).resolve().parents[1]; IM = T / 'images' / 'f110'; S = T / 'sorter'; P = S / 'pages'
P.mkdir(exist_ok=True)
LINEMAP = {1: 1, 2: 2, 4: 3, 5: 4, 6: 5}          # image line -> f110-N (f110crops/score.json, both passes)
FOCUS = ['BOX', 'z', 'T', 'U', 'w', '4']


def strip(band):
    es = sorted([e for e in json.load(open(IM / 'manifest.json'))['iiif_lines'] if e['band'] == band], key=lambda e: e['segment'])
    a, b = (Image.open(IM / e['crop']).convert('L') for e in es)
    off = es[1]['box'][0] - es[0]['box'][0]
    out = Image.new('L', (off + b.width, max(a.height, b.height)), 255)
    out.paste(b, (off, 0)); out.paste(a, (0, 0))
    return out


def blobs(im, gap=3, minw=6, thr=120):
    a = np.array(im); ink = a < thr
    col = ink.sum(0) > 1
    segs, s, last = [], None, -99
    for x, v in enumerate(col):
        if v:
            s = x if s is None else s; last = x
        elif s is not None and x - last > gap:
            segs.append([s, last]); s = None
    if s is not None:
        segs.append([s, last])
    return [g for g in segs if g[1] - g[0] >= minw]


def fit(segs, n):
    segs = [list(g) for g in segs]
    while len(segs) > n:
        i = min(range(len(segs)), key=lambda k: segs[k][1] - segs[k][0])
        if i == 0: j = 1
        elif i == len(segs) - 1: j = i - 1
        else: j = i - 1 if segs[i][0] - segs[i - 1][1] < segs[i + 1][0] - segs[i][1] else i + 1
        a, b = sorted((i, j)); segs[a] = [segs[a][0], segs[b][1]]; del segs[b]
    while len(segs) < n:
        i = max(range(len(segs)), key=lambda k: segs[k][1] - segs[k][0]); a, b = segs[i]; m = (a + b) // 2
        segs[i:i + 1] = [[a, m], [m + 1, b]]
    return segs


def nw(a, b):   # f110crops/score.py's alignment
    n, m = len(a), len(b); D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): D[i][0] = i
    for j in range(m + 1): D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + (a[i - 1] != b[j - 1]))
    i, j, pairs = n, m, {}
    while i > 0 and j > 0:
        if D[i][j] == D[i - 1][j - 1] + (a[i - 1] != b[j - 1]): pairs[i - 1] = j - 1; i -= 1; j -= 1
        elif D[i][j] == D[i - 1][j] + 1: i -= 1
        else: j -= 1
    return pairs


bour = {}
for l in open(T / 'ciphertext.txt'):
    p = l.rstrip('\n').split('\t')
    if p[0].startswith('f110-'): bour[int(p[0][5:])] = p[1].split()
passes = {}
for k in 'AB':
    d = {}
    for f in sorted(glob.glob(str(T / 'f110crops' / f'pass{k}_L*.tsv'))):
        for l in open(f).read().splitlines()[1:]:
            p = l.split('\t')
            if len(p) >= 2 and p[0].strip().isdigit(): d[int(p[0])] = p[1].split()
    passes[k] = d

signs, labels, focus, fitlog = [], [], [], []
for band in range(1, 7):
    page = f'f110_L{band:02d}'; im = strip(band); im.save(P / f'{page}.jpg', quality=85)
    bl = blobs(im); a = np.array(im)
    if band in LINEMAP:
        toks = bour[LINEMAP[band]]
        # per line, the profile setting whose blob count is the smallest at or above the token count, so the fit only
        # merges (splitting a blob in half is the worse error); falls back to the largest count if none reaches it
        opts = [blobs(im, gap=g, minw=w, thr=t) for g in (1, 2, 3) for w in (4, 6) for t in (120, 150)]
        ok = [o for o in opts if len(o) >= len(toks)]
        bl = min(ok, key=len) if ok else max(opts, key=len); boxes = fit(bl, len(toks))
        al = {k: nw(toks, passes[k].get(band, [])) for k in 'AB'}
    else:
        toks = ['L03-unplaced'] * len(bl); boxes = bl; al = {'A': {}, 'B': {}}
    fitlog.append((page, LINEMAP.get(band, '-'), len(bl), len(boxes)))
    for i, (x0, x1) in enumerate(boxes):
        sid = f'{page}_{i + 1:02d}'
        ys = np.where((a[:, x0:x1 + 1] < 120).sum(1) > 0)[0]
        y0, y1 = (int(ys.min()), int(ys.max())) if len(ys) else (0, im.height - 1)
        signs.append(dict(sid=sid, page=page, x=x0, y=y0, w=x1 - x0 + 1, h=y1 - y0 + 1))
        labels.append(dict(sid=sid, sign=toks[i], family=toks[i]))
        if toks[i] in FOCUS:
            ra = passes['A'][band][al['A'][i]] if i in al['A'] else '-'
            rb = passes['B'][band][al['B'][i]] if i in al['B'] else '-'
            focus.append((sid, f'f110-{LINEMAP[band]}.{i + 1}: transcription {toks[i]}, blind pass A {ra}, pass B {rb}; '
                               f'is this {toks[i]}, a variant of a keyed sign, or another sign?'))
for name, rs in (('signs.tsv', signs), ('labels.tsv', labels)):
    with open(S / name, 'w', newline='') as o:
        w = csv.DictWriter(o, fieldnames=list(rs[0]), delimiter='\t'); w.writeheader(); w.writerows(rs)
with open(S / 'focus.tsv', 'w') as o:
    for sid, q in focus: o.write(f'{sid}\t{q}\n')
with open(S / 'fit.tsv', 'w') as o:
    o.write('page\tline\tblobs\ttiles\n')
    for r in fitlog: o.write('\t'.join(map(str, r)) + '\n')
print(len(signs), 'signs;', len(focus), 'focus tiles;', len(set(l['sign'] for l in labels)), 'piles;', fitlog)
