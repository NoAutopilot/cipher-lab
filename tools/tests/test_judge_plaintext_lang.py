"""Offline test for tools/judge_plaintext.py's newly-wired "pt" language corpus (25 Sept 2026,
YX-PTJUDGE): a held-out Portuguese passage -- from the front matter of the 1855 Vieira edition that was
trimmed off before tools/data/pt17/vieira_cartas_tomoIV_1855.txt.gz was built, so it is not in the
corpus -- passes the language gate; the same passage with its letters shuffled, and a random-letter
string of the same length, both fail it. No network."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from judge_plaintext import judge, fold

# 1855 editorial "Introducção" to the Vieira letters (cartasdopadrean00vieigoog, lines ~192-260 of the
# raw IA djvu.txt) -- excluded from the committed pt17 corpus, which starts only after this front matter.
HELD_OUT_PT = (
    "INTRODUCÇAO. No Programma estampado a frente do primeiro volume dos Sermões deixamos consignados "
    "os motivos que nos determinaram a emprehender a reimpressão das Obras do Padre António Vieira, e "
    "ahi indicamos também o plano que tencionamos seguir quanto a ordem da impressão. Um Prologo em que "
    "se apreciasse e discutisse largamente o merecimento das Obras de Vieira era coisa para que nos não "
    "achávamos habilitados -- dissemo-lo então e de novo o repetimos -- e por isso nesta parte nos "
    "limitámos a chamar em nosso auxilio o testemunho competente e insuspeito de graves e profundos "
    "pensadores nacionaes e estrangeiros, que em differentes épocas tem pago o tributo de sua admiração "
    "e respeito ao talento transcendente do Padre Vieira. Se por ventura se entender que por isto "
    "incorremos em grande falta, por ella supplicamos a indulgência do publico; mas estamos convencidos "
    "de que não será assim, porque o merecimento de similhante escriptor está ja muito julgado por todos "
    "os homens competentes. Para conhecimento de quem não tiver presente o volume onde se acha o "
    "programma alludido, reproduziremos neste logar o que ahi dissemos relativamente a impressão das "
    "Cartas. Alterou-se a ordem seguida na antiga edição, porque se incluem algumas que se encontravam "
    "espalhadas por outras obras do Auctor, e deixam de imprimir-se outras de alheas pennas que ahi "
    "andavam enxeridas."
)

SPEC = {"judge": {"language": "pt", "letters_min": 50, "letters_max": 5000, "control_samples": 100}}


def test_pt_real_passage_passes():
    r = judge(SPEC, HELD_OUT_PT)
    assert r["checks"]["language"]["pass"], r["checks"]["language"]


def test_pt_shuffled_fails():
    letters = list(fold(HELD_OUT_PT))
    random.Random(7).shuffle(letters)
    r = judge(SPEC, "".join(letters))
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_pt_random_string_fails():
    rnd = random.Random(11)
    s = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(fold(HELD_OUT_PT))))
    r = judge(SPEC, s)
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


if __name__ == "__main__":
    test_pt_real_passage_passes()
    test_pt_shuffled_fails()
    test_pt_random_string_fails()
    print("ok")
