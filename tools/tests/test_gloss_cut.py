#!/usr/bin/env python3
"""Offline test for tools/gloss_cut.py (TXE2-RECUT2, 9 Oct 2026). No network.
Must catch: a gloss letter above the row whose stroke is ink-joined to a cipher sign (one component, the shape
iiif_lines --mask-neighbours keeps whole) -- its pixels beyond the envelope are replaced by paper.
Must not block: ink inside the envelope (the cipher row's core and UP/DOWN margins) is untouched, pixel for pixel;
and --stem-width keeps a thin stroke that touches the envelope while still removing a wide piece.
Run: python3 tools/tests/test_gloss_cut.py"""
import contextlib, io, os, sys, tempfile
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import gloss_cut as gc
from PIL import Image

fails = 0
def check(ok, what):
    global fails
    fails += not ok
    print('PASS' if ok else 'FAIL', what)

H, W = 120, 600
a = np.full((H, W, 3), 225, np.uint8)
for x in range(20, 580, 30):          # cipher row: blobs in rows 50-75
    a[50:76, x:x + 18] = 40
a[10:30, 300:330] = 40                # gloss letter (wide) above, rows 10-29
a[30:50, 312:316] = 40                # its stroke joined to the cipher blob below
a[36:50, 100:103] = 40                # a thin ascender of a sign at x=100 (touches the envelope)
img = Image.fromarray(a)
res, top, bot, med, rem, kept, removed = gc.cut(img, up=6, down=6)
r = np.asarray(res.convert('L'))
check(abs(med[0] - 50) <= 2 and abs(med[1] - 75) <= 2, f'core band found at rows 50-75 +-2 (got {med})')
check((r[10:30, 300:330] > 150).all(), 'joined gloss letter beyond the envelope is whitened')
check((r[50:76, 20:38] < 100).all() and (r[50:76, 290:308] < 100).all(), 'cipher core ink untouched')
check((r[44:50, 312:316] < 100).all(), 'joined stroke inside the UP margin kept')
check((r[36:41, 100:103] > 150).all(), 'thin ascender beyond the envelope cut without --stem-width')
res2, *_ = gc.cut(img, up=6, down=6, stem_width=6)
r2 = np.asarray(res2.convert('L'))
check((r2[36:41, 100:103] < 100).all(), '--stem-width keeps a thin stroke touching the envelope')
check((r2[10:30, 300:330] > 150).all(), '--stem-width still removes the wide gloss letter')
with tempfile.TemporaryDirectory() as d:
    p = os.path.join(d, 'c.png'); img.save(p)
    with contextlib.redirect_stdout(io.StringIO()):
        gc.main([p, '--out', os.path.join(d, 'o'), '--debug'])
    check(os.path.exists(os.path.join(d, 'o', 'c.png')) and os.path.exists(os.path.join(d, 'o', 'c_cut_debug.jpg'))
          and os.path.exists(os.path.join(d, 'o', 'gloss_cut.tsv')), 'main writes crop, debug overlay and tsv')
print('ALL PASS' if not fails else f'{fails} FAIL')
sys.exit(1 if fails else 0)
