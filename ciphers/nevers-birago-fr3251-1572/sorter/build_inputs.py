#!/usr/bin/env python3
"""NEVBIR-LOOKALIKE step 4 (2 Oct 2026): sign-sorter inputs for the two short 1572 runs, no.73 f.144r and no.85 f.168.

Pages are the cipher lines cut from the public Gallica region images already on disk (harvest/<leaf>/src_*.jpg, boxes
from harvest/<leaf>/manifest.json), one strip per line, written to sorter/pages/<leaf>_L<band>.jpg. Sign boxes are
APPROXIMATE: a column ink profile splits each strip into blobs, the passage's signs are taken from the side the
cipher is anchored to (prose before or after it on the same line), and the blob list is fitted to the passage's sign
count by merging the narrowest blob into its nearer neighbour, or halving the widest blob. Where two signs touch or
one sign is in two pieces a tile can be one position off; the sorter's context view shows the line, and focus.tsv
names passage and position so the person can check. Labels come from harvest/lookalike/<run>_passD.tsv (the
reconciled sequence after the look-alike pass). No values are written anywhere in sorter/.

  python3 sorter/build_inputs.py      (writes sorter/signs.tsv, labels.tsv, focus.tsv, pages/)
"""
import csv, json
from pathlib import Path
from PIL import Image
import numpy as np
T = Path(__file__).resolve().parents[1]; H = T / 'harvest'; S = T / 'sorter'; P = S / 'pages'
P.mkdir(exist_ok=True)
# passage -> (crop folder, band, anchor, prefix) ; anchor 'L' = signs from the left end, 'R' = from the right end, 'W' = whole line
LAYOUT = {'f144r': {'L03': ('f144r', 3, 'R'), 'L04.1': ('f144r', 4, 'L'), 'L04.2': ('f144r', 4, 'R'),
                    'L05': ('f144r', 5, 'W'), 'L06': ('f144r', 6, 'L')},
          'f168': {'R02': ('f168r', 2, 'W'), 'R03': ('f168r', 3, 'L'), 'V01': ('f168v', 1, 'R'),
                   'V02': ('f168v', 2, 'W'), 'V03': ('f168v', 3, 'L')}}


def strip(leaf, band):
    m = json.load(open(H / leaf / 'manifest.json'))['iiif_lines']
    es = [e for e in m if e['band'] == band]
    url = es[0]['source_url']; ox, oy = (int(v) for v in url.split('/full/')[0].split('/')[-1].split(',')[:2])
    x0 = min(e['box'][0] for e in es); y0 = min(e['box'][1] for e in es)
    x1 = max(e['box'][2] for e in es); y1 = max(e['box'][3] for e in es)
    return Image.open(H / leaf / es[0]['source_file']).crop((x0 - ox, y0 - oy, x1 - ox, y1 - oy))


def blobs(im, gap=4, minw=8, thr=120):
    a = np.array(im.convert('L')); h = a.shape[0]
    mid = a[int(h * .15):int(h * .85)] < thr
    col = (mid.sum(0) > 1) & (mid.mean(0) < .6)   # the second test drops the dark scan edge at the page border
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


signs, labels, focus = [], [], []
for run, lay in LAYOUT.items():
    seq = list(csv.DictReader(open(H / 'lookalike' / f'{run}_passD.tsv'), delimiter='\t'))
    by = {}
    for r in seq:
        by.setdefault(r['passage'], []).append(r)
    done = {}
    for psg, rows in by.items():
        leaf, band, anc = lay[psg]; page = f'{leaf}_L{band:02d}'
        if page not in done:
            im = strip(leaf, band); im.save(P / f'{page}.jpg', quality=85); done[page] = (im, blobs(im))
        im, bl = done[page]
        n = len(rows)
        if anc == 'W':      # the whole line is cipher: fit every blob to the sign count
            boxes = fit(bl, n)
        else:               # prose on the far side: drop fragments, take n blobs from the anchored side
            big = [g for g in bl if g[1] - g[0] >= 15]
            boxes = big[:n] if anc == 'L' else big[-n:]
        for r, (x0, x1) in zip(rows, boxes):
            sid = f"{run}_{psg}_{int(r['pos']):02d}"
            a = np.array(im.convert('L').crop((x0, 0, x1 + 1, im.height)))
            ys = np.where((a < 120).sum(1) > 0)[0]
            y0, y1 = (int(ys.min()), int(ys.max())) if len(ys) else (0, im.height - 1)
            signs.append(dict(sid=sid, page=page, x=x0, y=y0, w=x1 - x0 + 1, h=y1 - y0 + 1))
            lab = r['sign_id'] if r['sign_id'] not in ('', '?') else 'UNREAD'
            labels.append(dict(sid=sid, sign=lab, family=lab))
            if r.get('question'):
                focus.append((sid, r['question']))
for name, rows in (('signs.tsv', signs), ('labels.tsv', labels)):
    with open(S / name, 'w', newline='') as o:
        w = csv.DictWriter(o, fieldnames=list(rows[0]), delimiter='\t'); w.writeheader(); w.writerows(rows)
with open(S / 'focus.tsv', 'w') as o:
    for sid, q in focus:
        o.write(f'{sid}\t{q}\n')
print(len(signs), 'signs;', len(set(s['page'] for s in signs)), 'pages;', len(focus), 'focus tiles')
