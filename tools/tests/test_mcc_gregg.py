#!/usr/bin/env python3
"""Offline test for specs/cheap-tests/mccormick-1999/token_anneal.py --sufx --lexicon (MCC-GREGG, 15 Oct 2026).

Checks, on a tiny synthetic corpus (no tools/data read): (1) lexicon_lemmas undoes the regular inflections fixed in
PREREG-MCC-GREGG.md (walked > walk, stopped > stop, cities > city, making > make, quickly > quick); (2) lexicon_allows
admits a word iff it or a lemma is in the lexicon; (3) WordBigram(allowed=...) keeps only lexicon words in the pool, in
corpus-frequency order, capped at `pool`; (4) without `allowed` the pool is unchanged (MCC-SUFX behaviour); (5) fit_marks
on a lexicon pool still reads a control built from lexicon words.
Run: python3 tools/tests/test_mcc_gregg.py
"""
import importlib.util
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("ta", ROOT / "specs/cheap-tests/mccormick-1999/token_anneal.py")
ta = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ta)

CORPUS = ("he walked to the house and she looked at the markets then they talked slowly about the old horses "
          "and the boy wanted his letters sent quickly to the town " * 40).split()


def main():
    L = ta.lexicon_lemmas
    assert "walk" in L("walked") and "stop" in L("stopped") and "city" in L("cities")
    assert "make" in L("making") and "quick" in L("quickly") and "horse" in L("horses")
    lex = {"walk", "house", "look", "market", "talk", "slow", "horse", "boy", "want", "letter", "quick", "town", "the", "to"}
    ok = ta.lexicon_allows(lex)
    assert ok("walked") and ok("markets") and ok("slowly") and ok("the") and not ok("and") and not ok("she")
    wb0 = ta.WordBigram(CORPUS, pool=40)
    assert set(wb0.pool) == set(CORPUS)
    wb = ta.WordBigram(CORPUS, pool=40, allowed=ok)
    assert set(wb.pool) == {w for w in set(CORPUS) if ok(w)} and "and" not in wb.idx
    wb3 = ta.WordBigram(CORPUS, pool=3, allowed=ok)
    assert wb3.pool[0] == "the" and len(wb3.pool) == 3
    fmap = {c: "" for c in ta.SUFX_CLASSES}
    fmap.update(ed="E", e="SE", s="BE")
    lw = [w for w in CORPUS if ok(w)]
    ct, truth = ta.build_sufx_control([("code", "")] * 60, lw, random.Random(3), fmap, 0.0)
    got, row, dec = ta.fit_marks(wb, ct, alpha=3.0, beam=50)
    r = ta.skel_stats(dec, ct, truth)
    assert r["word_recovery"] > 0.9, r["word_recovery"]
    print("test_mcc_gregg: OK")


if __name__ == "__main__":
    main()
