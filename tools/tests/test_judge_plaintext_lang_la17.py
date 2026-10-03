"""Offline test for tools/judge_plaintext.py's "la17" language corpus (3 Oct 2026, GAPS57, account-4): a held-out passage of
a letter to G. J. Vossius (Vossii et ad eum epistolae, 1693, archive.org bub_gb_FK3cWikzFwsC, raw djvu lines about
83790-83804, the Elzevir / Historia Danica letter) which lies past the 650,000-letter cap tools/data/la17/build.py applies to
that volume, so it is unseen by the model (test 1 checks that). Hand normalisation of the OCR (long s restored, ligatures).
It passes the language gate; the same passage shuffled, and a random-letter string of the same length, both fail. No network."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from judge_plaintext import LANG_CORPORA, fold, judge, read_corpus

HELD_OUT_LA17 = (
    "Novum Testamentum Notas, quarum specimen Elzevirius hic ostendit, avidissime exspectamus. Misit mihi Historiam "
    "obsidionis Sylvae ducis, facto ab editione ejus anno: idem mihi in mittenda Historia Danica faciendum esse censeo. Nempe "
    "hoc est recte amicitiam colere, et amicum aestimare; cujus desiderio ab ipso initio satisfactum oportebat. Tu et ego non sic "
    "agimus, ac prohibeat praeses amicitiae Deus, qui conjunxit corda nostra. Is nos servet diutissime. Uxor liberique mei te "
    "et tuam atque tuos plurima salute impertiunt; resalutant officiose Laurenbergius et Stephanius"
)

SPEC = {"judge": {"language": "la17", "letters_min": 50, "letters_max": 5000, "control_samples": 100}}


def test_la17_corpus_is_six_files_over_1m_letters_and_excludes_the_passage():
    files = LANG_CORPORA["la17"]
    assert len(files) >= 5  # rule 3: under ~5 files the per-fold spread is unreliable (es17c)
    big = "".join(fold(read_corpus(p)) for p in files)
    assert len(big) >= 1_000_000, len(big)
    f = fold(HELD_OUT_LA17)
    assert not any(f[k:k + 40] in big for k in range(0, len(f) - 40, 20))


def test_la17_real_passage_passes():
    r = judge(SPEC, HELD_OUT_LA17)
    assert r["checks"]["language"]["pass"], r["checks"]["language"]


def test_la17_shuffled_fails():
    letters = list(fold(HELD_OUT_LA17))
    random.Random(7).shuffle(letters)
    r = judge(SPEC, "".join(letters))
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_la17_random_string_fails():
    rnd = random.Random(11)
    s = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(fold(HELD_OUT_LA17))))
    r = judge(SPEC, s)
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]
