#!/usr/bin/env python3
"""Offline test for tools/crib_list_fit.py (H48, 28 Sept 2026), on the committed espagnol142-mercy-1648 stream and key.
Must catch: H41's case -- on r16:2-r18:21 "burgsdorf" is the unique best against distractor names (including the
place names that fitted next in H41), 7 letters agreeing, 0 disagreeing, candidate True.
Must NOT pass: H46's case -- v04 anchored at v04:1 with a list whose unique best is "poca" at fit 0 (2 agree, 2
disagree): the minimum-fit rule must refuse it even though it is unique and P < 0.05. And H71's case -- a read,
name-free stretch (r19:6 onward, 62 tokens) where "xanten" fits 5 agree / 1 disagree (fit 4): --min-score must refuse it.
Run: python3 tools/tests/test_crib_list_fit.py"""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import crib_list_fit as clf  # noqa: E402

T = os.path.join(ROOT, "ciphers", "espagnol142-mercy-1648")
CODES, KEY = os.path.join(T, "cipher_codes_522.tsv"), os.path.join(T, "key.tsv")
FILLER = ["oranien", "garantie", "altenburg", "neuburg", "nassau", "blumenthal", "schuuerin", "uolmar", "norprath",
          "lothringen", "munster", "pommern", "meiern", "cleist", "uuinnenthal", "aitzema", "ochsenstirn", "iulich",
          "uuesel", "pfalzgraf", "rathen", "burgund"]


def test_positive():
    toks = clf.load_window(CODES, KEY, "r16:2", "r18:21")
    res = clf.rank(["burgsdorf"] + FILLER, toks)
    v = clf.verdict(res)
    assert v["best"] == "burgsdorf", v
    assert (v["score"], v["agree"], v["mismatch"], v["at"]) == (7, 7, 0, "r16:16"), v
    assert v["ties"] == 1 and v["candidate"], v


def test_minimum_fit_refuses():
    toks = clf.load_window(CODES, KEY, "v04:1", "v05:18")
    words = ["poca", "uida", "casa", "alma", "ualor", "conseio", "mano", "turno", "parte", "padre", "orden",
             "muier", "mucha", "misma", "medio", "cuenta", "persona", "gente", "hijo", "reino", "real", "cargo",
             "mayor", "hermano", "magestad", "alteza", "seruicio", "cuidado", "mano", "gusto"]
    v = clf.verdict(clf.rank(words, toks, anchor="start"))
    assert v["best"] == "poca" and v["ties"] == 1 and v["P"] < 0.05, v
    assert (v["agree"], v["mismatch"]) == (2, 2), v
    assert not v["candidate"], v


def test_min_score_refuses_read_text():
    toks = clf.load_window(CODES, KEY, None, None)
    locs = [t[2] for t in toks]
    st = locs.index("r19:6")
    res = clf.rank(["xanten", "tarent"] + FILLER, toks[st:st + 62])
    v = clf.verdict(res)
    assert v["best"] == "xanten" and v["score"] == 4, v
    assert not v["candidate"], v
    assert clf.verdict(res, min_score=0)["candidate"], "without --min-score the H71 false positive would pass"


if __name__ == "__main__":
    test_positive(); test_minimum_fit_refuses(); test_min_score_refuses_read_text(); print("test_crib_list_fit: ok")
