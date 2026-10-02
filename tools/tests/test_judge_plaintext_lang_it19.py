"""Offline test for tools/judge_plaintext.py's "it19" language corpus (2 Oct 2026, A2-CAS7): a held-out Italian
passage -- Carlo Botta, Storia d'Italia dal 1789 al 1814, tomo IV (archive.org storiaditaliadal45904gut, Project
Gutenberg 45904), a tome NOT among the five files committed to tools/data/it19/ (Botta's tomo I is) -- passes the
language gate; the same passage shuffled, and a random-letter string of the same length, both fail it. No network."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from judge_plaintext import judge, fold

HELD_OUT_IT19 = (
    "nemici di sua maestà, che ne abusavano per offenderla, tanto meno dar loro il passo libero per venire ad "
    "attaccarla, e che doveva o dissipargli essa medesima, o dare alle genti regie quel passaggio. Rispose la "
    "repubblica, che non consentirebbe mai a dare il passo; solo prometteva di reprimere gl'insulti, di prevenire "
    "le aggressioni, e di allontanare quanto potesse offendere la buona amicizia delle due parti. Ma queste "
    "protestazioni erano vane. Continuavano i Carrosiani ad ingrossarsi, ad ordinarsi, ed a trascorrere alle "
    "enormità più condannabili, poichè e continuamente traversavano il territorio Ligure per andar ad assaltare i "
    "regj, ed intraprendevano le vettovaglie, che per quelle strade viaggiavano verso il Piemonte, ed arrestavano "
    "e svaligiavano i corrieri. Nel che non la perdonarono nemmeno al corriero Ligure, a cui tolsero i pieghi "
    "diretti ai ministri regj, ed aprirono"
)

SPEC = {"judge": {"language": "it19", "letters_min": 50, "letters_max": 5000, "control_samples": 100}}


def test_it19_real_passage_passes():
    r = judge(SPEC, HELD_OUT_IT19)
    assert r["checks"]["language"]["pass"], r["checks"]["language"]


def test_it19_shuffled_fails():
    letters = list(fold(HELD_OUT_IT19))
    random.Random(7).shuffle(letters)
    r = judge(SPEC, "".join(letters))
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_it19_random_string_fails():
    rnd = random.Random(11)
    s = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(fold(HELD_OUT_IT19))))
    r = judge(SPEC, s)
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_it19_corpus_folds_to_at_least_1m_letters():
    from judge_plaintext import LANG_CORPORA, read_corpus
    total = sum(len(fold(read_corpus(p))) for p in LANG_CORPORA["it19"])
    assert total >= 1_000_000, total


if __name__ == "__main__":
    test_it19_real_passage_passes()
    test_it19_shuffled_fails()
    test_it19_random_string_fails()
    test_it19_corpus_folds_to_at_least_1m_letters()
    print("ok")
