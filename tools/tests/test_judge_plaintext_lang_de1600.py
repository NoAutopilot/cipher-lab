"""Offline test for tools/judge_plaintext.py's "de1600" language corpus (3 Oct 2026, CORP-DE16, account-4): a held-out
1611 chancery passage (a Wittelsbach/Habsburg act on the Rhenish estates' contribution) printed in Briefe und Acten zur
Geschichte des Dreissigjaehrigen Krieges, archive.org briefeundactenz00mayrgoog (the 1611 volume, deliberately NOT one of
de1600's six files; tools/data/de1600/build.py chunk filter output lines ~1200-1207). It passes the language gate; the same
passage shuffled, and a random-letter string of the same length, both fail. No network."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from judge_plaintext import LANG_CORPORA, fold, judge, read_corpus

HELD_OUT_DE1600 = (
    "überdies noch die unterländischen übertragen müssten entgegen gedachte rheinlendische sich von fernerer contribution "
    "eximirn da es doch am maisten sie unden beriert und da sie wie die heroben noch die zehn monat darüber herschiessen "
    "dardurch E L und der von Rittperg zue völliger abdankung wol geholfen were worden also dass sich dieselben irer quoten "
    "nit mit fueg zu entschitten sonder billich wie andere stend darzue gethan haben sollen"
)

SPEC = {"judge": {"language": "de1600", "letters_min": 50, "letters_max": 5000, "control_samples": 100}}


def test_de1600_corpus_is_six_files_over_1m_letters_and_excludes_the_passage():
    files = LANG_CORPORA["de1600"]
    assert len(files) >= 5  # rule 3: under ~5 files the per-fold spread is unreliable (es17c)
    big = "".join(fold(read_corpus(p)) for p in files)
    assert len(big) >= 1_000_000, len(big)
    f = fold(HELD_OUT_DE1600)
    assert not any(f[k:k + 40] in big for k in range(0, len(f) - 40, 20))


def test_de1600_real_passage_passes():
    r = judge(SPEC, HELD_OUT_DE1600)
    assert r["checks"]["language"]["pass"], r["checks"]["language"]


def test_de1600_shuffled_fails():
    letters = list(fold(HELD_OUT_DE1600))
    random.Random(7).shuffle(letters)
    r = judge(SPEC, "".join(letters))
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_de1600_random_string_fails():
    rnd = random.Random(11)
    s = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(fold(HELD_OUT_DE1600))))
    r = judge(SPEC, s)
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]
