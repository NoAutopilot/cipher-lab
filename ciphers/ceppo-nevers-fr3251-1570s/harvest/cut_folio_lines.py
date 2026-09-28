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
    'f87': ('c88_cipher_w.jpg', [185, 290, 395, 500, 600, 700], True),
}
SEG, HALF = 1150, 68
# f.87's lines rise to the right by about 25 px across the region at a 105 px pitch (HARVEST-D2 pass B of the flat
# crops, 28 Sept 2026: "the neighbouring line intrudes"); its 2x crops follow the line: one shear per region from the
# left/right row-profile correlation, the band sheared flat with an affine transform. f.21v and f.35 read fine flat.


def region_shear(im):
    """Vertical shift of the right third of the region against the left third (row ink profiles, best correlation over
    -50..50 px, under half the line pitch so the match cannot slip one line), as a slope per px: the lines of a page photographed slightly askew rise or fall together."""
    W, H = im.size; px = im.load()
    def prof(x0, x1):
        p = [sum(255 - px[x, y] for x in range(x0, x1, 4)) for y in range(H)]
        mu = sum(p) / H; return [v - mu for v in p]
    L, R = prof(0, W // 3), prof(2 * W // 3, W)
    best = max(range(-50, 51), key=lambda d: sum(L[y] * R[y + d] for y in range(50, H - 50)))
    return best / (2 * W / 3)


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
    shear = region_shear(im) if follow else 0.0
    print(f'{folio}: shear {shear * W:+.0f} px across the region' if follow else f'{folio}: flat')
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
        if follow:  # re-band along the sheared line for the 2x crops (centres are given at the left edge)
            m, k = shear, c; band = ImageOps.autocontrast(sheared_band(im, m, k, HALF), cutoff=1)
        cuts = [0]  # 2x, gap-aware, no overlap
        while W - cuts[-1] > SEG + 200:
            cuts.append(gap_cut(band, cuts[-1] + SEG))
        cuts.append(W)
        for k in range(len(cuts) - 1):
            a, b = cuts[k], cuts[k + 1]
            name = f'lines2x/{folio}_L{i:02d}_s{k + 1}.png'
            seg = band.crop((a, 0, b, y1 - y0)); seg = seg.resize((seg.width * 2, seg.height * 2), Image.LANCZOS)
            seg.save(HERE / folio / name)
            out2.append({'crop': name, 'src': src, 'box': [a, y0, b, y1], 'scale': 2,
                         **({'line': [round(m, 5), round(k, 1)], 'sheared': True} if follow else {})})
    json.dump(out1, open(HERE / folio / 'lines' / 'crops_manifest.json', 'w'), indent=0)
    json.dump(out2, open(HERE / folio / 'lines2x' / 'crops_manifest.json', 'w'), indent=0)
    print(folio, len(out1), len(out2))
