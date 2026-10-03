"""Offline test for tools/judge_plaintext.py's "de17" language corpus (3 Oct 2026, GAPS62, account-4): a held-out passage of
the 1635 Wallenstein-process deposition printed in Irmer, Die Verhandlungen Schwedens ... vol 3 (1891, archive.org
dieverhandlungen03irme, raw djvu lines about 36082-36096), which lies past the 450,000-letter cap tools/data/de17/build.py
applies to that volume, so it is unseen by the model (test 1 checks that). Hand normalisation of the OCR (long s to s, line
breaks joined). It passes the language gate; the same passage shuffled, and a random-letter string of the same length, both
fail. No network."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from judge_plaintext import LANG_CORPORA, fold, judge, read_corpus

HELD_OUT_DE17 = (
    "sich dieselbe an ihne, den alten, machen und alles wegnehmen. Nachod aber seie auf der seiten und fest, werde derowegen "
    "daselbst sicherer sein. Gleichwie nun der Adam dem Klusacken des Friedlands und sein böses vorhaben wider ew. kais. maj. "
    "ohne scheu entdecket, also ist leucht zue schließen, daß er selbiges dem Stracka gleichmeßig geoffenbaret habe, in "
    "erwegung, er denselben, wie er vorangezeigt, eben dieser ursachen zue sich erfordert, dem vater durch ihne geheime, "
    "hochimportirende sachen, so der feder nicht zu vertrauen, wissent zu machen; wie dann der zeug ausgesaget: Als der "
    "Stracka von Pilsen zuruckkommen, habe er ein schreiben mitgebracht, welches er, zeug, selbsten gelesen, darinnen der "
    "Adam den vater nochmalen, sich mit den besten sachen auf Nachod zu begeben, ermahnet"
)

SPEC = {"judge": {"language": "de17", "letters_min": 50, "letters_max": 5000, "control_samples": 100}}


def test_de17_corpus_is_five_files_over_1m_letters_and_excludes_the_passage():
    files = LANG_CORPORA["de17"]
    assert len(files) >= 5  # rule 3: under ~5 files the per-fold spread is unreliable (es17c)
    big = "".join(fold(read_corpus(p)) for p in files)
    assert len(big) >= 1_000_000, len(big)
    f = fold(HELD_OUT_DE17)
    assert not any(f[k:k + 40] in big for k in range(0, len(f) - 40, 20))


def test_de17_real_passage_passes():
    r = judge(SPEC, HELD_OUT_DE17)
    assert r["checks"]["language"]["pass"], r["checks"]["language"]


def test_de17_shuffled_fails():
    letters = list(fold(HELD_OUT_DE17))
    random.Random(7).shuffle(letters)
    r = judge(SPEC, "".join(letters))
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_de17_random_string_fails():
    rnd = random.Random(11)
    s = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(fold(HELD_OUT_DE17))))
    r = judge(SPEC, s)
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]
