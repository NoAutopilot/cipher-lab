#!/usr/bin/env python3
"""Offline test for tools/tx_compare.py (TXE-A, 9 Oct 2026): a synthetic page with 3 known signs, a tiny atlas, a line
read that disagrees with the atlas on one position. build must show exactly that position, the key TSV must hold its
candidates, and resolve must apply a pick and keep the line read's sign on 'none'. No network, no model."""
import csv, json, os, sys, tempfile
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import tx_compare as tc  # noqa: E402


def w(p, cols, rows):
    with open(p, 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(str(x) for x in r) + '\n')


def rd(p):
    return list(csv.DictReader(open(p), delimiter='\t'))


def setup(d):
    at = os.path.join(d, 'atlas'); os.makedirs(os.path.join(at, 'crops'))
    shapes = {'A': 'ellipse', 'B': 'rectangle', 'C': 'line'}
    signs, clus = [], []
    for page, seq in (('tg', 'ABC'), ('ex', 'AABBCC')):
        im = Image.new('L', (60 * len(seq) + 40, 120), 255); dr = ImageDraw.Draw(im)
        for i, c in enumerate(seq):
            x = 20 + 60 * i
            getattr(dr, shapes[c])((x, 30, x + 40, 80), **({'fill': 0} if c == 'C' else {'outline': 0, 'width': 4}))
            sid = f'{page}_01_{i + 1:03d}'
            signs.append((sid, page, 1, i + 1, x, 30, 40, 50, 1, 1, 0, ''))
            clus.append(('sign', sid, {'A': 0, 'B': 1, 'C': 2}[c], 1.0))
        im.save(os.path.join(at, 'crops', f'{page}.png'))
    w(os.path.join(at, 'signs.tsv'), 'sid page line pos x y w h rh rw dy marks'.split(), signs)
    w(os.path.join(at, 'clusters.tsv'), ['kind', 'id', 'cluster', 'dist'], [c[:1] + c[1:] for c in clus])
    json.dump({'signs': {'0': 'TA', '1': 'TB', '2': 'TC'}, 'marks': {},
               'override': {'tg_01_002': 'TA'}}, open(os.path.join(at, 'labels.json'), 'w'))  # override must be ignored
    topk = os.path.join(d, 'topk.tsv')
    w(topk, 'page line box pos x y w h code dist share cluster_code marks k1 d1 s1 k2 d2 s2 k3 d3 s3'.split(),
      [('tg', 1, 'tg_01_001', 1, 20, 30, 40, 50, 'TA', 1, 1.0, '_held', '', 'TA', 1, 1.0, 'TB', 2, 0.0, '', '', ''),
       ('tg', 1, 'tg_01_002', 2, 80, 30, 40, 50, 'TB', 1, 0.9, '_held', '', 'TB', 1, 0.9, 'TC', 2, 0.1, '', '', ''),
       ('tg', 1, 'tg_01_003', 3, 140, 30, 40, 50, 'TC', 1, 1.0, '_held', '', 'TC', 1, 1.0, '_', 2, 0.0, '', '', '')])
    lr = os.path.join(d, 'lr.tsv')
    w(lr, ['line', 'pos', 'sign'], [('tg_L01', 1, 'TA'), ('tg_L01', 2, 'TC'), ('tg_L01', 3, 'TC')])  # pos 2 disagrees
    conf = os.path.join(d, 'conf.tsv')
    w(conf, ['passage', 'merged', 'merged_conf'], [('L01', 'TA', 'H'), ('L01', 'TC', 'H'), ('L01', 'TC', 'H')])
    units = os.path.join(d, 'units.md')
    open(units, 'w').write('- u: tg_L01\n')
    return at, topk, lr, conf, units


def test_build_resolve():
    with tempfile.TemporaryDirectory() as d:
        at, topk, lr, conf, units = setup(d)
        out = os.path.join(d, 'out')
        common = ['--atlas', at, '--line-read', lr, '--units', units, '--out', out]
        shown = tc.main(['build', '--unit', 'u', '--topk', topk, '--conf', f'{conf}:tg', '--exemplars', '',
                         '--exclude-page', 'tg'] + common)
        assert [(s['line'], s['pos']) for s in shown] == [('tg_L01', '2')], shown
        key = rd(os.path.join(out, 'u', 'sheet_01.tsv'))
        assert len(key) == 1 and sorted(key[0]['cands'].split(',')) == ['TB', 'TC'], key
        assert os.path.exists(os.path.join(out, 'u', 'sheet_01.png'))
        bp = rd(os.path.join(out, 'box_pos.tsv'))
        assert [r['op'] for r in bp] == ['1:1'] * 3
        cands = key[0]['cands'].split(',')
        # a pick applies the picked code
        w(os.path.join(out, 'u', 'reads_01.tsv'), ['row', 'pick', 'conf', 'note'], [(1, cands.index('TB') + 1, 'H', '')])
        po = os.path.join(d, 'pass.tsv')
        res = tc.main(['resolve', '--unit', 'u', '--pass-out', po] + common)
        assert [r['sign'] for r in res] == ['TA', 'TB', 'TC'], res
        wt = rd(os.path.join(out, 'u', 'topk_weighted.tsv'))
        assert {(r['pos'], r['cand']): float(r['score']) for r in wt}[('2', 'TB')] == 1.0
        # 'none' keeps the line read's sign
        w(os.path.join(out, 'u', 'reads_01.tsv'), ['row', 'pick', 'conf', 'note'], [(1, 'none', 'M', '')])
        res = tc.main(['resolve', '--unit', 'u', '--pass-out', po] + common)
        assert [r['sign'] for r in res] == ['TA', 'TC', 'TC'], res


def test_library_and_agree():
    """TXE-S: `library` cuts the printed cell + secure tiles (excluded page never used); `build --library` shows them;
    `resolve --agree` changes L only where both readers pick the same non-L candidate."""
    with tempfile.TemporaryDirectory() as d:
        at, topk, lr, conf, units = setup(d)
        # printed key image with three cells, key map, secure list (one tile on the excluded page 'tg')
        pr = Image.new('L', (200, 60), 255); dr = ImageDraw.Draw(pr)
        dr.ellipse((10, 10, 50, 50), outline=0, width=4); dr.rectangle((70, 10, 110, 50), outline=0, width=4)
        dr.line((130, 10, 170, 50), fill=0, width=4); pr.save(os.path.join(d, 'print.png'))
        json.dump([{'id': 'TA', 'box': [5, 5, 55, 55]}, {'id': 'TB', 'box': [65, 5, 115, 55]},
                   {'id': 'TC', 'box': [125, 5, 175, 55]}], open(os.path.join(d, 'km.json'), 'w'))
        w(os.path.join(d, 'sec.tsv'), ['sid', 'code', 'page', 'grade'],
          [('ex_01_001', 'TA', 'ex', 'S'), ('ex_01_002', 'TA', 'ex', 'S'), ('ex_01_003', 'TB', 'ex', 'S'),
           ('tg_01_002', 'TB', 'tg', 'S')])
        import numpy as np
        np.savez(os.path.join(at, 'bitmaps.npz'), signs=np.random.RandomState(0).randint(0, 255, (9, 48, 48)).astype(np.uint8))
        lib = os.path.join(d, 'lib')
        counts = tc.main(['library', '--atlas', at, '--out-dir', lib, '--key-map', os.path.join(d, 'km.json'),
                          '--print-image', os.path.join(d, 'print.png'), '--secure', os.path.join(d, 'sec.tsv'),
                          '--exclude-page', 'tg'])
        assert counts == {'TA': (3, 2), 'TB': (2, 1), 'TC': (1, 0)}, counts
        refs = [r['ref'] for r in rd(os.path.join(lib, 'library.tsv'))]
        assert 'tg_01_002' not in refs and refs.count('ex_01_001') == 1
        out = os.path.join(d, 'out')
        common = ['--atlas', at, '--line-read', lr, '--units', units, '--out', out]
        tc.main(['build', '--unit', 'u', '--topk', topk, '--conf', f'{conf}:tg', '--exemplars', '', '--exclude-page', 'tg',
                 '--library', lib] + common)
        cands = rd(os.path.join(out, 'u', 'sheet_01.tsv'))[0]['cands'].split(',')
        iB, iC = cands.index('TB') + 1, cands.index('TC') + 1
        r1, r2 = os.path.join(d, 'r1'), os.path.join(d, 'r2'); os.makedirs(r1); os.makedirs(r2)
        po = os.path.join(d, 'pass.tsv')
        for p2, want in ((iB, 'TB'), (iC, 'TC'), ('none', 'TC')):     # agree -> change; disagree / none -> keep L (TC)
            w(os.path.join(r1, 'reads_01.tsv'), ['row', 'pick', 'conf', 'note'], [(1, iB if want != 'TC' or p2 != iC else iC, 'H', '')])
            w(os.path.join(r2, 'reads_01.tsv'), ['row', 'pick', 'conf', 'note'], [(1, p2, 'H', '')])
            res = tc.main(['resolve', '--unit', 'u', '--pass-out', po, '--agree', r1, r2] + common)
            assert res[1]['sign'] == want, (p2, res)
        # single reader by the TXE-A rule from a reads folder
        w(os.path.join(r2, 'reads_01.tsv'), ['row', 'pick', 'conf', 'note'], [(1, iB, 'L', '')])
        assert tc.main(['resolve', '--unit', 'u', '--pass-out', po, '--reads-dir', r2] + common)[1]['sign'] == 'TB'


if __name__ == '__main__':
    test_build_resolve(); test_library_and_agree(); print('ok')
