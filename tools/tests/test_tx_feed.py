#!/usr/bin/env python3
"""Offline test for tools/tx_feed.py (TXE2-FEED, 9 Oct 2026): synthetic 2-line unit, a planted reader split, a planted
taxonomy pair, a low-confidence-only tile; checks order (combo first), questions (sorted piles, pair feature, no value),
the absent-combo fallback, and that the base read's choice is not singled out."""
import os, sys, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import tx_feed

base = [dict(line='u_L01', pos=str(i), sign=s) for i, s in enumerate(['T18', 'T40', 'T41', 'T42'], 1)] + \
       [dict(line='u_L02', pos=str(i), sign=s) for i, s in enumerate(['T50', 'T51', 'T52'], 1)]
latt = [dict(line='u_L01', pos=r['pos'], sign=('T98' if r['pos'] == '1' else r['sign'])) for r in base[:4]]
rA = [dict(passage='L02', pos='1', sign_id='T50', conf='H'), dict(passage='L02', pos='2', sign_id='T60', conf='H'),
      dict(passage='L02', pos='3', sign_id='T52', conf='L')]
pairs = ['T18/T98']
cols, rows, order, absent = tx_feed.build(base, 'u', differ=[('latt', latt), ('readerA', rA)],
                                          lowconf=[('lowA', rA)], combo=['latt', 'vote4'], ren=[('L', 'u_L')],
                                          pairs=pairs)
assert absent == ['vote4'], absent
assert order[0]['line'] == 'u_L01' and order[0]['pos'] == '1' and order[0]['combo'] == 1
q = order[0]['q']
assert q.startswith('Which pile: T18 or T98?') and 'descender' in q, q
r2 = next(r for r in rows if r['line'] == 'u_L02' and r['pos'] == '2')
assert r2['q'] == 'Which pile: T51 or T60? (the reads split)', r2['q']        # sorted, base not first
r3 = next(r for r in rows if r['line'] == 'u_L02' and r['pos'] == '3')
assert r3['q'].startswith('A reader marked this sign unsure'), r3['q']
quiet = next(r for r in rows if r['line'] == 'u_L01' and r['pos'] == '2')
assert quiet['n_signals'] == 0 and quiet['combo'] == 0
for r in rows:                                                                 # no values, no colour words
    assert not any(w in r['q'].lower() for w in ('red', 'green', 'value', 'correct'))
# CLI end to end, absent-combo fallback
d = tempfile.mkdtemp()
w = lambda n, rs, cs: open(os.path.join(d, n), 'w').write('\t'.join(cs) + '\n' + ''.join('\t'.join(r[c] for c in cs) + '\n' for r in rs))
w('base.tsv', base, ['line', 'pos', 'sign']); w('a.tsv', rA, ['passage', 'pos', 'sign_id', 'conf'])
tx_feed.main(['--base', os.path.join(d, 'base.tsv'), '--unit', 'u', '--out', d, '--differ', 'readerA=' + os.path.join(d, 'a.tsv'),
              '--lowconf', 'lowA=' + os.path.join(d, 'a.tsv'), '--rename', 'L=u_L', '--combo', 'latt+vote4'])
foc = open(os.path.join(d, 'u_focus.tsv')).read().splitlines()
assert len(foc) == 2 and foc[0].startswith('u_L02_2\t'), foc
assert 'no combo column exists' in open(os.path.join(d, 'u_feed.tsv')).readline()
print('ok')
