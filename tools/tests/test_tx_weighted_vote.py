"""Offline test for tools/tx_weighted_vote.py (LANE TX-ENGINEER-2 X5, 9 Oct 2026): three readers, one biased."""
import io, os, sys, tempfile, contextlib, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import tx_weighted_vote as W
import tx_bench


def _w(d, name, text):
    p = os.path.join(d, name)
    with open(p, 'w') as f:
        f.write(text)
    return p


def test_biased_reader_fixed_by_loo_not_uniform():
    # truth: 6 lines "P S R"; reader A is right; readers B and C both read P as Q (a systematic bias).
    # Uniform: B+C outvote A at every P (base = B's read). LOO weights learn B/C's Q means P -> fixed.
    lines = ['f1_L%02d' % i for i in range(1, 7)]
    truth = '# t\nline\tpos\tref_sign\ttruth\tplain\tstatus\n'
    ra = rb = 'line\tpos\tsign\n'
    for ln in lines:
        for i, (t, b) in enumerate([('P', 'Q'), ('S', 'S'), ('R', 'R')], 1):
            truth += '%s\t%d\t%s\t%s\tx\tscored\n' % (ln, i, t, t)
            ra += '%s\t%d\t%s\n' % (ln, i, t)
            rb += '%s\t%d\t%s\n' % (ln, i, b)
    with tempfile.TemporaryDirectory() as d:
        _w(d, 't.truth.tsv', truth)
        bench = _w(d, 'B.tsv', 'item\ttruth\tsplit\nit1\tt.truth.tsv\tdev\n')
        pa, pb = _w(d, 'A.tsv', ra), _w(d, 'Bp.tsv', rb)
        pc = _w(d, 'C.tsv', rb)
        key = _w(d, 'key.tsv', 'sign\tvalue\nP\tp\nQ\tq\nR\tr\nS\ts\n')
        common = ['--bench', bench, '--item', 'it1', '--key', key, '--reader', 'A=' + pa, '--reader', 'B=' + pb,
                  '--reader', 'C=' + pc, '--base', pb]
        out_w, out_u = os.path.join(d, 'w.tsv'), os.path.join(d, 'u.tsv')
        with contextlib.redirect_stdout(io.StringIO()):
            assert W.main(['vote', '--loo', '--train', pa, '--out', out_w] + common) == 0
            assert W.main(['vote', '--uniform', '--out', out_u] + common) == 0
            assert W.main(['control', '--train', pa, '--out-dir', d, '--stem', 'x'] + common) == 0
            assert W.main(['learn', '--train', pa, '--out', os.path.join(d, 'w.json')] + common[:-2]) == 0
        T = tx_bench.read_tsv(os.path.join(d, 't.truth.tsv'))
        ew = tx_bench.position_errors(T, tx_bench.load_output([out_w]))
        eu = tx_bench.position_errors(T, tx_bench.load_output([out_u]))
        assert sum(ew.values()) == 0, ew
        assert sum(eu.values()) == 6, eu                    # uniform keeps the biased majority
        J = json.load(open(os.path.join(d, 'w.json')))
        assert J['counts']['B']['Q'] == {'P': 6}
        for s in range(1, 6):
            assert os.path.exists(os.path.join(d, 'x_perm%d_dev_tune.tsv' % s))


def test_loo_excludes_own_line():
    # a bias seen on ONE line only cannot be learnt when that line is held out
    truth = '# t\nline\tpos\tref_sign\ttruth\tplain\tstatus\nf1_L01\t1\tP\tP\tp\tscored\nf1_L02\t1\tR\tR\tr\tscored\n'
    with tempfile.TemporaryDirectory() as d:
        _w(d, 't.truth.tsv', truth)
        bench = _w(d, 'B.tsv', 'item\ttruth\tsplit\nit1\tt.truth.tsv\tdev\n')
        pb = _w(d, 'b.tsv', 'line\tpos\tsign\nf1_L01\t1\tQ\nf1_L02\t1\tR\n')
        key = _w(d, 'key.tsv', 'sign\nP\nQ\nR\n')
        out = os.path.join(d, 'o.tsv')
        with contextlib.redirect_stdout(io.StringIO()):
            W.main(['vote', '--loo', '--train', pb, '--out', out, '--bench', bench, '--item', 'it1', '--key', key,
                    '--reader', 'B=' + pb, '--base', pb])
        assert tx_bench.load_output([out])['f1_L01'] == ['Q']


if __name__ == '__main__':
    test_biased_reader_fixed_by_loo_not_uniform(); test_loo_excludes_own_line(); print('ok')
