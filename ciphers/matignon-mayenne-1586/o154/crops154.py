#!/usr/bin/env python3
"""MAT-154 (15 Oct 2026): per-token 3x windows of the 47 f.154 `o` tokens (o154/tokens154.tsv), the osplit/o3x_crops.py recipe on the
levelled line strips of lines154.py: sign columns from the column ink profile (read-free), the token's column estimated
proportionally from its position in Bourdeau's line (line 1 shifted by 6: its first 6 tokens sit on the clear line above the strip),
window = estimate +- 4 columns, upscaled 3x, no marker. Writes OUT/<id>.jpg, OUT/context.tsv (labels p-4..p+4, target as [id]; labels
only, no values) and OUT/manifest154.tsv. Images go to OUT only (scratchpad; never committed).
Usage: python3 crops154.py LV_DIR OUT     (LV_DIR = lines154.py output)
"""
import csv, os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
LV, OUT = sys.argv[1:3]; os.makedirs(OUT, exist_ok=True)
SHIFT = {'f154-1': 6}

def columns(img):
    g = np.asarray(img, dtype=float); h = g.shape[0]
    band = g[int(h * 0.25):int(h * 0.75)]
    ink = (band < 140).sum(0).astype(float)
    ink = np.convolve(ink, np.ones(5) / 5, 'same')
    on = ink > max(1.0, 0.04 * band.shape[0])
    cols, x = [], 0
    while x < len(on):
        if on[x]:
            s = x
            while x < len(on) and on[x]: x += 1
            if x - s >= 8: cols.append([s, x])
        x += 1
    merged = []
    for c in cols:
        if merged and c[0] - merged[-1][1] < 6: merged[-1][1] = c[1]
        else: merged.append(c)
    return merged

lines = {}
for l in open(os.path.join(T, 'ciphertext.txt')):
    p = l.rstrip('\n').split('\t')
    if p[0].startswith('f154-'): lines[p[0]] = p[1].split()
toks = list(csv.DictReader(open(os.path.join(HERE, 'tokens154.tsv')), delimiter='\t'))
pos_id = {(t['line'], int(t['position'])): t['id'] for t in toks}
man = open(os.path.join(OUT, 'manifest154.tsv'), 'w'); man.write('id\tline\tposition\tn_tok\tn_cols\tcol\tx0\tx1\n')
ctx = open(os.path.join(OUT, 'context.tsv'), 'w'); ctx.write('id\tcontext\n')
cache = {}
for t in toks:
    ln, p = t['line'], int(t['position']); k = int(ln.split('-')[1])
    if k not in cache:
        img = Image.open(os.path.join(LV, 'lines', f'L{k:02d}.jpg')).convert('L'); cache[k] = (img, columns(img))
    img, cols = cache[k]
    sh = SHIFT.get(ln, 0); n = len(lines[ln]) - sh; q = p - sh
    c = min(len(cols) - 1, max(0, round((q - 0.5) / n * len(cols) - 0.5)))
    a, b = max(0, c - 4), min(len(cols) - 1, c + 4)
    x0, x1 = max(0, cols[a][0] - 10), min(img.width, cols[b][1] + 10)
    w = img.crop((x0, 0, x1, img.height)); w = w.resize((w.width * 3, w.height * 3), Image.LANCZOS)
    w.save(os.path.join(OUT, f"{t['id']}.jpg"), quality=92)
    man.write(f"{t['id']}\t{ln}\t{p}\t{n}\t{len(cols)}\t{c}\t{x0}\t{x1}\n")
    seq = []
    for j in range(p - 4, p + 5):
        if 1 + sh <= j <= len(lines[ln]):
            seq.append(f"[{t['id']}]" if j == p else lines[ln][j - 1])
    ctx.write(f"{t['id']}\t{' '.join(seq)}\n")
print(len(toks), 'crops')
