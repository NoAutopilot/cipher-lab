#!/usr/bin/env python3
"""Offline test for specs/cheap-tests/mccormick-1999/token_anneal.py --skeleton (MCC-SKEL, 15 Oct 2026).

Checks, on a tiny synthetic corpus (no tools/data read): (1) skeleton() on fixed words under both schemes; (2) the lattice
decoder reads a run-on token (two skeletons written together) back into its two words and a lone skeleton into its word;
(3) a skeleton absent from the pool is read as UNK and lowers coverage; (4) shuffle_letters keeps every token's length and
the multiset of letters; (5) build_skel_control's truth matches its tokens (the skeletons of the truth words, joined).
Run: python3 tools/tests/test_mcc_skeleton.py
"""
import importlib.util
import random
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("ta", ROOT / "specs/cheap-tests/mccormick-1999/token_anneal.py")
ta = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ta)

CORPUS = ("he would go to the house and she would not go to the market " * 30).split()


def main():
    assert ta.skeleton("would") == "WLD"
    assert ta.skeleton("letter") == "LTR"
    assert ta.skeleton("house") == "HS" and ta.skeleton("house", "keepfinal") == "HSE"
    assert ta.skeleton("and") == "AND" and ta.skeleton("a") == "A"
    wb = ta.WordBigram(CORPUS, pool=20)
    dec = ta.SkelDecoder(wb, "drop", alpha=3.0, beam=50)
    toks = [("code", "HWLD"), ("code", "G"), ("code", "TTH"), ("code", "HS"), ("number", "7"), ("code", "SHWLDNT")]
    sc, segs = dec.decode(toks)
    per = dec.words_per_token(toks, segs)
    got = [[w for _, w in g] if g else None for g in per]
    assert got == [["he", "would"], ["go"], ["to", "the"], ["house"], None, ["she", "would", "not"]], got
    r = ta.skel_stats(dec, toks)
    assert abs(r["coverage"] - 1.0) < 1e-9, r
    r2 = ta.skel_stats(dec, [("code", "QXZ"), ("code", "HS")])
    assert abs(r2["coverage"] - 2 / 5) < 1e-9 and "?QXZ" in r2["decode"], r2
    rng = random.Random(1)
    sh = ta.shuffle_letters(toks, rng)
    assert [len(v) for _, v in sh] == [len(v) for _, v in toks]
    assert Counter("".join(v for k, v in sh if k == "code")) == Counter("".join(v for k, v in toks if k == "code"))
    kinds = [("code", ""), ("number", ""), ("code", ""), ("letter", "")] * 5
    ct, tr = ta.build_skel_control(kinds, CORPUS, random.Random(3), "drop", 0.5)
    for (k, v), t in zip(ct, tr):
        assert (t is None) == (k != "code")
        if t:
            assert v == "".join(ta.skeleton(w) for w in t)
    print("test_mcc_skeleton: OK")


if __name__ == "__main__":
    main()
