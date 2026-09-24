#!/usr/bin/env python3
"""Pairing test with a matched control (rule 3), 24 Sept 2026. Unseeded hard-EM (align_f86.em, seeded=False) of the
f.86 cipher segments against (a) the matching f.87 paragraph-1 stretches and (b) controls of the same length: the
same stretches with the letters of each shuffled (seeds 0-4), and f.87 paragraph 2 cut to the same lengths.
Statistic: share of group occurrences that take their group's modal value (key consistency)."""
import random, align_f86 as A


def consistency(segs):
    counts, _ = A.em(segs, seeded=False)
    tot = sum(sum(c.values()) for c in counts.values())
    return sum(c.most_common(1)[0][1] for c in counts.values()) / tot


segs = A.segments()
print('real      %.3f' % consistency(segs))
for seed in range(5):
    r = random.Random(seed)
    sh = [(n, t, ''.join(r.sample(p, len(p)))) for n, t, p in segs]
    print('shuffled%d %.3f' % (seed, consistency(sh)))
p2 = A.norm(' '.join(open('dechiffre_f87.txt').read().split('\n')[14:]))
p2 = (p2 * 3)
o, ctl = 0, []
for n, t, p in segs:
    ctl.append((n, t, p2[o:o + len(p)])); o += len(p)
print('para2     %.3f' % consistency(ctl))

# Seeded run (the seeds come from the real pairing, so this favours it; reported for completeness only)
def consistency_seeded(segs):
    counts, _ = A.em(segs, seeded=True)
    tot = sum(sum(c.values()) for c in counts.values())
    return sum(c.most_common(1)[0][1] for c in counts.values()) / tot


print('seeded real %.3f  shuffled0 %.3f  para2 %.3f' % (consistency_seeded(segs), consistency_seeded(
    [(n, t, ''.join(random.Random(0).sample(p, len(p)))) for n, t, p in segs]), consistency_seeded(ctl)))
