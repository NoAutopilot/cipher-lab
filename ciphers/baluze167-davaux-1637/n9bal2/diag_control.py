#!/usr/bin/env python3
"""N9-BAL2 diagnostic of the planted control's power (not a gate): at 0% error, how many run-2 tokens get their true chunk from the
F2-only fit, and what share of F1's encoded tokens also occur in run 2 (the ceiling on what an F2-fitted key can decode in F1)."""
import random
from collections import Counter
from fit_holdout import F1, F2, fit_key
acc, cov, cov_ok = [], [], []
for seed in range(20):
    rng = random.Random(100 + seed)
    hom = {c: [f's:{c}{k}' for k in range(rng.randint(1, 3))] for c in 'abcdefghilmnopqrstuxyz'}
    bg = [b for b, _ in (Counter(F1[i:i+2] for i in range(len(F1)-1)) + Counter(F2[i:i+2] for i in range(len(F2)-1))).most_common(40)]
    codes = {b: f'{10 + j}' for j, b in enumerate(bg)}; true = {v: k for k, v in codes.items()}
    for c, hs in hom.items():
        for h in hs: true[h] = c
    def enc(s):
        out, i = [], 0
        while i < len(s):
            if s[i:i+2] in codes and rng.random() < 0.6: out.append(codes[s[i:i+2]]); i += 2
            else: out.append(rng.choice(hom[s[i]])); i += 1
        return out
    r2 = enc(F2); f1 = enc(F1)
    key, ch, al = fit_key(r2)
    acc.append(sum(c == true[t] for t, c in al) / len(al))
    cov.append(sum(t in key for t in f1) / len(f1))
    cov_ok.append(sum(key.get(t) == true[t] for t in f1) / len(f1))
m = lambda x: sum(x) / len(x)
print(f'run-2 tokens fitted to their true chunk: mean {m(acc):.3f} (min {min(acc):.3f}); F1 tokens present in run 2: {m(cov):.3f}; '
      f'F1 tokens decoded correctly by the F2 fit: {m(cov_ok):.3f}  (20 seeds, 0% error)')
