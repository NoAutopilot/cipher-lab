#!/usr/bin/env python3
"""Offline test for tools/tx_prep.py (TXE-D, 9 Oct 2026): a synthetic grey page with three signs, one carrying a faint
tail outside its atlas box. render must write one tile per box per setting with a manifest; tight must grow to the
faint tail (ink-measured margin) and double the scale; gamma=0.5 must darken; thicken must add ink; invert must be
255 - plain; a single-channel source must mark the colour settings colour_non_test; sr4 must be 4x plain; lines must
split an over-wide crop with the stated overlap. No network, no model."""
import contextlib, io, json, os, sys, tempfile
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
import tx_prep as T  # noqa: E402


def _page(d):
    import cv2
    g = np.full((200, 400), 225, np.uint8)
    cv2.rectangle(g, (40, 60), (80, 120), 30, 4)              # sign 1 (box 40,60,41,61)
    cv2.line(g, (60, 120), (60, 150), 150, 2)                 # its faint tail, below the box, joined to it
    cv2.line(g, (160, 60), (200, 120), 30, 4)                 # sign 2
    cv2.circle(g, (290, 90), 25, 30, 3)                       # sign 3
    p = os.path.join(d, 'page.png')
    Image.fromarray(g).save(p)
    sig = 'sid\tpage\tline\tpos\tx\ty\tw\th\trh\trw\tdy\tmarks\n'
    sig += 'p1_01_001\tp1\t1\t1\t38\t58\t45\t65\t1\t1\t0\t\n'
    sig += 'p1_01_002\tp1\t1\t2\t158\t58\t45\t65\t1\t1\t0\t\n'
    sig += 'p1_01_003\tp1\t1\t3\t263\t63\t55\t55\t1\t1\t0\t\n'
    s = os.path.join(d, 'signs.tsv')
    open(s, 'w').write(sig)
    return p, s


def _q(f, *a):
    with contextlib.redirect_stdout(io.StringIO()):
        return f(*a)


def main():
    d = tempfile.mkdtemp()
    page, signs = _page(d)
    out = os.path.join(d, 'tiles')
    sets = ['plain', 'tight', 'gamma=0.5', 'thicken=1', 'invert', 'channel=R', 'sep', 'sr4', 'combo']
    argv = ['render', '--page', page, '--boxes', signs, '--page-name', 'p1', '--out', out, '--median-h', '60']
    for s in sets:
        argv += ['--setting', s]
    _q(T.main, argv)
    man = {s: json.load(open(os.path.join(out, s, 'manifest.json'))) for s in sets}
    for s in sets:
        assert set(man[s]['tiles']) == {'p1_01_001', 'p1_01_002', 'p1_01_003'}, s
        assert man[s]['parameters']['scale'] == T.SETTINGS[s]['scale'], s
    load = lambda s, sid='p1_01_001': np.array(Image.open(os.path.join(out, s, sid + '.png')).convert('L')).astype(float)
    # tight: the faint tail (to y=150) is outside the source box (ends y=123) and must be inside the tile
    t = man['tight']['tiles']['p1_01_001']
    assert t['ink_extent'][3] >= 148, t
    assert t['tile_box'][3] >= 150, t
    assert man['tight']['parameters']['scale'] == 2
    # plain tile: box grown 25% a side
    pt = man['plain']['tiles']['p1_01_002']['tile_box']
    assert pt[0] == 158 - 11 and pt[2] == 158 + 45 + 11, pt
    # gamma 0.5 darkens, thicken adds dark pixels, invert = 255 - plain
    assert load('gamma=0.5').mean() < load('plain').mean() - 5
    assert (load('thicken=1') < 100).sum() > (load('plain') < 100).sum()
    assert np.abs(load('invert') - (255 - load('plain'))).max() == 0
    # single-channel source: colour settings are flagged non-tests; channel=R equals plain
    assert man['channel=R'].get('colour_non_test') and man['sep'].get('colour_non_test')
    assert np.abs(load('channel=R') - load('plain')).max() == 0
    # sr4 is 4x plain
    a, b = Image.open(os.path.join(out, 'plain', 'p1_01_003.png')), Image.open(os.path.join(out, 'sr4', 'p1_01_003.png'))
    assert b.size == (4 * a.width, 4 * a.height)
    # tile_bitmap: the plain tile's re-binarised bitmap is non-empty and its size ratios are scale-free
    bm, rh, rw = T.tile_bitmap(os.path.join(out, 'plain', 'p1_01_003.png'), man['plain']['tiles']['p1_01_003'], 60)
    bm4, rh4, rw4 = T.tile_bitmap(os.path.join(out, 'sr4', 'p1_01_003.png'), man['sr4']['tiles']['p1_01_003'], 60)
    assert bm.max() > 0 and abs(rh - rh4) < 0.1 and abs(rw - rw4) < 0.1, (rh, rh4, rw, rw4)
    # lines: an over-wide crop is split in two with the overlap recorded
    cr = os.path.join(d, 'crops')
    os.makedirs(cr)
    Image.fromarray(np.full((60, 1400), 220, np.uint8)).save(os.path.join(cr, 'p1_L01_s1.jpg'))
    json.dump({'iiif_lines': [{'crop': 'p1_L01_s1.jpg', 'box': [0, 0, 1400, 60], 'source_url': ''}]},
              open(os.path.join(cr, 'manifest.json'), 'w'))
    o2 = os.path.join(d, 'lines')
    _q(T.main, ['lines', '--crops', cr, '--setting', 'sr2', '--out', o2])
    m2 = json.load(open(os.path.join(o2, 'manifest.json')))
    assert [m['crop'] for m in m2] == ['p1_L01_s1a.png', 'p1_L01_s1b.png'], m2
    assert m2[0]['width'] + m2[1]['width'] - 2800 == 100, m2
    assert 'overlap' in open(os.path.join(o2, 'crops_note.md')).read()
    # lines --segments: four segments sharing --overlap, under --max-w, covering the whole crop
    o3 = os.path.join(d, 'lines4')
    _q(T.main, ['lines', '--crops', cr, '--setting', 'sr4', '--out', o3, '--segments', '4', '--overlap', '200'])
    m3 = json.load(open(os.path.join(o3, 'manifest.json')))
    assert [m['crop'] for m in m3] == ['p1_L01_s1_q%d.png' % k for k in (1, 2, 3, 4)], m3
    assert all(m['width'] <= 2500 for m in m3) and sum(m['width'] for m in m3) - 3 * 200 >= 5600, m3
    assert 'segments' in open(os.path.join(o3, 'crops_note.md')).read()
    print('test_tx_prep: ok')


if __name__ == '__main__':
    main()
