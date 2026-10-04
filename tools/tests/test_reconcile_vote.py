#!/usr/bin/env python3
"""Offline test for tools/reconcile_passes.py --vote / --err-truth and tools/tx_bench.py --paired (TX-VIEWS, 4 Oct 2026).
1. Five passes on one synthetic line: the vote takes the 3-of-5 sign (vote_share 0.60), drops a sign only one pass
   inserted (gap majority), and keeps a sign four passes read and one dropped.
2. err_corr on a synthetic truth: two passes making the same wrong read on the same position correlate (phi 1.0, same_wrong
   1); a pass with errors elsewhere has phi below zero against them.
3. tx_bench.paired / sign_test: fixed/broken counted on the same positions; sign_test(8, 0) < 0.01, sign_test(3, 3) = 1.
Run: python3 tools/tests/test_reconcile_vote.py"""
import os, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import reconcile_passes as rp
import tx_bench as tb

fails = 0
def check(ok, what):
    global fails
    fails += not ok
    print('PASS' if ok else 'FAIL', what)

tmp = tempfile.mkdtemp()
def wp(name, signs):
    p = os.path.join(tmp, name + '.tsv')
    open(p, 'w').write('line\tpos\tsign\n' + ''.join('L1\t%d\t%s\n' % (i, s) for i, s in enumerate(signs, 1)))
    return p
truth_signs = ['a', 'b', 'c', 'd', 'e', 'f']
P = [wp('A', 'a b c d e f'.split()), wp('B', 'a x c d e f'.split()), wp('C', 'a x c d e f'.split()),
     wp('D', 'a b c d q e f'.split()), wp('E', 'a b c d e'.split())]
truth = os.path.join(tmp, 'truth.tsv')
open(truth, 'w').write('line\tpos\tref_sign\ttruth\tplain\tstatus\n' +
                       ''.join('L1\t%d\t%s\t%s\t%s\tscored\n' % (i, s, s, s) for i, s in enumerate(truth_signs, 1)))
r = rp.main(P + ['--vote', '--err-truth', truth, '--no-write'])
v = [(x[2], x[3]) for x in r['votes']]
check([s for s, _ in v] == truth_signs, 'vote sequence = truth (inserted q dropped, f kept): %s' % [s for s, _ in v])
check(v[1] == ('b', '0.60'), "3-of-5 sign 'b' at vote_share 0.60 (got %s)" % (v[1],))
check(v[5] == ('f', '0.80'), "4-of-5 sign kept despite one pass's gap (got %s)" % (v[5],))
corr = {(x[0], x[1]): x for x in r['err_corr']}
bc = corr[('B', 'C')]
check(bc[5] == 1 and bc[6] == 1 and bc[7] == 1.0, 'B and C share one same-wrong error, phi 1.0 (got %s)' % (bc,))
check(corr[('B', 'E')][7] < 0, 'B vs E (errors on different positions) phi < 0 (got %s)' % (corr[('B', 'E')][7],))
check(corr[('A', 'vote')][4] == 0, 'the vote has no error on this line')
tr = tb.read_tsv(truth)
pr = tb.paired(tr, tb.load_output([P[1]]), tb.load_output([P[0]]))
check((pr['fixed'], pr['broken'], pr['n']) == (1, 0, 6), 'paired B -> A: fixed 1 broken 0 on 6 (got %s)' % (pr,))
check(tb.sign_test(8, 0) < 0.01 and tb.sign_test(3, 3) == 1.0, 'sign test p(8,0) < 0.01 and p(3,3) = 1')
print('reconcile_vote: all tests pass' if not fails else 'reconcile_vote: %d FAILED' % fails)
sys.exit(1 if fails else 0)
