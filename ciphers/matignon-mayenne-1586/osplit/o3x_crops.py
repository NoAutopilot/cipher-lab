#!/usr/bin/env python3
"""MAT-O3X (15 Oct 2026): per-token 3x crops of the 78 f.91 `o` tokens of osplit/sort_tokens.tsv, for a blind re-sort.

Joins each cipher line's s1/s2 crops (regen_f91.sh / regen_f91c.sh / regen_f91e.sh output dirs) into one strip, finds sign columns
by the column ink profile (read-free), maps draft position p of n draft tokens to a sign column proportionally, and cuts a window of
the estimated column +- 4 columns, upscaled 3x, no marker (the estimate is often 1-3 columns off). The sorter finds the token from the
reader LABEL sequence of positions p-4..p+4 (labels only, no values), written to OUT/o3x_context.tsv.
Images go to OUT only (scratchpad; never committed). Writes OUT/o3x_manifest.tsv (id, strip, column, n_cols, n_tok, x0, x1).
Usage: python3 o3x_crops.py A_DIR C_DIR E_DIR OUT
"""
import csv, os, sys
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); F91 = os.path.join(HERE, '..', 'f91')
A, C, E, OUT = sys.argv[1:5]; os.makedirs(OUT, exist_ok=True)
PRE = {'A': 'f91r_ciA', 'B': 'f91r_ciB', 'D': 'f91v_ciD'}

def join(d, stem):
    import json
    man = {m['crop']: m for m in json.load(open(os.path.join(d, 'manifest.json')))['iiif_lines']}
    s1, s2 = f'{stem}_s1.jpg', f'{stem}_s2.jpg'
    if not os.path.exists(os.path.join(d, s2)):
        return Image.open(os.path.join(d, f'{stem}.jpg')).convert('L')
    a, b = Image.open(os.path.join(d, s1)).convert('L'), Image.open(os.path.join(d, s2)).convert('L')
    off = man[s2]['box'][0] - man[s1]['box'][0]
    h = min(a.height, b.height); out = Image.new('L', (off + b.width, h), 255)
    out.paste(a.crop((0, 0, a.width, h)), (0, 0)); out.paste(b.crop((0, 0, b.width, h)), (off, 0))
    return out

def strip(draft, line):
    b, n = line[0], int(line[1:])
    if draft == 'f91':
        if b == 'E': return join(os.path.join(A, 'crops'), f'f92r_ciE_L{n:02d}')
        return join(os.path.join(A, 'crops'), f'{PRE[b]}_L{n:02d}')
    if draft == 'f91c': return join(os.path.join(C, 'crops'), f'ci{b}_L{n:02d}')
    return Image.open(os.path.join(E, 'lines', f'E{n}.jpg')).convert('L')

def columns(img):
    g = np.asarray(img, dtype=float); h = g.shape[0]
    band = g[int(h * 0.2):int(h * 0.8)]              # middle band: the target line, not clipped neighbours
    ink = (band < 150).sum(0).astype(float)
    ink = np.convolve(ink, np.ones(5) / 5, 'same')
    on = ink > max(1.0, 0.04 * band.shape[0])
    cols, x = [], 0
    while x < len(on):
        if on[x]:
            s = x
            while x < len(on) and on[x]: x += 1
            if x - s >= 8: cols.append([s, x])
        x += 1
    merged = []                                      # join columns split by a gap < 6 px
    for c in cols:
        if merged and c[0] - merged[-1][1] < 6: merged[-1][1] = c[1]
        else: merged.append(c)
    return merged

ntok, lab = {}, {}
for i in ('f91', 'f91c', 'f91e'):
    for r in csv.DictReader(open(os.path.join(F91, f'ciphertext_draft_{i}.tsv')), delimiter='\t'):
        k = (i, r['line']); ntok[k] = max(ntok.get(k, 0), int(r['position']))
        lab[(i, r['line'], int(r['position']))] = r['sign'] if r['confidence'] == 'H' else '?'
ctx = []
rows = []
for r in csv.DictReader(open(os.path.join(HERE, 'sort_tokens.tsv')), delimiter='\t'):
    k = (r['draft'], r['line']); p = int(r['position']); n = ntok[k]
    im = strip(*k); cols = columns(im)
    j = min(len(cols) - 1, round((p - 0.5) / n * len(cols) - 0.5)) if cols else 0
    lo, hi = max(0, j - 4), min(len(cols) - 1, j + 4)
    x0, x1 = max(0, cols[lo][0] - 10), min(im.width, cols[hi][1] + 10)
    w = im.crop((x0, 0, x1, im.height)).resize(((x1 - x0) * 3, im.height * 3), Image.LANCZOS).convert('RGB')
    w.save(os.path.join(OUT, f"{r['id']}.jpg"), quality=90)
    ctx.append([r['id'], ' '.join('[' + r['id'] + ']' if q == p else lab.get((k[0], k[1], q), '')
                                   for q in range(max(1, p - 4), min(n, p + 4) + 1)).strip()])
    rows.append([r['id'], f'{k[0]}:{k[1]}', j + 1, len(cols), n, x0, x1])
with open(os.path.join(OUT, 'o3x_manifest.tsv'), 'w') as f:
    f.write('id\tstrip\tcolumn\tn_cols\tn_tok\tx0\tx1\n'); [f.write('\t'.join(map(str, x)) + '\n') for x in rows]
with open(os.path.join(OUT, 'o3x_context.tsv'), 'w') as f:
    f.write('id\tlabels\n'); [f.write('\t'.join(x) + '\n') for x in ctx]
print(len(rows), 'crops')
