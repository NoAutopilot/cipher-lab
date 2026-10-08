"""Offline test for tools/judge_plaintext.py's "nl16" language corpus (8 Oct 2026, NL16-11106, LANE FAMILY account 2): a held-out
1561 passage of Coornhert's Officia Ciceronis (DBNL cice001offi01, deliberately NOT one of nl16's five files; see
tools/data/nl16/build.py). It passes the language gate; the same passage shuffled, and a random-letter string of the same
length, both fail. No network."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from judge_plaintext import LANG_CORPORA, fold, judge, read_corpus

HELD_OUT_NL16 = (
    "te besorghen niet alleen voor hun selfs maer voor wijf kint vrienden ende die onder hun bescherminge staen "
    "Vvelcke sorchvuldicheyt de herten verwect ooc vromer maect om haer saken te doen Ondersoeckinghe des waerheyts is den "
    "natuerlijcken aert der menschen Ende in sonderheyt soo is de ondersoeckinghe ende het nasporen vander waerheyt den "
    "rechten aert ende eyghenschap des menschen Daeromme als wy vrij zijn van nootlijcke sorchvuldicheyt so begheeren vvy "
    "yet te sien te hooren oft te leeren ende achten de kennisse der verborghen oft wonderlijcke saken noodtruftich om "
    "salichlijcken te leuen"
)

SPEC = {"judge": {"language": "nl16", "letters_min": 50, "letters_max": 5000, "control_samples": 100}}


def test_nl16_corpus_is_five_files_over_1m_letters_and_excludes_the_passage():
    files = LANG_CORPORA["nl16"]
    assert len(files) >= 5  # rule 3: under ~5 files the per-fold spread is unreliable (es17c)
    big = "".join(fold(read_corpus(p)) for p in files)
    assert len(big) >= 1_000_000, len(big)
    f = fold(HELD_OUT_NL16)
    assert not any(f[k:k + 40] in big for k in range(0, len(f) - 40, 20))


def test_nl16_real_passage_passes():
    r = judge(SPEC, HELD_OUT_NL16)
    assert r["checks"]["language"]["pass"], r["checks"]["language"]


def test_nl16_shuffled_fails():
    letters = list(fold(HELD_OUT_NL16))
    random.Random(7).shuffle(letters)
    r = judge(SPEC, "".join(letters))
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_nl16_random_string_fails():
    rnd = random.Random(11)
    s = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(fold(HELD_OUT_NL16))))
    r = judge(SPEC, s)
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]
