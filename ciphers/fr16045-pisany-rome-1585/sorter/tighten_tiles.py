#!/usr/bin/env python3
"""Tighten the f.75 sorter tiles to the sign's own ink (owner, 4 Oct 2026: the tiles were tall, thin strips carrying the
lines above and below, so the sign showed tiny).

    python3 ciphers/fr16045-pisany-rome-1585/sorter/tighten_tiles.py      (reads signs.tsv + pages/, writes signs_tight.tsv)

Per tile, inside its original box: ink = pixels darker than the page's own threshold (Otsu on the strip); rows with ink
are grouped into vertical runs split by gaps of >= GAP blank rows; the run with the most ink is the sign (a tall letter
such as a long s is one run, a stray stroke from the line above is a separate, smaller run). The box is cut to that run's
rows and the columns that carry ink in it, plus MARGIN px, never larger than the original box. Tiles with no clear run
keep their original box. Labels, ids and order are unchanged, so labels.tsv and focus.tsv stay valid."""
import csv
from pathlib import Path
from PIL import Image
import numpy as np
H = Path(__file__).resolve().parent
GAP, MARGIN, MINH = 4, 6, 14

def otsu(a):
    hist = np.bincount(a.ravel(), minlength=256).astype(float); tot = a.size; s = np.dot(np.arange(256), hist)
    wb = sb = 0; best = (0, 128)
    for t in range(256):
        wb += hist[t]; sb += t * hist[t]
        if wb == 0 or wb == tot: continue
        mb, mf = sb / wb, (s - sb) / (tot - wb); v = wb * (tot - wb) * (mb - mf) ** 2
        if v > best[0]: best = (v, t)
    return best[1]

def runs(mask):
    out, start, gap = [], None, 0
    for i, on in enumerate(mask):
        if on:
            if start is None: start = i
            gap = 0; end = i
        elif start is not None:
            gap += 1
            if gap >= GAP: out.append((start, end)); start = None
    if start is not None: out.append((start, end))
    return out

rows = list(csv.DictReader(open(H / 'signs.tsv'), delimiter='\t'))
pages, thr, changed = {}, {}, 0
for r in rows:
    p = r['page']
    if p not in pages:
        pages[p] = np.array(Image.open(H / 'pages' / f'{p}.jpg').convert('L')); thr[p] = otsu(pages[p])
    a = pages[p]; x, y, w, h = (int(r[k]) for k in ('x', 'y', 'w', 'h'))
    t = a[y:y + h, x:x + w] < thr[p]
    rr = runs(t.sum(1) >= 2)
    if not rr: continue
    s, e = max(rr, key=lambda q: t[q[0]:q[1] + 1].sum())
    if e - s + 1 < MINH and len(rr) == 1 and h <= MINH * 2: continue
    cols = np.where(t[s:e + 1].sum(0) >= 1)[0]
    if not len(cols): continue
    nx0, nx1 = max(0, cols[0] - MARGIN), min(w, cols[-1] + 1 + MARGIN)
    ny0, ny1 = max(0, s - MARGIN), min(h, e + 1 + MARGIN)
    new = (x + nx0, y + ny0, nx1 - nx0, ny1 - ny0)
    if new != (x, y, w, h): changed += 1
    r['x'], r['y'], r['w'], r['h'] = map(str, new)
with open(H / 'signs_tight.tsv', 'w', newline='') as f:
    wr = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter='\t', lineterminator='\n'); wr.writeheader(); wr.writerows(rows)
print('tiles', len(rows), 'tightened', changed)
