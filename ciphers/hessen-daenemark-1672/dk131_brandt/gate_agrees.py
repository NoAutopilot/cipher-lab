"""BRANDT-GATE test 1 (PREREG-BRANDT-GATE.md, pushed 13865ab70 before this score): token 'agrees' count on pairs_0020.tsv,
same computation as explore_agrees.py, n 2000 derangements, seed 20261009. Gate: real > control max AND p < 0.01."""
import sys, random
sys.path.insert(0, '../../../tools')
import interlinear_align as ia
pairs = ia.load_pairs('pairs_0020.tsv')
kw = dict(floor=150, clear_consumes=True, prior=None, code_prefix=None, null_cost=-3.0, wildcard=None, max_chunk=8,
          seg_bonus=1.0, len_prior=0.0)
def agrees(ps):
    prep, res, counts, shown = ia.run_align(ps, **kw)
    return sum(1 for r in ia.token_rows(prep, res, counts, shown) if r[-1] == 'agrees')
N = 2000
real = agrees(pairs)
rng = random.Random(20261009); idx = list(range(len(pairs))); d = []
for _ in range(N):
    while True:
        p = idx[:]; rng.shuffle(p)
        if all(a != b for a, b in zip(idx, p)): break
    d.append(agrees([dict(q, plain_raw=pairs[k]['plain_raw']) for q, k in zip(pairs, p)]))
d.sort()
pv = (1 + sum(x >= real for x in d)) / (N + 1)
ok = real > d[-1] and pv < 0.01
print('TEST1 agrees: real %d; control mean %.2f, p95 %d, p99 %d, max %d, n %d; p = %.4f; gate %s'
      % (real, sum(d) / N, d[int(.95 * N)], d[int(.99 * N)], d[-1], N, pv, 'PASS' if ok else 'FAIL'))
