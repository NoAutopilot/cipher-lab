#!/usr/bin/env python3
"""UNA-NEVBIR control (9 Oct 2026): the mixed lattice of each letter position-shuffled (random.Random(100+s), s=0..4), same
lam-4 decode + 200 value-shuffled keys, as tx_decode/shuffled_target.py. Run from harvest/."""
import random, sys, json
sys.path.insert(0, '../../../tools'); import key_decode_lattice as K
from judge_plaintext import LANG_CORPORA, NgramModel, read_corpus
O = 'tx_decode/mix/'
key = K.read_key('key_1572_sheet.tsv'); out = {}
for L, g in [('f144r', 'it16dip'), ('f168', 'it16dip'), ('f117', 'fr')]:
    model = NgramModel([read_corpus(p) for p in LANG_CORPORA[g]]); lm = K.LM(model)
    lat = K.read_topk(O + L + '_mix_topk.tsv'); res = []
    for s in range(5):
        l2 = lat[:]; random.Random(100 + s).shuffle(l2)
        c = K.control(l2, key, lm, model, 200, 1, 4.0, 64)
        res.append((c['lattice']['rank'], round(c['lattice']['z'], 2), c['top1']['rank'], round(c['top1']['z'], 2)))
    out[L] = res; print(L, 'shuffled-target mix (lattice rank, z, top1 rank, z):', res, flush=True)
json.dump(out, open(O + 'shuffled_target_mix.json', 'w'), indent=1)
