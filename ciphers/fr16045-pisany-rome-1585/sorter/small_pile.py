#!/usr/bin/env python3
"""Put the f.75 sorter's tiny tiles in one pile, SMALL (owner, 4 Oct 2026: "they need to be efficient").

    python3 ciphers/fr16045-pisany-rome-1585/sorter/small_pile.py     (reads signs.tsv, labels.tsv, pages/; writes labels_small.tsv)

A tile is small when it is under 18 px tall or carries under 60 ink pixels (ink = darker than the strip's 8th percentile
+ 20). On the 4 Oct v3 cut that is 99 of 1,290 tiles: mostly dots and specks, about ten real signs (thin strokes, a few
small letters), checked by eye on a montage. They are not dropped: the owner pulls the real ones out of SMALL and marks
the rest "Not a letter" in one go. Every other tile keeps its label."""
import csv
from pathlib import Path
import numpy as np
from PIL import Image
H = Path(__file__).resolve().parent
rows = list(csv.DictReader(open(H / 'signs.tsv'), delimiter='\t')); pages = {}; small = set()
for r in rows:
    p = pages.setdefault(r['page'], np.array(Image.open(H / 'pages' / f"{r['page']}.jpg").convert('L')))
    x, y, w, h = (int(r[k]) for k in ('x', 'y', 'w', 'h')); thr = np.percentile(p, 8) + 20
    if h < 18 or int((p[y:y + h, x:x + w] < thr).sum()) < 60: small.add(r['sid'])
lab = list(csv.DictReader(open(H / 'labels.tsv'), delimiter='\t'))
for r in lab:
    if r['sid'] in small: r['sign'], r['family'] = 'SMALL', 'SMALL'
with open(H / 'labels_small.tsv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(lab[0].keys()), delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(lab)
print('small tiles', len(small), 'of', len(rows))
