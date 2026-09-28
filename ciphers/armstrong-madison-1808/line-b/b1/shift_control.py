"""B1 shift control: corr(n(v), n(10v + 10k)) for k = -3..3. A padding device aligns only at k = 0; a smooth
frequency trend in both ranges would correlate at neighbouring k as well. Also: the collapsed vocabulary."""
import sys
from collections import Counter
sys.path.insert(0, '.')
from padding_test import target_tokens
toks = target_tokens(); c = Counter(toks)
def corr(xs, ys):
    mx = sum(xs)/len(xs); my = sum(ys)/len(ys)
    sxy = sum((x-mx)*(y-my) for x, y in zip(xs, ys)); sxx = sum((x-mx)**2 for x in xs); syy = sum((y-my)**2 for y in ys)
    return sxy / (sxx*syy) ** 0.5 if sxx and syy else float('nan')
print("k  corr(n(v), n(10v+10k)) over v=10..99   [also +/-1..9 unit offsets at k=0 as a finer control]")
for k in range(-3, 4):
    xs = [c[v] for v in range(10, 100)]; ys = [c[10*v + 10*k] for v in range(10, 100)]
    print(f"{k:+d}  {corr(xs, ys):.3f}")
for u in range(1, 10):
    xs = [c[v] for v in range(10, 100)]; ys = [c[10*v + u] for v in range(10, 100)]
    print(f"units offset +{u}: {corr(xs, ys):.3f}")
# x0 tokens whose /10 is present
x0 = [v for v in toks if v >= 100 and v % 10 == 0]
print(f"\nx0 book tokens {len(x0)} of {sum(1 for v in toks if v>=100)} book tokens; with /10 present: "
      f"{sum(1 for v in x0 if v//10 in c)} tokens ({len(set(v for v in x0 if v//10 in c))} distinct); "
      f"with /10 absent: {sum(1 for v in x0 if v//10 not in c)} tokens ({len(set(v for v in x0 if v//10 not in c))} distinct)")
print("x0 values with /10 absent:", sorted(Counter(v for v in x0 if v//10 not in c).items(), key=lambda kv:-kv[1]))
# collapse
def strip(v):
    while v % 10 == 0 and v >= 10: v //= 10
    return v
col = [strip(v) for v in toks]; cc = Counter(col)
print(f"\ncollapsed: distinct {len(cc)} (was {len(c)}), singletons {sum(1 for n in cc.values() if n==1)} (was {sum(1 for n in c.values() if n==1)}), "
      f"tokens <100: {sum(1 for v in col if v<100)} (was {sum(1 for v in toks if v<100)}), distinct <100: {len(set(v for v in col if v<100))}")
print("collapsed top 25:", cc.most_common(25))
u = Counter(v % 10 for v in col if v >= 100)
print("collapsed book units digits:", sorted(u.items()), "n=", sum(u.values()))
