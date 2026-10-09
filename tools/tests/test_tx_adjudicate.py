#!/usr/bin/env python3
"""Offline test for tools/tx_adjudicate.py (TXE-K, 9 Oct 2026): a synthetic two-line agreement file with a split, a
split+gap run and an order swap; a tiny page image and box map; a truth file. items must build 3 items (the swap merged),
packet must write sheets, a call file with no base/sonnet labels and a key, resolve must apply picks (and keep the base
label when the pick equals the committed adjudication), and score must call the right option right. No network, no model."""
import csv, os, sys, tempfile
from PIL import Image

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import tx_adjudicate as ta  # noqa: E402


def w(p, cols, rows):
    with open(p, 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(str(x) for x in r) + '\n')


def rd(p):
    return list(csv.DictReader(open(p), delimiter='\t'))


def main():
    d = tempfile.mkdtemp()
    j = lambda x: os.path.join(d, x)
    AG = ['passage', 'posA', 'idA', 'confA', 'posB', 'idB', 'confB', 'status', 'merged', 'merged_conf']
    w(j('agr.tsv'), AG, [
        ['L01', 1, 'T10', 'H', 1, 'T10', 'H', 'agree', 'T10', 'H'],
        ['L01', 2, 'T50', 'M', 2, 'T92', 'M', 'split+adj', 'T50', 'M'],      # item 1
        ['L01', 3, 'T11', 'H', 3, 'T11', 'H', 'agree', 'T11', 'H'],
        ['L01', 4, 'T29', 'M', 4, 'T24', 'M', 'split+adj', 'T29', 'H'],      # item 2 (split + gap)
        ['L01', '', '', '', 5, 'T88', 'H', 'gapA+adj', 'NONE', 'H'],
        ['L01', 5, 'T12', 'H', 6, 'T12', 'H', 'agree', 'T12', 'H'],
        ['L02', 1, 'T10', 'H', 1, 'T10', 'H', 'agree', 'T10', 'H'],
        ['L02', '', '', '', 2, 'T95', 'H', 'gapA+adj', 'T95', 'M'],          # item 3 (swap, merged)
        ['L02', 2, 'T96', 'M', 3, 'T96', 'M', 'agree', 'T96', 'M'],
        ['L02', 3, 'T95', 'M', '', '', '', 'gapB', '', ''],
    ])
    base = [('p_L01', 1, 'T10'), ('p_L01', 2, 'X_CE'), ('p_L01', 3, 'T11'), ('p_L01', 4, 'T29'), ('p_L01', 5, 'T12'),
            ('p_L02', 1, 'T10'), ('p_L02', 2, 'T95'), ('p_L02', 3, 'T96')]
    w(j('L.tsv'), ['line', 'pos', 'sign'], base)
    r = ta.items([j('agr.tsv')], j('L.tsv'), 'p', ['L01', 'L02'], j('items.tsv'))
    I = rd(j('items.tsv'))
    assert r['items'] == 3, I
    assert I[1]['candB'] == 'T24 T88' and I[1]['sonnet'] == 'T29' and I[1]['base_pos'] == '4'
    assert I[2]['candA'] == 'T96 T95' and I[2]['candB'] == 'T95 T96' and I[2]['base_pos'] == '2,3', I[2]
    # page + boxes: two lines, signs 40 px apart
    Image.new('L', (400, 200), 255).save(j('page.jpg'))
    S, BP = [], []
    for ln, n in ((1, 5), (2, 3)):
        for k in range(n):
            sid = f'pg_{ln:02d}_{k + 1:03d}'
            S.append([sid, 'pg', ln, k + 1, 20 + 40 * k, 20 + 90 * (ln - 1), 30, 40, 1, 1, 0, ''])
            BP.append([sid, f'p_L0{ln}', k + 1, '1:1'])
    w(j('signs.tsv'), ['sid', 'page', 'line', 'pos', 'x', 'y', 'w', 'h', 'rh', 'rw', 'dy', 'marks'], S)
    w(j('bp.tsv'), ['sid', 'line', 'pos', 'op'], BP)
    Image.new('RGB', (50, 50), 'white').save(j('sheet.png'))
    r = ta.packet(j('items.tsv'), j('signs.tsv'), j('bp.tsv'), j('page.jpg'), 'pg', j('sheet.png'), j('out'), per=2, call=2)
    assert r == dict(items=3, sheets=2, calls=2), r
    call = open(j('out/call_01.md')).read()
    assert 'X_CE' not in call and 'sonnet' not in call.lower()
    K = {k['item']: k for k in rd(j('out/key.tsv'))}
    # reads: item 1 picks B (T92); item 2 picks the option equal to the committed T29 (base kept); item 3 '?'
    opt = lambda it, side: '1' if K[it]['opt1'] == side else '2'
    w(j('reads.tsv'), ['item', 'answer', 'conf', 'note'], [[1, opt('1', 'B'), 'M', ''], [2, opt('2', 'A'), 'H', ''],
                                                            [3, '?', 'L', '']])
    ta.resolve(j('items.tsv'), j('out/key.tsv'), j('reads.tsv'), j('L.tsv'), j('res.tsv'))
    got = [(r['line'], r['sign']) for r in rd(j('res.tsv'))]
    assert got == [('p_L01', 'T10'), ('p_L01', 'T92'), ('p_L01', 'T11'), ('p_L01', 'T29'), ('p_L01', 'T12'),
                   ('p_L02', 'T10'), ('p_L02', 'T95'), ('p_L02', 'T96')], got
    # B's two-sign option inserts
    w(j('reads2.tsv'), ['item', 'answer', 'conf', 'note'], [[2, opt('2', 'B'), 'H', '']])
    ta.resolve(j('items.tsv'), j('out/key.tsv'), j('reads2.tsv'), j('L.tsv'), j('res2.tsv'))
    assert [r['sign'] for r in rd(j('res2.tsv')) if r['line'] == 'p_L01'] == ['T10', 'X_CE', 'T11', 'T24', 'T88', 'T12']
    # score: truth says L01 pos2 is T92, so B is right on item 1
    TR = ['line', 'pos', 'ref_sign', 'truth', 'plain', 'status']
    w(j('truth.tsv'), TR, [[l, p, s, 'T92' if (l, p) == ('p_L01', 2) else s, 'a', 'scored'] for l, p, s in base])
    w(j('bench.tsv'), ['item', 'truth'], [['it', 'truth.tsv']])
    out, per = ta.score(j('items.tsv'), j('out/key.tsv'), [j('reads.tsv')], j('L.tsv'), j('bench.tsv'), 'it', ['r'])
    son, rr = out
    assert son['right'] == 2 and son['wrong'] == 1, son      # committed T50 on item 1 wrong
    assert rr['right'] == 2 and rr['abstain'] == 1 and rr['better_than_sonnet'] == 1, rr
    print('test_tx_adjudicate: ok')


if __name__ == '__main__':
    main()
