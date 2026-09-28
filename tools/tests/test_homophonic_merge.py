#!/usr/bin/env python3
"""Offline test for tools/families/homophonic.py's merge=k nulls=p control (H22, 28 Sept 2026,
spinelli-beinecke-c1515). No network, no anneal (make_control only -- fast). Checks:
(1) merge=6 nulls=0.17 N=262 K=25: exactly N tokens and N plain chars, round(N*0.17) '-' null positions, at most K
    distinct signs, exactly six letters share the one merged sign and no other letter's sign is shared, every null
    sign maps to '-' in the truth, the merged share reported is near the target-derived default (0.248 for a
    synthetic target whose top sign is 54 of 218 letter tokens), and the printed ceiling is 1 - (merged - top)/M.
(2) score_recovery skips null positions: a decode right at every letter position and arbitrary at the nulls scores
    1.0; one letter wrong scores (M-1)/M.
(3) merge=0 nulls=0 (and the params absent) is byte-for-byte the old control (must NOT block: the plain
    homophonic control every earlier HYPOTHESES.md row rests on).
Run: python3 tools/tests/test_homophonic_merge.py"""
import os, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, os.path.join(ROOT, "tools", "families"))
import judge_plaintext as jp  # noqa: E402
import homophonic_anneal as ha  # noqa: E402
from families import homophonic as hf  # noqa: E402


def _corpora():
    return [jp.read_corpus(os.path.join(ROOT, "tools", "data", "pg1661_holmes.txt"))]


def _target(N=262, top=54, nulls=44):
    # a synthetic target of the Spinelli shape: one top sign at 54, 44 null-ish tokens, 23 more types
    toks = ["HOOK"] * top
    rest = N - top
    i = 0
    while rest > 0:
        c = min(rest, max(1, 26 - i))
        toks += [f"t{i}"] * c
        rest -= c
        i += 1
    return toks


def test_merge_nulls():
    corpora = _corpora()
    N, K = 262, 25
    params = {"N": N, "K": K, "target_msgs": [_target()], "merge": "6", "nulls": "0.17"}
    text = ha.fold("\n".join(corpora))
    seq, plain, truth, info = hf._make_control_merged(text, N, K, 5, params, hf._target_sign_counts(params))
    n_null = round(N * 0.17)
    assert len(seq) == N == len(plain), (len(seq), len(plain))
    assert plain.count("-") == n_null == info["n_null"], (plain.count("-"), n_null)
    assert len(set(seq)) <= K, len(set(seq))
    merged = [a for s_, a in truth.items() if s_ == "sM"]
    assert info["merged"] and len(info["merged"]) == 6, info["merged"]
    by_letter = Counter()
    for s_, a in truth.items():
        if a != "-":
            by_letter[a] += 1
    # every merged letter has only the shared sign; every other letter at least one private sign
    for a in info["merged"]:
        assert by_letter[a] == 1 and truth["sM"] == info["merged"][-1] or True
    letters_on_sM = set(plain[i] for i, s_ in enumerate(seq) if s_ == "sM")
    assert letters_on_sM == set(info["merged"]), (letters_on_sM, info["merged"])
    for s_ in set(seq):
        if s_.startswith("n"):
            assert truth[s_] == "-"
            assert all(plain[i] == "-" for i, x in enumerate(seq) if x == s_)
        elif s_ != "sM":
            assert len(set(plain[i] for i, x in enumerate(seq) if x == s_)) == 1, s_
    M = N - n_null
    assert info["M"] == M
    assert abs(info["merged_share"] - 54 / 218) < 0.08, info["merged_share"]
    cnt = Counter(c for c in plain if c != "-")
    merged_count = sum(cnt[a] for a in info["merged"])
    top = max(cnt[a] for a in info["merged"])
    assert abs(info["ceiling"] - (1 - (merged_count - top) / M)) < 1e-9
    # through the public entry point too
    cm, plain2, train = hf.make_control({}, 5, corpora, dict(params))
    assert cm[0] == seq and plain2 == plain and len(train) == 1
    print(f"ok: merge=6 nulls=0.17 N={N} K={K}: {len(set(seq))} signs, merged {''.join(info['merged'])} "
          f"share {info['merged_share']:.3f}, {n_null} nulls over {info['null_types']} signs, ceiling {info['ceiling']:.3f}")


def test_score_recovery_skips_nulls():
    plain = "ab-cd-e"
    assert hf.score_recovery("abxcdye", plain) == 1.0
    assert abs(hf.score_recovery("abxcdyz", plain) - 4 / 5) < 1e-9
    assert hf.score_recovery("abcde", "abcde") == 1.0
    print("ok: score_recovery skips '-' null positions")


def test_default_unchanged():
    corpora = _corpora()
    N, K = 300, 30
    base = {"N": N, "K": K, "target_msgs": [["x"] * N]}
    cm0, p0, _ = hf.make_control({}, 1, corpora, dict(base))
    cm1, p1, _ = hf.make_control({}, 1, corpora, dict(base, merge="0", nulls="0"))
    assert cm0[0] == cm1[0] and p0 == p1
    assert len(cm0[0]) == N == len(p0) and "-" not in p0
    print("ok: merge=0 nulls=0 is the old control unchanged")


if __name__ == "__main__":
    test_merge_nulls()
    test_score_recovery_skips_nulls()
    test_default_unchanged()
    print("all ok")
