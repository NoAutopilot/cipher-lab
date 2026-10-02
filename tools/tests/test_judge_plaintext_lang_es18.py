"""Offline test for tools/judge_plaintext.py's "es18" and "es18p" language corpora (2 Oct 2026, GAPS5-na-schonenberg-
1678-1716, account-4): a held-out Spanish passage -- Philip V's 1709 circular letter to the cities on the peace
negotiations (archive.org A10903513, "Copia de carta circular que el Rey nuestro señor se sirvio de escribir a las
ciudades..."), an item NOT among the seven files committed to tools/data/es18/ -- passes the language gate under both
keys; the same passage shuffled, and a random-letter string of the same length, both fail it. The passage is the raw
djvu OCR run through tools/data/es18/build.py's long-s repair (the same step the corpus files had), so residual OCR
noise ("coníuelo", "tocaíle", "convcríaciones") stays as the corpus itself looks. The same passage FAILs es17c7
(1634-1648): -1.033 vs real_p05 -0.865 on 2 Oct 2026 -- the era gap this corpus was built to close. No network."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from judge_plaintext import judge, fold

HELD_OUT_ES18 = (
    "Los primeros rumores de vna Paz General, me pudieron servir de su-mo coníuelo , por lo que miraban al publico "
    "reposo j pero oyéndolos esforzados fm mi interveiKion , oportunamente declaré en bañante forma; que , sin "
    "concurrencia , y noticia mia., nada podía tratarse , ni ofrecerse en cosa que me tocaíle , que tuvieífc firmeza, "
    "ni consentir yo en ello, y que antes de aífcntir a Tratado de indecoro ,'e ignominia a mi Períbna , y a mi "
    "Nación Española , perdería la vida , a la frente de vn íblo Esquadron de Eípañoles, que nicquedaííe. "
    "Continuadas las señales de adelantaríc las I convcríaciones sin mi participación *, tuve por predio hazer "
    "patente manifcítacion de mi prqpoiito , y como medio el mas proporcionado para que que fueífe notorio ; tomi "
    "el de elegir Plenipotenciarios, que en mi Real Nombre debieíTen con currir a los Tratados , y que de todos "
    "modos no dexaflen dudar mi difpoíicion a la Paz, y mi firmeza de no conícntir en nada, que con este nombre "
    "fucile realmente íolo diípendio afrento^ lo de mi Dignidad Real , y de la Nación Eípanola. En la elección de "
    "Primer Plenipotenciario, atendiaque se hallaíTenvnidas todas las circunstancias de nacimiento, autoridad ,zeío, "
    "prudencia, talentos, y reputación, enque digna , y euni' plidamente íe afíaní^aílc el dcíempeño de aíTump» tos "
    "tan graves : como se verifica en ia acreditad"
)


def _spec(lang):
    return {"judge": {"language": lang, "letters_min": 50, "letters_max": 5000, "control_samples": 100}}


def test_es18_real_passage_passes():
    for lang in ("es18", "es18p"):
        r = judge(_spec(lang), HELD_OUT_ES18)
        assert r["checks"]["language"]["pass"], (lang, r["checks"]["language"])


def test_es18_shuffled_fails():
    letters = list(fold(HELD_OUT_ES18))
    random.Random(7).shuffle(letters)
    for lang in ("es18", "es18p"):
        r = judge(_spec(lang), "".join(letters))
        assert not r["checks"]["language"]["pass"], (lang, r["checks"]["language"])


def test_es18_random_string_fails():
    rnd = random.Random(11)
    s = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(fold(HELD_OUT_ES18))))
    for lang in ("es18", "es18p"):
        r = judge(_spec(lang), s)
        assert not r["checks"]["language"]["pass"], (lang, r["checks"]["language"])


if __name__ == "__main__":
    test_es18_real_passage_passes(); test_es18_shuffled_fails(); test_es18_random_string_fails(); print("ok")
