"""Offline test for tools/judge_plaintext.py's "la"/"la18" language corpus (26 Sept 2026, LANE B7 bLAJ): a
held-out Latin passage -- Leibniz's own preface to Codex juris gentium diplomaticus (1693, archive.org
bub_gb_8cMJ0H457Y0C), hand-corrected from noisy period OCR (long-s/ligature misreads) but not from any of the
three Zaluski volumes committed to tools/data/la18/ -- passes the language gate; the same passage shuffled,
and a random-letter string of the same length, both fail it. No network."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from judge_plaintext import judge, fold

HELD_OUT_LA18 = (
    "Qui Heraldica tractant, invenient non tantum solennium descriptiones, "
    "ut in Epistola Joannis Regis Galliae de institutione militum stellae de bipartito, "
    "aut in coronatione Regis Siciliae Ludovici Andegavensis a Papa ipso approbatione peracta. "
    "Et hujus Imperatoris aquila bicipiti nomen; hic tamen binae quidem aquilae adhibitae sunt, "
    "sed non conjunctae in unum corpus. Nec minus Genealogi habebunt unde suas tabulas emendent, "
    "firment vel locupletent. Matrimonia Austriacorum tractata cum Regia Galliae familia leguntur, "
    "et Palatinum quoque, sed credo in herba interceptum, ubi mirabere tot in imo loco Rupertos "
    "inter se diversos, quorum unus, qui dicitur pater Infantis, postea factus est Rex Romanorum."
)

SPEC = {"judge": {"language": "la18", "letters_min": 50, "letters_max": 5000, "control_samples": 100}}
SPEC_LA = {"judge": {"language": "la", "letters_min": 50, "letters_max": 5000, "control_samples": 100}}


def test_la18_real_passage_passes():
    r = judge(SPEC, HELD_OUT_LA18)
    assert r["checks"]["language"]["pass"], r["checks"]["language"]


def test_la_alias_matches_la18():
    r = judge(SPEC_LA, HELD_OUT_LA18)
    assert r["checks"]["language"]["pass"], r["checks"]["language"]


def test_la18_shuffled_fails():
    letters = list(fold(HELD_OUT_LA18))
    random.Random(7).shuffle(letters)
    r = judge(SPEC, "".join(letters))
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_la18_random_string_fails():
    rnd = random.Random(11)
    s = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(fold(HELD_OUT_LA18))))
    r = judge(SPEC, s)
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_la18_corpus_folds_to_at_least_200k_letters():
    from judge_plaintext import LANG_CORPORA, read_corpus
    total = sum(len(fold(read_corpus(p))) for p in LANG_CORPORA["la18"])
    assert total >= 200_000, total


if __name__ == "__main__":
    test_la18_real_passage_passes()
    test_la_alias_matches_la18()
    test_la18_shuffled_fails()
    test_la18_random_string_fails()
    test_la18_corpus_folds_to_at_least_200k_letters()
    print("ok")
