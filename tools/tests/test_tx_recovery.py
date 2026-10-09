"""Offline test for tools/tx_recovery.py (TXE-G, 9 Oct 2026): recovery renderings and the box re-derivation."""
import os, sys, tempfile
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import tx_recovery as t


def page(faint=False):
    """Paper 210 with a gentle gradient, one heavy bar and one hairline bar (the 'thin stroke' case)."""
    g = np.full((200, 300), 210, np.uint8) + np.linspace(0, 30, 300, dtype=np.uint8)[None, :]
    g[50:150, 40:52] = 60                       # heavy stroke, 12 px
    g[50:150, 200:202] = 150 if faint else 60   # hairline, 2 px
    return g


def test_plain_and_sauvola_find_both_strokes():
    for s in ('plain', 'sauvola'):
        m = t.page_mask(page(), s, 60.0)
        assert m[100, 45] == 1 and m[100, 200] == 1, s
        assert m[10, 120] == 0, s               # paper stays paper despite the gradient


def test_swn_thickens_only_the_thin_box():
    m = t.page_mask(page(), 'plain', 60.0)
    boxes = [(30, 40, 32, 120), (32, 40, 30, 120), (190, 40, 22, 120)]   # two heavy boxes, one hairline
    thick, _, thin = t.box_masks(m, boxes, 'swn')
    base_thick, _, base_thin = t.box_masks(m, boxes, 'plain')
    assert thick.sum() == base_thick.sum()      # above the median width: untouched
    assert thin.sum() > base_thin.sum()         # below it: one dilation


def test_stroke_width():
    m = np.zeros((40, 40), np.uint8)
    m[5:35, 10:16] = 1
    assert 3 <= t.stroke_width(m) <= 7
    assert t.stroke_width(np.zeros((5, 5), np.uint8)) == 0.0


def test_render_is_ink_black_on_white_and_same_size():
    for s in t.SETTINGS:
        r = t.render(page(), s, 60.0)
        assert r.shape == (200, 300) and r.dtype == np.uint8
        assert r[100, 45] < r[10, 120], s


def test_bitmap_and_bench_recipe():
    b = t.bitmap(np.ones((10, 20), np.uint8))
    assert b.shape == (48, 48) and b[24, 24] == 255 and b[2, 24] == 0
    with tempfile.TemporaryDirectory() as d:
        tk = os.path.join(d, 'topk.tsv')
        with open(tk, 'w') as f:
            f.write('page\tline\tbox\tpos\tx\tk1\n')
            f.write('f1\t1\tf1_01_002\t2\t90\tT2\nf1\t1\tf1_01_001\t1\t10\tT1\nf1\t1\tf1_01_003\t3\t50\t_\n'
                    'f2\t1\tf2_01_001\t1\t5\tT9\n')
        out = os.path.join(d, 'b.tsv')
        assert t.bench(tk, ['f1_01_'], out) == 2
        lines = open(out).read().split('\n')
        assert lines[1] == 'f1_L01\t10\tT1' and lines[2] == 'f1_L01\t90\tT2'


if __name__ == '__main__':
    for n, f in list(globals().items()):
        if n.startswith('test_'):
            f()
    print('ok')
