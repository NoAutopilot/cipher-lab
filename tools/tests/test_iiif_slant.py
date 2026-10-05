#!/usr/bin/env python3
"""Offline test for tools/iiif_lines.py --deskew and --mask-neighbours (SLANT-CROP, 5 Oct 2026). No network.
1. label_components: diagonal touch joins (8-connectivity), a one-pixel gap separates, counts match.
2. Synthetic page, 6 lines of blobs sloping b=0.03 over 2000 px (60 px drift, pitch 100): --deskew fits b within 0.004,
   and in the rotated crop the line's ink centroid sits within 8 px of the crop's middle row at BOTH ends, while the
   fixed-y crop's right end is off by more than 20 px.
3. --mask-neighbours on the same page with one tall mark per line (reaching 75 px below its line centre, past the band
   edge): every tall mark of the cut line is kept whole (its pixels all present), the neighbour lines' ink in the
   margin rows is removed, and the manifest records removed/kept counts.
4. Neither flag given: crops and manifest exactly as before (no deskew_deg, no mask).
Run: python3 tools/tests/test_iiif_slant.py"""
import contextlib, io, os, shutil, sys, tempfile
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import iiif_lines as il
from PIL import Image, ImageDraw

fails = 0
def check(ok, what):
    global fails
    fails += not ok
    print('PASS' if ok else 'FAIL', what)

def run(*args):
    with contextlib.redirect_stdout(io.StringIO()):
        return il.main(list(args))

# 1. components
m = np.zeros((6, 8), bool)
m[0, 0] = m[1, 1] = True            # diagonal touch: one component
m[4, 4] = m[4, 6] = True            # gap of one column: two components
lab, n = il.label_components(m)
check(n == 3 and lab[0, 0] == lab[1, 1] and lab[4, 4] != lab[4, 6], f'label_components: {n} components (want 3)')
m2 = np.zeros((5, 5), bool); m2[1:4, 1:4] = True; m2[2, 2] = False
lab2, n2 = il.label_components(m2)
check(n2 == 1, 'label_components: a ring is one component')

tmp = tempfile.mkdtemp()
try:
    W, H, pitch, b = 2000, 700, 100, 0.03
    im = Image.new('RGB', (W, H), (235, 225, 200)); d = ImageDraw.Draw(im)
    centres0 = [80 + pitch * i for i in range(6)]
    tall = {}                                   # line index -> tall-mark box
    for li, c0 in enumerate(centres0):
        x = 60
        k = 0
        while x < W - 80:
            y = c0 + b * x
            d.ellipse([x, y - 12, x + 26, y + 12], fill=(30, 25, 20))
            if k == 7:                          # one tall descending stroke per line
                bx = [x + 34, int(y) - 10, x + 42, int(y) + 75]
                d.rectangle(bx, fill=(30, 25, 20)); tall[li] = bx; x += 16
            x += 26 + 30; k += 1
    page = os.path.join(tmp, 'slant.jpg'); im.save(page, quality=95)

    # 2. deskew
    out = os.path.join(tmp, 'd')
    r = run('--image', page, '--out', out, '--prefix', 'd', '--deskew', '200', '--only-lines', '3')
    fb = r['fits'][3]['b']
    check(abs(fb - b) < 0.004, f'--deskew fit b={fb:.4f} (truth {b})')
    e = r['entries'][0]
    crop = np.asarray(Image.open(os.path.join(out, e['crop'])).convert('L')) < 120
    hgt = crop.shape[0]
    def centroid(cols):
        # ink rows of the strongest run near the middle (the cut line), weighted by ink count
        w = crop[:, cols].sum(axis=1).astype(float)
        mid = hgt // 2
        sl = slice(max(0, mid - 30), mid + 30)
        ys = np.arange(hgt)[sl]
        return float((ys * w[sl]).sum() / max(1, w[sl].sum()))
    lc, rc = centroid(slice(80, 400)), centroid(slice(crop.shape[1] - 400, crop.shape[1] - 80))
    check(abs(lc - hgt / 2) < 8 and abs(rc - hgt / 2) < 8,
          f'deskewed crop: line centroid {lc:.0f} / {rc:.0f} px at left / right vs middle {hgt / 2:.0f}')
    check('deskew_deg' in e and abs(e['deskew_deg'] - np.degrees(np.arctan(b))) < 0.25, f"manifest deskew_deg {e.get('deskew_deg')}")
    out_f = os.path.join(tmp, 'f')
    r = run('--image', page, '--out', out_f, '--prefix', 'f', '--only-lines', '3')
    fc = np.asarray(Image.open(os.path.join(out_f, r['entries'][0]['crop'])).convert('L')) < 120
    top, bot, _ = r['bands'][2]
    # fixed-y crop: where is line 3's ink at the right end relative to the band middle
    ytrue = centres0[2] + b * (W - 240)
    check(abs(ytrue - (top + bot) / 2) > 20, f'fixed-y band middle is {abs(ytrue - (top + bot) / 2):.0f} px off the line at the right end')

    # 3. mask
    out_m = os.path.join(tmp, 'm')
    r = run('--image', page, '--out', out_m, '--prefix', 'm', '--deskew', '200', '--mask-neighbours', '--only-lines', '3')
    e = r['entries'][0]
    mk = e.get('mask', {})
    cm = np.asarray(Image.open(os.path.join(out_m, e['crop'])).convert('L')) < 120
    bt, bb_ = mk.get('band_rows', [0, 0])
    above = cm[:max(0, bt - 4)].sum()
    below_cols = np.ones(cm.shape[1], bool)
    # the tall mark of line 3 is the only ink allowed below the band: its columns in crop coordinates
    tx0, _, tx1, _ = tall[2]
    below_cols[max(0, tx0 - 6):tx1 + 6] = False
    below = cm[bb_ + 4:, below_cols].sum()
    check(mk.get('removed', 0) > 0 and above == 0 and below == 0,
          f"--mask-neighbours: removed {mk.get('removed')} components; ink left above band {above}, below band (bar the tall mark) {below}")
    tall_ink = cm[bb_ + 4:, max(0, tx0 - 6):tx1 + 6].sum()
    check(tall_ink > 50,
          f'tall mark of the cut line kept whole past the band edge ({tall_ink} px below the band)')
    # unmasked but taller crop takes in the neighbours (the control for the check above)
    out_u = os.path.join(tmp, 'u')
    r = run('--image', page, '--out', out_u, '--prefix', 'u', '--deskew', '200', '--slope-margin', str(mk.get('margin', 40)), '--only-lines', '3')
    cu = np.asarray(Image.open(os.path.join(out_u, r['entries'][0]['crop'])).convert('L')) < 120
    check(cu[:max(0, bt - 4)].sum() > 0, 'control: the same taller crop without the mask holds neighbour ink above the band')

    # 4. default unchanged
    r = run('--image', page, '--out', os.path.join(tmp, 'n'), '--prefix', 'n', '--only-lines', '3')
    e = r['entries'][0]
    check('deskew_deg' not in e and 'mask' not in e and e['method'] == 'tools/iiif_lines.py row ink profile',
          'no flags: method and manifest unchanged')
finally:
    shutil.rmtree(tmp)
print('iiif_slant: all tests pass' if not fails else f'iiif_slant: {fails} FAILED')
sys.exit(1 if fails else 0)
