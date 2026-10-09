#!/usr/bin/env python3
"""Offline test for tools/tx_features.py (no network, no model, no page image)."""
import os, sys, tempfile
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import tx_features as T


def phi():
    """A closed loop on top of a long stem: loops 1, desc long, upright."""
    g = np.zeros((60, 30), bool)
    g[2:22, 3] = g[2:22, 26] = g[2, 3:27] = g[21, 3:27] = True
    g[21:58, 14:16] = True  # stem from the loop bottom down
    return g


def test_phi():
    f, raw = T.features(phi())
    assert f['loops'] == '1' and f['desc'] == 'long' and f['asc'] == 'none' and f['lean'] == 'upright', (f, raw)


def test_c_shape_one_body():
    g = np.zeros((40, 30), bool)
    g[2:6, 2:28] = g[34:38, 2:28] = g[2:38, 2:6] = True
    f, _ = T.features(g)
    assert f['desc'] == 'none' and f['asc'] == 'none' and f['bars'] == '2' and f['loops'] == '0', f


def test_dot_and_lean():
    g = np.zeros((50, 50), bool)
    for y in range(10, 48):
        x = 10 + (48 - y) // 2  # top leans right
        g[y, x:x + 3] = True
    g[2:5, 40:43] = True  # a dot
    f, _ = T.features(g)
    assert f['dots'] == '1' and f['lean'] == 'right', f


def test_parse_and_contradict():
    w = T.parse_written('desc=long asc=none bars=1 loops=1 dots=2 lean=upright tail=none junk=7')
    assert w['dots'] == '2+' and 'junk' not in w and len(w) == 7
    cell = {'desc': 'long', 'asc': 'none', 'bars': '2', 'loops': '1', 'dots': '0', 'lean': 'upright', 'tail': 'none'}
    assert T.contradictions(w, cell) == ['bars', 'dots']


def test_consist_cli():
    d = tempfile.mkdtemp()
    cells = os.path.join(d, 'c.tsv'); raw = os.path.join(d, 'r.tsv'); wrong = os.path.join(d, 'w.tsv')
    open(cells, 'w').write('cell\t' + '\t'.join(T.FEATS) + '\nT18\tlong\tnone\t2\t2\t0\tupright\tnone\n')
    open(raw, 'w').write('passage\tpos\tfeatures\tsign_id\talt\tconf\tnote\n'
                         'L01\t1\tdesc=long asc=none bars=2 loops=2 dots=0 lean=upright tail=none\tT18\t\tH\t\n'
                         'L01\t2\tdesc=none asc=long bars=0 loops=2 dots=0 lean=upright tail=none\tT18\t\tM\t\n')
    open(wrong, 'w').write('line\tpos\nf178v_L01\t2\n')
    out = os.path.join(d, 'o.tsv')
    assert T.main(['consist', '--raw', raw, '--cells', cells, '--wrong', wrong, '--out', out]) == 0
    rows = open(out).read().splitlines()
    assert rows[1].split('\t')[4] == '0' and rows[2].split('\t')[4] == '3' and rows[2].endswith('\t1')


if __name__ == '__main__':
    for k, v in list(globals().items()):
        if k.startswith('test_'):
            v(); print('ok', k)


def test_task1_names_no_sheet_or_cell():
    t = T.task1_text(crops=['a_L01_s1.jpg'], raw='out.tsv')
    assert 'sign_sheet' not in t and 'T18' not in t and 'cell' not in t.lower(), t
    assert 'desc=none|short|long' in t


def test_comply_cli():
    d = tempfile.mkdtemp()
    cells = os.path.join(d, 'c.tsv'); base = os.path.join(d, 'b.tsv'); raw = os.path.join(d, 'r.tsv')
    ctrl = os.path.join(d, 'k.tsv'); mp = os.path.join(d, 'm.tsv')
    open(cells, 'w').write('cell\t' + '\t'.join(T.FEATS) + '\nT18\tlong\tnone\t2\t2\t0\tupright\tnone\n'
                           'T19\tnone\tlong\t1\t0\t0\tleft\tleft\n')
    open(base, 'w').write('line\tpos\tsign\n' + ''.join(f'f178v_L01\t{i}\tT18\n' for i in range(1, 11)))
    hdr = 'passage\tpos\t' + '\t'.join(T.FEATS) + '\tconf\tnote\n'
    a = 'long\tnone\t2\t2\t0\tupright\tnone'; b = 'none\tlong\t1\t0\t0\tleft\tleft'
    open(raw, 'w').write(hdr + ''.join(f'L01\t{i}\t{a if i % 2 else b}\tH\t\n' for i in range(1, 11)))
    open(mp, 'w').write('tile\tcell\n1\tT18\n2\tT19\n')
    open(ctrl, 'w').write(hdr + f'TILES\t1\t{a}\tH\t\nTILES\t2\t{a}\tH\t\n')  # tile 2 wrong on 6 features
    args = ['comply', '--raw1', raw, '--base', base, '--cells', cells, '--control', ctrl, '--map', mp]
    assert T.main(args) == 4  # control 1/2 = 0.5 < 0.7
    open(ctrl, 'w').write(hdr + f'TILES\t1\t{a}\tH\t\nTILES\t2\t{b}\tH\t\n')
    assert T.main(args) == 0
    open(raw, 'w').write(hdr + ''.join(f'L01\t{i}\t{a}\tH\t\n' for i in range(1, 11)))  # constant -> (b) fails
    assert T.main(args) == 4


def test_task2_carries_feats():
    d = tempfile.mkdtemp()
    cells = os.path.join(d, 'c.tsv'); f1 = os.path.join(d, 'f.tsv'); out = os.path.join(d, 't.md')
    open(cells, 'w').write('cell\t' + '\t'.join(T.FEATS) + '\nT18\tlong\tnone\t2\t2\t0\tupright\tnone\n')
    open(f1, 'w').write('passage\tpos\t' + '\t'.join(T.FEATS) + '\tconf\tnote\nL01\t1\tlong\tnone\t2\t2\t2\tupright\tnone\tH\t\n')
    assert T.main(['task2', '--crops', 'x.jpg', '--signsheet', 's.png', '--cells', cells, '--feats', f1,
                   '--raw', 'o.tsv', '--out', out]) == 0
    t = open(out).read()
    assert 'L01\t1\tlong\tnone\t2\t2\t2+\tupright\tnone' in t and 'mismatch' in t
