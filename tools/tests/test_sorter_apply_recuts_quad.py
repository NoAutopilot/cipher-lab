#!/usr/bin/env python3
"""Offline test for free-corner (quad) and stray-ink (mask) recuts (SORTER-QUAD, owner 5 Oct 2026): sign_sorter_apply.py's
recuts.tsv export of {quad, mask} docs beside old {x, y, w, h} ones, and tools/sorter_apply_recuts.py's perspective cut,
mask painting and unchanged old-form behaviour. Synthetic image only.
Run: python3 tools/tests/test_sorter_apply_recuts_quad.py"""
import csv, json, sys, tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import numpy as np
from PIL import Image, ImageDraw
import sign_sorter_apply as sa
import sorter_apply_recuts as ar

fails = 0
def check(name, ok, extra=''):
    global fails
    print('PASS' if ok else 'FAIL', name, extra if not ok else ''); fails += not ok

# ---- library: a sheared quad warps to an upright tile; a rectangle quad equals the old crop; a stroke whitens its area
im = Image.new('L', (220, 110), 250); g = ImageDraw.Draw(im)
Q = [[50, 40], [90, 50], [90, 80], [50, 70]]                      # a sign slanting down to the right (a parallelogram)
g.polygon([tuple(p) for p in Q], fill=0)
g.ellipse((83, 41, 87, 45), fill=100)                             # neighbour ink inside the bounding box, above the slanted top
W, H = ar.quad_size(Q); top, bot, side = ar.margins(W, H)
check('quad_size: longer top/bottom edge x longer side', (W, H) == (41, 30), (W, H))
t = np.asarray(ar.crop_quad(im, Q))
check('quad cut: upright tile of the expected size', t.shape == (H + top + bot, W + 2 * side), t.shape)
inner = t[top + 2:top + H - 2, side + 2:side + W - 2]
check('quad cut: inside the quad is all ink, the neighbour blob is not in it', inner.max() < 40 and not ((inner > 80) & (inner < 140)).any(),
      (inner.min(), inner.max()))
check('quad cut: just above the warped top edge is paper (left of the blob)', t[top - 3, side + 2:side + 25].min() > 240)
bb = np.asarray(ar.crop_box(im, 50, 40, 40, 40))
check('control: the bounding box crop does hold the neighbour blob', ((bb > 80) & (bb < 140)).any())
R = [[50, 40], [90, 40], [90, 70], [50, 70]]
rq, rb = np.asarray(ar.crop_quad(im, R)).astype(int), np.asarray(ar.crop_box(im, 50, 40, 40, 30)).astype(int)
check('rectangle quad == the old crop_box at the same box (bilinear rounding: within 1 grey level)', rq.shape == rb.shape and np.abs(rq - rb).max() <= 1)
off = np.asarray(ar.crop_quad(im, [[2, 2], [30, 2], [30, 32], [2, 32]]))
check('quad cut off the page edge: padded with paper', off.shape == (30 + 27 + 10, 28 + 10) and off[0, 0] == 255)
sq = Image.new('L', (200, 100), 250); ImageDraw.Draw(sq).rectangle((50, 30, 89, 59), fill=0)
mk = np.asarray(ar.crop_quad(ar.paint_mask(sq, [{'r': 3, 'pts': [[60, 45], [70, 45]]}]), [[50, 30], [90, 30], [90, 60], [50, 60]]))
top2, _, side2 = ar.margins(40, 30)
check('mask: the stroke area is white', mk[top2 + 15, side2 + 10:side2 + 21].min() > 240 and mk[top2 + 15 - 2, side2 + 12] > 240,
      mk[top2 + 15, side2 + 8:side2 + 23])
check('mask: ink outside the stroke stays ink', mk[top2 + 15, side2 + 30] < 20 and mk[top2 + 5, side2 + 12] < 20)
check('mask: paint_mask leaves the source untouched', np.asarray(sq)[45, 65] == 0)

# ---- export: a quad + mask doc and an old {x, y, w, h} doc side by side
d = Path(tempfile.mkdtemp()); (d / 'pages').mkdir(); (d / 'db' / 'recuts').mkdir(parents=True)
pg = Image.new('L', (220, 110), 250); g = ImageDraw.Draw(pg)
g.polygon([tuple(p) for p in Q], fill=0); g.rectangle((130, 40, 150, 70), fill=0); g.rectangle((152, 50, 156, 60), fill=0)
pg.save(d / 'pages' / 'L01.png')
(d / 'signs.tsv').write_text('sid\tpage\tx\ty\tw\th\nL01_01\tL01\t50\t40\t40\t40\nL01_02\tL01\t130\t40\t20\t30\n')
(d / 'labels.tsv').write_text('sid\tsign\nL01_01\tA\nL01_02\tB\n')
docs = {'L01_01': {'sid': 'L01_01', 'page': 'L01', 'quad': Q, 'mask': [{'r': 2.5, 'pts': [[60, 55], [64, 57]]}, {'r': 1, 'pts': []}],
                   'x': 50, 'y': 40, 'w': 40, 'h': 40, 'old': [50, 40, 40, 40], 'at': '2026-10-05T10:00:00Z'},
        'L01_02': {'sid': 'L01_02', 'page': 'L01', 'x': 130, 'y': 40, 'w': 27, 'h': 30, 'old': [130, 40, 20, 30], 'at': '2026-10-05T10:01:00Z'},
        'Lq': {'sid': 'Lq', 'quad': [[1, 2], [3]], 'at': ''}}
for k, v in docs.items():
    (d / 'db' / 'recuts' / (k + '.json')).write_text(json.dumps(v))
sa.main(['--labels', str(d / 'labels.tsv'), '--db', str(d / 'db'), '--out', str(d / 'settled.tsv')])
rows = {r['tile']: r for r in csv.DictReader(open(d / 'recuts.tsv'), delimiter='\t')}
check('export: malformed quad doc without a box dropped', sorted(rows) == ['L01_01', 'L01_02'], sorted(rows))
q = rows['L01_01']
check('export: quad row carries quad, mask (empty stroke dropped) and its bounding box', json.loads(q['quad']) == Q
      and json.loads(q['mask']) == [{'r': 2.5, 'pts': [[60, 55], [64, 57]]}] and [q[k] for k in ('new_x', 'new_y', 'new_w', 'new_h')] == ['50', '40', '40', '40'])
check('export: old-form row leaves quad and mask empty', rows['L01_02']['quad'] == '' and rows['L01_02']['mask'] == '' and rows['L01_02']['new_w'] == '27')
nobox = sa.recut_rows([{'sid': 'z', 'quad': [[0, 0], [10, 1], [10, 9], [0, 8]]}])
check('export: a quad doc with no x y w h gets its bounding box', nobox and nobox[0][6:10] == [0, 0, 10, 9], nobox)

# ---- apply: the quad row is warped and masked, the old row is cut as before
rc = ar.main(['--recuts', str(d / 'recuts.tsv'), '--signs', str(d / 'signs.tsv'), '--pages', str(d / 'pages'), '--tiles', str(d / 'tiles')])
S = {r['sid']: r for r in csv.DictReader(open(d / 'signs.tsv'), delimiter='\t')}
check('apply: exit 0, both applied', rc == 0, rc)
t1 = np.asarray(Image.open(d / 'tiles' / 'L01_01.jpg'))
check('apply: quad tile is the warped size', t1.shape == (H + top + bot, W + 2 * side), t1.shape)
check('apply: quad tile carries the mask (a white hole in the ink)', t1[top + 2:top + H - 2, side + 2:side + W - 2].max() > 200
      and np.median(t1[top + 2:top + H - 2, side + 2:side + W - 2]) < 40)
check('apply: signs.tsv gets the quad bounding box', [S['L01_01'][k] for k in 'xywh'] == ['50', '40', '40', '40'])
t2 = Image.open(d / 'tiles' / 'L01_02.jpg')
check('apply: old-form row cut exactly as crop_box', t2.size == ar.crop_box(pg, 130, 40, 27, 30).size and [S['L01_02'][k] for k in 'xywh'] == ['130', '40', '27', '30'])
legacy = d / 'legacy.tsv'   # a recuts.tsv written before 5 Oct 2026 has no quad / mask columns at all
legacy.write_text('tile\tpage\told_x\told_y\told_w\told_h\tnew_x\tnew_y\tnew_w\tnew_h\tat\nL01_02\tL01\t130\t40\t20\t30\t130\t40\t27\t30\t\n')
check('apply: a pre-quad recuts.tsv (no quad column) still applies', ar.main(['--recuts', str(legacy), '--signs', str(d / 'signs.tsv'),
      '--pages', str(d / 'pages'), '--tiles', str(d / 'tiles')]) == 0)
bad = d / 'bad.tsv'
bad.write_text('\t'.join(sa.RECUT_COLS) + '\nL01_01\tL01\t50\t40\t40\t40\t50\t40\t40\t40\t\t[[1,2]]\t\n')
check('apply: a malformed quad cell is skipped, exit 2', ar.main(['--recuts', str(bad), '--signs', str(d / 'signs.tsv'), '--pages', str(d / 'pages'),
      '--tiles', str(d / 'tiles')]) == 2)
print('ALL PASS' if not fails else '%d FAILED' % fails); sys.exit(1 if fails else 0)
