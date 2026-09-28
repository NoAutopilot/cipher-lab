#!/usr/bin/env python3
"""Offline test for the slot-grammar option of tools/families/nomenclator.py (H27, 28 Sept 2026). Seconds, no corpus.

(1) inflect/deinflect round-trip on the suffix classes; (2) grammar_book puts a root at slot 0 and its inflections at
the slots the per-book map names, keeps only one of plural/past at slot 1 (the other becomes its own root), and
assigns each family one decade; (3) the slot-map string round-trips through the solver's param parser.
Run: python3 tools/tests/test_nomenclator_grammar.py"""
import os, random, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from families import nomenclator as nm  # noqa: E402


def test_grammar():
    for r, c in [("measure", "s"), ("measure", "ed"), ("carry", "s"), ("carry", "ed"), ("make", "ing"), ("great", "est"),
                 ("happy", "ness"), ("probable", "ly"), ("act", "ion"), ("create", "ion"), ("agree", "ing"), ("wish", "s"),
                 ("govern", "ment"), ("read", "able"), ("strong", "er")]:
        f = nm.inflect(r, c)
        assert r in nm.deinflect(f, c), (r, c, f, nm.deinflect(f, c))
    rng = random.Random(1)
    sm = nm.make_slot_map(rng)
    assert sm[0] == "" and sm[1] == "s|ed" and sorted(sm[s] for s in range(2, 10)) == sorted(nm.GRAMMAR_CLASSES)
    words = ["measure", "measures", "measured", "measuring", "government", "govern", "governs", "ship", "ships", "shipping"]
    fr = {w: 100 - i for i, w in enumerate(words)}
    book, roots = nm.grammar_book(words, lambda w: fr[w], rng, 5, sm)
    assert roots and all(100 <= v < 150 for v in book.values())
    dec_m = book["measure"] // 10
    assert book["measure"] % 10 == 0 and book["measures"] == dec_m * 10 + 1  # commoner of plural/past at slot 1
    assert book["measured"] % 10 == 0 and book["measured"] // 10 != dec_m  # the other form is its own root
    ing = [s for s, c in sm.items() if c == "ing"][0]
    assert book["measuring"] == dec_m * 10 + ing
    assert book["governs"] == book["govern"] // 10 * 10 + 1
    ment = [s for s, c in sm.items() if c == "ment"][0]
    assert book["government"] == book["govern"] // 10 * 10 + ment
    assert len({v // 10 for v in book.values()}) == len(roots) <= 5
    s = ";".join(f"{k}:{v}" for k, v in sm.items())
    assert nm._slot_map_param({"slot_map": s}) == sm
    print("test_nomenclator_grammar: ok")


if __name__ == "__main__":
    test_grammar()
