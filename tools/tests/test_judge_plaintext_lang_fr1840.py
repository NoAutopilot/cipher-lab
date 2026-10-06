"""Offline test for tools/judge_plaintext.py's "fr1840" language corpus (6 Oct 2026, R11-ZESCORP): a held-out 1847
diplomatic letter quoted in Guizot's Memoires tome VIII (archive.org mmoirespourser08guiz, raw djvu lines 440-476), a
volume NOT among the five committed to tools/data/fr1840/ (Guizot tomes VI-VII only), passes the language gate; the
same passage shuffled, and a random-letter string of the same length, both fail it. Raw OCR left as is ("J'allacbais",
"preocciii)alion"), as the corpus itself is raw OCR. No network."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from judge_plaintext import judge, fold

HELD_OUT_FR1840 = (
    "J'allacbais trop de prix aux rapports qui s'étaient établis entre vous et moi dans le poste éminent où la "
    "confiance du roi vous a appelé, pour que leur cessation ne m'ait pas fait éprouver des regrets. Aussi j'ai été "
    "très-toucbé de ceux que vous avez eu la bonté de me témoigner par la lettre que vous m'avez fait l'honneur de "
    "m'écrire le 6 de ce mois, et je mets de Tempressement à vous en remercier. Je vous remercie aussi d'avoir bien "
    "voulu vous charger d'entretenir les souvenirs que j'ai eu occasion de laisser en Angleterre. J'en suis tiop "
    "honoré, même dans l'intérêt de notre chère France, pour que je n'attache pas le plus grand prix à les cultiver, "
    "et ce soin ne pouvait être confié à de plus dignes mains. Vous le savez, Monsieur, pendant la dernière [lériode "
    "que j'ai passée aux affaires, ma constante préocciii)alion a été de resserrer les liens d'amilié qui unissent les "
    "deux pays. J'ai l'honneur de vous renouveler, Monsieur l'ambassadeur, les assurances de ma haute considération "
    "et de mon amitié."
)

SPEC = {"judge": {"language": "fr1840", "letters_min": 50, "letters_max": 5000, "control_samples": 100}}


def test_fr1840_real_passage_passes():
    r = judge(SPEC, HELD_OUT_FR1840)
    assert r["checks"]["language"]["pass"], r["checks"]["language"]


def test_fr1840_shuffled_fails():
    letters = list(fold(HELD_OUT_FR1840))
    random.Random(7).shuffle(letters)
    r = judge(SPEC, "".join(letters))
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_fr1840_random_string_fails():
    rnd = random.Random(11)
    s = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(fold(HELD_OUT_FR1840))))
    r = judge(SPEC, s)
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_fr1840_corpus_folds_to_at_least_1m_letters():
    from judge_plaintext import LANG_CORPORA, read_corpus
    total = sum(len(fold(read_corpus(p))) for p in LANG_CORPORA["fr1840"])
    assert total >= 1_000_000, total
