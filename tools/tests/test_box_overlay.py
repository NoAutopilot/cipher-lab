#!/usr/bin/env python3
"""Offline test for tools/iiif_lines.py --box-overlay / --random-geometry (TXE4-8 BOX-ANCHOR, 12 Oct 2026).
1. A synthetic two-segment line (s1, s2 crops sharing an overlap) with 8 boxes: every overlay is the crop plus the
   number band (crop pixels untouched), one overlay per page, overlay_manifest.tsv counts 8 boxes.
2. --random-geometry: the same per-line count, every box inside the line's ink extent and the pen band, each on the
   page that holds its centre; a second seed gives a different set; the can-vary share is computable.
3. The overlay palette passes tools/cvd_check.py (PASS, not WARN or FAIL).
Must NOT block: a box file whose lines are not all in --overlay-lines (the others are skipped, not an error).
Run: python3 tools/tests/test_box_overlay.py"""
import os, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import iiif_lines as il
from PIL import Image, ImageDraw
import numpy as np

fails = 0
def check(ok, what):
    global fails
    fails += not ok
    print('PASS' if ok else 'FAIL', what)

with tempfile.TemporaryDirectory() as td:
    crops = os.path.join(td, 'images'); os.makedirs(crops)
    W, H, OV = 600, 100, 100     # two 600 px crops overlapping by 100 px: line coordinates 0..1100
    line = np.full((H, W + W - OV), 235, dtype=np.uint8)
    rng = np.random.RandomState(3)
    pen = []  # (x_line, w)
    x = 40
    for i in range(8):
        w = int(rng.randint(30, 60)); line[30:70, x:x + w] = 20; pen.append((x, w)); x += w + int(rng.randint(15, 40))
    Image.fromarray(line[:, :W]).save(os.path.join(crops, 'p_L01_s1.jpg'), quality=95)
    Image.fromarray(line[:, W - OV:]).save(os.path.join(crops, 'p_L01_s2.jpg'), quality=95)
    rows = []
    for i, (xl, w) in enumerate(pen, 1):
        page, x0 = ('L01_s1', 0) if xl + w <= W else ('L01_s2', W - OV)
        rows.append(dict(line='L01', pos=i, sid=f'L01_{i:03d}', page=page, x_line=xl, x=xl - x0, y=28, w=w, h=44))
    rows.append(dict(line='L99', pos=1, sid='L99_001', page='L99_s1', x_line=5, x=5, y=0, w=10, h=10))  # skipped line
    bp = os.path.join(td, 'boxes.tsv'); il.write_box_rows(rows, bp)
    out = os.path.join(td, 'ov')
    class A: pass
    a = A(); a.box_overlay = bp; a.overlay_out = out; a.overlay_lines = 'L01'; a.prefix = 'p_'; a.out = crops
    a.random_geometry = None; a.ink = 170; a.quality = 92
    res = il.run_box_overlay(a)
    man = res['overlays']
    check(len(man) == 2 and sum(m['boxes'] for m in man) == 8, '1. two overlays, 8 numbered boxes (L99 skipped)')
    ov = Image.open(os.path.join(out, 'p_L01_s1_boxes.jpg'))
    check(ov.size == (W, H + il.OVERLAY_BAND), '1. overlay = crop + number band')
    src = np.asarray(Image.open(os.path.join(crops, 'p_L01_s1.jpg')).convert('L')).astype(int)
    top = np.asarray(ov.convert('L'))[:H].astype(int)
    inside = np.abs(top[32:68, pen[0][0] + 3:pen[0][0] + pen[0][1] - 3] - src[32:68, pen[0][0] + 3:pen[0][0] + pen[0][1] - 3]).mean()
    check(inside < 6, '1. ink inside a box is not painted over (mean abs diff %.1f)' % inside)
    check(os.path.exists(os.path.join(out, 'overlay_manifest.tsv')), '1. overlay_manifest.tsv written')
    # 2. random geometry
    a.random_geometry = 7; a.overlay_out = os.path.join(td, 'ovr')
    res_r = il.run_box_overlay(a)
    rr = [r for r in res_r['rows'] if r['line'] == 'L01']
    check(len(rr) == 8, '2. random set has the pen count (8)')
    e0, e1 = pen[0][0], pen[-1][0] + pen[-1][1]
    check(all(e0 <= r['x_line'] and r['x_line'] + r['w'] <= e1 + 1 for r in rr), '2. every random box inside the ink extent')
    check(all(r['y'] == 28 and r['h'] == 44 for r in rr), '2. random boxes take the pen band as height')
    check(all((r['page'] == 'L01_s1') == (r['x_line'] + r['w'] / 2 < W) or r['page'] == 'L01_s2' for r in rr),
          '2. each random box on the page holding its centre')
    rr2 = il.random_geometry([r for r in rows if r['line'] == 'L01'], crops, 8, 'p_')
    check([r['x_line'] for r in rr2] != [r['x_line'] for r in rr], '2. another seed gives another set')
    share, far, tot = il.box_iou_share(rr, [r for r in rows if r['line'] == 'L01'])
    check(tot == 8 and 0.0 <= share <= 1.0, '2. can-vary share computable (%d/%d)' % (far, tot))
    same, _, _ = il.box_iou_share([r for r in rows if r['line'] == 'L01'], [r for r in rows if r['line'] == 'L01'])
    check(same == 0.0, '2. the pen set against itself has can-vary share 0')
    # 3. palette
    pal = il.overlay_palette_check()
    check(pal['verdict'] == 'PASS', '3. overlay palette passes cvd_check (%s)' % pal['verdict'])
print('box_overlay test:', 'FAIL' if fails else 'OK', fails)
sys.exit(1 if fails else 0)
