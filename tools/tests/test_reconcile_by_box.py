#!/usr/bin/env python3
"""Offline test for tools/reconcile_passes.py --by-box (TXE4-8 BOX-ANCHOR, 12 Oct 2026).
Two per-box passes over one line of 5 boxes: boxes 1 and 3 agree, box 2 differs, box 4 is empty ('-') in both (an
agreement on NONE), box 5 is present in pass A only (a gap column). Expect agree 3/5, 2 disagreement columns, and a
multi-token box ('a b') kept as ONE answer. Must NOT block: a pass without a 'box' column exits with a message naming it.
Run: python3 tools/tests/test_reconcile_by_box.py"""
import contextlib, io, os, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import reconcile_passes as rp

fails = 0
def check(ok, what):
    global fails
    fails += not ok
    print('PASS' if ok else 'FAIL', what)

with tempfile.TemporaryDirectory() as td:
    A = os.path.join(td, 'A.tsv'); B = os.path.join(td, 'B.tsv')
    open(A, 'w').write('line\tbox\tsigns\talt\tconf\nL01\t1\tp\t\tH\nL01\t2\ta b\t\tM\nL01\t3\tx\t\tH\nL01\t4\t-\t\tH\nL01\t5\tz\t\tL\n')
    open(B, 'w').write('line\tbox\tsigns\talt\tconf\nL01\t1\tp\t\tH\nL01\t2\ta\t\tH\nL01\t3\tx\t\tH\nL01\t4\t-\t\tH\n')
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rp.main([A, B, '--by-box', '--out-dir', os.path.join(td, 'rec'), '--no-write'])
    out = buf.getvalue()
    check('agree 3/5' in out, 'agree 3/5 by box (%s)' % out.strip().splitlines()[0][:80])
    check('disagreement columns 2' in out, 'two disagreement columns (box 2 differs, box 5 a gap)')
    check('(by-box)' in out, 'method printed as by-box')
    P, _ = rp.load_box_pass(A, type('a', (), {'line_sub': None, 'halves': False})())
    check(P['L01'][1][0] == 'a b' and P['L01'][3][0] == 'NONE', "multi-token box kept as one answer; '-' -> NONE")
    bad = os.path.join(td, 'bad.tsv'); open(bad, 'w').write('line\tpos\tsign\nL01\t1\tp\n')
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            rp.main([bad, B, '--by-box', '--no-write'])
        check(False, 'a pass without a box column is refused')
    except SystemExit as e:
        check('box' in str(e), 'a pass without a box column is refused, naming the column')
print('reconcile_by_box test:', 'FAIL' if fails else 'OK', fails)
sys.exit(1 if fails else 0)
