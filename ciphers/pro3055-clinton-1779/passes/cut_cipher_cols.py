#!/usr/bin/env python3
"""Cut the 2894 cipher (H-1649 pages 184-185, images/h1649/img827_full.jpg and img828_full.jpg, native 6080x4056)
into one crop per column half, for blind transcription passes (GAPS2-pro3055-clinton-1779, 2 Oct 2026).

Why not tools/iiif_lines.py: the cipher is written in COLUMNS of figure pairs (8 on page 184, 7 on page 185), read
top to bottom then left to right, so the natural reading unit is a column strip, not a text line. This script finds
the valleys of the column ink profile nearest to hand-estimated boundaries (from the 1520 px previews), cuts each
column as a vertical strip, splits it at a row-profile valley near the middle with one row of overlap, upscales 2x
(digits ~30 px tall at native, ~60 px after), draws a tick at the overlap boundary, and writes images/h1649/p18N_cols/
plus a manifest. Run from the repo root: python3 ciphers/pro3055-clinton-1779/passes/cut_cipher_cols.py
"""
import json, os, sys
import numpy as np
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.abspath(__file__))
IMG = os.environ.get('CLINTON_H1649_DIR') or os.path.join(ROOT, '..', 'images', 'h1649')  # env override: regen_images.sh
INK = 150          # pixel darker than this counts as ink (microfilm positive, dark ink on grey)
SCALE = 2
QUALITY = 55

# page: (file, region x0,y0,x1,y1 in native px, estimated column boundaries in native px, row range)
PAGES = {
    'p184': dict(file='img827_full.jpg', x0=2200, x1=4180, y0=640, y1=2320,
                 bounds=[2724, 2912, 3108, 3308, 3500, 3692, 3896]),
    'p185': dict(file='img828_full.jpg', x0=2240, x1=4120, y0=580, y1=2080,
                 bounds=[2652, 2896, 3120, 3344, 3580]),
}

def smooth(v, w):
    k = np.ones(w) / w
    return np.convolve(v, k, mode='same')

def nearest_valley(profile, x_est, x0, win=60):
    lo, hi = max(0, x_est - x0 - win), min(len(profile), x_est - x0 + win)
    seg = profile[lo:hi]
    return x0 + lo + int(np.argmin(seg))

def main():
    out_manifest = {}
    for page, cfg in PAGES.items():
        im = Image.open(os.path.join(IMG, cfg['file'])).convert('L')
        a = np.array(im)
        x0, x1, y0, y1 = cfg['x0'], cfg['x1'], cfg['y0'], cfg['y1']
        reg = a[y0:y1, x0:x1]
        ink = (reg < INK).astype(np.int32)
        col = smooth(ink.sum(axis=0).astype(float), 25)
        bounds = [x0] + [nearest_valley(col, b, x0) for b in cfg['bounds']] + [x1]
        print(page, 'column boundaries (native x):', bounds)
        outdir = os.path.join(IMG, page + '_cols')
        os.makedirs(outdir, exist_ok=True)
        entries = []
        for ci in range(len(bounds) - 1):
            cx0, cx1 = bounds[ci], bounds[ci + 1]
            strip = ink[:, cx0 - x0:cx1 - x0]
            row = smooth(strip.sum(axis=1).astype(float), 15)
            mid = len(row) // 2
            lo, hi = mid - 120, mid + 120
            split = lo + int(np.argmin(row[lo:hi]))     # a row valley near the middle
            overlap = 70                                # about one row pitch (~56 px) plus margin
            halves = [('a', 0, min(len(row), split + overlap)), ('b', max(0, split - overlap), len(row))]
            for tag, ry0, ry1 in halves:
                box = (cx0, y0 + ry0, cx1, y0 + ry1)
                crop = im.crop(box).resize(((cx1 - cx0) * SCALE, (ry1 - ry0) * SCALE), Image.LANCZOS)
                d = ImageDraw.Draw(crop)
                # tick at the overlap boundary: the row 'split' in strip coordinates
                ty = (split - ry0) * SCALE
                if 0 < ty < crop.size[1]:
                    d.line([(0, ty), (18, ty)], fill=0, width=3)
                    d.line([(crop.size[0] - 18, ty), (crop.size[0], ty)], fill=0, width=3)
                name = f'{page}_c{ci + 1}{tag}.jpg'
                crop.save(os.path.join(outdir, name), quality=QUALITY)
                entries.append(dict(crop=name, source=cfg['file'], box=list(box), scale=SCALE,
                                    column=ci + 1, half=tag, split_row_native=y0 + split,
                                    size=list(crop.size)))
        out_manifest[page] = dict(region=[x0, y0, x1, y1], bounds=bounds, crops=entries)
        with open(os.path.join(outdir, 'manifest.json'), 'w') as f:
            json.dump(out_manifest[page], f, indent=1)
        print(page, len(entries), 'crops ->', outdir)

if __name__ == '__main__':
    main()
