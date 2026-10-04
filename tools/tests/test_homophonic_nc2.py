#!/usr/bin/env python3
"""Offline test for homophonic_anneal's norm="nc2" (SCORE-NC2, 4 Oct 2026; Lasry, Biermann and Tomokiyo 2023 App. A):
dividing the n-gram score by sum N_c^2 ranks a degenerate all-one-letter key BELOW the true key on a synthetic case
where the plain log-likelihood ranks it ABOVE; the anneal's incremental nc2 score matches a full re-score; and the
default norm="none" path is unchanged."""
import os, random, sys
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(R, 'tools'))
import homophonic_anneal as ha

# A corpus dominated by runs of one letter: under plain log-likelihood "eeee..." is nearly free (P(e|ee) ~ 1),
# the C1161RA failure shape ("all free signs to i") in its purest form.
true = ha.fold('lesennemisontpasselarivieredelalysetmarchentersgand' * 2)
m = ha.Model(['e' * 3000, true, 'nousauonsreceuostrelettredudixiemedecemois' * 3], 3)
deg = 'e' * len(true)
plain_t, plain_d = ha.score(m, true, 0.0), ha.score(m, deg, 0.0)
nc2_t, nc2_d = ha.score(m, true, 0.0, 'nc2'), ha.score(m, deg, 0.0, 'nc2')
assert plain_d > plain_t, (plain_t, plain_d)          # plain LL prefers the degenerate key
assert nc2_t > nc2_d, (nc2_t, nc2_d)                  # nc2 prefers the true key
print(f'ok ranking: plain true {plain_t:.1f} < degenerate {plain_d:.1f}; nc2 true {nc2_t:.1f} > degenerate {nc2_d:.1f}')

# Every shifted n-gram term is >= 0 (floor is the model minimum), so the ratio has the paper's sign.
assert all(m.logp(true[i:i + 3]) >= ha.nc2_floor(m) - 1e-9 for i in range(len(true) - 2))
print('ok floor')

# Incremental anneal score under nc2 equals a full re-score of the returned key (and with uni_w > 0).
seq = [str(ord(c) % 7) + c for c in true]               # a few homophones per letter
for uw in (0.0, 1.0):
    sc, key = ha.anneal(seq, m, 3000, random.Random(5), uw, norm='nc2')
    full = ha.score(m, ''.join(key[x] for x in seq), uw, 'nc2')
    assert abs(sc - full) < 1e-6, (sc, full)
print('ok incremental == full')

# Default path unchanged: norm="none" gives the same result as omitting it, seed for seed.
a = ha.solve(seq, m, 2, 2000, 3, 1.0)
b = ha.solve(seq, m, 2, 2000, 3, 1.0, norm='none')
assert a == b
try:
    ha.solve(seq, m, 1, 10, 1, 1.0, noise=0.1, norm='nc2'); raise AssertionError('noise+nc2 should refuse')
except ValueError:
    pass
print('ok default unchanged; noise+nc2 refused')
