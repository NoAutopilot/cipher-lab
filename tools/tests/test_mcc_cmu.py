#!/usr/bin/env python3
"""Offline test for specs/cheap-tests/mccormick-1999/token_anneal.py --sufx --phonetic (MCC-CMU, 15 Oct 2026).

Checks, on a tiny synthetic pronouncing dictionary and corpus (no tools/data or network read): (1) without
load_phonetic() sufx_key is MCC-SUFX's letter skeleton (earlier modes unchanged); (2) load_phonetic keeps the first
pronunciation, drops stress digits and '(2)' variants; (3) phon_skeleton strips the ending class's own phones
(walked -> WC, horses -> HRS, dancing -> DNS), writes /k/ as C, /z/ as S, keeps a vowel-initial word's first letter and
collapses runs; (4) an out-of-dictionary word falls back to the letter skeleton; (5) fit_marks on a phonetic control
reads it back.
Run: python3 tools/tests/test_mcc_cmu.py
"""
import importlib.util
import random
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("ta", ROOT / "specs/cheap-tests/mccormick-1999/token_anneal.py")
ta = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ta)

DICT = """# test dict
walked W AO1 K T
horses HH AO1 R S AH0 Z
dancing D AE1 N S IH0 NG
know N OW1
know(2) N OW2 W
city S IH1 T IY0
odd AA1 D
the DH AH0
to T UW1
house HH AW1 S
market M AA1 R K AH0 T
markets M AA1 R K AH0 T S
boy B OY1
letters L EH1 T ER0 Z
town T AW1 N
slowly S L OW1 L IY0
talked T AO1 K T
wanted W AO1 N T AH0 D
quickly K W IH1 K L IY0
sent S EH1 N T
old OW1 L D
"""
CORPUS = ("the boy walked to the house and the boy talked slowly to the town then the horses wanted the letters "
          "sent quickly to the old market and the markets " * 40).split()


def main():
    fmap = {c: "" for c in ta.SUFX_CLASSES}
    fmap.update(ed="E", e="SE", s="BE")
    assert ta.sufx_key("walked", fmap) == "WLKE"            # letter skeleton (MCC-SUFX) while PHON is empty
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "t.dict"; p.write_text(DICT)
        assert ta.load_phonetic(p) == 20
    assert ta.PHON["know"] == ["N", "OW"] and ta.PHON["walked"] == ["W", "AO", "K", "T"]
    P = ta.phon_skeleton
    assert P("walked", "ed") == "WC" and P("horses", "s") == "HRS" and P("dancing", "ing") == "DNS"
    assert P("know", "other") == "N" and P("city", "y") == "ST" and P("odd", "d") == "O" and P("the", "e") == "TH"
    assert P("market", "t") == "MRC" and P("wanted", "ed") == "WNT" and P("nonesuch", "other") is None
    assert ta.sufx_key("walked", fmap) == "WCE" and ta.sufx_key("zzyzx", fmap) == ta.skeleton("zzyzx", "drop")
    wb = ta.WordBigram(CORPUS, pool=40)
    ct, truth = ta.build_sufx_control([("code", "")] * 60, CORPUS, random.Random(3), fmap, 0.0)
    got, row, dec = ta.fit_marks(wb, ct, alpha=3.0, beam=50)
    r = ta.skel_stats(dec, ct, truth)
    assert r["word_recovery"] > 0.8, r["word_recovery"]
    ta.PHON.clear()
    assert ta.sufx_key("walked", fmap) == "WLKE"
    print("test_mcc_cmu: OK")


if __name__ == "__main__":
    main()
