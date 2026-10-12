#!/usr/bin/env python3
"""Offline test of tools/tx_selfcheck.py (TXE4-4 SELF-CHECK, 12 Oct 2026). No atlas, no network, no truth file:
synthetic features. (1) LOLO never trains on the classified line: a label unique to the classified line can never be
its own top-1 vote. (2) The isotonic map is monotone non-decreasing and reproduces a clean step. (3) The flip rule
flips only where p1 >= tau and pA <= eps, and never to the pass's own sign."""
import os, sys, random
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import tx_selfcheck as SC


def synth():
    rnd = np.random.default_rng(3)
    rows, X, labels = [], [], {}
    # 3 lines x 12 boxes; two shape classes 'A' (near 0) and 'B' (near 5); line 3 carries a label 'Z' nowhere else
    for ln in (1, 2, 3):
        for p in range(1, 13):
            sid = f'pg_{ln:02d}_{p:03d}'
            cls = 'A' if p % 2 else 'B'
            X.append(rnd.normal(0.0 if cls == 'A' else 5.0, 0.3, size=4))
            rows.append(dict(sid=sid, page='pg', line=str(ln)))
            labels[sid] = 'Z' if ln == 3 else cls
    return np.array(X), rows, labels


def test_lolo_never_trains_on_own_line():
    X, rows, labels = synth()
    tk = SC.lolo_topk(X, rows, labels, [r['sid'] for r in rows], own=labels)
    l3 = [r for r in tk if r['line'] == 'pg_3']
    assert l3 and all(r['k1'] != 'Z' and r['k2'] != 'Z' and r['k3'] != 'Z' for r in l3), 'a line-3-only label voted on line 3'
    # with the other lines' labels the shape classes are recovered on line 3
    assert all((r['k1'] == 'A') == (int(r['sid'][-3:]) % 2 == 1) for r in l3)
    # and the pass's own sign 'Z' on line 3 has share 0 (absent from every voter) -> uA = -0.25
    assert all(float(r['sA']) == 0.0 and float(r['uA']) == -SC.LAM_MARGIN for r in l3)
    print('ok test_lolo_never_trains_on_own_line')


def test_isotonic_monotone():
    rnd = random.Random(1)
    u = [rnd.random() for _ in range(200)]
    y = [1.0 if (x > 0.5) != (rnd.random() < 0.1) else 0.0 for x in u]
    knots = SC.pav(u, y)
    ps = [SC.calibrate(knots, x / 100) for x in range(101)]
    assert all(b >= a for a, b in zip(ps, ps[1:])), 'isotonic map not monotone'
    assert SC.calibrate(knots, 0.05) < 0.3 < 0.7 < SC.calibrate(knots, 0.95)
    print('ok test_isotonic_monotone')


def test_flip_rule_respects_tau_eps():
    knots = [(0.0, 0.0), (1.0, 1.0)]   # identity
    tk = [dict(sid='a', line='L', pos='1', sign='T1', k1='T2', u1='0.9', uA='0.05'),   # flips at tau .8 eps .1
          dict(sid='b', line='L', pos='2', sign='T1', k1='T2', u1='0.7', uA='0.05'),   # p1 under tau
          dict(sid='c', line='L', pos='3', sign='T1', k1='T2', u1='0.9', uA='0.3'),    # pA over eps
          dict(sid='d', line='L', pos='4', sign='T2', k1='T2', u1='0.9', uA='0.9'),    # own sign is the top-1
          dict(sid='e', line='L', pos='5', sign='T1', k1='', u1='', uA='')]            # nothing classified
    f = SC.flips_for(tk, knots, 0.8, 0.1)
    assert [x['sid'] for x in f] == ['a'], f
    assert [x['sid'] for x in SC.flips_for(tk, knots, 0.6, 0.1)] == ['a', 'b']
    assert [x['sid'] for x in SC.flips_for(tk, knots, 0.8, 0.5)] == ['a', 'c']
    assert all(x['new'] != x['old'] for x in SC.flips_for(tk, knots, 0.0, 1.0))
    print('ok test_flip_rule_respects_tau_eps')


if __name__ == '__main__':
    test_lolo_never_trains_on_own_line(); test_isotonic_monotone(); test_flip_rule_respects_tau_eps()
    print('test_tx_selfcheck: all passed')
