"""Offline test for tools/judge_plaintext.py's "sv17" language corpus (3 Oct 2026, GAPS67, account-4): a held-out passage of
a 1632 Swedish field letter (Lech crossing, march on Lauingen) printed in Rikskansleren Axel Oxenstiernas skrifter och
brefvexling (archive.org rikskanslerenax00palagoog, raw djvu lines about 38525-38544), which lies past the 450,000-letter cap
tools/data/sv17/build.py applies to that volume, so it is unseen by the model (test 1 checks that). Hand normalisation of
the OCR (hyphenated line breaks joined, å to a as build.py does). It passes the language gate; the same passage shuffled,
and a random-letter string of the same length, both fail. No network."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from judge_plaintext import LANG_CORPORA, fold, judge, read_corpus

HELD_OUT_SV17 = (
    "hijtöffver, thet han skulle haffva veelat (som doch fangarne altidh haffva berättat) inlata sigh medh oss i nagon "
    "huffvudaction, da vij skulle haffva träd t medh honom tillsamman och uthgangen stält i Gudz händer. Och ehuruväll "
    "fienden allenast i förstonne medh sitt cavallerie haar passerat öffver Lechen, sa är han doch, när han sagh oss halla "
    "i bataille, ater gangen tillhakar igen och sigh intet vijdare medh oss engagerat. Elliest haffve vij och under varande "
    "belägring ingen synnerlig skada lidit, uthan nagre officerare och gemene äre qvätzte vordne, hvilket i tocka "
    "belägringar icke annorlunda kan afflöpa. Och är, öffver thet som förmält är, icke till thet ringesta mehra förelupit, "
    "hvaraff fienden skulle kunna tillägna sigh een föreeel. Och aldenstund vij nu försporde, fienden intet veela inlata "
    "sigh medh oss i nagon huffvudaction, haffve vij deropa tagit var marche hijtt at Donau moot Lauging, icke till att "
    "quittera landet, uthan sij till, hvadh fienden, som nu effter fangernes berättelser skall hafva satt sigh emellan "
    "Aiche och Schrobenhausen, ma haffva i sinnet"
)

SPEC = {"judge": {"language": "sv17", "letters_min": 50, "letters_max": 5000, "control_samples": 100}}


def test_sv17_corpus_is_six_files_over_1m_letters_and_excludes_the_passage():
    files = LANG_CORPORA["sv17"]
    assert len(files) >= 5  # rule 3: under ~5 files the per-fold spread is unreliable (es17c)
    big = "".join(fold(read_corpus(p)) for p in files)
    assert len(big) >= 1_000_000, len(big)
    f = fold(HELD_OUT_SV17)
    assert not any(f[k:k + 40] in big for k in range(0, len(f) - 40, 20))


def test_sv17_real_passage_passes():
    r = judge(SPEC, HELD_OUT_SV17)
    assert r["checks"]["language"]["pass"], r["checks"]["language"]


def test_sv17_shuffled_fails():
    letters = list(fold(HELD_OUT_SV17))
    random.Random(7).shuffle(letters)
    r = judge(SPEC, "".join(letters))
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_sv17_random_string_fails():
    rnd = random.Random(11)
    s = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(fold(HELD_OUT_SV17))))
    r = judge(SPEC, s)
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]
