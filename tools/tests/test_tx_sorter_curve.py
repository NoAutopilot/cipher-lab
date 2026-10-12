#!/usr/bin/env python3
"""Offline test for tools/tx_sorter_curve.py: a toy leaf, one line of 6 signs, two atlas clusters, one impure.
Cluster 1 (pos 1-3) is pure value a but the read has pos 2 wrong (X); cluster 2 (pos 4-6) holds value b at 4-5 and
value c at 6 (impure). Cluster propagation: a decision on pos 2 fixes it (net +1); a decision on pos 4 breaks pos 6
(its minority). Pile propagation (cluster x current sign) leaves pos 6 alone when its read differs. No network, no model."""
import json, os, subprocess, sys, tempfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import join_check as JC

TOOL = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tx_sorter_curve.py')
TRUTH = 'line\tpos\tref_sign\ttruth\tplain\tstatus\n' + ''.join(
    'u_L01\t%d\t%s\t%s\t%s\tscored\n' % (p, s, s, v) for p, s, v in
    [(1, 'A', 'a'), (2, 'A', 'a'), (3, 'A', 'a'), (4, 'B', 'b'), (5, 'B', 'b'), (6, 'C', 'c')])
BASE = 'line\tpos\tsign\n' + ''.join('u_L01\t%d\t%s\n' % (p, s) for p, s in
                                     [(1, 'A'), (2, 'X'), (3, 'A'), (4, 'B'), (5, 'B'), (6, 'C')])
MAP = 'sid\tline\tpos\top\n' + ''.join('b%d\tu_L01\t%d\t1:1\n' % (p, p) for p in range(1, 7))
CL = 'id\tkind\tcluster\tdist\n' + ''.join('b%d\tsign\t%d\t%.1f\n' % (p, 1 if p <= 3 else 2, p) for p in range(1, 7))
SIG = 'line\tpos\tsign\tn_signals\n' + ''.join('u_L01\t%d\tS\t%d\n' % (p, n) for p, n in
                                              [(1, 0), (2, 1), (3, 0), (4, 3), (5, 0), (6, 0)])


def run(d, mode, extra=()):
    out = os.path.join(d, 'c_%s.tsv' % mode)
    r = subprocess.run([sys.executable, TOOL, '--truth', d + '/t.tsv', '--base', d + '/b.tsv', '--lines', d + '/b.tsv',
                        '--map', d + '/m.tsv', '--clusters', d + '/c.tsv', '--signals', d + '/s.tsv', '--seeds', '3',
                        '--kmax', '6', '--propagate', mode, '--out', out] + list(extra),
                       capture_output=True, text=True, check=True)
    rows = [l.split('\t') for l in open(out) if not l.startswith('#')][1:]
    return json.loads(r.stdout), rows


def _pass_sidecar(p):
    JC.write_sidecar(p, dict(verdict='PASS', n=0, overall={}, share0=1.0, sharepm1=0.0, b1=True, b2=True, b3=True,
                             p95_0=0.0, p95_pm1=0.0, b2_bound=0.05, lines={}, draws=0, seed=0))


def test_toy():
    with tempfile.TemporaryDirectory() as d:
        for n, t in (('t', TRUTH), ('b', BASE), ('m', MAP), ('c', CL), ('s', SIG)):
            open('%s/%s.tsv' % (d, n), 'w').write(t)
        _pass_sidecar('%s/m.tsv' % d)
        s, rows = run(d, 'cluster')
        assert s['base_wrong'] == 1 and s['scored'] == 6 and s['clusters'] == 2, s
        # doubt order: pos 4 first (3 signals) -> cluster 2 set to B, pos 6 broken; then pos 2 fixes cluster 1
        a = [r for r in rows if r[0] == 'a_doubt']
        assert (a[1][3], a[1][6]) == ('2', '1'), a[1]        # k=1: wrong 2, broken 1
        assert (a[2][3], a[2][5]) == ('1', '1'), a[2]        # k=2: pos 2 fixed
        # oracle: one decision (pos 2) reaches 0 and stops (no decision has a positive net after that)
        assert s['orderings']['d_oracle']['to_2pct'] == 1 and s['orderings']['d_oracle']['steps'] == 1, s
        # size order: cluster sizes tie, pos 1 (dist 1) first -> fixes pos 2 by propagation
        b = [r for r in rows if r[0] == 'b_size']
        assert b[1][3] == '0', b[1]
        s, rows = run(d, 'pile')
        a = [r for r in rows if r[0] == 'a_doubt']
        assert a[1][6] == '0', a[1]                          # pile: pos 6 (read C) is not in pos 4's pile
        s, rows = run(d, 'none')
        assert s['propagation'] == 'none (per tile)' and 'b_size' not in s['orderings'], s
        assert s['orderings']['d_oracle']['steps'] == 1, s


if __name__ == '__main__':
    test_toy()
    print('ok')


# TXE3-1 (11 Oct 2026): the lattice / disagree / margin orders, --at / --thresholds cells and --dump-dir.
# Toy: 6 signs, read has pos 2 wrong (X for A). Signals: only pos 2 disagrees. Atlas top-k: pos 2 has the smallest
# d2-d1 gap, pos 5 has no k2 (infinite margin, last among mapped), pos 6 is unmapped (after). Lattice: a two-candidate
# lattice where only pos 2 carries weight on an alternative, so its value is the only positive one and it ranks first.
# Key: A a, B b, C c, X x (a sign in the key, wrong value) under a tiny corpus of 'abab...' prose.
SIG2 = 'line\tpos\tsign\tdisagree\tn_signals\n' + ''.join('u_L01\t%d\tS\t%d\t%d\n' % (p, d, d) for p, d in
                                                           [(1, 0), (2, 1), (3, 0), (4, 0), (5, 0), (6, 0)])
TOPK_ATLAS = 'page\tline\tbox\tpos\tk1\td1\tk2\td2\n' + ''.join('u\t1\tb%d\t%d\t%s\t%s\t%s\t%s\n' % r for r in
    [(1, 1, 'A', '2.0', 'B', '5.0'), (2, 2, 'A', '2.0', 'X', '2.1'), (3, 3, 'A', '2.0', 'B', '4.0'),
     (4, 4, 'B', '2.0', 'A', '3.0'), (5, 5, 'B', '2.0', '', ''), (6, 6, 'C', '2.0', 'A', '2.5')])
MAP2 = 'sid\tline\tpos\top\n' + ''.join('b%d\tu_L01\t%d\t1:1\n' % (p, p) for p in range(1, 6))   # pos 6 unmapped
LAT = 'line\tpos\tcand\tscore\n' + ''.join('u_L01\t%d\t%s\t%s\n' % r for r in
    [(1, 'A', '1.0'), (2, 'X', '0.6'), (2, 'A', '0.4'), (3, 'A', '1.0'), (4, 'B', '1.0'), (5, 'B', '1.0'), (6, 'C', '1.0')])
KEY = 'sign\tvalue\nA\ta\nB\tb\nC\tc\nX\tx\n'


def test_txe3_orders():
    with tempfile.TemporaryDirectory() as d:
        for n, t in (('t', TRUTH), ('b', BASE), ('m', MAP2), ('c', CL), ('s', SIG2), ('k', TOPK_ATLAS), ('l', LAT), ('key', KEY)):
            open('%s/%s.tsv' % (d, n), 'w').write(t)
        _pass_sidecar('%s/m.tsv' % d)
        open(d + '/corpus.txt', 'w').write(('aab abba cab bac ' * 200))
        out = d + '/c.tsv'
        r = subprocess.run([sys.executable, TOOL, '--truth', d + '/t.tsv', '--base', d + '/b.tsv', '--lines', d + '/b.tsv',
                            '--map', d + '/m.tsv', '--clusters', d + '/c.tsv', '--signals', d + '/s.tsv', '--margin', d + '/k.tsv',
                            '--lattice', d + '/l.tsv', '--key', d + '/key.tsv', '--lattice-corpus', d + '/corpus.txt',
                            '--seeds', '6', '--kmax', '6', '--propagate', 'none', '--at', '1', '3', '--thresholds', '0.5', '0.0',
                            '--dump-dir', d + '/dump', '--out', out], capture_output=True, text=True, check=True)
        s = json.loads(r.stdout)
        o = s['orderings']
        for name in ('disagree', 'margin', 'disagree_margin', 'lattice'):
            assert o[name]['wrong_at']['1'] == 0, (name, o[name])          # pos 2 asked first -> fixed at k=1
            assert o[name]['to_pct']['0.0'] == 1, (name, o[name])
        # margin order among the rest: pos 5 (no k2) is the last mapped tile, pos 6 (unmapped) after it
        rows = [l.rstrip('\n').split('\t') for l in open(out) if not l.startswith('#')][1:]
        assert any(r[0] == 'margin' for r in rows)
        # random seeds vary on the endpoint (the control can fail differently from the target)
        bands = o['c_random']['err_at_min_mean_max']
        assert any(bands[k][0] < bands[k][2] for k in ('1', '3')) and o['c_random']['seeds'] == 6, bands
        assert o['c_random']['to_pct_reached']['0.0'] <= 6
        # dumps: one file per named ordering per --at k, scored positions intact
        assert os.path.exists(d + '/dump/lattice_k1.tsv') and os.path.exists(d + '/dump/margin_k3.tsv')
        dump = [l.split('\t') for l in open(d + '/dump/disagree_k1.tsv')][1:]
        assert len(dump) == 6 and dump[1][2].strip() == 'A', dump
        # a_doubt and d_oracle still present; b_size absent under none
        assert 'a_doubt' in o and 'd_oracle' in o and 'b_size' not in o


def test_map_requires_a_pass_sidecar():
    """TXE4-0 REPAIR unit 2 (12 Oct 2026): --map with no PASS sidecar is refused; --allow-unchecked-join reproduces
    the old output and stamps it to stderr."""
    with tempfile.TemporaryDirectory() as d:
        for n, t in (('t', TRUTH), ('b', BASE), ('m', MAP), ('c', CL), ('s', SIG)):
            open('%s/%s.tsv' % (d, n), 'w').write(t)
        out = os.path.join(d, 'c.tsv')
        argv = [sys.executable, TOOL, '--truth', d + '/t.tsv', '--base', d + '/b.tsv', '--lines', d + '/b.tsv',
                '--map', d + '/m.tsv', '--clusters', d + '/c.tsv', '--signals', d + '/s.tsv', '--seeds', '3',
                '--kmax', '6', '--propagate', 'cluster', '--out', out]
        r = subprocess.run(argv, capture_output=True, text=True)
        assert r.returncode == 2 and 'no .joincheck.json sidecar' in r.stderr, r.stderr
        r2 = subprocess.run(argv + ['--allow-unchecked-join', 'reproducing an old result'], capture_output=True, text=True)
        assert r2.returncode == 0 and 'UNCHECKED JOIN: reproducing an old result' in r2.stderr, r2.stderr


if __name__ == '__main__':
    test_txe3_orders()
    test_map_requires_a_pass_sidecar()
    print('ok txe3')
