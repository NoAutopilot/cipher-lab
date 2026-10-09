"""Offline test for tools/tx_bench.py (TX-BENCH, 3 Oct 2026)."""
import io, json, os, sys, tempfile, contextlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import tx_bench


def _w(d, name, text):
    p = os.path.join(d, name)
    with open(p, 'w') as f:
        f.write(text)
    return p


def _run(argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = tx_bench.main(argv)
    return rc, buf.getvalue()


def test_scoring():
    with tempfile.TemporaryDirectory() as d:
        # truth: 6 positions; pos 2 is a homophone set, pos 6 excluded
        _w(d, 't.truth.tsv', '# x\nline\tpos\tref_sign\ttruth\tplain\tstatus\n'
           'L1\t1\tA\tA\ta\tscored\nL1\t2\tB\tB|C\tb\tscored\nL1\t3\tD\tD\td\tscored\n'
           'L1\t4\tE\tE\te\tscored\nL1\t5\tF\tF\tf\tscored\nL1\t6\tX\t\t\texcluded:off-sheet\n')
        bench = _w(d, 'B.tsv', 'item\ttruth\tsplit\nit1\tt.truth.tsv\teval\n')
        # perfect, with a homophone swap at pos 2 (C in place of B) -> 0 errors
        o = _w(d, 'o1.tsv', 'line\tpos\tsign\n' + ''.join('L1\t%d\t%s\n' % (i + 1, s) for i, s in enumerate('ACDEFX')))
        rc, out = _run([o, '--bench', bench, '--json'])
        r = json.loads(out)['items'][0]
        assert rc == 0 and r['errors'] == 0 and r['scored'] == 5 and r['excluded'] == 1, r
        # misread D->Q, deleted E, one inserted Z: 3 errors / 5
        o = _w(d, 'o2.tsv', 'passage\tpos\tsign_id\n' + ''.join('L1\t%d\t%s\n' % (i + 1, s) for i, s in enumerate('ABQFZX')))
        rc, out = _run([o, '--bench', bench, '--json'])
        r = json.loads(out)['items'][0]
        assert (r['wrong'], r['deleted'], r['inserted'], r['errors']) == (1, 1, 1, 3), r
        assert any('<-Q' in c for c in r['top_confusions']) and any('<deleted>' in c for c in r['top_confusions']), r
        lo, hi = r['wilson95']
        assert lo < 0.6 < hi
        # an output on lines the bench does not have -> exit 2
        o = _w(d, 'o3.tsv', 'line\tpos\tsign\nZZ\t1\tA\n')
        rc, _ = _run([o, '--bench', bench])
        assert rc == 2


def test_label_map():
    # reconciler split one instruction label into two (D and 4); a reader given only '4' is right under the map
    with tempfile.TemporaryDirectory() as d:
        _w(d, 't.truth.tsv', 'line\tpos\tref_sign\ttruth\tplain\tstatus\n'
           'L1\t1\tD\tD\ta\tscored\nL1\t2\tq\tq\tq\tscored\nL1\t3\t4\t4\tl\tscored\n')
        bench = _w(d, 'B.tsv', 'item\ttruth\tsplit\nit1\tt.truth.tsv\tdev\n')
        o = _w(d, 'o.tsv', 'line\tpos\tsign\nL1\t1\t4\nL1\t2\tq\nL1\t3\t4\n')
        rc, out = _run([o, '--bench', bench, '--json'])
        assert rc == 0 and json.loads(out)['items'][0]['errors'] == 1
        m = _w(d, 'm.tsv', '# c\nfrom\tto\nD\t4\n')
        rc, out = _run([o, '--bench', bench, '--json', '--label-map', m])
        assert rc == 0 and json.loads(out)['items'][0]['errors'] == 0
        # a genuine misread stays wrong under the map
        o2 = _w(d, 'o2.tsv', 'line\tpos\tsign\nL1\t1\tq\nL1\t2\tq\nL1\t3\t4\n')
        rc, out = _run([o2, '--bench', bench, '--json', '--label-map', m])
        assert json.loads(out)['items'][0]['errors'] == 1


def test_wilson():
    lo, hi = tx_bench.wilson(0, 10)
    assert lo == 0.0 and 0.25 < hi < 0.35
    assert tx_bench.wilson(0, 0) == (0.0, 0.0)


def test_repo_bench_parses():
    root = os.path.join(os.path.dirname(__file__), '..', '..')
    b = os.path.join(root, 'BENCHMARK-TX.tsv')
    if not os.path.exists(b):
        return
    for item in tx_bench.read_tsv(b):
        rows = tx_bench.read_tsv(os.path.join(root, item['truth']))
        assert sum(r['status'] == 'scored' for r in rows) == int(item['n_scored']), item['item']
        assert item['split'] in ('dev', 'eval')




def test_exclude_flagged():
    with tempfile.TemporaryDirectory() as d:
        # pos 3 flagged (excluded under the switch), pos 4 corrected (stays scored), pos 6 excluded already
        _w(d, 't.truth.tsv', '# x\nline\tpos\tref_sign\ttruth\tplain\tstatus\tflag\n'
           'L1\t1\tA\tA\ta\tscored\t\nL1\t2\tB\tB\tb\tscored\t\nL1\t3\tD\tD\td\tscored\talignment-doubtful\n'
           'L1\t4\tE\tE|Q\te\tscored\tcorrected:key-doubtful\nL1\t5\tF\tF\tf\tscored\t\nL1\t6\tX\t\t\texcluded:off-sheet\t\n')
        bench = _w(d, 'B.tsv', 'item\ttruth\tsplit\nit1\tt.truth.tsv\teval\n')
        # wrong at 3 (flagged) and 5 (not flagged); Q at 4 is right after correction
        o = _w(d, 'o.tsv', 'line\tpos\tsign\n' + ''.join('L1\t%d\t%s\n' % (i + 1, s) for i, s in enumerate('ABZQZX')))
        rc, out = _run([o, '--bench', bench, '--json'])
        r = json.loads(out)['items'][0]
        assert (r['errors'], r['scored']) == (2, 5) and 'flagged_excluded' not in r, r
        rc, out = _run([o, '--bench', bench, '--json', '--exclude-flagged'])
        r = json.loads(out)['items'][0]
        f = r['flagged_excluded']
        assert (r['errors'], r['scored']) == (2, 5), r  # as measured unchanged by the switch
        assert (f['errors'], f['scored'], f['flagged']) == (1, 4, 1), f
        rc, out = _run([o, '--bench', bench, '--exclude-flagged'])
        assert 'as measured 0.400 (2/5) | flagged excluded 0.250 (1/4)' in out, out
        # a truth file with no flag column: both figures equal
        _w(d, 't.truth.tsv', '# x\nline\tpos\tref_sign\ttruth\tplain\tstatus\nL1\t1\tA\tA\ta\tscored\n')
        o = _w(d, 'o3.tsv', 'line\tpos\tsign\nL1\t1\tA\n')
        rc, out = _run([o, '--bench', bench, '--json', '--exclude-flagged'])
        f = json.loads(out)['items'][0]['flagged_excluded']
        assert (f['errors'], f['scored'], f['flagged']) == (0, 1, 0), f


if __name__ == '__main__':
    test_scoring(); test_label_map(); test_wilson(); test_repo_bench_parses(); test_exclude_flagged(); print('ok')
