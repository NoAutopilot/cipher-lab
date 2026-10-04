#!/usr/bin/env python3
"""Offline test for tools/reconcile_passes.py.
1. fr2980-gramont f.30 blind passes, --method difflib: must give 1195/2010 agreeing signs, the figure
   ciphers/fr2980-gramont/reconcile_f30.py prints for the same files.
2. A synthetic three-pass case with an insertion and a substitution: the draft must keep the majority
   sign, mark the two disputed columns M, and list them in the disagreement table.
3. --sign-map (bMALG, malsburg-hessen-1636 glyph conventions): two passes disagreeing only because one
   reads a stroke as '1'/'11' and the other as 'i'/'ii' (and '2' vs 'z') must agree fully once both are
   substituted through the map, and the same tokens must still disagree with no map given.
4. REC-CONF (27 Sept 2026): confidence labels 'medium' and 'm' must normalise to M (the outside-review bug --
   they used to pass through unflagged and the agreed sign was written H regardless); an unrecognised label
   must exit non-zero rather than being silently treated as confident; an agreed M/M sign must land in
   ciphertext_draft.tsv at confidence M, not H, and also in uncertain.tsv.
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
def w(name, rows, confs=None):
    p = os.path.join(tmp, name)
    confs = confs or ['H'] * len(rows)
    open(p, 'w').write('line\tpos\tsign\tconf\n'
                        + ''.join(f'L1\t{i}\t{s}\t{c}\n' for i, (s, c) in enumerate(zip(rows, confs), 1)))
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

# REC-CONF: 'medium' and 'm' must normalise to M, not pass through unflagged as the outside review found.
A = w('A.tsv', ['a', 'b', 'c'], confs=['H', 'medium', 'H'])
B = w('B.tsv', ['a', 'b', 'c'], confs=['H', 'm', 'H'])
r = rp.main([A, B, '--no-write'])
draft_conf = {d[0] + ':' + d[1]: d[3] for d in r['draft']}
check(draft_conf['L1:2'] == 'M', f"agreed 'medium'/'m' sign reads M, not H (got {draft_conf['L1:2']!r})")
check(draft_conf['L1:1'] == 'H' and draft_conf['L1:3'] == 'H', 'agreed H/H signs either side still read H')
check(any(u[0] == 'L1' and u[1] == '2' for u in r['uncertain']), "agreed M/M sign ('medium'/'m') lands in uncertain.tsv")
check(r['agreed_h'] == 2 and len(r['uncertain']) == 1, f"agreed-H 2 / agreed-uncertain 1 (got {r['agreed_h']}/{len(r['uncertain'])})")

# an unrecognised confidence label is a fatal error, never silently treated as confident
C = w('C.tsv', ['a', 'b', 'c'], confs=['H', 'sortof', 'H'])
try:
    rp.main([A, C, '--no-write'])
    check(False, "unrecognised confidence label 'sortof' exits non-zero")
except SystemExit as e:
    check(e.code not in (0, None), f"unrecognised confidence label 'sortof' exits non-zero (code {e.code!r})")

# TX-ALTS --keep-alts: 'a/b?' aligns on its first choice and every alternative reaches lattice.tsv
A2 = w('A2.tsv', ['a', 'b/x?', 'c'], confs=['H', 'M', 'H'])
B2 = w('B2.tsv', ['a', 'b', 'c'])
r = rp.main([A2, B2, '--keep-alts', '--no-write'])
check(r['agree'] == 3, f"a/b? token aligns on its first choice under --keep-alts (agree {r['agree']}/3)")
lat2 = {(l, c): float(s) for l, p_, c, s in r['lattice'] if p_ == '2'}
check(set(c for _, c in lat2) == {'b', 'x'} and lat2[('L1', 'b')] > lat2[('L1', 'x')] > 0,
      f"lattice keeps the alternative x beside b at position 2 (got {lat2})")
r = rp.main([A2, B2, '--no-write'])
check(r['agree'] == 2, f"without --keep-alts 'b/x' stays one literal sign, as before (agree {r['agree']}/3)")

print('reconcile_passes:', 'all tests pass' if not fails else f'{fails} failures')
sys.exit(1 if fails else 0)
