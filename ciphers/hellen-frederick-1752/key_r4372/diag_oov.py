#!/usr/bin/env python3
"""N4-HEL6, NOT pre-registered (4 Oct 2026): why R4372 LR100's junction-PMI statistic beats the order shuffle on R1953.
test_sibling.pmi() returns 0 when the left word is out of the fr18 vocabulary (log pc/pc), above the in-vocabulary unseen-pair
floor (-1.204); this measures the share of pairs scoring exactly 0 in the real order vs the order shuffle, and the statistic with
those pairs set to the floor. Writes diag_oov_output.txt."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'sibling_michell'))
import test_sibling as ts
pmi = ts.bigram(); k = {c: v for c, v in ts.load_key(os.path.join(HERE, 'key_LR100.tsv')).items() if v.strip()}
toks = ts.target_tokens(os.path.join(os.path.dirname(HERE), 'ciphertext_R1953.txt'))
def pairs(t):
    s = []
    for x, y in zip(t, t[1:]):
        if x in k and y in k:
            a, c = ts.words(k[x]), ts.words(k[y])
            if a and c: s.append(pmi(a[-1], c[0]))
    return s
o = []; r = pairs(toks)
for seed in (1, 2):
    rng = random.Random(seed); z = []; sh = []; shf = []
    fl = lambda s: [(-1.204 if x == 0 else x) for x in s]
    for _ in range(200):
        t = toks[:]; rng.shuffle(t); s = pairs(t)
        z.append(sum(x == 0 for x in s) / len(s)); sh.append(sum(fl(s)) / len(s))
        shf.append(sum(fl([x for x in s if x < 3])) / max(1, len([x for x in s if x < 3])))
    rv = sum(fl(r)) / len(r); rr = fl([x for x in r if x < 3]); rv2 = sum(rr) / len(rr)
    o.append(f'seed {seed}: real {len(r)} pairs, share scoring 0 (OOV left word) {sum(x == 0 for x in r)/len(r):.3f} vs order-shuffle mean {sum(z)/200:.3f}'
             f' | OOV->floor: real {rv:.3f} vs shuffle mean {sum(sh)/200:.3f}, p {sum(x >= rv for x in sh)/200:.3f}'
             f' | OOV->floor and pairs with pmi>=3 dropped: real {rv2:.3f} vs {sum(shf)/200:.3f}, p {sum(x >= rv2 for x in shf)/200:.3f}')
open(os.path.join(HERE, 'diag_oov_output.txt'), 'w').write('\n'.join(o) + '\n'); print('\n'.join(o))
