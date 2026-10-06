"""Offline test for tools/families/columnar_homophonic.py (R15-KAL14, 6 Oct 2026): transpose/untranspose round trip at
irregular widths, and the solver reads a width-1 (no transposition) simple substitution of a repetitive text."""
import os, random, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from families import columnar_homophonic as F


def test_roundtrip():
    seq = list(range(23))
    for w in (2, 5, 7, 12):
        order = list(range(w)); random.Random(w).shuffle(order)
        c = F.transpose(seq, w, order)
        plain = np.empty(len(c), dtype=int)
        plain[F.untranspose_index(len(c), w, order)] = c
        assert list(plain) == seq, w


def test_shift_recovery():
    t = "abcdefghijklmnopqrstuvwxyz" * 4
    assert F.score_recovery(t, t) == 1.0
    assert F.score_recovery("xxxx" + t[:-4], t) > 0.9
    assert F.score_recovery("z" * len(t), t) < 0.1


def test_widths():
    assert F._widths("2-4,7") == [2, 3, 4, 7]


def test_width1_reads():
    text = ("the quick brown fox jumps over the lazy dog and then the dog sleeps under the old oak tree while the fox "
            "runs into the green forest to find another place to rest ") * 40
    corp = [text]
    plain = "".join(c for c in text if c.isalpha())[:600]
    letters = sorted(set(plain)); signs = [f"s{i}" for i in range(len(letters))]
    random.Random(3).shuffle(signs); key = dict(zip(letters, signs))
    dec, sc, info = F.solve([[key[a] for a in plain]], {}, 1, 2, corp, {"widths": "1", "iters": "20000"})
    assert F.score_recovery(dec, plain) > 0.9, F.score_recovery(dec, plain)


if __name__ == "__main__":
    test_roundtrip(); test_shift_recovery(); test_widths(); test_width1_reads(); print("ok")
