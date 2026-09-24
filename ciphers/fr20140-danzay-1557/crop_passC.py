#!/usr/bin/env python3
"""Blind second reader (pass C) line crops for f.35r-v, from the native images on disk only.

Each line strip is cut at a whitespace column near its middle and the two halves are stacked
(left half on top) at native resolution. Output goes to passC_crops/ (not committed; rerun to regenerate).
Line centres are the ink-row peaks of each page's text block (smoothed dark-pixel row counts)."""
import os
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'passC_crops')
# page: image, line centres (ink-row peaks, native px), x0, x1, label prefix
PAGES = [('native_f69.jpg', [3780, 3916, 4066, 4206, 4348, 4500, 4652, 4809], 1860, 4720, 'R'),
         ('native_f70.jpg', [646, 779, 921, 1067, 1204, 1351, 1510, 1664, 1806, 1940, 2091, 2233, 2388,
                             2538, 2679, 2822, 2942, 3087, 3226, 3376, 3527, 3677, 3812, 3971, 4122, 4276,
                             4419, 4558, 4707], 980, 3920, 'V')]
UP, DOWN = 105, 80

def main():
    os.makedirs(OUT, exist_ok=True)
    for img, centres, x0, x1, pre in PAGES:
        g = np.array(Image.open(os.path.join(HERE, 'images', img)).convert('L'))
        for i, c in enumerate(centres):
            strip = g[c - UP:c + DOWN, x0:x1]
            ink = (strip < 120).sum(0)
            mid = strip.shape[1] // 2
            w = 250
            cut = mid - w + int(np.argmin(np.convolve(ink, np.ones(15), 'same')[mid - w:mid + w]))
            left, right = strip[:, :cut], strip[:, cut:]
            W = max(left.shape[1], right.shape[1])
            canvas = np.full((strip.shape[0] * 2 + 10, W), 255, np.uint8)
            canvas[:strip.shape[0], :left.shape[1]] = left
            canvas[strip.shape[0] + 10:, :right.shape[1]] = right
            name = '%s%02d.jpg' % (pre, i + 1)
            Image.fromarray(canvas).save(os.path.join(OUT, name), quality=85)
            print(name, 'centre', c, 'cut', x0 + cut)

if __name__ == '__main__':
    main()
