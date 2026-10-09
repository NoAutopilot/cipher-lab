#!/usr/bin/env python3
"""Offline test for tools/tx_tile_gate.py (TXE-F): a synthetic page with a wide two-valley box (joined), a box cut by
its band (bad-crop), a small round blob (blot) and normal signs (good); score labels each as named, recut splits the
joined box in two and grows the cut one to its own ink. No network, no model."""
import os
import sys
import tempfile

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import tx_tile_gate as g  # noqa: E402


def ring(a, x, y, w, h, t=4):
    yy, xx = np.mgrid[0:h, 0:w]
    cy, cx = (h - 1) / 2, (w - 1) / 2
    r = np.sqrt(((yy - cy) / (h / 2)) ** 2 + ((xx - cx) / (w / 2)) ** 2)
    a[y:y + h, x:x + w][(r <= 1.0) & (r >= 1.0 - 2.0 * t / min(w, h))] = 0


def build():
    a = np.full((200, 700), 255, np.uint8)
    boxes = []
    for i, x in enumerate((20, 80, 140, 200, 260)):                     # five normal signs, 40 x 40
        ring(a, x, 35, 40, 40)
        boxes.append(('n%d' % i, x, 35, 40, 40))
    # joined: three bars 12 px wide joined by a thin top stroke -> 2 interior valleys, 100 px wide (> 1.8 x 40)
    for bx in (330, 374, 418):
        a[35:75, bx:bx + 12] = 0
    a[35:38, 330:430] = 0
    boxes.append(('join', 330, 35, 100, 40))
    # bad-crop: a vertical stroke 60..130 whose box (70..110) runs below the band bottom (100)
    a[60:130, 480:490] = 0
    a[60:66, 470:500] = 0
    boxes.append(('cut', 468, 70, 34, 40))
    # blot: a filled disk in an 18 x 18 box with a 1 px margin (ink mass ~0.68, 1 component, aspect 1, h 18 < 0.6 x 40);
    # a box drawn tight on a solid disk touches 40% of its perimeter and the registered rule order labels it bad-crop
    yy, xx = np.mgrid[0:18, 0:18]
    a[50:68, 560:578][((yy - 8.5) ** 2 + (xx - 8.5) ** 2) <= 8.4 ** 2] = 0
    boxes.append(('blot', 560, 50, 18, 18))
    signs = [dict(sid=s, page='p', line='1', pos='', x=x, y=y, w=w, h=h, rh='1', rw='1') for s, x, y, w, h in boxes]
    bands = {1: [(0, 20, 700, 100)]}
    return a, signs, bands


def test_score_labels():
    a, signs, bands = build()
    rows, meta = g.score_page(signs, a, bands)
    lab = {r['sid']: r['label'] for r in rows}
    assert all(lab['n%d' % i] == 'good' for i in range(5)), lab
    assert lab['join'] == 'joined', (lab, [r for r in rows if r['sid'] == 'join'])
    assert lab['cut'] == 'bad-crop', lab
    assert lab['blot'] == 'blot', (lab, [r for r in rows if r['sid'] == 'blot'])
    cut = [r for r in rows if r['sid'] == 'cut'][0]
    assert cut['band'] == 'cut' and cut['own_y'] == 60 and cut['own_h'] == 70, cut


def test_recut():
    a, signs, bands = build()
    rows, meta = g.score_page(signs, a, bands)
    t = {r['sid']: {k: str(v) for k, v in r.items()} for r in rows}
    parts = g.recut_box(a, meta['thr'], t['join'])
    assert len(parts) == 2 and parts[0][4] == 'a' and parts[1][4] == 'b'
    assert parts[0][0] == 330 and parts[0][2] + parts[1][2] == 100 and 20 < parts[0][2] < 80, parts
    (x, y, w, h, _), = g.recut_box(a, meta['thr'], t['cut'])
    assert y < 60 and y + h > 130 and h > 70, (x, y, w, h)          # grown past the band to the full stroke + margin
    from PIL import Image
    img = g.render_tile(Image.fromarray(a), meta['thr'], (x, y, w, h), [(400, 35, 30, 40)], 2)
    assert img.height >= 2 * h


def test_sheet_and_resolve():
    a, signs, bands = build()
    from PIL import Image
    d = tempfile.mkdtemp()
    img = g.render_tile(Image.fromarray(a), 128, (20, 35, 40, 40), [], 2)
    rows = [dict(row=i + 1, line='p_L01', pos=str(i + 1), L_sign='T1', sid='n', label='bad-crop', part='', img=img)
            for i in range(3)]
    sheets = g.make_sheets(rows, os.path.join(d, 'u'), 2)
    assert len(sheets) == 2 and os.path.exists(sheets[0])
    # resolve: a units README, a line read, reads files
    open(os.path.join(d, 'README.md'), 'w').write('- u: p_L01\n')
    g.wr(os.path.join(d, 'L.tsv'), ['line', 'pos', 'sign'], [dict(line='p_L01', pos=str(i), sign='T1') for i in (1, 2, 3, 4)])
    g.wr(os.path.join(d, 'u', 'reads_01.tsv'), ['row', 'sign_id', 'conf'], [dict(row=1, sign_id='T9', conf='H'),
                                                                          dict(row=2, sign_id='?', conf='L')])
    g.wr(os.path.join(d, 'u', 'reads_02.tsv'), ['row', 'sign_id', 'conf'], [dict(row=1, sign_id='T7', conf='M')])
    out = os.path.join(d, 'out.tsv')
    g.main(['resolve', '--unit', 'u', '--dir', d, '--units', os.path.join(d, 'README.md'),
            '--line-read', os.path.join(d, 'L.tsv'), '--pass-out', out])
    got = [r['sign'] for r in g.rd(out)]
    assert got == ['T9', 'T1', 'T7', 'T1'], got


if __name__ == '__main__':
    test_score_labels(); test_recut(); test_sheet_and_resolve()
    print('ok')
