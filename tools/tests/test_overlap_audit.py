"""Offline test for tools/overlap_audit.py (synthetic crops; no network, no repo files)."""
import contextlib
import io
import json
import sys
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import overlap_audit as oa


def _make(tmp, ov=300, n=20, pitch=60, gap=0):
    W = 100 + n * pitch
    line = np.full((80, W), 255, np.uint8)
    rng = np.random.default_rng(1)
    for i in range(n):
        x = 50 + i * pitch
        line[20:60, x + 10:x + 10 + int(rng.integers(25, 45))] = 0
        line[30 + int(rng.integers(0, 15)):35 + int(rng.integers(15, 25)), x + 5:x + 50] = 0
    w = (W + ov) // 2
    b1, b2 = (0, w), (W - w, W)
    ents = []
    for k, (a, b) in enumerate((b1, b2), 1):
        Image.fromarray(line[:, a:b]).save(tmp / f'X_L01_s{k}.png')
        ents.append({'crop': f'X_L01_s{k}.png', 'box': [a, 0, b, 80]})
    json.dump({'iiif_lines': ents}, open(tmp / 'm.json', 'w'))
    with open(tmp / 't.tsv', 'w') as f:
        f.write('line\tpos\tref_sign\ttruth\tplain\tstatus\n')
        for i in range(n):
            f.write(f'X_L01\t{i + 1}\tS{i}\tS{i}\tx\tscored\n')
    return b1, b2, W


def test_pixel_match_equals_box_overlap():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); b1, b2, _ = _make(tmp, ov=300)
        o, v = oa.pixel_overlap(str(tmp / 'X_L01_s1.png'), str(tmp / 'X_L01_s2.png'))
        assert abs(o - (b1[1] - b2[0])) <= 2 and v > 0.95


def test_deletion_in_overlap_is_inside_and_values_never_reported():
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d); b1, b2, W = _make(tmp, ov=300)
        mid = (b2[0] + b1[1]) / 2           # centre of the overlap zone
        p_in = int(round((mid - 50) / 60)) + 1
        with open(tmp / 'p.tsv', 'w') as f:
            f.write('line\tpos\tsign\n')
            k = 0
            for i in range(20):
                if i + 1 in (p_in, 2):       # one deletion in the overlap, one near the line start
                    continue
                k += 1; f.write(f'X_L01\t{k}\tS{i}\n')
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            oa.main(['--manifest', str(tmp / 'm.json'), '--crop-dir', str(tmp), '--truth', str(tmp / 't.tsv'),
                     '--pass', f'P={tmp / "p.tsv"}', '--json', str(tmp / 'o.json')])
        out = json.load(open(tmp / 'o.json'))
        zones = sorted((r['pos'], r['zone']) for r in out['passes']['P']['indels'])
        assert zones == [(2.0, 'outside'), (float(p_in), 'inside')]
        assert 'S1' not in buf.getvalue()


def test_zero_overlap_cut_is_seam_not_inside():
    segs = [{'x0': 0, 'x1': 500}, {'x0': 500, 'x1': 1000}]
    z = oa.zones_of(segs)
    assert oa.classify(500, z, 30) == 'seam' and oa.classify(520, z, 30) == 'seam'
    assert oa.classify(600, z, 30) == 'outside'


if __name__ == '__main__':
    for name, fn in list(globals().items()):
        if name.startswith('test_'):
            fn()
    print('ok')
