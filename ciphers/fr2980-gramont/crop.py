#!/usr/bin/env python3
"""Cut line crops (two halves per line) from the full-resolution IIIF regions of BnF fr.2980 f.29r, f.30r, f.30v.
Usage: crop.py SRC_DIR OUT_DIR. Full-resolution sources are re-fetchable from the IIIF regions in images/manifest.json.
Lines slope, so each half is located separately by a comb fit (first centre, pitch) to its ink projection."""
import sys, json, numpy as np
from PIL import Image
SRC, OUT = sys.argv[1], sys.argv[2]
# folio: (file, y range holding the cipher lines, pitch, n lines, x0, xsplit, x1), measured on 100 px grids
CFG = {'f29r': ('f29r_full.jpg', 2455, 4070, 115, 14, 280, 1940, 3600),
       'f30r': ('f30r_full.jpg', 585, 4520, 112, 35, 520, 2040, 3560),
       'f30v': ('f30v_full.jpg', 555, 2910, 117.6, 20, 1180, 2620, 4050)}
# pitch from the autocorrelation of the ink projection; line counts checked by eye on the page
def peaks(a, y0, y1, l, r, p, n):
    """Fit a comb (first centre c0, pitch q) to the ink projection of one half-page band; robust to slope and gaps."""
    sm = np.convolve((a[:, l:r] < 120).sum(1), np.ones(21) / 21, 'same')
    best = None
    for q in np.arange(p * .93, p * 1.07, .25):
        for c0 in range(y0, y0 + int(p * .6)):
            ys = (c0 + q * np.arange(n)).astype(int)
            if ys[-1] >= y1 + p * .5: continue
            sc = sm[ys].sum()
            if best is None or sc > best[0]: best = (sc, c0, q)
    _, c0, q = best
    out = []
    for i in range(n):  # then let each line settle on its own peak within a quarter pitch
        c = int(c0 + q * i); w = int(q * .25)
        out.append(c - w + int(np.argmax(sm[c - w:c + w])))
    return out
lines = {}
for fo, (fn, y0, y1, p, n, x0, xs, x1) in CFG.items():
    im = Image.open(f'{SRC}/{fn}').convert('L'); a = np.array(im).astype(float)
    halves = {'a': (x0, xs + 40), 'b': (xs - 40, x1)}
    comb = {h: peaks(a, y0, y1, l, r, p, n) for h, (l, r) in halves.items()}  # one comb fit per half
    for i in range(n):
        lid = f'{fo}_L{i+1:02d}'; rec = {}
        for h, (l, r) in halves.items():
            c = comb[h][i]; top, bot = c - int(p * .7), c + int(p * .62)
            im.crop((l, top, r, bot)).save(f'{OUT}/{lid}{h}.jpg', quality=82)
            rec[h] = [l, top, r, bot]
        lines[lid] = rec
json.dump(lines, open(f'{OUT}/crops.json', 'w'))
print(len(lines), 'lines')
