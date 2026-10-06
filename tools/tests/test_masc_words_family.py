#!/usr/bin/env python3
"""Offline test for tools/families/masc_words.py (R12D-FAIR, 6 Oct 2026). No network, no anneal.
(1) catches: the control's training text must keep word boundaries and must not contain the control window
    (the first run's bug left the lexicon empty); (2) must NOT block: the control cipher is identical to masc's for the
    same seed (so masc_words vs masc is a like-for-like gain test); (3) segmentation finds real words in a known phrase.
Run: python3 tools/tests/test_masc_words_family.py"""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path[:0] = [os.path.join(ROOT, "tools"), os.path.join(ROOT, "tools", "families")]
import judge_plaintext as jp  # noqa: E402
from families import masc, masc_words  # noqa: E402

corp = [jp.read_corpus(os.path.join(ROOT, "tools", "data", "pg1661_holmes.txt"))]
P = {"N": 67, "K": 21, "target_msgs": [[str(i % 21) for i in range(67)]]}
m1, p1, _ = masc.make_control({}, 2, corp, dict(P))
m2, p2, train = masc_words.make_control({}, 2, corp, dict(P))
assert m1 == m2 and p1 == p2, "masc_words control differs from masc"
assert " " in train[0] and p2 not in train[0].replace(" ", ""), "training text lost spaces or leaks the window"
lex = masc_words.lexicon(train)
assert len(lex) > 1000, len(lex)
segs = masc_words.segment("thequickmanwasthere", lex)
assert "the" in segs and "was" in segs, segs
print("ok: masc_words control == masc control, train keeps spaces without window, lexicon", len(lex), "segment", segs)
