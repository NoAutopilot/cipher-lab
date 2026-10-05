#!/usr/bin/env python3
"""N9-BAL3 anchored positive control (PREREG-N9BAL3.md step 4): N9-BAL2's planted control unchanged, plus K anchors = the true
values of K planted s: tokens drawn at random per seed among the s: tokens in planted run 2, passed to n9bal3/anch.py.
N9-BAL2 docstring follows. N9-BAL2 positive control (PREREG-N9BAL2.md): F2 + F1 encoded with a random key of this design (each letter 1-3 sign homophones, the 40
commonest bigrams of the two fragments as 2-letter numeral codes, greedy encode at p=0.6), F2's ciphertext as run 2, F1 planted in the c510
passage (padded with encoded filler to the reconciled c510 length), four filler passages at the reconciled c511 run lengths, token error at
ERR by random substitution from the inventory; same fit and statistic (fit_holdout.run), 20 seeds, 200 null draws each.
  python3 planted_control_anch.py RECONCILED.tsv ERR K
"""
import random, sys
from collections import Counter
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "n9bal2"))
from fit_holdout import load, F1, F2, CANDS, norm
from anch import run
FILL = norm("les dernieres lettres que nous auons du camp de banier sont du sept de ce mois monsieur de beauregard ma enuoie ouuertes les "
            "incluses pour son eminence et pour vous et sur ce que ie luy auois mande de lartifice des imperiaux qui proposent la paix pour "
            "rallentir ledit sieur banier il ma rescrit que ce general promet dans peu de temps de les en faire parler plus serieusement et "
            "quil ne cessera point de leur faire une rude guerre ie tascheray aussy a le confirmer dans le sentiment quil a tesmoigne")
def main():
    rows = load(sys.argv[1]); err = float(sys.argv[2]); K = int(sys.argv[3])
    L = {n: sum(1 for r in rs for k, t in rows.get(r, []) if k == 'cipher') for n, rs in CANDS.items()}
    res = []
    for seed in range(20):
        rng = random.Random(100 + seed)
        hom = {c: [f's:{c}{k}' for k in range(rng.randint(1, 3))] for c in 'abcdefghilmnopqrstuxyz'}
        bg = [b for b, _ in Counter(F1[i:i+2] for i in range(len(F1)-1)) .most_common()]
        bg = [b for b, _ in (Counter(F1[i:i+2] for i in range(len(F1)-1)) + Counter(F2[i:i+2] for i in range(len(F2)-1))).most_common(40)]
        codes = {b: f'{10 + j}' for j, b in enumerate(bg)}
        inv = [t for v in hom.values() for t in v] + list(codes.values())
        def enc(s):
            out, i = [], 0
            while i < len(s):
                if s[i:i+2] in codes and rng.random() < 0.6: out.append(codes[s[i:i+2]]); i += 2
                else: out.append(rng.choice(hom.get(s[i], ['s:?']))); i += 1
            return out
        def noisy(ts): return [rng.choice(inv) if rng.random() < err else t for t in ts]
        fill = enc(FILL); pos = 0
        def take(n):
            nonlocal pos
            seg = fill[pos:pos+n]; pos = (pos + n) % max(1, len(fill) - n); return seg
        r = {'R2a': [('cipher', t) for t in noisy(enc(F2))]}
        f1 = enc(F1); pad = max(0, L['c510'] - len(f1))
        r['R510a'] = [('cipher', t) for t in noisy(take(pad // 2) + f1 + take(pad - pad // 2))]
        for n, rs in CANDS.items():
            if n != 'c510': r[rs[0]] = [('cipher', t) for t in noisy(take(L[n]))]
        truth = {t: c for c, v in hom.items() for t in v}
        s2 = sorted({t for k, t in r['R2a'] if t.startswith('s:') and t in truth})
        arng = random.Random(500 + seed); pick = arng.sample(s2, min(K, len(s2)))
        out = run(r, {t: truth[t] for t in pick}, draws=200); res.append(out)
        print(f"seed {seed}: T {out['T']:.3f} at {out['where']} null1 p99 {out['p1']:.3f} null2 p99 {out['p2']:.3f} -> {out['verdict']}")
    Ts = [o['T'] for o in res]
    print(f"control at err {err}, K {K}: T mean {sum(Ts)/len(Ts):.3f} min {min(Ts):.3f}; PASS {sum(o['verdict']=='PASS' for o in res)}/20; "
          f"F1 found at c510 in {sum(o['where']=='c510' for o in res)}/20")
if __name__ == '__main__': main()
