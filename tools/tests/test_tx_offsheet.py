#!/usr/bin/env python3
"""Offline test for tools/tx_offsheet.py: a synthetic line of drawn glyphs (bars, rings, boxes) with one planted
off-sheet shape (an X) that the readers label as an on-sheet cell; detect must rank it in the top flagged share,
and a reader NEW: flag must be flagged regardless of score."""
import csv, json, os, sys, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from PIL import Image, ImageDraw
import tx_offsheet as T


def glyph(d, kind, x):
    if kind == 'I':
        d.line([(x + 10, 20), (x + 10, 60)], fill=0, width=4)
    elif kind == 'O':
        d.ellipse([x + 2, 22, x + 30, 58], outline=0, width=4)
    elif kind == 'B':
        d.rectangle([x + 2, 24, x + 30, 56], outline=0, width=4)
    elif kind == 'X':
        d.line([(x + 2, 22), (x + 30, 58)], fill=0, width=4); d.line([(x + 30, 22), (x + 2, 58)], fill=0, width=4)


def main():
    tmp = tempfile.mkdtemp()
    seq = list('IOBIOBIOBIOBIOBIOBIOBIOB')
    planted = 10
    shapes = list(seq); shapes[planted] = 'X'
    im = Image.new('L', (60 + 45 * len(seq), 80), 255)
    d = ImageDraw.Draw(im)
    for k, s in enumerate(shapes):
        glyph(d, s, 30 + 45 * k)
    crop = os.path.join(tmp, 'syn_L01.jpg'); im.save(crop)
    truth = os.path.join(tmp, 'truth.tsv')
    with open(truth, 'w') as f:
        f.write('line\tpos\tref_sign\ttruth\tplain\tstatus\n')
        for k, s in enumerate(seq):
            f.write('syn_L01\t%d\t%s\t%s\tx\tscored\n' % (k + 1, s, s))
    passes = []
    for name, nw in (('A', None), ('B', 3)):
        p = os.path.join(tmp, 'pass%s.tsv' % name)
        with open(p, 'w') as f:
            f.write('line\tpos\tsign\n')
            for k, s in enumerate(seq):
                f.write('syn_L01\t%d\t%s\n' % (k + 1, 'NEW:hook' if nw == k else s))
        passes.append(p)
    cfg = {'item': 'syn', 'truth_for_ref': truth, 'lines': {'syn_L01': [crop]}, 'skeleton': {'syn_L01': seq},
           'passes': passes, 'line_prefix': None, 'label_map': None, 'band': [0.0, 1.0]}
    rows, F, cells = T.detect(cfg, q=0.15)
    assert len(rows) == len(seq), len(rows)
    top = max(rows, key=lambda r: r['score'])
    assert top['pos'] == str(planted + 1), ('planted X not top', top)
    fl = {r['pos'] for r in rows if r['flagged']}
    assert str(planted + 1) in fl and '4' in fl, fl
    assert len(fl) <= int(0.15 * len(rows)), len(fl)
    cells_out = T.grow(cfg, rows, F, cells, thr=0.9, min_size=1)
    assert cells_out and all(c['cell'].startswith('NEW_') for c in cells_out)
    # recall: baseline = the skeleton read; truth disagrees at the planted X and at pos 2 (pos 2 verifier-flagged)
    truth2 = os.path.join(tmp, 'truth2.tsv')
    with open(truth2, 'w') as f:
        f.write('line\tpos\tref_sign\ttruth\tplain\tstatus\tflag\n')
        for k, s in enumerate(seq):
            tv = 'Z' if k in (planted, 1) else s
            f.write('syn_L01\t%d\t%s\t%s\tx\tscored\t%s\n' % (k + 1, s, tv, 'align-conflict' if k == 1 else ''))
    cfg2 = dict(cfg, truth_for_ref=truth2)
    r1 = T.recall(cfg2, rows, passes[0])
    assert r1['errors'] == 2 and r1['caught'] >= 1 and r1['caught_score_only'] >= 1, r1
    r2 = T.recall(cfg2, rows, passes[0], exclude_flagged=True)
    assert r2['errors'] == 1 and r2['exclude_flagged'], r2
    # census: a page holding only the planted shape's kind (X) is near a flagged tile; a page of I bars is near a cell
    for name, kind in (('pgX', 'X'), ('pgI', 'I')):
        pim = Image.new('L', (400, 80), 255); pd = ImageDraw.Draw(pim)
        for k in range(6):
            glyph(pd, kind, 20 + 60 * k)
        pim.save(os.path.join(tmp, name + '.jpg'))
    cen = T.census(cfg, rows, [os.path.join(tmp, 'pgX.jpg'), os.path.join(tmp, 'pgI.jpg')])
    assert cen[0]['near_flagged_not_cell'] > cen[1]['near_flagged_not_cell'], cen
    assert cen[1]['near_cell'] >= 1, cen
    print('test_tx_offsheet: ALL PASS')


if __name__ == '__main__':
    main()
