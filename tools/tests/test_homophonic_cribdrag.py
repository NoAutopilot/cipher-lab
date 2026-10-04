#!/usr/bin/env python3
"""Offline test for families/homophonic.py --param crib=drag (RUN3-SANG, 4 Oct 2026).
(a) crib absent: byte-for-byte unchanged -- covered by test_homophonic_alphabet.py (a)'s pre-option fixture (passes
    after this option was added, 4 Oct 2026); not repeated here.
(b) _plant_targets finds a 6-gram x3 and a bigram x8 outside it; _plant gives every occurrence identical signs.
(c) _top_repeat finds the planted repeats in the cipher; _crib_drag returns a key whose pinned signs carry its chosen
    cribs, and with crib_oracle the planted 6-gram is a candidate (it need not win -- the RUN3-SANG lesson).
Must NOT block: a cipher with no 6-gram repeat (R6 None) still solves (stage 2 runs on R2 alone)."""
import os, random, sys
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(R, 'tools'))
import homophonic_anneal as ha
from families import homophonic as h

rng = random.Random(5)
words = "krol polski senat sejm hetman pan wojsko list pisze prosze teraz bardzo".split()
text = "".join(rng.choice(words) + ("warsza" if i % 9 == 0 else "") + ("ie" if i % 3 == 0 else "") for i in range(4000))
w = text[1000:1232]
pt = h._plant_targets(w)
assert pt is not None, 'no plant target found'
g, s6, b, s2 = pt
assert len(s6) == 3 and len(s2) == 8 and all(w[i:i + 6] == g for i in s6) and all(w[i:i + 2] == b for i in s2)
model = ha.Model([text[:900] + text[1300:]], 3)
seq, p, truth = ha.make_control(w, 60, 232, model, 1)
seq2 = h._plant(seq, p)
assert all(seq2[i:i + 6] == seq2[s6[0]:s6[0] + 6] for i in s6)
assert all(seq2[i:i + 2] == seq2[s2[0]:s2[0] + 2] for i in s2)
assert all(truth[x] == a for x, a in zip(seq2, p)), 'planting broke sign -> letter consistency'
print('ok (b) plant')
assert h._top_repeat(seq2, 6) is not None
h._LAST_PLANT = (g, b, seq2, p)
sc, key, info = h._crib_drag(seq2, model, ha.fold(text), 1, 1, {"m6": 20, "m2": 8, "keep": 2, "drag_iters": 500,
                                                               "iters": 2000, "crib_oracle": "1"})
r6 = info["R6"].split()
assert "".join(key[x] for x in r6) == info["crib6"], 'pinned R6 signs do not carry the chosen crib'
print('ok (c) drag pins its chosen crib; chosen', info["crib6"], info["crib2"], 'planted', g, b)
h._LAST_PLANT = None
flat = [f"x{i % 40}" for i in range(232)]
rng.shuffle(flat)
flat[10:12] = flat[50:52] = flat[90:92] = ["x1", "x2"]
sc, key, info = h._crib_drag(flat, model, ha.fold(text), 1, 1, {"m6": 5, "m2": 5, "keep": 1, "drag_iters": 300,
                                                              "iters": 500})
print('ok (must-not-block) no R6 ->', info["R6"], 'R2', info["R2"])
