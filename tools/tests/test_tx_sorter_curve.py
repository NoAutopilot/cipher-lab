#!/usr/bin/env python3
"""Offline test for tools/tx_sorter_curve.py: a toy leaf, one line of 6 signs, two atlas clusters, one impure.
Cluster 1 (pos 1-3) is pure value a but the read has pos 2 wrong (X); cluster 2 (pos 4-6) holds value b at 4-5 and
value c at 6 (impure). Cluster propagation: a decision on pos 2 fixes it (net +1); a decision on pos 4 breaks pos 6
(its minority). Pile propagation (cluster x current sign) leaves pos 6 alone when its read differs. No network, no model."""
import json, os, subprocess, sys, tempfile

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


def test_toy():
    with tempfile.TemporaryDirectory() as d:
        for n, t in (('t', TRUTH), ('b', BASE), ('m', MAP), ('c', CL), ('s', SIG)):
            open('%s/%s.tsv' % (d, n), 'w').write(t)
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
