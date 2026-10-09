#!/usr/bin/env python3
"""Offline test for tools/tx_pair_hints.py (no network, no model, no page image)."""
import os, random, sys, tempfile
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import tx_pair_hints as T


def glyph(desc, seed):
    """A 40x20 stroke; with desc the box extends 15 px below the line (baseline at row 40 of a 55-row box)."""
    rnd = random.Random(seed)
    h = 55 if desc else 40
    ink = np.zeros((h, 20), bool)
    ink[5:h - 2, 9:11] = True
    ink[10 + rnd.randint(0, 3), 4:16] = True  # one short bar (12/20 = 0.6, not counted as a long bar)
    return ink, h


def test_stats():
    ink = np.zeros((30, 30), bool)
    ink[5:25, 5] = ink[5:25, 24] = ink[5, 5:25] = ink[24, 5:25] = True
    assert T.count_loops(ink) == 1
    assert T.count_bars(ink) == 2
    assert T.count_bars(np.zeros((10, 10), bool)) == 0
    assert T.descender(55, 40, 55) > 0.25 and T.descender(38, 40, 40) == 0.0


def test_descender_pair_kept():
    sa, sb = [], []
    for i in range(6):
        ink, h = glyph(True, i)
        sa.append(T.tile_stats(ink, 40 + 15 + (i % 2), 40, h))
        ink, h = glyph(False, i)
        sb.append(T.tile_stats(ink, 40 - (i % 2), 40, h))
    ok, best, d, ma, mb, ds, why = T.decide('TA', 'TB', sa, sb)
    assert ok and best == 'descender' and d > 1, (ok, best, d, ds)
    s = T.sentence('TA', 'TB', best, ma, mb)
    assert 'below the line' in s and "TB's does not" in s, s


def test_identical_dropped():
    sa = [T.tile_stats(*glyph(False, i)[:1], 40, 40, 40) for i in range(5)]
    ok, best, d, *_ , why = T.decide('TA', 'TB', sa, list(sa))
    assert not ok and d < 1 and 'd\'' in why


def test_too_few_dropped():
    sa = [T.tile_stats(*glyph(False, i)[:1], 40, 40, 40) for i in range(5)]
    ok, *_, why = T.decide('TA', 'TB', sa, sa[:1])
    assert not ok and 'too few' in why


def test_norm_and_assemble():
    with tempfile.TemporaryDirectory() as d:
        raw = os.path.join(d, 'raw.tsv')
        open(raw, 'w').write('passage\tpos\tsign_id\talt\tconf\tnote\nL01\t1\tT18\t\tH\t\nL01\t2\tT98\t\tM\t\n')
        out = os.path.join(d, 'p.tsv')
        T.main(['norm', '--raw', raw, '--leaf', 'f178v', '--out', out])
        assert open(out).read().splitlines() == ['line\tpos\tsign', 'f178v_L01\t1\tT18', 'f178v_L01\t2\tT98']
        b, h = os.path.join(d, 'b.md'), os.path.join(d, 'h.md')
        open(b, 'w').write('BASE BRIEF\n'); open(h, 'w').write('## hints\n- TA vs TB\n')
        t = os.path.join(d, 't.md')
        T.main(['assemble', '--base', b, '--hints', h, '--signsheet', 's.png', '--sheet', 'hs.png', '--crops', 'c1.jpg',
                '--raw', raw, '--out', t])
        txt = open(t).read()
        assert txt.startswith('BASE BRIEF') and '- TA vs TB' in txt and 'Write your TSV to:' in txt


if __name__ == '__main__':
    for k, f in list(globals().items()):
        if k.startswith('test_'):
            f()
    print('ok')
