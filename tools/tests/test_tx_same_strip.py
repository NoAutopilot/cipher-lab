#!/usr/bin/env python3
"""Offline test for tools/tx_same_strip.py (plan + resolve, no images)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import tx_same_strip as t


def main():
    page = 'f9'
    L, box = [], []
    seq = ['A1', 'B2', 'A1', 'C3', 'B2', 'A1', 'B2', 'C3', 'A1', 'B2']
    for i, s in enumerate(seq, 1):
        L.append({'line': f'{page}_L01', 'pos': str(i), 'sign': s})
        box.append({'sid': f'{page}_01_{i:03d}', 'line': f'{page}_L01', 'pos': str(i), 'op': '1:1'})
    L.append({'line': 'f8_L01', 'pos': '1', 'sign': 'C3'})                     # another leaf: never a strip
    box.append({'sid': 'f8_01_001', 'line': 'f8_L01', 'pos': '1', 'op': '1:1'})
    pos = [{'line': f'{page}_L01', 'pos': '5'}, {'line': f'{page}_L01', 'pos': '99'}]
    topk = [{'line': f'{page}_L01', 'pos': '5', 'cand': 'B2', 'score': '0.7'},
            {'line': f'{page}_L01', 'pos': '5', 'cand': 'A1', 'score': '0.2'}]
    rows, c = t.plan(L, pos, box, topk, page, {}, per_strip=6, seed=0)
    assert c == {'positions': 2, 'shown': 1, 'unmapped': 1, 'one_strip': 0}, c
    r = rows[0]
    signs = {x[1] for x in r['cands']}
    assert signs == {'B2', 'A1'}, signs
    for letter, sign, why, sids in r['cands']:
        assert all(s.startswith(page + '_') for s in sids)
        nums = {int(s[-3:]) for s in sids}
        assert not nums & {4, 5, 6}, nums                                    # own position and neighbours excluded
        own = {i + 1 for i, s in enumerate(seq) if s == sign} - {4, 5, 6}
        assert nums == own, (sign, nums, own)
    # control: strips shifted, key letters keep their sign
    rows2, _ = t.plan(L, pos, box, topk, page, {}, per_strip=6, seed=0, swap_seed=1)
    a = {x[0]: (x[1], x[3]) for x in r['cands']}
    b = {x[0]: (x[1], x[3]) for x in rows2[0]['cands']}
    assert all(a[k][0] == b[k][0] for k in a) and all(a[k][1] != b[k][1] for k in a)
    # partner rule
    assert t.partner('T18', {}) == 'T98' and t.partner('T76', {frozenset(('T76', 'T86')): 5}) == 'T86'
    # resolve
    d = tempfile.mkdtemp()
    t.wr(os.path.join(d, 'L.tsv'), ['line', 'pos', 'sign'], L)
    t.wr(os.path.join(d, 'key.tsv'), ['row', 'line', 'pos', 'L', 'A', 'B'],
         [{'row': 1, 'line': f'{page}_L01', 'pos': '5', 'L': 'B2', 'A': 'A1', 'B': 'B2'},
          {'row': 2, 'line': f'{page}_L01', 'pos': '6', 'L': 'A1', 'A': 'A1', 'B': 'C3'}])
    t.wr(os.path.join(d, 'reads.tsv'), ['row', 'pick', 'conf'], [{'row': 1, 'pick': 'A', 'conf': 'H'},
                                                                  {'row': 2, 'pick': 'neither', 'conf': 'L'}])
    st = t.main(['resolve', '--line-read', os.path.join(d, 'L.tsv'), '--key', os.path.join(d, 'key.tsv'),
                 '--reads', os.path.join(d, 'reads.tsv'), '--pass-out', os.path.join(d, 'out.tsv')])
    out = {(r['line'], r['pos']): r['sign'] for r in t.rd(os.path.join(d, 'out.tsv'))}
    assert out[(f'{page}_L01', '5')] == 'A1' and out[(f'{page}_L01', '6')] == 'A1' and st['changed'] == 1
    print('test_tx_same_strip: ok')


if __name__ == '__main__':
    main()
