#!/usr/bin/env python3
"""R14-LVN10C (6 Oct 2026): per-token crops of WVO 4610 p3 for lvn10/PREREG_C.md. Usage:
  tokcrops.py PAGE300.png OUTDIR
PAGE300.png is `pdftoppm -png -r 300 -f 3 -l 3 04610.pdf` (sha1 a41b5df838e49cefb71e30cdfbe0803f3947d591). The 22 physical
lines are R12-LVN10's iiif_lines.py centres (region 120,1150,2350,1950). In each line band (centre -30..+26 px) every run of
inked columns (ink < 150, columns joined across gaps <= 12 px, x >= 250) is one token blob; comma/dot specks (width < 24 px and
< 500 ink px) are dropped. Each blob is cut with 8 px x-padding and its own vertical window (centre -48..+42), upscaled 1.5x,
and tiled in a fixed pseudo-random order (seed 4610) into contact sheets of 32 tiles (4 columns), each tile under a letters-only label
(AA, AB, ...). Writes OUTDIR/sheet_NN.png, OUTDIR/blobs.tsv (label, phys line, x0, x1, page order, sheet). No transcription
is read: blobs are cut from the image only, so a reader sees no transcription value. Offline.
--repair (R14-LVN10D, 6 Oct 2026, lvn10/PREREG_D.md): the speck filter above dropped tall narrow digits (a hooked '1', a
narrow '8'/'9'), so leading digits went missing; with --repair a narrow blob is dropped only if it is shorter than 20 px or
its top sits more than 9 px below the local x-height top (median top of wide blobs within 250 px), and kept blobs <= 16 px
apart are joined (any width) when no dropped speck lies between. Wide tiles get a 2-column sheet so none is truncated. Shuffle seed 4611 (fresh order for fresh reads)."""
import sys, os, random, itertools, string
import numpy as np
from PIL import Image, ImageDraw
C = [26, 105, 197, 278, 348, 448, 534, 630, 713, 808, 891, 993, 1072, 1168, 1261, 1349, 1427, 1521, 1604, 1682, 1766, 1843]
REPAIR = '--repair' in sys.argv; sys.argv = [a for a in sys.argv if a != '--repair']
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
img = Image.open(src).convert('L'); im = np.asarray(img).astype(int)
blobs = []
def track(i):
    """--repair: the written lines slope (up to ~90 px lower at the right than at the left on p3), so a fixed band cuts the
    left half of a line from the line below/above. Track the line's ink centre from the right margin leftwards in 120 px
    windows (search +-25 px around the running estimate, gain 0.7), fit a quadratic, return the centre y for every column."""
    bw = (im < 150).astype(int); y0 = 1150 + C[i]; est = y0; pts = []
    for xr in range(2470, 250, -120):
        xl = max(250, xr - 120); prof = bw[est - 40:est + 40, xl:xr].sum(1).astype(float)
        if prof.sum() < 150: continue
        k = np.convolve(prof, np.ones(15) / 15, 'same')[15:-15]
        est = est + int(round((int(np.argmax(k)) - 25) * 0.7)); pts.append(((xl + xr) / 2, est))
    p = np.polyfit([a for a, _ in pts], [b for _, b in pts], 2)
    return np.round(np.polyval(p, np.arange(250, 2470))).astype(int)
YC = {}
def band(i):
    if not REPAIR: y = 1150 + C[i]; return im[y - 30:y + 26, 250:2470] < 150
    if i not in YC: YC[i] = track(i)
    return np.stack([im[yc - 30:yc + 26, 250 + x] for x, yc in enumerate(YC[i])], 1) < 150
for i, c in enumerate(C):
    y = 1150 + c; ink = band(i).sum(0)
    ss = []
    for x in np.where(ink >= 2)[0]:
        if ss and x - ss[-1][1] <= 12: ss[-1][1] = x
        else: ss.append([x, x])
    if not REPAIR:
        for a, b in ss:
            tot = int(ink[a:b + 1].sum())
            if tot < 60 or (b - a < 24 and tot < 500): continue
            blobs.append((i + 1, int(a) + 250, int(b) + 250, y))
        continue
    # --repair (R14-LVN10D): a narrow blob is a speck (comma/dot) only if it is short or sits low against the local
    # x-height; a tall narrow blob whose top reaches the local top (a hooked '1', a narrow '8' or '9') is kept, then
    # joined to the next kept blob when <= 16 px apart and no speck lies between them.
    seg = []
    for a, b in ss:
        tot = int(ink[a:b + 1].sum()); r = np.where(band(i)[:, a:b + 1].sum(1) > 0)[0]
        seg.append([int(a), int(b), tot, int(r[0]) - 30, int(r[-1]) - 30])
    wide = [s for s in seg if s[1] - s[0] >= 30 and s[2] >= 500]
    lt = int(np.median([s[3] for s in wide])) if wide else -20
    kept = []
    for a, b, tot, top, bot in seg:
        if tot < 60: continue
        if b - a < 24 and tot < 500:
            near = [s[3] for s in wide if abs(s[0] - a) <= 250]
            loc = int(np.median(near)) if near else lt
            if not (bot - top + 1 >= 20 and top - loc <= 9 and top > -30): kept.append([a, b, 1]); continue
        kept.append([a, b, 0])
    jn = []
    for a, b, sp in kept:
        if sp: jn.append([a, b, 1]); continue
        p = jn[-1] if jn else None
        # join every kept pair <= 16 px apart with no dropped speck between: digits of one number can sit 13-22 px apart and
        # cannot be told from comma gaps; 16 joins the two splits the eye check found without chaining half-lines (30 did) (R14-LVN10D eye check: '115' cut '11'|'5', '77' cut '7'|'7'); an over-joined tile
        # shows two comma-separated numbers, which the reader writes in order, so over-joining loses nothing
        if p and not p[2] and a - p[1] <= 16: p[1] = b
        else: jn.append([a, b, 0])
    for a, b, sp in jn:
        if not sp: blobs.append((i + 1, a + 250, b + 250, int(YC[i][(a + b) // 2])))
from PIL import ImageFont
FONT = ImageFont.load_default(size=30)
labels = [''.join(p) for p in itertools.product(string.ascii_uppercase, repeat=2)]
order = list(range(len(blobs))); random.Random(4611 if REPAIR else 4610).shuffle(order)
PER, COLS = (16, 2) if REPAIR else (32, 4)
tiles = []
for k, bi in enumerate(order):
    L, x0, x1, y = blobs[bi]
    t = img.crop((x0 - 8, y - 48, x1 + 9, y + 42)); t = t.resize((int(t.width * 1.5), int(t.height * 1.5)))
    tiles.append((labels[k], bi, t))
rows = []
for s in range(0, len(tiles), PER):
    grp = tiles[s:s + PER]; TW = 1500 if REPAIR else 540; TH = 185
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
    f.write('label\tphys\tx0\tx1\tpage_order\tsheet\ttruncated' + ('\tyc' if REPAIR else '') + '\n')
    for lab, bi, sh, tr in rows:
        L, x0, x1, y = blobs[bi]; f.write(f'{lab}\t{L}\t{x0}\t{x1}\t{bi}\t{sh}\t{int(tr)}' + (f'\t{y}' if REPAIR else '') + '\n')
print(len(blobs), 'blobs,', (len(tiles) + PER - 1) // PER, 'sheets;', sum(r[3] for r in rows), 'tiles truncated at the sheet width')
