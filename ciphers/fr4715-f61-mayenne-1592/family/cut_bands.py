#!/usr/bin/env python3
"""F61-FAMILY band cutter for interlined leaves (28 Sept 2026). The shared tools/iiif_lines.py finds lines by row-ink
peaks, but on a leaf whose cipher lines each carry a small clear gloss ABOVE them the gloss rows are peaks too and the
band edges fall between gloss and cipher. This cutter finds the CIPHER line centres (heavy rows, min distance --pitch)
and cuts each band from centre-UP to centre+DOWN so the gloss above rides with its cipher line; each band is cut into
segments no wider than --seg native px with --overlap px shared (boundary tick drawn), scaled by --scale, and a debug
overlay is written. Native boxes go to sheets/<prefix>_bands.json.
  python3 cut_bands.py IMAGE x,y,w,h OUTDIR PREFIX [--pitch 130] [--up 95] [--down 60] [--seg 1400] [--overlap 100] [--scale 1.6] [--centres y1,y2,...  (hand-set cipher-row centres in region y, overriding detection)]
"""
import sys, json, numpy as np
from PIL import Image, ImageDraw
a = sys.argv; img, reg, out, pre = a[1], [int(v) for v in a[2].split(',')], a[3], a[4]
def opt(n, d): return type(d)(a[a.index(n) + 1]) if n in a else d
pitch, up, down, seg, ov, sc = opt('--pitch', 130), opt('--up', 95), opt('--down', 60), opt('--seg', 1400), opt('--overlap', 100), opt('--scale', 1.6)
x, y, w, h = reg
im = Image.open(img).convert('L').crop((x, y, x + w, y + h))
arr = np.asarray(im); prof = (arr < 150).sum(axis=1).astype(float)
k = 9; prof = np.convolve(prof, np.ones(k) / k, mode='same')
# peaks: local maxima above 30% of max, at least `pitch` apart, greedy by height
cand = [i for i in range(1, h - 1) if prof[i] >= prof[i-1] and prof[i] >= prof[i+1] and prof[i] > 0.30 * prof.max()]
cand.sort(key=lambda i: -prof[i]); centres = []
for c in cand:
    if all(abs(c - o) >= pitch for o in centres): centres.append(c)
centres.sort()
if '--centres' in a: centres = [int(v) for v in a[a.index('--centres') + 1].split(',')]
print('centres (region y):', centres, 'profile max', int(prof.max()))
dbg = im.convert('RGB'); d = ImageDraw.Draw(dbg); boxes = {}
for n, c in enumerate(centres, 1):
    starts = list(range(0, max(1, w - ov), seg - ov))
    for s, x0 in enumerate(starts, 1):
        x1 = min(w, x0 + seg)
        # per-segment centre (--local N): the ink-profile peak of this segment's columns within +-N px of the band centre,
        # so a row that rises across the leaf keeps its gloss inside the band in every segment (28 Sept 2026: the first
        # f.274 cut lost the right half of every gloss row and the readers assigned them to the wrong band)
        cc = c
        if '--local' in a:
            N = opt('--local', 35); pr = (arr[:, x0:x1] < 150).sum(axis=1).astype(float); pr = np.convolve(pr, np.ones(k) / k, mode='same')
            lo, hi = max(0, c - N), min(h, c + N); cc = lo + int(np.argmax(pr[lo:hi]))
        y0, y1 = max(0, cc - up), min(h, cc + down)
        d.line((x0, cc, x1, cc), fill=(255, 0, 0), width=2); d.rectangle((x0, y0, x1 - 1, y1), outline=(0, 0, 255), width=2)
        band = im.crop((0, y0, w, y1)); crop = band.crop((x0, 0, x1, band.height)).convert('RGB')
        crop = crop.resize((int(crop.width * sc), int(crop.height * sc)), Image.LANCZOS)
        dd = ImageDraw.Draw(crop)
        if s > 1: dd.line((int(ov * sc), 0, int(ov * sc), 12), fill=(255, 0, 0), width=3)
        if x1 < w: dd.line((crop.width - int(ov * sc), 0, crop.width - int(ov * sc), 12), fill=(255, 0, 0), width=3)
        name = f'{pre}_L{n:02d}_s{s}.jpg'; crop.save(f'{out}/{name}', quality=90)
        boxes[name] = [x + x0, y + y0, x + x1, y + y1]
        if x1 >= w: break
dbg.save(f'{out}/{pre}_bands_debug.jpg', quality=80)
json.dump({'image': img, 'region': reg, 'centres': centres, 'pitch': pitch, 'up': up, 'down': down, 'scale': sc, 'boxes': boxes}, open(f'{out}/{pre}_bands.json', 'w'), indent=1)
print('bands', len(centres), 'crops', len(boxes))
