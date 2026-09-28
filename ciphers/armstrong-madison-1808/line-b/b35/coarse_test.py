"""B35 addendum: does a coarser inventory rescue reader agreement? Learn label merges from the confusions on crops
1-15 (union-find over every pair confused >=2 times), then measure positional agreement on the held-out crops 16-29
under the merged labels, against the raw agreement there. Also the reverse split. Pure held-out: the merge rule never
sees the crops it is scored on."""
import sys; sys.argv = ["x"]
from reconcile import A, B, glyphs, Counter
def conf_pairs(crops):
    c = Counter()
    for k in crops:
        ga, gb = glyphs(A[k]), glyphs(B[k])
        if len(ga) == len(gb):
            for x, y in zip(ga, gb):
                if x != y and "??" not in (x, y): c[tuple(sorted((x, y)))] += 1
    return c
def merge_map(c, thr=2):
    par = {}
    def f(x):
        par.setdefault(x, x)
        while par[x] != x: par[x] = par[par[x]]; x = par[x]
        return x
    for (x, y), n in c.items():
        if n >= thr: par[f(x)] = f(y)
    return f
def agree(crops, f):
    s = t = 0
    for k in crops:
        ga, gb = glyphs(A[k]), glyphs(B[k])
        if len(ga) == len(gb):
            for x, y in zip(ga, gb): t += 1; s += (f(x) == f(y))
    return s, t
for train, test in (((range(1, 16)), range(16, 30)), (range(16, 30), range(1, 16))):
    c = conf_pairs(train); f = merge_map(c)
    classes = len({f(x) for k in A for x in glyphs(A[k])} | {f(x) for k in B for x in glyphs(B[k])})
    raw = agree(test, lambda x: x); merged = agree(test, f)
    print(f"train crops {min(train)}-{max(train)} -> merged inventory of {classes} classes (from {len({x for k in A for x in glyphs(A[k])} | {x for k in B for x in glyphs(B[k])})} labels used); "
          f"held-out {min(test)}-{max(test)}: raw {raw[0]}/{raw[1]} = {raw[0]/raw[1]:.2f}, merged {merged[0]}/{merged[1]} = {merged[0]/merged[1]:.2f}")
