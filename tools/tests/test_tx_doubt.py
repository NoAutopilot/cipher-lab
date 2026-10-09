#!/usr/bin/env python3
"""Offline test for tools/tx_doubt.py: a synthetic 20-position unit with planted signals and planted wrong positions;
the recall / flag-share table and the best-combination search must return the planted answer. No network, no model."""
import csv, os, sys, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import tx_doubt as TD  # noqa: E402

WRONG = {3, 7, 11, 15}                      # planted wrong positions
PLANT = {'show': {3, 7, 11, 1, 2, 4, 5, 6, 8, 9},   # high recall, high share
         'disagree': {3, 7},                # half the errors at 10%
         'latt': {11, 15},                  # the other half at 10%
         'pair': {1, 2}, 'bandcut': {20}, 'thin': set(), 'contrast': set(), 'stab': set(), 'freq': {15, 16}}


def rows():
    out = []
    for p in range(1, 21):
        r = dict(line='u_L01', pos=str(p), sign='T1')
        for s in TD.SIGNALS:
            r[s] = str(int(p in PLANT[s]))
        r['n_signals'] = str(sum(int(r[s]) for s in TD.SIGNALS))
        out.append(r)
    return out


def test_tables():
    rs, wrong = rows(), {('u_L01', p): p in WRONG for p in range(1, 21)}
    s = TD.stats(rs, wrong, ['show'])
    assert (s['tp'], s['wrong'], s['flagged'], s['n']) == (3, 4, 10, 20) and abs(s['share'] - 0.5) < 1e-9, s
    s = TD.stats(rs, wrong, ['disagree', 'latt'])
    assert s['recall'] == 1.0 and abs(s['share'] - 0.2) < 1e-9, s
    best = TD.best_combos(rs, wrong, TD.SIGNALS, 3, [0.10, 0.15, 0.20])
    assert best[(2, 0.2)]['combo'] == 'disagree+latt' and best[(2, 0.2)]['recall'] == 1.0, best[(2, 0.2)]
    assert best[(1, 0.1)]['tp'] == 2 and best[(1, 0.1)]['combo'] in ('disagree', 'latt', 'freq'), best[(1, 0.1)]
    assert best[(1, 0.1)]['combo'] in ('disagree', 'latt'), best[(1, 0.1)]   # ties: alphabetical among equal share
    assert best[(3, 0.15)]['tp'] == 2, best[(3, 0.15)]     # no 3-flag set holds 3 errors (cap 0.15 = 3 of 20)
    n2 = TD.nmin_stats(rs, wrong, 2)
    assert n2['tp'] == 4 and n2['flagged'] == 6, n2      # 3, 7, 11 (show+x), 15 (latt+freq), 1, 2 (show+pair)


def test_freq_flags():
    L = [dict(line='p_L01', pos=str(i), sign='TA') for i in range(30)] + \
        [dict(line='p_L01', pos=str(30 + i), sign='TB') for i in range(30)]
    key = {'TA': 'a', 'TB': 'b', 'TC': 'a'}
    over = TD.freq_flags(L, key, {'a': 0.5, 'b': 0.5})
    assert ('p', 'TA') in over and ('p', 'TB') not in over, over   # TA carries all of 'a' though it has a homophone


def test_measure_end_to_end():
    d = tempfile.mkdtemp()
    rs = rows()
    with open(os.path.join(d, 'u_signals.tsv'), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rs[0]), delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(rs)
    with open(os.path.join(d, 'truth.tsv'), 'w') as f:
        f.write('line\tpos\tref_sign\ttruth\tstatus\tplain\n')
        for p in range(1, 21):
            t = 'T2' if p in WRONG else 'T1'
            f.write(f'u_L01\t{p}\t{t}\t{t}\tscored\tx\n')
    with open(os.path.join(d, 'read.tsv'), 'w') as f:
        f.write('line\tpos\tsign\n' + ''.join(f'u_L01\t{p}\tT1\n' for p in range(1, 21)))
    rep = TD.main(['measure', '--unit', 'u', '--out', d, '--truth', os.path.join(d, 'truth.tsv'),
                   '--read', os.path.join(d, 'read.tsv'), '--combo', 'disagree+latt'])
    assert rep['L']['combo']['recall'] == 1.0 and rep['L']['best']['k2_cap0.2']['combo'] == 'disagree+latt', rep['L']
    fl = TD.main(['list', '--unit', 'u', '--out', d, '--combo', 'disagree+latt'])
    assert [int(r['pos']) for r in fl] == [3, 7, 11, 15]


if __name__ == '__main__':
    test_tables(); test_freq_flags(); test_measure_end_to_end()
    print('ok')
