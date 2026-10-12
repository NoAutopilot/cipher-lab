#!/usr/bin/env python3
"""Offline test for tools/box_clip_check.py (BOXCLIP, 12 Oct 2026). No network, no model, no repository data.

A synthetic page where the right answer is known by construction (white paper 255, black ink 0):
  A  a g-shaped sign (ellipse body, 4 px tail running 35 rows below it); the machine box holds the body and the tail's
     first rows only -> FLAGGED CLIPPED, grown box reaches the tail's end and keeps the body's width.
  B  the same sign with a box that holds all of it -> not flagged.
  C/D two signs joined by a 10 px ligature, D twice C's size; C's box holds C and 4 px of the bridge, D's holds D and
     4 px of it. The joined component touches D's box (about 500 ink pixels) more than C's (about 260), so for C it is a
     neighbour's ink (ignored, C not flagged); for D the far side is C's box (a neighbour), so nothing is outside ->
     not flagged. Without the neighbour rule (C's box alone on the page) C IS flagged, which shows the rule is what
     saves it.
  E  a body with an 11-row tail, the box ending 9 rows short of its end, leaving about 10% of its ink outside: not flagged at 0.25, flagged at 0.05 (--thr is live).
  F  an empty box: not flagged, no components.
  G  a flat grey page: nothing flagged (the contrast floor), no crash.
Also: the same page at half size with the boxes in the original units and scale 0.5 gives the same flags; the CLI runs end
to end on temp files and writes the flags TSV; every box is returned in order with its sid.
"""
import csv
import os
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import box_clip_check as BC  # noqa: E402

W, H = 420, 130


def page():
    im = Image.new('L', (W, H), 255)
    d = ImageDraw.Draw(im)
    # A: body y 30-50, x 30-46; tail x 36-40 down to y 85
    d.ellipse([30, 30, 46, 50], fill=0); d.line([(38, 48), (38, 85)], fill=0, width=4)
    # B: same shape at x 90, tail down to y 85
    d.ellipse([90, 30, 106, 50], fill=0); d.line([(98, 48), (98, 85)], fill=0, width=4)
    # C, D joined by a bridge at y 40
    d.ellipse([160, 30, 176, 50], fill=0); d.ellipse([186, 24, 206, 56], fill=0); d.line([(176, 40), (186, 40)], fill=0, width=3)
    # E: body with a short tail (y 49 to 60)
    d.ellipse([280, 30, 296, 50], fill=0); d.line([(288, 49), (288, 60)], fill=0, width=3)
    return np.asarray(im)


BOXES = [
    ('A', 26, 26, 24, 28),      # body + first 4 rows of tail
    ('B', 86, 26, 24, 64),      # whole sign
    ('C', 156, 26, 24, 28),     # C + 4 px of bridge
    ('D', 182, 20, 28, 40),     # D (twice C's ink) + 4 px of bridge
    ('E', 276, 26, 24, 25),     # body + first rows of the tail (box ends at y 51)
    ('F', 350, 26, 24, 28),     # empty
]


def test_known_answers():
    r = {g['sid']: g for g in BC.check_boxes(page(), BOXES)}
    assert [g['sid'] for g in BC.check_boxes(page(), BOXES)] == [b[0] for b in BOXES]
    assert r['A']['flagged'] and r['A']['outside_frac'] >= 0.25, r['A']
    gx, gy, gw, gh = r['A']['grown']
    assert abs(gx - 30) <= 3 and abs(gy - 30) <= 3 and abs(gy + gh - 87) <= 3 and 14 <= gw <= 22, r['A']['grown']
    assert not r['B']['flagged'] and r['B']['outside_frac'] == 0.0 and r['B']['grown'] == (86, 26, 24, 64), r['B']
    assert not r['C']['flagged'] and r['C']['n_comp'] == 0, r['C']
    assert not r['D']['flagged'] and r['D']['outside_frac'] < 0.2, r['D']
    assert not r['E']['flagged'] and 0 < r['E']['outside_frac'] < 0.25, r['E']
    assert not r['F']['flagged'] and r['F']['n_comp'] == 0 and r['F']['outside_frac'] == 0.0, r['F']


def test_neighbour_rule_is_what_saves_c():
    alone = BC.check_boxes(page(), [BOXES[2]])[0]
    assert alone['flagged'] and alone['outside_frac'] > 0.6, alone
    with_nb = BC.check_boxes(page(), [BOXES[2], BOXES[3]])[0]
    assert not with_nb['flagged'] and with_nb['n_comp'] == 0, with_nb
    # a box on another line (vertical overlap under half) is not a neighbour: C is flagged again
    far = ('D', 182, 70, 28, 40)
    assert BC.check_boxes(page(), [BOXES[2], far])[0]['flagged']


def test_threshold_is_live():
    e = BOXES[4]
    assert not BC.check_boxes(page(), [e])[0]['flagged']
    assert BC.check_boxes(page(), [e], thr=0.05)[0]['flagged']


def test_scale():
    half = np.asarray(Image.fromarray(page()).resize((W // 2, H // 2), Image.LANCZOS))
    r = {g['sid']: g for g in BC.check_boxes(half, BOXES, scale=0.5)}
    assert r['A']['flagged'] and not r['B']['flagged'] and not r['C']['flagged'] and not r['D']['flagged'], r
    assert not r['E']['flagged'] and not r['F']['flagged'], r
    gx, gy, gw, gh = r['A']['grown']
    assert abs(gy + gh - 87) <= 6 and abs(gx - 30) <= 6, r['A']['grown']


def test_flat_page():
    flat = np.full((H, W), 200, dtype=np.uint8)
    for g in BC.check_boxes(flat, BOXES):
        assert not g['flagged'] and g['n_comp'] == 0
    noisy = np.clip(200 + np.random.RandomState(0).randint(-3, 4, (H, W)), 0, 255).astype(np.uint8)
    assert not any(g['flagged'] for g in BC.check_boxes(noisy, BOXES))


def test_cli():
    with tempfile.TemporaryDirectory() as t:
        Image.fromarray(page()).save(os.path.join(t, 'P1.png'))
        with open(os.path.join(t, 'signs.tsv'), 'w', newline='') as f:
            w = csv.writer(f, delimiter='\t', lineterminator='\n')
            w.writerow(['sid', 'page', 'x', 'y', 'w', 'h'])
            for sid, x, y, ww, hh in BOXES:
                w.writerow([sid, 'P1', x, y, ww, hh])
        out = os.path.join(t, 'flags.tsv')
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools/box_clip_check.py'), '--boxes',
                            os.path.join(t, 'signs.tsv'), '--pages-dir', t, '--out', out, '--summary'],
                           capture_output=True, text=True)
        assert r.returncode == 0, r.stderr
        assert 'P1: 1 of 6 boxes flagged clipped' in r.stdout, r.stdout
        rows = list(csv.DictReader(open(out), delimiter='\t'))
        assert [x['sid'] for x in rows] == [b[0] for b in BOXES]
        assert [x['flagged'] for x in rows] == ['1', '0', '0', '0', '0', '0'], rows
        h = subprocess.run([sys.executable, os.path.join(ROOT, 'tools/box_clip_check.py'), '--help'], capture_output=True, text=True)
        assert h.returncode == 0 and '--boxes' in h.stdout


if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_') and callable(fn):
            fn(); print('ok', name)
    print('test_box_clip_check: all passed')
