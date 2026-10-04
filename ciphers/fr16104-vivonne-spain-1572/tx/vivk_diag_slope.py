#!/usr/bin/env python3
"""N5-VIVK post-hoc diagnostic (NOT pre-registered, no gate): Arm A re-learned with the start slope set to the observed
letters-per-sign ratio of the whole stream instead of 1.0; reports only per-code agreement with key_tomokiyo.tsv on
codes with >= 3 training occurrences. Run: python3 ciphers/fr16104-vivonne-spain-1572/tx/vivk_diag_slope.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(1, '/home/user/cipher-lab/tools')
import numpy as np, vivk_test as v, stream_align as sa
r = json.load(open(os.path.join(HERE, 'vivk_result.json')))
train = v.tokens(os.path.join(HERE, 'f102r_rec.tsv')) + v.tokens(os.path.join(HERE, 'f102v_rec.tsv'))
held = v.tokens(os.path.join(HERE, 'f103r_rec.tsv'))
let = sa.letters(open(os.path.join(HERE, 'dec_norm.txt')).read())
j0 = r['j0']; slope = (len(let) - j0) / (len(train) + len(held))
codes = sorted(set(train) | set(held)); ids = {c: n for n, c in enumerate(codes)}
tk = {l.split('\t')[0]: l.split('\t')[1] for l in open(os.path.join(HERE, '..', 'key_tomokiyo.tsv')) if not l.startswith('code')}
counts, path = sa.learn(np.array([ids[c] for c in train]), let[j0:], len(codes), slope=slope)
key = sa.decode(counts)
comp = agree = 0; dis = []
for c in sorted(set(train)):
    if train.count(c) >= 3 and c in tk and key[ids[c]] >= 0:
        comp += 1; a = chr(97 + key[ids[c]])
        agree += a == tk[c]
        if a != tk[c]: dis.append(f'{c}:{a}/{tk[c]}')
print(json.dumps({'slope': round(slope, 3), 'compared': comp, 'agree': agree, 'disagreements': dis,
                  'jend': j0 + max(j for i, j in path)}))
