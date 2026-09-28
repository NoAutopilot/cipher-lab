#!/usr/bin/env python3
"""H33d (28 Sept 2026): regenerate images/p2x_L*_s*.jpg, the red-channel-cleaned, DESKEWED line crops of the p.[2]
upper plain block of the 7 Sept 1519 letter (canvas 10867299), from the full canvas.

  python3 passes/p2x_cut.py FULL_CANVAS.jpg OUT_DIR
  (FULL_CANVAS = https://collections.library.yale.edu/iiif/2/10867299/full/full/0/default.jpg, 3577x4997, fetched once)

Steps: (1) glyphs/prepare.py's cleaning without the component drop -- red channel, divide by a 61x61 grey closing,
stretch so 0.20 x background -> black and 0.80 x background -> white (bleed-through is light in red, ink dark);
(2) a global shear estimate: the row ink profile of eight 400-px column windows, each cross-correlated with its
neighbour (shift within +-60 px), the cumulative shifts fitted to a line -> b = -0.0386 (lines rise to the right,
about 123 px over the 3200-px block); (3) deskew y' = y - b*x with cv2.warpAffine; (4) scipy find_peaks on the
deskewed row profile (Gaussian sigma 6, distance 100, prominence 8 percent of max) -> 12 lines; (5) bands of +-95 px
around each peak, two segments x 300-2700 and 1100-3500, JPEG q80. Why not tools/iiif_lines.py --follow-slope: on this
block it duplicates bands (L01/L02, L06/L07, L09/L10 share one intercept) with or without cleaning -- the H33b fault;
a --deskew option on the tool would replace this script (suggested, not done here).
"""
import sys, os, json
import cv2, numpy as np
from scipy.signal import find_peaks
from scipy.ndimage import gaussian_filter1d
src, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
img = cv2.imread(src); r = img[:, :, 2]
bg = cv2.morphologyEx(r, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (61, 61)))
norm = np.clip(r.astype(float) / np.maximum(bg, 1) * 255, 0, 255)
lo, hi = 0.20, 0.80
clean = (np.clip((norm - lo * 255) / ((hi - lo) * 255), 0, 1) * 255).astype(np.uint8)
X0, Y0, W, H = 300, 100, 3200, 2000
ink = 255 - clean[Y0:Y0 + H, X0:X0 + W].astype(float)
win = 400
prof = [gaussian_filter1d(ink[:, i * win:(i + 1) * win].sum(1), 6) for i in range(W // win)]
def best_shift(a, b, maxs=60):
    best = None
    for s in range(-maxs, maxs + 1):
        c = np.dot(a[s:], b[:len(b) - s]) if s >= 0 else np.dot(a[:s], b[-s:])
        if best is None or c > best[0]: best = (c, s)
    return best[1]
shifts = [0]
for i in range(1, len(prof)): shifts.append(shifts[-1] + best_shift(prof[i - 1], prof[i]))
xs = np.array([(i + 0.5) * win for i in range(len(prof))])
b = round(-np.polyfit(xs, np.array(shifts, float), 1)[0], 5)   # a positive shift means the next window's lines sit higher
M = np.float32([[1, 0, 0], [-b, 1, 0]])
des = cv2.warpAffine(clean, M, (clean.shape[1], clean.shape[0] + 300), borderValue=255)
p = gaussian_filter1d((255 - des[Y0:Y0 + H + 200, X0:X0 + W].astype(float)).sum(1), 6)
pk, _ = find_peaks(p, distance=100, prominence=p.max() * 0.08)
ys = [int(v + Y0) for v in pk]
print(f'slope b={b:.5f}; {len(ys)} lines at deskewed y {ys}')
HH, segs = 95, [(300, 2700), (1100, 3500)]
for i, y in enumerate(ys, 1):
    for si, (x0, x1) in enumerate(segs, 1):
        cv2.imwrite(os.path.join(out, f'p2x_L{i:02d}_s{si}.jpg'), des[y - HH:y + HH, x0:x1], [cv2.IMWRITE_JPEG_QUALITY, 80])
json.dump({'b': float(b), 'ys': ys}, open(os.path.join(out, 'p2x_deskew.json'), 'w'))
