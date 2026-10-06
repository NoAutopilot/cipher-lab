"""Offline test for tools/judge_plaintext.py's "es1600" language corpus (6 Oct 2026, R12-OLDCORP, account 2): a held-out
Spanish passage -- the Archduke Albert to the Duke of Lerma, Brussels, 9 June 1606 (CODOIN tomo XLII, archive.org
coleccindedocu42madruoft djvu text, printed pp. 565-566, which lies past the 650k-letter cap at which
tools/data/es1600/build.py cut that file, so it is NOT in the committed corpus, grep-checked) --
passes the language gate; the same passage shuffled, and a random-letter string of the same length, both fail it.
No network."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from judge_plaintext import judge, fold

HELD_OUT_ES1600 = (
    "Señor duque: El marqués Spínola llegó aquí á los 30 del pasado, habiendo venido de Milán aquí algo despacio, por "
    "haber venido siempre con tercianas, las cuales le dejaron luego; y porque creo que fueron causa de que pudiese venir "
    "mejor acompañado para lo que tocaba á su seguridad, se podría decir que se podrían dar por bien empleadas: que de "
    "otra manera pienso cierto se arriesgara el marqués, como lo ha hecho otras veces, y fuera de mayor consideración, "
    "sabiéndose el cuidado con que andaban algunos de cogerle, como V. S. muy bien sabe. En fin él está aquí y bueno, y "
    "atendiendo á lo que hay que hacer con el cuidado y diligencia que siempre. Cuando llegó me dio la carta de V. S. de "
    "los 11 de abril, con que holgué mucho como siempre, y me hizo larga relación de todo lo que había pasado en los "
    "particulares que V. S. apunta en su carta."
)


def _spec():
    return {"judge": {"language": "es1600", "letters_min": 50, "letters_max": 5000, "control_samples": 100}}


def test_es1600_real_passage_passes():
    r = judge(_spec(), HELD_OUT_ES1600)
    assert r["checks"]["language"]["pass"], r["checks"]["language"]


def test_es1600_shuffled_fails():
    letters = list(fold(HELD_OUT_ES1600))
    random.Random(7).shuffle(letters)
    r = judge(_spec(), "".join(letters))
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_es1600_random_string_fails():
    rnd = random.Random(11)
    s = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(fold(HELD_OUT_ES1600))))
    r = judge(_spec(), s)
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


if __name__ == "__main__":
    test_es1600_real_passage_passes(); test_es1600_shuffled_fails(); test_es1600_random_string_fails(); print("ok")
