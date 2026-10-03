"""Offline test for tools/judge_plaintext.py's "nl18" corpus (3 Oct 2026, NL18-CORPUS): a held-out 1781 Dutch passage --
a petition to the States General about arming merchant ships against enemy privateers, raw archive.org OCR of
aandehoogmogende00unse (NOT one of the seven files in tools/data/nl18/, and left with its long-s-as-f OCR unrepaired)
-- passes the language gate; the same letters shuffled, and a random-letter string, fail it. No network."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from judge_plaintext import judge, fold, LANG_CORPORA, read_corpus

HELD_OUT_NL18 = " Op. al crly. manieren te werden voorgekomen. — angrethitsred ___Pat ondertusfchen van de zyde der Supplianten drartoe nicts anders kan werden in 't werk gefteld, dan door de Schepen, die zy gewoon zyn op dit Vaarwater te gebruiken, -te brengen in een ftaat van bchoorlyke tegenweer, € genoegzaam ten Oorloge toe te ruften, wanneer zy kloek en gefchikt genoeg kunnen werden gemaakt, om, welke van 's Vyands Kapers het zouden moogen zyn, op Zig zelven te ftaan, en, vereenigt in eenigen getalle „ei lende, zelfs hunne Oorlogfchepen werk genoeg te kunnen verfchaf- fen, en daar door ’s Lands Zee-magt niet weinig in de hand te werken en te adfifteeren. — Dan dat door de immenfe verhoogde pryzen van alles, wat tot de uitrufting van Schepen fpetteert, en de „byna verdubbelde Maand en Handgelden, welke men ter bekoming van zeevarende moet befteeden, zodanige FEquipagie „en Monture. dezer „Schepen zo "

SPEC = {"judge": {"language": "nl18", "letters_min": 50, "letters_max": 5000, "control_samples": 100}}


def test_nl18_real_passage_passes():
    r = judge(SPEC, HELD_OUT_NL18)
    assert r["checks"]["language"]["pass"], r["checks"]["language"]


def test_nl18_shuffled_fails():
    letters = list(fold(HELD_OUT_NL18)); random.Random(7).shuffle(letters)
    assert not judge(SPEC, "".join(letters))["checks"]["language"]["pass"]


def test_nl18_random_string_fails():
    rnd = random.Random(11)
    s = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(fold(HELD_OUT_NL18))))
    assert not judge(SPEC, s)["checks"]["language"]["pass"]


def test_nl18_has_at_least_5_files_and_1m_letters():
    assert len(LANG_CORPORA["nl18"]) >= 5
    assert sum(len(fold(read_corpus(p))) for p in LANG_CORPORA["nl18"]) >= 1_000_000


if __name__ == "__main__":
    test_nl18_real_passage_passes(); test_nl18_shuffled_fails(); test_nl18_random_string_fails()
    test_nl18_has_at_least_5_files_and_1m_letters(); print("ok")
