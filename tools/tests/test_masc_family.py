#!/usr/bin/env python3
"""Offline test for tools/families/masc.py's noise=p param (A2-LAG3, 3 Oct 2026). No network, no anneal.
(1) noise absent leaves the control a true simple substitution: one sign per plaintext letter, same positions.
(2) noise=0.25 redraws about a quarter of tokens, keeps N, and uses only the control's own sign labels.
Run: python3 tools/tests/test_masc_family.py"""
import os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, os.path.join(ROOT, "tools", "families"))
import judge_plaintext as jp  # noqa: E402
from families import masc  # noqa: E402


def _corpora():
    return [jp.read_corpus(os.path.join(ROOT, "tools", "data", "pg1661_holmes.txt"))]


def test_noise():
    corpora = _corpora()
    N = 300
    tgt = [[str(i % 20) for i in range(N)]]
    clean, plain, _ = masc.make_control({}, 1, corpora, {"N": N, "K": 20, "target_msgs": tgt})
    seq = clean[0]
    assert len(seq) == N == len(plain)
    m = {}
    for s, a in zip(seq, plain):
        assert m.setdefault(s, a) == a, "clean control is not one sign per letter"
    noisy, plain2, _ = masc.make_control({}, 1, corpora, {"N": N, "K": 20, "target_msgs": tgt, "noise": "0.25"})
    nseq = noisy[0]
    assert plain2 == plain and len(nseq) == N
    assert set(nseq) <= set(seq)
    changed = sum(1 for a, b in zip(seq, nseq) if a != b) / N
    assert 0.10 < changed < 0.30, changed
    print("ok: masc noise=0.25 changed share", round(changed, 3), "N", N)


if __name__ == "__main__":
    test_noise()
