"""Offline test for tools/judge_plaintext.py's "fr18" language corpus (25 Sept 2026, LANE ZX2 ZX2-FR18): a
held-out French passage -- from Torcy's Memoires tome troisieme (memoiresdemonsie03torc, archive.org), a
volume NOT among the six files (memoiresdemonsie01torc, memoiresdemonsie02torc, mmoiresduducde01invill,
mmoiresduducde02vill, mmoiresetlettre01margoog, lagazettedefran01unkngoog) committed to tools/data/fr18/ --
passes the language gate; the same passage shuffled, and a random-letter string of the same length, both fail
it. Left as raw OCR (long-s misread as "f": "amufoient", "fauiTes", "fans", "fages" etc.) rather than
hand-corrected, since that is what tools/data/fr18's own corpus looks like too (see its README.md). No
network."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from judge_plaintext import judge, fold

# Torcy, Memoires tome troisieme, on the failed 1710 Gertruydenberg negotiations and the case for peace --
# held out of the committed fr18 corpus (only tomes I-II of Torcy are in tools/data/fr18/).
HELD_OUT_FR18 = (
    "les qu'ils avoient rejettées. Ils amufoient "
    "les Peuples de ces fauiTes efpérances , pour "
    "endormir leurs maux & rendre plus léger le "
    "poids d'une guerre preiîance , dont la fin ne "
    "le pouvoit prévoir. "
    "La paix ne devoit pas être l'ouvrage des "
    "hommes , Dieu s'étoit réfervé les moyens "
    "& les momens de la rendre à l'Europe. Il "
    "permit que les plus éclairés du Confeil bles- "
    "lés des difcours qu'on tenoit en Hollande, "
    "opinèrent à renvoyer Gaultier en Angleterre "
    "fans admettre le peu de propolîtions dont il "
    "avoit été chargé. Ils dirent qu'il feroit con- "
    "tre la dignité du Roi , de rechercher encore "
    "les Hollandois , & de leur propofer de nou- "
    "velles Conférences, après tant de procédés "
    "indignes de leur part, principalement en "
    "dernier lieu à Geertruydenberg; & que rien "
    "n'autoriferoit davantage leurs pronoftiçs , & "
    "les bruits qu'ils répandoient que la France , "
    "hors d'état de faire une campagne, céde- "
    "roit enfin & confentiroit à toutes les condi- "
    "tions que les Alliés exigeroient d'elle. "
    "Ces réflexions étoient fages, mais la paix "
    "étoit encore plus néceiTaire que dans les "
    "tems où le Roi confentoit aux plus grands "
    "facrifices pour l'obtenir. On auroit alors "
    "donné beaucoup pour détacher l'Angleterre "
    "de fes Alliés ; un préfent confidérable fait "
    "à Marlborough , eût été utilement employé : "
    "ce qu'on auroit acheté bien cher dans ces "
    "tems difficiles, s'offroit de foi-même fans "
    "qu'il en coûtât rien au Roi ni au Royaume."
)

SPEC = {"judge": {"language": "fr18", "letters_min": 50, "letters_max": 5000, "control_samples": 100}}


def test_fr18_real_passage_passes():
    r = judge(SPEC, HELD_OUT_FR18)
    assert r["checks"]["language"]["pass"], r["checks"]["language"]


def test_fr18_shuffled_fails():
    letters = list(fold(HELD_OUT_FR18))
    random.Random(7).shuffle(letters)
    r = judge(SPEC, "".join(letters))
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_fr18_random_string_fails():
    rnd = random.Random(11)
    s = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(fold(HELD_OUT_FR18))))
    r = judge(SPEC, s)
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_fr18_corpus_folds_to_at_least_1m_letters():
    from judge_plaintext import LANG_CORPORA, read_corpus
    total = sum(len(fold(read_corpus(p))) for p in LANG_CORPORA["fr18"])
    assert total >= 1_000_000, total


if __name__ == "__main__":
    test_fr18_real_passage_passes()
    test_fr18_shuffled_fails()
    test_fr18_random_string_fails()
    test_fr18_corpus_folds_to_at_least_1m_letters()
    print("ok")
