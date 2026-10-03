#!/usr/bin/env python3
"""TX-DECODE shuffled-target check (3 Oct 2026): the lattice positions of each re-tested letter are permuted (5 seeds) and
the same lam-4 lattice decode + 200 value-shuffled keys is run; if the real key still ranks 1 on a shuffled target, the
rank on the real target reflects letter frequencies, not text. Run from ciphers/: python3 nevers-birago-fr3251-1572/harvest/tx_decode/shuffled_target.py"""
import random, sys, json
sys.path.insert(0, '../tools'); import key_decode_lattice as K
from judge_plaintext import LANG_CORPORA, NgramModel, read_corpus
O = 'nevers-birago-fr3251-1572/harvest/tx_decode/'
key = K.read_key('nevers-birago-fr3251-1572/harvest/key_1572_sheet.tsv'); out = {}
for L, g in [('f144r', 'it16dip'), ('f168', 'it16dip'), ('f117', 'fr')]:
    model = NgramModel([read_corpus(p) for p in LANG_CORPORA[g]]); lm = K.LM(model)
    lat = K.read_topk(O + L + '_topk.tsv'); res = []
    for s in range(5):
        l2 = lat[:]; random.Random(100 + s).shuffle(l2)
        c = K.control(l2, key, lm, model, 200, 1, 4.0, 64)
        res.append((c['lattice']['rank'], round(c['lattice']['z'], 2), c['top1']['rank'], round(c['top1']['z'], 2)))
    out[L] = res; print(L, 'shuffled-target (lattice rank, z, top1 rank, z):', res)
json.dump(out, open(O + 'shuffled_target.json', 'w'))
