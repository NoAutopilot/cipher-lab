#!/usr/bin/env python3
"""Offline test for ciphers/kaliningrad-2015/scripts/pattern_crib.py: a small synthetic Russian-like
corpus (about 300 letters), a control window relabelled with random sign names, and the constraint-
propagation solver recovering most of it. No network, runs in well under 10 s.

Usage: python3 tools/tests/test_pattern_crib.py
"""
import gzip
import shutil
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "ciphers" / "kaliningrad-2015" / "scripts"))
import pattern_crib as pc  # noqa: E402

# A tiny made-up Russian-ish devotional passage, repeated across two "chapters" with enough repeated
# word forms (и, бог, свет, земля, сказал ...) that word-pattern crib matching has something to lock
# onto -- deliberately small and self-contained, not a real Bible excerpt.
CHAPTER_1 = """
и сказал бог да будет свет и стал свет и увидел бог свет что он хорош
и отделил бог свет от тьмы и назвал бог свет днем а тьму ночью
и был вечер и было утро день один и сказал бог да будет твердь
"""

CHAPTER_2 = """
и сотворил бог небо и землю земля же была безвидна и пуста
и тьма над бездною и дух божий носился над водою и сказал бог
да будет свет и стал свет и был вечер и было утро день один
"""


def build_fixture_corpus(tmpdir):
    corpus = Path(tmpdir) / "corpus"
    corpus.mkdir()
    with gzip.open(corpus / "01_test.txt.gz", "wt", encoding="utf-8") as f:
        f.write("== CHAPTER 1 ==\n" + CHAPTER_1 + "\n== CHAPTER 2 ==\n" + CHAPTER_2 + "\n")
    return corpus


def test_pattern_of():
    toks = list("elhxikixacel")
    assert pc.pattern_of(toks) == (0, 1, 2, 3, 4, 5, 4, 3, 6, 7, 0, 1)


def test_cipher_signs_A_merges_apostrophe():
    assert pc.cipher_signs_A("en'ifvn") == ["e", "n'", "i", "f", "v", "n"]


def test_cipher_signs_B_keeps_apostrophe_separate():
    assert pc.cipher_signs_B("en'ifvn") == ["e", "n", "'", "i", "f", "v", "n"]


def test_plain_tokens_A_merges_soft_sign():
    # день -> д,е,н,ь -> merges н+ь
    assert pc.plain_tokens_A("день") == ["д", "е", "нь"]


def test_load_ciphertext_words_count():
    words, abbrevs = pc.load_ciphertext_words()
    assert len(words) + len(abbrevs) == 196  # 206 raw tokens minus 10 all-dot filler tokens
    assert len(abbrevs) >= 8


def test_solver_recovers_control_window(tmp_path):
    corpus = build_fixture_corpus(tmp_path)
    chap_key, cws, true_toks, n_letters, label = pc.make_control_window(
        str(corpus), "B", seed=1, target_signs=120
    )
    assert n_letters >= 100  # each fixture chapter is a bit under 300 letters on its own
    vocab, _wc, _chapters = pc.build_vocab(str(corpus), "B", exclude_chapter=None)
    matched, sign2letter = pc.solve(cws, vocab)
    recovered = pc.score_control(cws, true_toks, sign2letter, label)
    assert recovered >= 0.8, f"expected >=0.8 letters recovered on an in-vocabulary window, got {recovered:.3f}"


def test_solver_holdout_is_harder_or_equal(tmp_path):
    corpus = build_fixture_corpus(tmp_path)
    chap_key, cws, true_toks, n_letters, label = pc.make_control_window(
        str(corpus), "B", seed=1, target_signs=120
    )
    vocab_in, _wc, _c = pc.build_vocab(str(corpus), "B", exclude_chapter=None)
    matched_in, s2l_in = pc.solve(cws, vocab_in)
    recovered_in = pc.score_control(cws, true_toks, s2l_in, label)

    vocab_out, _wc2, _c2 = pc.build_vocab(str(corpus), "B", exclude_chapter=chap_key)
    matched_out, s2l_out = pc.solve(cws, vocab_out)
    recovered_out = pc.score_control(cws, true_toks, s2l_out, label)

    assert recovered_out <= recovered_in + 1e-9


def test_shuffle_null_runs():
    words, _abbrevs = pc.load_ciphertext_words()
    cws = pc.cipher_word_signs_for("B", words)
    shuffled = pc.shuffle_null(cws, seed=1)
    assert len(shuffled) == len(cws)
    assert sum(len(s) for _w, s in shuffled) == sum(len(s) for _w, s in cws)


def main():
    t0 = time.time()
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in tests:
        import inspect
        if "tmp_path" in inspect.signature(t).parameters:
            with tempfile.TemporaryDirectory() as d:
                t(Path(d))
        else:
            t()
        print(f"ok  {t.__name__}")
    dt = time.time() - t0
    print(f"{len(tests)} tests passed in {dt:.2f}s")
    assert dt < 10, f"test suite took {dt:.2f}s, expected under 10s"
    return 0


if __name__ == "__main__":
    sys.exit(main())
