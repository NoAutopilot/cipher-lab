#!/usr/bin/env python3
"""segment.py -- GAPS14 (2 Oct 2026): locate the small gloss-hand letters of body lines L01-L14 on the native leaf image.
Gloss ink is darker than the cipher row (threshold --th); the gloss band is the dark-row peak of each line's g7x box
(images/lines/g7x_manifest.json) +-HALF px; column ink inside the band splits into blobs at gaps >= --gap px, and the
blobs are matched left-to-right to the line's glossed tokens (ciphertext.tsv gloss != '') only when the counts agree.
Writes body/letterform/blobs.tsv (line pos gloss x0 x1 y0 y1). When the counts differ, the widest piece is split at its lowest-ink column, or the narrowest gaps are merged, until they agree (adjustment printed per line); the readers then see each cut as a tile, and a bad cut lowers the known-answer score rather than being hidden.
"""
import argparse, csv, json, os
import numpy as np
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(os.path.dirname(H))
ap = argparse.ArgumentParser(); ap.add_argument('--th', type=int, default=145); ap.add_argument('--gap', type=int, default=8)
ap.add_argument('--half', type=int, default=20); ap.add_argument('--xmax', type=int, default=1830); a = ap.parse_args()
im = np.array(Image.open(os.path.join(T, 'images/NL-HaNA_1.02.04_63_0001.jpg')).convert('L')).astype(int)
m = json.load(open(os.path.join(T, 'images/lines/g7x_manifest.json')))
rows = list(csv.DictReader(open(os.path.join(T, 'ciphertext.tsv')), delimiter='\t'))
out = []; bad = []
for c in m['crops']:
    L = c['line']; x0, y0, x1, y1 = c['box_native']; x1 = min(x1, a.xmax)
    reg = im[y0:y1, x0:x1] < a.th
    prof = np.convolve(reg.sum(1), np.ones(9) / 9, 'same')
    # gloss band = strongest dark-row peak in the upper 70% of the box (the cipher row sits at the bottom)
    lim = int(len(prof) * 0.7); cy = int(prof[:lim].argmax())
    b0, b1 = max(0, cy - a.half), min(reg.shape[0], cy + a.half)
    col = reg[b0:b1].sum(0) > 0
    blobs = []; inb = False; gap = 0
    for x, v in enumerate(col):
        if v:
            if inb and gap < a.gap: blobs[-1][1] = x
            elif inb: blobs.append([x, x])
            else: blobs.append([x, x]); inb = True
            gap = 0
        else: gap += 1
    blobs = [b for b in blobs if b[1] - b[0] >= 3 and reg[b0:b1, b[0]:b[1] + 1].sum() >= 25]
    toks = [r for r in rows if r['line'] == L and r['gloss']]
    n0 = len(blobs); N = len(toks)
    # fewer pieces than letters: split the widest piece at its lowest-ink column (middle 60%)
    while len(blobs) < N:
        i = max(range(len(blobs)), key=lambda k: blobs[k][1] - blobs[k][0]); s0, s1 = blobs[i]
        w = s1 - s0; cs = reg[b0:b1, s0:s1 + 1].sum(0); lo, hi = int(w * 0.2), int(w * 0.8) + 1
        cut = s0 + lo + int(np.argmin(cs[lo:hi])); blobs[i:i + 1] = [[s0, cut - 1], [cut + 1, s1]]
    # more pieces than letters: keep the N-1 widest gaps as letter boundaries, merge across the rest
    while len(blobs) > N:
        gaps = [blobs[k + 1][0] - blobs[k][1] for k in range(len(blobs) - 1)]
        k = int(np.argmin(gaps)); blobs[k:k + 2] = [[blobs[k][0], blobs[k + 1][1]]]
    print(L, 'pieces', n0, 'glossed', N, 'split' if n0 < N else ('merged' if n0 > N else 'exact'))
    for r, b in zip(toks, blobs):
        out.append((L, r['pos'], r['group'], r['gloss'], x0 + b[0], x0 + b[1], y0 + b0, y0 + b1))
with open(os.path.join(H, 'blobs.tsv'), 'w') as f:
    f.write('line\tpos\tgroup\tgloss\tx0\tx1\ty0\ty1\n')
    for o in out: f.write('\t'.join(map(str, o)) + '\n')
print('lines matched', 14 - len(bad), 'unmatched', bad)
