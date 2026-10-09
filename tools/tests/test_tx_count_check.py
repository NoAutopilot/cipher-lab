"""Offline test for tools/tx_count_check.py (LANE TX-ENGINEER-2 X19, 9 Oct 2026): synthetic strip, pen-lift merge."""
import os, sys, json, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import tx_count_check as C


def test_count_blobs_with_pen_lift():
    import numpy as np
    from PIL import Image
    a = np.full((40, 400), 255, np.uint8)
    xs = [10, 60, 110, 160, 210]
    for x in xs:
        a[12:28, x:x + 20] = 0
    a[12:28, 222:224] = 255                  # a 2 px pen lift inside the last sign
    with tempfile.TemporaryDirectory() as d:
        Image.fromarray(a[:, :250]).save(os.path.join(d, 'f1_L01_s1.png'))
        Image.fromarray(a[:, 150:]).save(os.path.join(d, 'f1_L01_s2.png'))
        json.dump({'iiif_lines': [{'crop': 'f1_L01_s1.png', 'box': [0, 0, 250, 40]},
                                  {'crop': 'f1_L01_s2.png', 'box': [150, 0, 400, 40]}]},
                  open(os.path.join(d, 'manifest.json'), 'w'))
        R = C.line_runs([os.path.join(d, 'manifest.json')])
        assert len(R['f1_L01']) == 6, R          # raw runs split the pen lift
        assert C.count_from_runs(R['f1_L01'], 0.5) == 5
        assert C.count_from_runs(R['f1_L01'], 0.0) == 6


if __name__ == '__main__':
    test_count_blobs_with_pen_lift(); print('ok')
