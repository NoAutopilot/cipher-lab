#!/usr/bin/env python3
"""Regenerate glyphs/p1_clean.png and glyphs/p2_clean.png, the inputs to tools/glyph_atlas.py segment (H11).

The native region crops (images/src_2_*.jpg) carry heavy brown bleed-through from the other side of the leaf;
tools/glyph_atlas.py's own background-normalised binarisation then reads thousands of specks as signs (median
sign height 4 px, 68 'lines' on p.[1]). Two fixes, both here so a re-run is one command:
  1. the RED channel only -- brown bleed-through is light in red, black ink stays dark (blue would do the reverse);
  2. background-normalise (divide by a 61x61 grey closing), threshold at 0.55 x background, and drop every connected
     component under 200 px area; everything else is painted white.
Result (27 Sept 2026): p1 283 components, p2 69, median height ~75 px; segment then finds 213 + 50 signs.
  python3 glyphs/prepare.py            writes glyphs/p1_clean.png, glyphs/p2_clean.png
Needs opencv-python-headless and numpy (pip install).
"""
import os, sys
import cv2, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
PAGES = {'p1': 'images/src_2_10867298_450_440_3000_1740.jpg', 'p2': 'images/src_2_10867299_360_1997_3055_456.jpg'}
REL, MIN_AREA = 0.55, 200
for name, rel in PAGES.items():
    img = cv2.imread(os.path.join(T, rel))
    r = img[:, :, 2]  # OpenCV is BGR: index 2 is red
    bg = cv2.morphologyEx(r, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (61, 61)))
    norm = np.clip(r.astype(float) / np.maximum(bg, 1) * 255, 0, 255).astype(np.uint8)
    ink = (norm < REL * 255).astype(np.uint8)
    n, lab, stats, _ = cv2.connectedComponentsWithStats(ink, connectivity=8)
    keep = np.zeros(n, bool); keep[1:] = stats[1:, cv2.CC_STAT_AREA] >= MIN_AREA
    clean = np.where(keep[lab], norm, 255).astype(np.uint8)
    out = os.path.join(HERE, f'{name}_clean.png'); cv2.imwrite(out, clean)
    print(f'{name}: kept {int(keep.sum())} components -> {out}')
