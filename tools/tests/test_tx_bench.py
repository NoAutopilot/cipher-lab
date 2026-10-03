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


if __name__ == '__main__':
    test_scoring(); test_wilson(); test_repo_bench_parses(); print('ok')
