#!/usr/bin/env python3
"""Offline test for the soft/hard paired move and the two-stage solve (R9-KAL6, 6 Oct 2026, kaliningrad-2015):
homophonic_anneal.soft_pairs / anneal(pairs=, pair_prob=) and families/homophonic.py --param soft=pair|two-stage.

Must catch: a solver that reads the base letters but leaves the rare soft letters at their hard partners.
Must NOT change: no pairs (or pair_prob 0) is byte-for-byte the old anneal; soft absent is the old family solve
(the default-alphabet fixture of test_homophonic_alphabet.py (a) also still holds).
(a) soft_pairs pairs each upper-case soft letter with its lower case both ways, and nothing for the default alphabet.
(b) ha.solve with pairs=None and with pairs given but pair_prob 0 return the identical key and score.
(c) a synthetic K-36 cipher over ru-s3p-soft (a Gospels window of tools/data/ru19_soft/s3p_soft.txt.gz) is read back
    at >= 0.9 by soft=pair (seed 5) and soft=two-stage (seed 6), one restart each, through families.homophonic.solve,
    soft letters reported. Measured when written (6 Oct 2026, seeds 1-6, one restart each): no soft param
    0/6 restarts >= 0.9 (best 0.24), pair 2/6, two-stage 1/6 -- single restarts rarely converge at this design, so
    the seeds are pinned (deterministic), not a claim about the rate.
"""
import gzip, os, sys
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
T = os.path.join(R, 'tools')
sys.path.insert(0, T)
import homophonic_anneal as ha  # noqa: E402
from families import homophonic as fh  # noqa: E402

# (a)
p = ha.soft_pairs(ha.ALPHABETS['ru-s3p-soft'])
assert p['N'] == 'n' and p['n'] == 'N' and len(p) == 26, p
assert ha.soft_pairs(ha.DEFAULT_ALPHA) == {}
print('ok (a) soft_pairs')

COR = os.path.join(T, 'data', 'ru19_soft', 's3p_soft.txt.gz')
ha.set_alphabet('ru-s3p-soft')
text = ha.fold(gzip.open(COR, 'rt', encoding='utf-8').read())
start = 2000000
plain, train = text[start:start + 1000], text[:start] + text[start + 1000:]
model = ha.Model([train], 3)
seq, pl, truth = ha.make_control(plain, 36, 1000, model, 7)

# (b)
r0 = ha.solve(seq, model, 1, 6000, 3, 1.0)
r1 = ha.solve(seq, model, 1, 6000, 3, 1.0, pairs=p, pair_prob=0.0)
assert r0[0][0] == r1[0][0] and r0[0][1] == r1[0][1]
print('ok (b) pair_prob 0 identical to no pairs')

# (c)
soft = [i for i, c in enumerate(pl) if c.isupper()]
for mode, sd in (('pair', 5), ('two-stage', 6)):
    ha.set_alphabet('ru-s3p-soft')
    dec, sc, info = fh.solve([seq], {}, sd, 1, [train], {'alphabet': 'ru-s3p-soft', 'soft': mode})
    share = fh.score_recovery(dec, pl)
    ss = sum(dec[i] == pl[i] for i in soft) / max(1, len(soft))
    assert share >= 0.9, (mode, share)
    print(f'ok (c) soft={mode}: {share:.3f} of 1000 positions, soft letters {ss:.3f} of {len(soft)}')
ha.set_alphabet(None)
print('all ok')
