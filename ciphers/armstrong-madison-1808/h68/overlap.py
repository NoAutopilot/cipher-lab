"""H68: overlap of the 27 Dec 1807 (M34 roll 13 f.0390) groups >1600 with the target's values >1600,
against 2,000 random value sets of the same size from the same numeric range (rule 3: an order shuffle
could not differ, so the control redraws values). Readings from h67/reads.tsv (two passes)."""
import re, random
tgt = {int(x) for x in re.findall(r'\d+', open('ciphertext.txt').read()) if 1600 < int(x) < 2000}
sets = {
    'firm (both passes 17xx)': {1716, 1717},
    'maximal (any pass or Bourdeau 17xx)': {1701, 1716, 1717, 1719, 1725, 1727, 1730, 1757, 1768},
}
lo, hi = 1601, 1800
random.seed(68)
print(f'target distinct values 1601-1999: {len(tgt)}; in {lo}-{hi}: {len([v for v in tgt if v<=hi])}')
for name, s in sets.items():
    obs = len(s & tgt)
    null = sorted(len(set(random.sample(range(lo, hi + 1), len(s))) & tgt) for _ in range(2000))
    p = sum(n >= obs for n in null) / len(null)
    print(f'{name}: n={len(s)} overlap={obs} {sorted(s & tgt)}  null mean={sum(null)/len(null):.2f} p99={null[int(.99*len(null))]}  P(null>=obs)={p:.3f}')
