"""Offline test for tools/judge_plaintext.py's "fr1810" language corpus (1 Oct 2026, BER-FRCORP): a held-out
Napoleonic-era official passage -- Davout to the Minister of War (duc de Feltre), Hamburg, 23-24 January 1812,
letters 1009-1010 of Mazade's Correspondance du marechal Davout tome III (archive.org correspondanced00davogoog,
raw djvu lines 16142-16160) -- which is NOT in the committed corpus: tools/data/fr1810's copy of that volume is
cut before its first 1812 letter (MANIFEST.tsv), so this text is unseen by the model. It passes the language gate;
the same passage shuffled, and a random-letter string of the same length, both fail it. Left as raw OCR
("Thonneur", "marcbes", "lOlO") rather than hand-corrected, as the corpus itself is raw OCR. No network."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from judge_plaintext import judge, fold

HELD_OUT_FR1810 = (
    "AU MINISTRE DE LA GUERRE DUC DE FELTRE. Hambourg, 23 janvier 1812. Monseigneur, j'ai Thonneur de rendre "
    "compte à Votre Excellence que j'ai reçu l'avis de M. le général gouverneur de Glogau que Ton faisait souvent "
    "faire des marcbes de dix ou douze lieues aux troupes prussiennes pour les accoutumer à la fatigue. Ces "
    "promenades se font par détacliements de 40 à 50 hommes. lOlO. AU MINISTRE DE LA GUERRE DUC DE FELTRE. "
    "Hambourg, 24 janvier 1812. Monseigneur, j'ai l'iionneur d'adresser à Votre Excellence copie d'une lettre de "
    "M. le général Rapp faisant connaître que le résident de Prusse à Danzig a communiqué à ce général une lettre "
    "de son souverain, par laquelle il lui est ordonné de faire arrêter, sans en référer au gouvernement de "
    "province, tout individu que le général Rapp lui dénoncerait comme tenant des propos contre le gouvernement "
    "français."
)

SPEC = {"judge": {"language": "fr1810", "letters_min": 50, "letters_max": 5000, "control_samples": 100}}


def test_fr1810_real_passage_passes():
    r = judge(SPEC, HELD_OUT_FR1810)
    assert r["checks"]["language"]["pass"], r["checks"]["language"]


def test_fr1810_shuffled_fails():
    letters = list(fold(HELD_OUT_FR1810))
    random.Random(7).shuffle(letters)
    r = judge(SPEC, "".join(letters))
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_fr1810_random_string_fails():
    rnd = random.Random(11)
    s = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(fold(HELD_OUT_FR1810))))
    r = judge(SPEC, s)
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_fr1810_corpus_folds_to_at_least_1m_letters():
    from judge_plaintext import LANG_CORPORA, read_corpus
    total = sum(len(fold(read_corpus(p))) for p in LANG_CORPORA["fr1810"])
    assert total >= 1_000_000, total
