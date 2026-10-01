#!/usr/bin/env python3
"""Offline test for tools/sign_sorter_apply.py on hand-made decisions. Run: python3 tools/tests/test_sign_sorter_apply.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import sign_sorter_apply as sa

fails = 0
def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name); fails += not ok

labels = [{'sid': s, 'sign': g} for s, g in [('a', 'X'), ('b', 'X'), ('c', 'X'), ('d', 'XB'), ('e', 'XB2'), ('f', 'DOT'), ('g', 'X'), ('h', 'X')]]
piles = [{'pile': 'X', 'verdict': 'same', 'outliers': ['g']}, {'pile': 'XB2', 'merge_into': 'XB'}, {'pile': 'XB', 'merge_into': 'XBAR'},
         {'pile': 'DOT', 'verdict': 'mark'}, {'pile': 'Q1', 'merge_into': 'Q2'}, {'pile': 'Q2', 'merge_into': 'Q1'}]
moves = [{'sid': 'b', 'to': 'X1'}, {'sid': 'c', 'to': 'BAD-CUT'}, {'sid': 'h', 'to': 'ASIDE'}]
rows, summ = sa.apply(labels, piles, moves, [{'id': 'X1'}])
r = {x[0]: x for x in rows}
check('untouched tile kept', r['a'][2:] == ('X', 'kept'))
check('moved to new pile', r['b'][2:] == ('X1', 'moved'))
check('bad cut', r['c'][3] == 'bad-cut' and r['c'][2] == '')
check('merge followed transitively', r['d'][2:] == ('XBAR', 'merged') and r['e'][2:] == ('XBAR', 'merged'))
check('not-letter pile', r['f'][3] == 'not-letter')
check('legacy outlier and ASIDE both aside', r['g'][3] == 'aside' and r['h'][3] == 'aside')
check('merge cycle does not hang', sa.apply([{'sid': 'z', 'sign': 'Q1'}], piles, [], [])[0][0][2] in ('Q1', 'Q2'))
check('summary counts', summ['by_status']['bad-cut'] == 1 and summ['confirmed_piles'] == ['X'] and summ['new_piles'] == ['X1'])
print('FAILED' if fails else 'ALL PASS'); sys.exit(1 if fails else 0)
