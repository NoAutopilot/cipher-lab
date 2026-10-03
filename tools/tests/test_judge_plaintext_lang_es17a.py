"""Offline test for tools/judge_plaintext.py's "es17a" language corpus (3 Oct 2026, OLD-ES17A, account 1): a held-out
Spanish passage -- Cabrera de Cordoba, Relaciones, letter "De Madrid a 3 de Mayo 1614" (archive.org relacionesdelasc00cabr,
djvu line ~27426), which lies past the 650k-letter cap at which tools/data/es17a/build.py cut that file, so it is NOT in
the committed corpus -- passes the language gate; the same passage shuffled, and a random-letter string of the same
length, both fail it. No network."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from judge_plaintext import judge, fold

HELD_OUT_ES17A = (
    "Detuvose S. M. hasta los 10 del pasado, sin ir a Aranjuez, por ver la mascara que los señores y caballeros "
    "hicieron el dia antes, por el nacimiento del hijo del de Saldaña, que fue de sesenta y cuatro caballeros, muy "
    "costosamente aderezados, cuyos vestidos se estimaron en mas de 80.000 ducados; y salio con ellos el conde de "
    "Saldaña, y S. M. estuvo con sus Altezas a verlos correr en la huerta del duque de Lerma, y despues anduvieron por "
    "el lugar corriendo en diferentes calles, y en la Mayor cayo el conde de Olivares, arrimandose el caballo a una "
    "reja, pero coa sangrarse estuvo luego bueno, y aquel dia fue de mucho regocijo para toda la Corte."
)


def _spec():
    return {"judge": {"language": "es17a", "letters_min": 50, "letters_max": 5000, "control_samples": 100}}


def test_es17a_real_passage_passes():
    r = judge(_spec(), HELD_OUT_ES17A)
    assert r["checks"]["language"]["pass"], r["checks"]["language"]


def test_es17a_shuffled_fails():
    letters = list(fold(HELD_OUT_ES17A))
    random.Random(7).shuffle(letters)
    r = judge(_spec(), "".join(letters))
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_es17a_random_string_fails():
    rnd = random.Random(11)
    s = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(fold(HELD_OUT_ES17A))))
    r = judge(_spec(), s)
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


if __name__ == "__main__":
    test_es17a_real_passage_passes(); test_es17a_shuffled_fails(); test_es17a_random_string_fails(); print("ok")
