#!/usr/bin/env python3
"""Cut line crops of the cipher lines of fr.3251 ff.21v, 35, 87 from the committed native regions (HARVEST-D, 28 Sept
2026; 2x mode added by HARVEST-D2 the same day). Line centres set by eye on each region's grid and checked against the
row ink profile (HARVEST-D2: peaks within the 120 px bands on all three regions).
  python3 cut_folio_lines.py      # writes <folio>/lines/<folio>_Lnn_sk.png (1x, 1700 px, 150 px overlap) and
                                  # <folio>/lines2x/<folio>_Lnn_sk.png (2x upscale of ~1150 px segments cut at the
                                  # column-ink minimum nearest the nominal boundary, no overlap), with crops_manifest.json
Lines on f.21v mix prose and cipher: a reader transcribes only the cipher signs. Both crop sets are gitignored and
regenerable; the reader passes of HARVEST-D2 used lines2x/.
"""
import json
from pathlib import Path
from PIL import Image, ImageOps

HERE = Path(__file__).resolve().parent
FOLIOS = {  # folio: (source region, nominal line centres at the LEFT edge, follow the slope?)
    'f21v': ('c23_cipher_w.jpg', [120, 200, 280, 376, 456, 536, 610, 690, 760, 836, 910], False),
    'f35': ('c36_cipher_w.jpg', [206, 300], False),
    'f87': ('c88_cipher_wt.jpg', [283, 393, 527, 625, 730], True),  # tall region (HARVEST-D2), centres at x=0; FIVE lines:
    # HARVEST-D's sixth centre (700 in the old region) was the fallen right end of line 5, not a line (every reader found 'L06' empty)
}
SEG, HALF = 1150, 62
# f.87's lines FALL to the right by about 80-100 px across the region at a 105-110 px pitch and not in a straight line
# (HARVEST-D2, 28 Sept 2026: two reader pairs on flat and on globally-sheared crops both found the target line cut at the
# crop bottom from the second segment on). Its 2x crops follow each line: all row peaks of a heavily smoothed ink
# profile are found per 450 px window, each line's centre is tracked window to window (nearest peak to the previous
# centre plus the expected fall), and every segment is sheared flat between its left and right local centres. The
# tall region c88_cipher_wt.jpg (pct:52,67,43,18) replaces c88_cipher_w.jpg, whose bottom edge clipped L06's right end.


def row_peaks(px, H, a, b, k=22, sep=75, n=10):
    """The n strongest, well-separated row peaks of the ink profile over columns a..b (k = half the smoothing box)."""
    prof = [sum(255 - px[x, y] for x in range(a, b, 2)) for y in range(H)]
    sm = [sum(prof[max(0, y - k):y + k + 1]) for y in range(H)]
    out = []
    for y in sorted(range(k, H - k), key=lambda y: -sm[y]):
        if all(abs(y - o) >= sep for o in out):
            out.append(y)
        if len(out) == n:
            break
    return sorted(out)


def track_lines(im, centres, win=450, fall=12, tol=45):
    """Per line, the local centre at each window midpoint: the peak nearest the previous centre + fall, else the
    prediction itself. Returns {line index: [(x_mid, y), ...]}."""
    W, H = im.size; px = im.load(); cur = list(centres); tracks = {i: [(0, c)] for i, c in enumerate(centres)}
    for a in range(0, W - win // 2, win):
        b = min(W, a + win); pk = row_peaks(px, H, a, b)
        for i, c in enumerate(cur):
            pred = c + fall; near = min(pk, key=lambda y: abs(y - pred)) if pk else pred
            cur[i] = near if abs(near - pred) <= tol else pred
            tracks[i].append(((a + b) / 2, cur[i]))
    return tracks


def at(track, x):
    """Piecewise-linear centre of a tracked line at column x."""
    for (x0, y0), (x1, y1) in zip(track, track[1:]):
        if x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0) if x1 > x0 else y0
    return track[-1][1]


def sheared_band(im, m, k, half):
    """Band of height 2*half following y = m*x + k, sheared flat (output (x, y) <- input (x, y + m*x))."""
    W, H = im.size
    y0 = k - half
    return im.transform((W, 2 * half), Image.AFFINE, (1, 0, 0, m, 1, y0), resample=Image.BICUBIC)


def gap_cut(band, x, window=90):
    """Column with the least ink within +-window of x (a gap between signs), so no sign is split or doubled."""
    W, H = band.size
    px = band.load()
    best, bx = None, x
    for cx in range(max(1, x - window), min(W - 1, x + window)):
        ink = sum(255 - px[cx, y] for y in range(H)) + sum(255 - px[cx - 1, y] for y in range(H))
        if best is None or ink < best:
            best, bx = ink, cx
    return bx


for folio, (src, centres, follow) in FOLIOS.items():
    im = Image.open(HERE / folio / src).convert('L'); W, H = im.size
    tracks = track_lines(im, centres) if follow else None
    if follow:
        for i, t in tracks.items():
            print(f'{folio} L{i + 1:02d}: centre {t[0][1]} at x=0 -> {t[-1][1]} at x={int(t[-1][0])}')
    else:
        print(f'{folio}: flat')
    for sub in ('lines', 'lines2x'):
        (HERE / folio / sub).mkdir(exist_ok=True)
    out1, out2 = [], []
    for i, c in enumerate(centres, 1):
        y0, y1 = max(0, c - HALF), min(H, c + HALF)
        band = ImageOps.autocontrast(im.crop((0, y0, W, y1)), cutoff=1)
        a = 0; k = 1
        while a < W:  # 1x, overlapping (HARVEST-D's original cut)
            b = min(W, a + 1700); name = f'lines/{folio}_L{i:02d}_s{k}.png'
            band.crop((a, 0, b, y1 - y0)).save(HERE / folio / name)
            out1.append({'crop': name, 'src': src, 'box': [a, y0, b, y1]})
            if b == W:
                break
            a = b - 150; k += 1
        if follow:  # 2x crops follow the tracked line: a sheared preview band for the gap cuts, then per-segment shear
            tr = tracks[i - 1]
            band = ImageOps.autocontrast(sheared_band(im, (at(tr, W) - at(tr, 0)) / W, at(tr, 0), HALF), cutoff=1)
        cuts = [0]  # 2x, gap-aware, no overlap
        while W - cuts[-1] > SEG + 200:
            cuts.append(gap_cut(band, cuts[-1] + SEG))
        cuts.append(W)
        for k in range(len(cuts) - 1):
            a, b = cuts[k], cuts[k + 1]
            name = f'lines2x/{folio}_L{i:02d}_s{k + 1}.png'
            if follow:
                ya, yb = at(tr, a), at(tr, b); m = (yb - ya) / (b - a)
                seg = im.transform((b - a, 2 * HALF), Image.AFFINE, (1, 0, a, m, 1, ya - HALF), resample=Image.BICUBIC)
                seg = ImageOps.autocontrast(seg, cutoff=1); box = [a, round(ya), b, round(yb)]
            else:
                seg = band.crop((a, 0, b, y1 - y0)); box = [a, y0, b, y1]
            seg = seg.resize((seg.width * 2, seg.height * 2), Image.LANCZOS)
            seg.save(HERE / folio / name)
            out2.append({'crop': name, 'src': src, 'box': box, 'scale': 2,
                         **({'tracked_centres_left_right': [round(ya), round(yb)]} if follow else {})})
    json.dump(out1, open(HERE / folio / 'lines' / 'crops_manifest.json', 'w'), indent=0)
    json.dump(out2, open(HERE / folio / 'lines2x' / 'crops_manifest.json', 'w'), indent=0)
    print(folio, len(out1), len(out2))
