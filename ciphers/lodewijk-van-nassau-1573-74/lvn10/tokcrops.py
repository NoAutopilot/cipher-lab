#!/usr/bin/env python3
"""R14-LVN10C (6 Oct 2026): per-token crops of WVO 4610 p3 for lvn10/PREREG_C.md. Usage:
  tokcrops.py PAGE300.png OUTDIR
PAGE300.png is `pdftoppm -png -r 300 -f 3 -l 3 04610.pdf` (sha1 a41b5df838e49cefb71e30cdfbe0803f3947d591). The 22 physical
lines are R12-LVN10's iiif_lines.py centres (region 120,1150,2350,1950). In each line band (centre -30..+26 px) every run of
inked columns (ink < 150, columns joined across gaps <= 12 px, x >= 250) is one token blob; comma/dot specks (width < 24 px and
< 500 ink px) are dropped. Each blob is cut with 8 px x-padding and its own vertical window (centre -48..+42), upscaled 1.5x,
and tiled in a fixed pseudo-random order (seed 4610) into contact sheets of 32 tiles (4 columns), each tile under a letters-only label
(AA, AB, ...). Writes OUTDIR/sheet_NN.png, OUTDIR/blobs.tsv (label, phys line, x0, x1, page order, sheet). No transcription
is read: blobs are cut from the image only, so a reader sees no transcription value. Offline."""
import sys, os, random, itertools, string
import numpy as np
from PIL import Image, ImageDraw
C = [26, 105, 197, 278, 348, 448, 534, 630, 713, 808, 891, 993, 1072, 1168, 1261, 1349, 1427, 1521, 1604, 1682, 1766, 1843]
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
img = Image.open(src).convert('L'); im = np.asarray(img).astype(int)
blobs = []
for i, c in enumerate(C):
    y = 1150 + c; ink = (im[y - 30:y + 26, 250:2470] < 150).sum(0)
    ss = []
    for x in np.where(ink >= 2)[0]:
        if ss and x - ss[-1][1] <= 12: ss[-1][1] = x
        else: ss.append([x, x])
    for a, b in ss:
        tot = int(ink[a:b + 1].sum())
        if tot < 60 or (b - a < 24 and tot < 500): continue
        blobs.append((i + 1, int(a) + 250, int(b) + 250, y))
from PIL import ImageFont
FONT = ImageFont.load_default(size=30)
labels = [''.join(p) for p in itertools.product(string.ascii_uppercase, repeat=2)]
order = list(range(len(blobs))); random.Random(4610).shuffle(order)
PER, COLS = 32, 4
tiles = []
for k, bi in enumerate(order):
    L, x0, x1, y = blobs[bi]
    t = img.crop((x0 - 8, y - 48, x1 + 9, y + 42)); t = t.resize((int(t.width * 1.5), int(t.height * 1.5)))
    tiles.append((labels[k], bi, t))
rows = []
for s in range(0, len(tiles), PER):
    grp = tiles[s:s + PER]; TW = 540; TH = 185
    nrow = (len(grp) + COLS - 1) // COLS
    sh = Image.new('L', (COLS * TW, nrow * TH), 255); d = ImageDraw.Draw(sh)
    for j, (lab, bi, t) in enumerate(grp):
        cx, cy = (j % COLS) * TW, (j // COLS) * TH
        d.rectangle((cx, cy, cx + TW - 1, cy + TH - 1), outline=0)
        d.text((cx + 6, cy + 2), 'tile ' + lab, fill=0, font=FONT)
        tt = t if t.width <= TW - 12 else t.crop((0, 0, TW - 12, t.height))
        sh.paste(tt, (cx + 6, cy + 40))
        rows.append((lab, bi, s // PER + 1, t.width > TW - 12))
    sh.save(os.path.join(out, 'sheet_%02d.png' % (s // PER + 1)))
with open(os.path.join(out, 'blobs.tsv'), 'w') as f:
    f.write('label\tphys\tx0\tx1\tpage_order\tsheet\ttruncated\n')
    for lab, bi, sh, tr in rows:
        L, x0, x1, y = blobs[bi]; f.write(f'{lab}\t{L}\t{x0}\t{x1}\t{bi}\t{sh}\t{int(tr)}\n')
print(len(blobs), 'blobs,', (len(tiles) + PER - 1) // PER, 'sheets;', sum(r[3] for r in rows), 'tiles truncated at the sheet width')
