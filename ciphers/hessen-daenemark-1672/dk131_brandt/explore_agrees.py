"""BRANDT-TX EXPLORATORY (not pre-registered, does not change PREREG-BRANDT-TX's FAIL): the tool's token-level 'agrees' count
(a token whose chunk equals its value's top meaning, value seen >= 2 times) for the real pairs vs 200 derangements, seed 1672,
same alignment parameters as the primary run."""
import sys, random, collections
sys.path.insert(0, '../../../tools')
import interlinear_align as ia
pairs = ia.load_pairs('pairs_0020.tsv')
kw = dict(floor=150, clear_consumes=True, prior=None, code_prefix=None, null_cost=-3.0, wildcard=None, max_chunk=8,
          seg_bonus=1.0, len_prior=0.0)
def agrees(ps):
    prep, res, counts, shown = ia.run_align(ps, **kw)
    rows = ia.token_rows(prep, res, counts, shown)
    return sum(1 for r in rows if r[-1] == 'agrees')
real = agrees(pairs)
rng = random.Random(1672); idx = list(range(len(pairs))); d = []
for _ in range(200):
    while True:
        p = idx[:]; rng.shuffle(p)
        if all(a != b for a, b in zip(idx, p)): break
    d.append(agrees([dict(q, plain_raw=pairs[k]['plain_raw']) for q, k in zip(pairs, p)]))
d.sort()
print('EXPLORATORY agrees: real %d; control mean %.1f, p95 %d, max %d; p = %.4f' % (real, sum(d)/len(d), d[190], d[-1],
      (1 + sum(x >= real for x in d)) / 201))
