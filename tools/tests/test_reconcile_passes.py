#!/usr/bin/env python3
"""Offline test for tools/reconcile_passes.py.
1. fr2980-gramont f.30 blind passes, --method difflib: must give 1195/2010 agreeing signs, the figure
   ciphers/fr2980-gramont/reconcile_f30.py prints for the same files.
2. A synthetic three-pass case with an insertion and a substitution: the draft must keep the majority
   sign, mark the two disputed columns M, and list them in the disagreement table.
3. --sign-map (bMALG, malsburg-hessen-1636 glyph conventions): two passes disagreeing only because one
   reads a stroke as '1'/'11' and the other as 'i'/'ii' (and '2' vs 'z') must agree fully once both are
   substituted through the map, and the same tokens must still disagree with no map given.
Run: python3 tools/tests/test_reconcile_passes.py"""
import os, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import reconcile_passes as rp

fails = 0
def check(ok, what):
    global fails
    fails += not ok
    print('PASS' if ok else 'FAIL', what)

g = os.path.join(ROOT, 'ciphers', 'fr2980-gramont')
r = rp.main([os.path.join(g, 'passA_f30.tsv'), os.path.join(g, 'passB_f30.tsv'), '--method', 'difflib', '--no-write'])
check((r['agree'], r['cols']) == (1195, 2010), 'Gramont f.30 difflib agreement 1195/2010 (reconcile_f30.py)')

tmp = tempfile.mkdtemp()
def w(name, rows):
    p = os.path.join(tmp, name)
    open(p, 'w').write('line\tpos\tsign\tconf\n' + ''.join(f'L1\t{i}\t{s}\tH\n' for i, s in enumerate(rows, 1)))
    return p
A = w('A.tsv', ['a', 'b', 'c', 'd', 'e', 'f'])
B = w('B.tsv', ['a', 'b', 'x', 'c', 'd', 'e', 'f'])      # insertion x
C = w('C.tsv', ['a', 'b', 'c', 'd', 'q', 'f'])           # substitution e->q
r = rp.main([A, B, C, '--no-write'])
signs = [d[2] for d in r['draft']]
check(signs == ['a', 'b', 'x', 'c', 'd', 'e', 'f'], f'three-pass draft keeps majority signs {signs}')
check(sum(1 for d in r['draft'] if d[3] == 'M') == 2 and len(r['dis']) == 2, 'two disputed columns marked M and listed')
check(r['agree'] == 5 and r['cols'] == 7, 'agreement 5/7')

A = w('A.tsv', ['1', 'ii', 'z', '30'])
B = w('B.tsv', ['i', '11', '2', '30'])
r0 = rp.main([A, B, '--no-write'])
check(r0['agree'] == 1 and r0['cols'] == 4, f"no map: only the untouched token agrees ({r0['agree']}/{r0['cols']})")
m = os.path.join(tmp, 'sign_map.tsv')
open(m, 'w').write('pass_reading\tcanonical\tevidence\tcount\tgrade\n'
                    'i\t1\tfoo\t1\tH\nii\t11\tfoo\t1\tH\nz\t2\tfoo\t1\tM\n')
r1 = rp.main([A, B, '--sign-map', m, '--no-write'])
check(r1['agree'] == 4 and r1['cols'] == 4, f"--sign-map: all four tokens agree ({r1['agree']}/{r1['cols']})")
check([d[2] for d in r1['draft']] == ['1', '11', '2', '30'], 'draft carries the canonical signs, not the raw ones')

print('reconcile_passes:', 'all tests pass' if not fails else f'{fails} failures')
sys.exit(1 if fails else 0)
