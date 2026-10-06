#!/usr/bin/env python3
"""Enhance clear-text word crops for decode-1162 (DEC1162-ENHANCE, 6-7 Oct 2026).

For each row of a boxes TSV (id, page, line, crop, row, x0, x1, word -- the format of ../focus/boxes.tsv) cuts the word
from ../../images/clear/<crop>.jpg at native resolution (no upscaling), with a 25 px margin, and writes three files:
  <id>_grey.png  greyscale -> background flattened (morphological black top-hat: closing by a max-then-min filter of
                 size BG, minus the image; ink becomes bright on 0) -> inverted back to dark ink on white -> contrast
                 stretch between the P_LO and P_HI percentiles of the flattened line band
  <id>_bin.png   Sauvola binarisation of <id>_grey.png (window W, k K, R 128), ink black on white
  <id>_line.png  the whole enhanced line band (same flattening + stretch), word boxed in red
Source images are only read, never written.
Usage: python3 enhance.py BOXES.tsv OUTDIR      Parameters: BG=31 P_LO=60 P_HI=99.5 W=41 K=0.34 (constants below)
"""
import csv, os, sys
import numpy as np
from PIL import Image, ImageFilter, ImageDraw

BG, P_LO, P_HI, W, K, R, MARGIN = 31, 60, 99.5, 41, 0.34, 128.0, 25
H = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(H, '..', '..', 'images', 'clear')

def yrange(row, h):
    return {'a': (0, int(h * .62)), 'b': (int(h * .38), h), 'c': (int(h * .5), h), 'f': (0, h)}[row]

def flatten(g):
    """Black top-hat on a greyscale PIL image; returns dark-ink-on-white uint8 array, contrast-stretched."""
    closed = g.filter(ImageFilter.MaxFilter(BG)).filter(ImageFilter.MinFilter(BG))
    th = np.asarray(closed, dtype=np.float64) - np.asarray(g, dtype=np.float64)  # ink > 0
    lo, hi = np.percentile(th, P_LO), np.percentile(th, P_HI)
    th = np.clip((th - lo) / max(hi - lo, 1e-6), 0, 1)
    return (255 * (1 - th)).astype(np.uint8)

def sauvola(a):
    a = a.astype(np.float64)
    p = W // 2
    pad = np.pad(a, p, mode='reflect')
    ii = np.pad(pad, ((1, 0), (1, 0))).cumsum(0).cumsum(1)
    ii2 = np.pad(pad ** 2, ((1, 0), (1, 0))).cumsum(0).cumsum(1)
    h, w = a.shape
    def box(s):
        return s[W:W + h, W:W + w] - s[:h, W:W + w] - s[W:W + h, :w] + s[:h, :w]
    n = W * W
    m = box(ii) / n
    sd = np.sqrt(np.maximum(box(ii2) / n - m * m, 0))
    t = m * (1 + K * (sd / R - 1))
    return np.where(a > t, 255, 0).astype(np.uint8)

def main(boxes, out):
    os.makedirs(out, exist_ok=True)
    with open(boxes, newline='') as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    for b in rows:
        im = Image.open(os.path.join(IMG, b['crop'] + '.jpg')).convert('L')
        w, h = im.size
        y0, y1 = yrange(b['row'], h)
        x0, x1 = max(0, int(b['x0']) - MARGIN), min(w, int(b['x1']) + MARGIN)
        band = im.crop((0, y0, w, y1))
        eb = flatten(band)
        grey = Image.fromarray(eb[:, x0:x1])
        grey.save(os.path.join(out, b['id'] + '_grey.png'))
        Image.fromarray(sauvola(eb)[:, x0:x1]).save(os.path.join(out, b['id'] + '_bin.png'))
        line = Image.fromarray(eb).convert('RGB')
        d = ImageDraw.Draw(line)
        d.rectangle([x0, 0, x1, y1 - y0 - 1], outline=(220, 0, 0), width=3)
        line.save(os.path.join(out, b['id'] + '_line.png'))
    print('enhanced', len(rows), 'crops ->', out)

if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[1] in ('-h', '--help'):
        print(__doc__); sys.exit(0 if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help') else 2)
    main(sys.argv[1], sys.argv[2])
