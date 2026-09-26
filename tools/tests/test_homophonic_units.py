#!/usr/bin/env python3
"""Offline test for tools/families/homophonic.py units=syl (bMALN, 26 Sept 2026): letter+syllable homophonic design.
(1) encode_units/expand_units round-trip on folded text, greedy longest match (sch before ch).
(2) make_control units=syl: N unit tokens, K distinct signs, plain is a unit string of length N.
(3) a small solve (clean control, generous N, short anneal) recovers well above chance, and split_decode expands
    to letters. Run: python3 tools/tests/test_homophonic_units.py (about a minute)."""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, os.path.join(ROOT, "tools", "families"))
import judge_plaintext as jp  # noqa: E402
from families import homophonic as hf  # noqa: E402


def test_roundtrip():
    p = {"units": "syl"}
    u = hf.encode_units("Und der Schreiber", p)
    assert hf.expand_units(u, p) == "undderschreiber", hf.expand_units(u, p)
    assert u[0] == "A" and u[1] == "B" and u[2] == "E", u   # und, der, sch (not ch)


def test_control_and_solve():
    corpora = [jp.read_corpus(os.path.join(ROOT, "tools", "data", "de16", "composed_enhg.txt"))]
    N, K = 1500, 60
    params = {"N": N, "K": K, "units": "syl", "iters": 150000}
    cm, plain, train = hf.make_control({}, 1, corpora, dict(params))
    assert len(cm[0]) == N and len(plain) == N and len(set(cm[0])) <= K
    dec, sc, info = hf.solve(cm, {}, 1, 6, train, dict(params))
    rec = hf.score_recovery(dec, plain)
    assert rec > 0.3, rec
    lines = hf.split_decode(dec, cm)
    assert lines and all(c.islower() for c in lines[0]), lines[0][:40]
    print(f"units=syl clean control N={N} K={K}: recovery {rec:.3f}")


if __name__ == "__main__":
    test_roundtrip()
    test_control_and_solve()
    print("ok")
