#!/usr/bin/env python3
"""Offline test for tools/families/masc_inj.py (R12D-FAIR2, 6 Oct 2026). No network.
(1) catches: a decode key that maps two cipher signs to one plain letter (the instrument must be strictly injective);
(2) must NOT block: a known English phrase under a random one-to-one key, cut mid-word at both ends, is read back
    (edge words and OOV skips do not stop the search). Run: python3 tools/tests/test_masc_inj_family.py"""
import os, random, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path[:0] = [os.path.join(ROOT, "tools"), os.path.join(ROOT, "tools", "families")]
import judge_plaintext as jp  # noqa: E402
import homophonic_anneal as ha  # noqa: E402
from families import masc_inj  # noqa: E402

corp = [jp.read_corpus(os.path.join(ROOT, "tools", "data", "pg1661_holmes.txt"))]
assert masc_inj.pattern("letter") == (0, 1, 2, 2, 1, 3)
plain = ha.fold("ingthatthemanwhocameintotheroomwasnotthepersonwehadexpectedtoseeatallyesterdayeve")
rng = random.Random(5)
letters = sorted(set(plain))
signs = [f"s{i}" for i in range(len(letters))]
rng.shuffle(signs)
key = dict(zip(letters, signs))
dec, sc, info = masc_inj.solve([[key[c] for c in plain]], {}, 1, 1, corp, {"beam": 1000})
k = info["key"]
assert len(set(k.values())) == len(k), "decode key is not injective"
rec = masc_inj.score_recovery(dec, plain)
assert rec >= 0.9, (rec, dec)
print(f"ok: injective key, recovery {rec:.3f}: {dec}")
