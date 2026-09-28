#!/usr/bin/env python3
"""F61-FAMILY-5 (28 Sept 2026): band cutter for a leaf whose cipher rows curve (fr.3982 f.97r: the rows descend 30-70 px
across the leaf, unevenly, so cut_bands.py's fixed centres, --track and --local all put some s3-s5 windows on the wrong row).
Rows are detected PER SEGMENT COLUMN: in each segment's x-window the ink-weight profile (dark pixels per row, smoothed) gives
the cipher-row peaks (local maxima above --frac of the window's max, at least --pitch apart, greedy by weight -- the gloss rows
are far lighter and lose to the cipher rows); the rows of segment 1 define the bands, and each band is chained to the nearest
peak of the next segment within --link px of its previous centre (no peak within reach: the previous centre + --slope x step
is used and the segment is flagged). Bands are then cut exactly as cut_bands.py does (centre - up .. centre + down, --scale,
overlap ticks), boxes to sheets/<PREFIX>_bands.json with a 'flags' list, debug overlay alongside.
  python3 chain_rows.py IMAGE x,y,w,h OUTDIR PREFIX [--pitch 80] [--frac 0.45] [--link 40] [--up 70] [--down 55] [--seg 760] [--overlap 60] [--scale 2.0] [--first y1,y2,... (hand-set segment-1 centres, region y)]
"""
import sys, json, numpy as np
from PIL import Image, ImageDraw
a = sys.argv; img, reg, out, pre = a[1], [int(v) for v in a[2].split(',')], a[3], a[4]
def opt(n, d): return type(d)(a[a.index(n) + 1]) if n in a else d
pitch, frac, link, up, down, seg, ov, sc = opt('--pitch', 80), opt('--frac', 0.45), opt('--link', 40), opt('--up', 70), opt('--down', 55), opt('--seg', 760), opt('--overlap', 60), opt('--scale', 2.0)
x, y, w, h = reg
im = Image.open(img).convert('L').crop((x, y, x + w, y + h)); arr = np.asarray(im)
starts = list(range(0, max(1, w - ov), seg - ov)); wins = [(x0, min(w, x0 + seg)) for x0 in starts]
wins = [wn for i, wn in enumerate(wins) if i == 0 or wins[i - 1][1] < w]
def peaks(x0, x1):
    pr = (arr[:, x0:x1] < 150).sum(axis=1).astype(float); k = 9; pr = np.convolve(pr, np.ones(k) / k, mode='same')
    cand = [i for i in range(1, h - 1) if pr[i] >= pr[i - 1] and pr[i] >= pr[i + 1] and pr[i] > frac * pr.max()]
    cand.sort(key=lambda i: -pr[i]); P = []
    for c in cand:
        if all(abs(c - o) >= pitch for o in P): P.append(c)
    return sorted(P)
first = [int(v) for v in a[a.index('--first') + 1].split(',')] if '--first' in a else peaks(*wins[0])
rows = [[c] for c in first]; flags = []
# --rows "y1,y2,y3,y4,y5;..." (F61-FAMILY-5): hand-set per-segment centres, one band per ';' group (a band the chaining lost)
if '--rows' in a:
    rows = [[int(v) for v in g.split(',')] for g in a[a.index('--rows') + 1].split(';')]; first = [r[0] for r in rows]
for s in range(1, len(wins)):
    if '--rows' in a: break
    P = peaks(*wins[s])
    for n, r in enumerate(rows, 1):
        prev = r[-1]; near = [p for p in P if abs(p - prev) <= link]
        if near: r.append(min(near, key=lambda p: abs(p - prev)))
        else: r.append(min(h - 1, prev + int(round(0.011 * (seg - ov))))); flags.append(f'L{n:02d}_s{s + 1}: no peak within {link} px, extrapolated')
dbg = im.convert('RGB'); d = ImageDraw.Draw(dbg); boxes = {}
names = a[a.index('--names') + 1].split(',') if '--names' in a else [f'L{n:02d}' for n in range(1, len(rows) + 1)]
for n, r in enumerate(rows, 1):
    for s, ((x0, x1), cc) in enumerate(zip(wins, r), 1):
        y0, y1 = max(0, cc - up), min(h, cc + down)
        d.line((x0, cc, x1, cc), fill=(255, 0, 0), width=2); d.rectangle((x0, y0, x1 - 1, y1), outline=(0, 0, 255), width=2)
        crop = im.crop((x0, y0, x1, y1)).convert('RGB'); crop = crop.resize((int(crop.width * sc), int(crop.height * sc)), Image.LANCZOS)
        dd = ImageDraw.Draw(crop)
        if s > 1: dd.line((int(ov * sc), 0, int(ov * sc), 12), fill=(255, 0, 0), width=3)
        if x1 < w: dd.line((crop.width - int(ov * sc), 0, crop.width - int(ov * sc), 12), fill=(255, 0, 0), width=3)
        name = f'{pre}_{names[n - 1]}_s{s}.jpg'; crop.save(f'{out}/{name}', quality=90); boxes[name] = [x + x0, y + y0, x + x1, y + y1]
dbg = dbg.resize((dbg.width // 3, dbg.height // 3)); dbg.save(f'{out}/{pre}_bands_debug.jpg', quality=75)
json.dump({'image': img, 'region': reg, 'centres': first, 'per_segment_centres': rows, 'pitch': pitch, 'frac': frac, 'link': link, 'up': up, 'down': down, 'scale': sc, 'flags': flags, 'boxes': boxes}, open(f'{out}/{pre}_bands.json', 'w'), indent=1)
print('bands', len(rows), 'crops', len(boxes), 'flags', len(flags)); [print(' ', f) for f in flags]
for n, r in enumerate(rows, 1): print(f'L{n:02d}', r, 'steps', [r[i + 1] - r[i] for i in range(len(r) - 1)])
