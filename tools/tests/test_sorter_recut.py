"""Offline test for tools/sorter_recut.py (synthetic sloped line, no files outside a temp dir)."""
import sys, tempfile
from pathlib import Path
import numpy as np
from PIL import Image
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import sorter_recut as sr

W, H, PITCH = 1600, 600, 100


def page(n=20, gap=70, slope=0.06):
    g = np.full((H, W), 235, np.uint8); xs = []
    for k in range(n):
        x = 60 + k * gap; y = int(300 + slope * x)
        g[y - 22:y + 22, x:x + 6] = 60; g[y - 22:y - 16, x:x + 30] = 60      # a 30 px wide "sign" (stem + bar)
        xs.append(x + 15)
    return g, xs, np.array([300 + slope * x for x in range(W)], float)


def test_segment_one_tile_per_sign():
    g, xs, tr = page(); cfg = sr.Cfg(pitch=PITCH, half=80)
    boxes, wmed = sr.segment(sr.deskew(g, tr, cfg), cfg)
    assert len(boxes) == len(xs), len(boxes)
    assert all(abs((b[0] + b[2]) / 2 - x) < 4 for b, x in zip(boxes, xs))


def test_touching_signs_are_split():
    g, xs, tr = page(gap=40); y = int(300 + .06 * 90)
    g[y - 22:y - 16, 88:102] = 60                                     # join signs 1 and 2 by their bars (one 70 px blob)
    cfg = sr.Cfg(pitch=PITCH, half=80)
    boxes, _ = sr.segment(sr.deskew(g, tr, cfg), cfg)
    assert len(boxes) == len(xs), len(boxes)


def test_align_and_run():
    assert sr.align([10, 50, 90], [12, 88], 45) == {0: 0, 2: 1}
    g, xs, tr = page(); cols = [[('S1', 'S1')] * len(xs)]
    with tempfile.TemporaryDirectory() as d:
        cfg = sr.Cfg(pitch=PITCH, half=80, nclu=3)
        tiles, stats = sr.run(g, [tr], ['p_L01'], cols, [xs], d, Path(d) / 'pages', cfg)
        assert stats[0][1] == len(xs) and stats[0][3] == len(xs)
        assert all(t['sign'] == 'S1' for t in tiles)
        assert sr.small_pile(d) == 0 and (Path(d) / 'labels_small.tsv').exists()


if __name__ == '__main__':
    for k, f in list(globals().items()):
        if k.startswith('test_'): f(); print('ok', k)
