"""Offline test for tools/judge_plaintext.py's "fr17" language corpus (3 Oct 2026, TOOL-FR17, account-4): a held-out
1640 passage of Jean Chapelain's letters (Tamizey de Larroque, Lettres de Jean Chapelain tome I, archive.org
lettresdejeancha01chap, raw djvu lines about 70030-70075: the letter of 21 May 1640 and his 28 May letter to Bouchard
quoted in the note) which lies past the 650,000-letter cap tools/data/fr17/build.py applies to that volume, so it is
unseen by the model (test 1 checks that). It passes the language gate; the same passage shuffled, and a random-letter
string of the same length, both fail it. Light hand normalisation of OCR (amy, Chalais) only. No network."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from judge_plaintext import LANG_CORPORA, fold, judge, read_corpus

HELD_OUT_FR17 = (
    "de Gamillac de venir à luy et de luy ayder à tuer son homme. Il est fort plaint, et en mon particulier, j'y ay regret "
    "à cause de luy et à cause du marquis de Flamarens, son amy intime et qui en sera inconsolable. Mlle de Chalais s'est "
    "sentie infiniment obligée de ce que vous m'avés escrit pour elle et est vostre admiratrice aussy bien que vostre servante "
    "très humble. Elle est partie d'aujourd'huy pour Bourbon. Pour la Congiura de M. l'abbé de Retz, je vous confirme que "
    "c'est un ouvrage différent de celuy de M. Mascardi, quoyque ce soit le mesme sujet qu'il traitte et que le travail en "
    "est assés beau, sinon pour aller du pair avec l'italien, au moins pour ne luy céder de guères"
)

SPEC = {"judge": {"language": "fr17", "letters_min": 50, "letters_max": 5000, "control_samples": 100}}


def test_fr17_corpus_is_six_files_over_1m_letters_and_excludes_the_passage():
    files = LANG_CORPORA["fr17"]
    assert len(files) >= 5  # rule 3: under ~5 files the per-fold spread is unreliable (es17c)
    big = "".join(fold(read_corpus(p)) for p in files)
    assert len(big) >= 1_000_000, len(big)
    f = fold(HELD_OUT_FR17)
    assert not any(f[k:k + 40] in big for k in range(0, len(f) - 40, 40))


def test_fr17_real_passage_passes():
    r = judge(SPEC, HELD_OUT_FR17)
    assert r["checks"]["language"]["pass"], r["checks"]["language"]


def test_fr17_shuffled_fails():
    letters = list(fold(HELD_OUT_FR17))
    random.Random(7).shuffle(letters)
    r = judge(SPEC, "".join(letters))
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_fr17_random_string_fails():
    rnd = random.Random(11)
    s = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(fold(HELD_OUT_FR17))))
    r = judge(SPEC, s)
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]
