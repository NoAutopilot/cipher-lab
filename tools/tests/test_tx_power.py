"""Offline test for tools/tx_power.py (LANE TX-ENGINEER-2 round 0a, 9 Oct 2026): the power audit must say a clean 30% fixer
cannot pass p < 0.01 on 15 errors, can on 60, and that the no-op and the 30%-worse controls never pass."""
import io, os, sys, random, contextlib, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import tx_power


def test_simulate_shapes():
    rng = random.Random(3)
    m15 = tx_power.simulate(15, 376, 0.3, [0.01, 0.05], 400, rng)
    m60 = tx_power.simulate(60, 700, 0.3, [0.01, 0.05], 400, rng)
    assert m15['clean'][0.01] < 0.2, m15           # 15 errors: a clean 30% fixer almost never reaches p < 0.01
    assert m60['clean'][0.01] > 0.9, m60           # 60 errors: it does
    assert m15['noop'][0.05] == 0.0 and m60['noop'][0.05] == 0.0
    assert m15['worse'][0.05] == 0.0 and m60['worse'][0.05] == 0.0   # a worse instrument never passes (fixed > broken fails)
    assert m60['random3'][0.01] <= 0.02


def test_min_errors_monotone():
    rng = random.Random(5)
    e01 = tx_power.min_errors(0.3, 0.01, 200, rng)
    e05 = tx_power.min_errors(0.3, 0.05, 200, rng)
    assert e01 is not None and e05 is not None and e05 <= e01
    assert 25 <= e01 <= 45, e01


def test_main_from_files():
    with tempfile.TemporaryDirectory() as d:
        t = os.path.join(d, 't.truth.tsv')
        with open(t, 'w') as f:
            f.write('line\tpos\tref_sign\ttruth\tplain\tstatus\n')
            for i in range(1, 41):
                f.write('f1_L01\t%d\tA\tA\ta\tscored\n' % i)
        b = os.path.join(d, 'B.tsv')
        with open(b, 'w') as f:
            f.write('item\ttruth\tsplit\nit1\t%s\teval\n' % t)
        o = os.path.join(d, 'o.tsv')
        with open(o, 'w') as f:
            f.write('line\tpos\tsign\n')
            for i in range(1, 41):
                f.write('f1_L01\t%d\t%s\n' % (i, 'A' if i > 4 else 'Z'))   # 4 errors
        md = os.path.join(d, 'out.md')
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = tx_power.main(['--bench', b, '--unit', 'u=it1:' + o, '--pool', 'p=u', '--draws', '50', '--md', md])
        assert rc == 0
        txt = open(md).read()
        assert '| u | 4 | 40 | 0.3 |' in txt and '| p | 4 | 40 |' in txt, txt
