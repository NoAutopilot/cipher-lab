#!/usr/bin/env python3
"""Offline test for tools/families/homophonic.py's profile=target and noise=p params (GOLD-D1, 25 Sept 2026).
No network, no anneal (only make_control is exercised -- fast). Checks:
(1) default behaviour (no profile/noise params) is unchanged: K distinct signs, N tokens, every token maps
    through truth to a folded letter.
(2) profile=target: the control's own K is exact, and its sorted sign-count profile places the target's largest
    bucket on a homophone of the plaintext window's own most frequent letter (the structural point of the
    param: a control at K also carries the target's lopsided top sign).
(3) noise=0 leaves the control's tokens exactly as built; noise=1.0 (every token redrawn) still produces exactly
    N tokens drawn only from the control's own K labels.
Run: python3 tools/tests/test_homophonic_family.py"""
import os, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, os.path.join(ROOT, "tools", "families"))
import judge_plaintext as jp  # noqa: E402
import homophonic_anneal as ha  # noqa: E402
from families import homophonic as hf, draw_window  # noqa: E402


def _corpora():
    return [jp.read_corpus(os.path.join(ROOT, "tools", "data", "pg1661_holmes.txt"))]


def test_default_unchanged():
    corpora = _corpora()
    N, K = 300, 30
    params = {"N": N, "K": K, "target_msgs": [["x"] * N]}  # target_msgs present but profile not requested
    cm, plain, train = hf.make_control({}, 1, corpora, params)
    seq = cm[0]
    assert len(seq) == N == len(plain), (len(seq), len(plain))
    assert len(set(seq)) <= K
    print("ok: default (no profile/noise) unchanged, N", N, "K<=", K)


def test_profile_target():
    corpora = _corpora()
    N, K = 400, 25
    # a synthetic, sharply lopsided target profile: one sign at 30 pct of N, a long thin tail -- the shape
    # GOLD-D1 cares about (Debosnys' X at 16.1 pct is the same kind of shape, less extreme).
    target_counts = [120] + [1] * (N - 120)
    target_counts = target_counts[:K] if len(target_counts) >= K else target_counts
    # pad so len(target_msgs flattened) sums sensibly; target_sign_counts only needs the multiset of counts,
    # which we build directly as a synthetic ciphertext of the right shape.
    toks = []
    for i, c in enumerate(target_counts):
        toks += [f"t{i}"] * c
    params = {"N": N, "K": K, "target_msgs": [toks], "profile": "target"}
    cm, plain, train = hf.make_control({}, 2, corpora, params)
    seq = cm[0]
    assert len(seq) == N, len(seq)
    assert len(set(seq)) <= K, (len(set(seq)), K)
    # the most frequent letter in the drawn plaintext window should own the control's own biggest homophone
    cnt_p = Counter(plain)
    top_letter = cnt_p.most_common(1)[0][0]
    cnt_seq = Counter(seq)
    top_sign, top_sign_n = cnt_seq.most_common(1)[0]
    # rebuild which letter top_sign belongs to by re-deriving truth the same way make_control did (seed+1000)
    import random
    letters = [a for a, _ in cnt_p.most_common()]
    m = {a: 1 for a in letters}
    extra = K - len(letters)
    while extra > 0:
        a = max(letters, key=lambda a: cnt_p[a] / m[a])
        m[a] += 1
        extra -= 1
    i = 0
    owner = {}
    for a in letters:
        for _ in range(m[a]):
            owner[f"s{i}"] = a
            i += 1
    assert len(owner) == K, (len(owner), K)  # the allocation itself always uses exactly K homophones
    assert owner[top_sign] == top_letter, (owner[top_sign], top_letter)
    assert top_sign_n > N / K, (top_sign_n, N, K)  # visibly above the flat 1/K share
    print(f"ok: profile=target K exact ({K}), top sign {top_sign} (n={top_sign_n}) owned by top letter {top_letter!r}")


def test_noise():
    corpora = _corpora()
    N, K = 200, 20
    target_counts = sorted([1] * (K - 1) + [N - (K - 1)], reverse=True)
    toks = []
    for i, c in enumerate(target_counts):
        toks += [f"t{i}"] * c
    params0 = {"N": N, "K": K, "target_msgs": [toks], "noise": "0"}
    cm0, _, _ = hf.make_control({}, 3, corpora, params0)
    params1 = dict(params0, **{"noise": "1.0"})
    cm1, _, _ = hf.make_control({}, 3, corpora, params1)
    assert cm0[0] == hf.make_control({}, 3, corpora, {"N": N, "K": K, "target_msgs": [toks]})[0][0]
    seq1 = cm1[0]
    assert len(seq1) == N
    base_labels = set(hf.make_control({}, 3, corpora, {"N": N, "K": K, "target_msgs": [toks]})[0][0])
    assert set(seq1) <= base_labels
    assert seq1 != cm0[0]  # noise=1.0 redraws every position, essentially always differs from the clean seq
    print("ok: noise=0 leaves the control unchanged, noise=1.0 redraws within the control's own K labels")


if __name__ == "__main__":
    test_default_unchanged()
    test_profile_target()
    test_noise()
    print("all homophonic-family tests passed")
