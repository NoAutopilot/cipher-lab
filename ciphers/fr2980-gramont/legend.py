#!/usr/bin/env python3
"""Build the sign legend from Lasry's published table for Gramont's cipher (1530) (cryptiana GL/BnF_fr3071_f17.png)
and Tomokiyo's reconstruction (francisGramont.png). Glyphs are located by connected components and assigned to a
column by the pixel x-centre of the column header, not by eye (LESSONS.md, Raince 1526). Writes legend.tsv
(code, source, bbox, letter by pixel column) and legend_sheet.png (neutral codes only, no letter values), which is
what the transcription passes see."""
import numpy as np, random
from PIL import Image, ImageDraw
from scipy import ndimage
R = '../../sources/cryptiana/web/'
im = Image.open(R + 'GL/BnF_fr3071_f17.png').convert('RGB'); a = np.array(im).astype(int)
blk = (a[..., 0] < 90) & (a[..., 1] < 90) & (a[..., 2] < 90)
lab, _ = ndimage.label(ndimage.binary_dilation(blk, iterations=3))
boxes = []
for s in ndimage.find_objects(lab):
    y0, y1, x0, x1 = s[0].start, s[0].stop, s[1].start, s[1].stop
    if y0 >= 75 and (y1 - y0) * (x1 - x0) >= 60: boxes.append([y0, y1, x0, x1])
# fold small fragments (dots, detached strokes) into the nearest larger box
big = [b for b in boxes if (b[1] - b[0]) * (b[3] - b[2]) > 150]
for f in [b for b in boxes if b not in big]:
    cy, cx = (f[0] + f[1]) / 2, (f[2] + f[3]) / 2
    t = min(big, key=lambda b: abs((b[0] + b[1]) / 2 - cy) + abs((b[2] + b[3]) / 2 - cx))
    t[:] = [min(t[0], f[0]), max(t[1], f[1]), min(t[2], f[2]), max(t[3], f[3])]
# header x-centres measured from the blue header letters (pixel columns)
HDR = dict(zip('A B C D E F G I L M N O P Q R S T V X'.split(),
               [19, 64, 108, 154, 199, 244, 288, 334, 380, 423, 469, 514, 559, 604, 650, 694, 738, 784, 829]))
def value(b):
    cy, cx = (b[0] + b[1]) / 2, (b[2] + b[3]) / 2
    if cy < 300: return min(HDR, key=lambda k: abs(HDR[k] - cx))
    if cy < 368: return min({'LL': 19, 'RR': 70, 'SS': 121}.items(), key=lambda kv: abs(kv[1] - cx))[0]
    if cy < 410: return 'COM' if cx < 60 else 'CON'
    return 'unknown(Lasry)'
# split boxes that hold two stacked glyphs (tall box with an empty row of pixels inside)
out = []
for b in big:
    sub = blk[b[0]:b[1], b[2]:b[3]].sum(1)
    gaps = [i for i in range(8, len(sub) - 8) if sub[i] == 0]
    if b[1] - b[0] > 45 and gaps:
        g = gaps[len(gaps) // 2]
        out += [[b[0], b[0] + g, b[2], b[3]], [b[0] + g, b[1], b[2], b[3]]]
    else: out.append(b)
big = out
rows = [('L', b, value(b), im.crop((b[2] - 3, b[0] - 3, b[3] + 3, b[1] + 3))) for b in big]
# Tomokiyo: nulls column and the bottom word-sign row (et?, roy, pape; con/com duplicate Lasry's)
t = Image.open(R + 'francisGramont.png').convert('RGBA'); bg = Image.new('RGBA', t.size, 'white'); t = Image.alpha_composite(bg, t).convert('RGB'); ta = np.array(t).astype(int)
tb = (ta[..., 0] < 150) & (ta[..., 1] < 150) & (ta[..., 2] < 150)  # dark ink only; the magenta header bars drop out
tlab, _ = ndimage.label(ndimage.binary_dilation(tb, iterations=3))
for s in ndimage.find_objects(tlab):
    y0, y1, x0, x1 = s[0].start, s[0].stop, s[1].start, s[1].stop
    cx = (x0 + x1) / 2
    if tb[y0:y1, x0:x1].sum() < 25: continue
    if 590 < cx < 635 and 30 < y0 < 200: v = 'null(Tomokiyo)'
    elif y0 > 212 and x1 < 390: v = {0: 'CON', 1: 'COM', 2: 'ET?', 3: 'ROY', 4: 'PAPE'}[int(np.argmin([abs(cx - c) for c in (60, 110, 170, 225, 330)]))]
    else: continue
    rows.append(('T', [y0, y1, x0, x1], v, t.crop((x0 - 3, y0 - 3, x1 + 3, y1 + 3))))
random.seed(1530); order = list(range(len(rows))); random.shuffle(order)
codes = {i: f'k{n+1:02d}' for n, i in enumerate(order)}
with open('legend.tsv', 'w') as f:
    f.write('code\tsource\tbbox_y0,y1,x0,x1\tvalue_by_pixel_column\n')
    for i in sorted(order, key=lambda i: codes[i]):
        src, b, v, _ = rows[i]
        f.write(f"{codes[i]}\t{'Lasry GL/BnF_fr3071_f17.png' if src == 'L' else 'Tomokiyo francisGramont.png'}\t{','.join(map(str, b))}\t{v}\n")
cell = 110; cols = 8; n = len(rows)
sheet = Image.new('RGB', (cols * cell, ((n + cols - 1) // cols) * cell), 'white'); d = ImageDraw.Draw(sheet)
for k, i in enumerate(sorted(order, key=lambda i: codes[i])):
    g = rows[i][3].convert('L'); sc = min(70 / g.height, 90 / g.width, 2.2)
    g = g.resize((max(1, int(g.width * sc)), max(1, int(g.height * sc))))
    x, y = (k % cols) * cell, (k // cols) * cell
    sheet.paste(g, (x + 10, y + 5)); d.text((x + 10, y + 88), codes[i], fill='red'); d.rectangle([x, y, x + cell - 1, y + cell - 1], outline='#bbb')
sheet.save('legend_sheet.png'); print(n, 'signs')
