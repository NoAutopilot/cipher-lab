#!/usr/bin/env python3
"""Offline test for specs/cheap-tests/mccormick-1999/token_anneal.py --sufx (MCC-SUFX, 15 Oct 2026).

Checks, on a tiny synthetic corpus (no tools/data read): (1) suffix_class and sufx_key on fixed words; (2) shuffle_types
keeps every token's length, keeps repeated types repeated (same type -> same new string), and with keep_marks keeps each
type's final SE/BE/E mark; (3) fit_marks recovers a planted class -> mark map from a control built with it and reads the
control's words back; (4) mark_profile counts token-final marks by longest match.
Run: python3 tools/tests/test_mcc_sufx.py
"""
import importlib.util
import random
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("ta", ROOT / "specs/cheap-tests/mccormick-1999/token_anneal.py")
ta = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ta)

CORPUS = ("he walked to the house and she looked at the markets then they talked slowly about the old horses "
          "and the boy wanted his letters sent quickly to the town " * 40).split()


def main():
    assert ta.suffix_class("walked") == ("walk", "ed")
    assert ta.suffix_class("looking") == ("look", "ing")
    assert ta.suffix_class("horses") == ("hors", "s") and ta.suffix_class("boys") == ("boy", "s")
    assert ta.suffix_class("house") == ("hous", "e") and ta.suffix_class("town") == ("tow", "n")
    fmap = {c: "" for c in ta.SUFX_CLASSES}
    fmap.update(ed="E", e="SE", s="BE")
    assert ta.sufx_key("walked", fmap) == "WLKE" and ta.sufx_key("house", fmap) == "HSSE"
    toks = [("code", "NCBE"), ("number", "7"), ("code", "WLD"), ("code", "NCBE"), ("code", "TRSE"), ("code", "TRSE")]
    for km in (False, True):
        sh = ta.shuffle_types(toks, random.Random(4), keep_marks=km)
        assert [len(v) for _, v in sh] == [len(v) for _, v in toks] and sh[1] == ("number", "7")
        assert sh[0][1] == sh[3][1] and sh[4][1] == sh[5][1]
        if km:
            assert sh[0][1].endswith("BE") and sh[4][1].endswith("SE")
    prof = ta.mark_profile(toks)
    assert abs(prof["SE"] - 2 / 5) < 1e-9 and abs(prof["BE"] - 2 / 5) < 1e-9 and abs(prof[""] - 1 / 5) < 1e-9, prof
    wb = ta.WordBigram(CORPUS, pool=40)
    kinds = [("code", "")] * 60
    ct, truth = ta.build_sufx_control(kinds, CORPUS, random.Random(3), fmap, 0.0)
    got, row, dec = ta.fit_marks(wb, ct, alpha=3.0, beam=50)
    used = set(ta.suffix_class(w)[1] for t in truth for w in t)
    assert all(got[c] == fmap[c] for c in used), (got, used)
    r = ta.skel_stats(dec, ct, truth)
    assert r["word_recovery"] > 0.9, r["word_recovery"]
    print("test_mcc_sufx: OK")


if __name__ == "__main__":
    main()
