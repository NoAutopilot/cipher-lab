#!/usr/bin/env python3
"""Offline test for tools/iiif_lines.py --views / --views-of (TX-VIEWS, 4 Oct 2026).
1. Every named view is written for every crop under OUT/views/<view>/, with a manifest entry under iiif_lines_views.
2. Geometry: pad grows the crop (content shifted, not scaled), s080/s125 rescale by 0.8/1.25, warp and contrast keep size.
3. warp is seeded from the crop name: a re-run is byte-identical, and the warp actually moves pixels (not a copy).
4. --views 2 takes the first two of the default order; an unknown view name is refused.
Run: python3 tools/tests/test_iiif_views.py"""
import os, sys, tempfile, json, hashlib
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import numpy as np
from PIL import Image, ImageDraw
import iiif_lines as il

fails = 0
def check(ok, what):
    global fails
    fails += not ok
    print('PASS' if ok else 'FAIL', what)

tmp = tempfile.mkdtemp()
crop = os.path.join(tmp, 'x_L01_s1.jpg')
im = Image.new('RGB', (400, 60), (235, 225, 205))
d = ImageDraw.Draw(im)
for k in range(8):
    d.ellipse([20 + 45 * k, 15, 50 + 45 * k, 45], outline=(30, 20, 10), width=3)
im.save(crop, quality=95)
out = os.path.join(tmp, 'out')
r = il.main(['--out', out, '--views', 'pad,s080,s125,warp,contrast', '--views-of', crop])
check(len(r['views']) == 5, 'five views written for one crop')
sz = {v: Image.open(os.path.join(out, 'views', v, 'x_L01_s1.jpg')).size for v in il.VIEW_ORDER}
check(sz['pad'][0] > 400 and sz['pad'][1] > 60, 'pad grows the canvas %s' % (sz['pad'],))
check(sz['s080'] == (320, 48) and sz['s125'] == (500, 75), 's080/s125 rescale %s %s' % (sz['s080'], sz['s125']))
check(sz['warp'] == (400, 60) and sz['contrast'] == (400, 60), 'warp/contrast keep size')
man = json.load(open(os.path.join(out, 'manifest.json')))
check(len(man['iiif_lines_views']) == 5 and all(e['from_crop'].endswith('x_L01_s1.jpg') for e in man['iiif_lines_views']),
      'manifest has one iiif_lines_views entry per view')
h1 = hashlib.md5(open(os.path.join(out, 'views', 'warp', 'x_L01_s1.jpg'), 'rb').read()).hexdigest()
il.main(['--out', out, '--views', 'warp', '--views-of', crop])
h2 = hashlib.md5(open(os.path.join(out, 'views', 'warp', 'x_L01_s1.jpg'), 'rb').read()).hexdigest()
check(h1 == h2, 'warp re-run byte-identical (seeded from the crop name)')
a0 = np.asarray(Image.open(crop).convert('L')).astype(int)
aw = np.asarray(Image.open(os.path.join(out, 'views', 'warp', 'x_L01_s1.jpg')).convert('L')).astype(int)
check(np.abs(a0 - aw).mean() > 1.0, 'warp moves pixels (mean abs diff %.2f)' % np.abs(a0 - aw).mean())
check(il.parse_views('2') == ['pad', 's125'], '--views 2 = first two of the default order')
try:
    il.parse_views('blur'); ok = False
except ValueError:
    ok = True
check(ok, 'unknown view refused')
print('iiif_views: all tests pass' if not fails else 'iiif_views: %d FAILED' % fails)
sys.exit(1 if fails else 0)
