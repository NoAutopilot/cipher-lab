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


def test_stage1_finds_order():
    """KAL-2ST (15 Oct 2026): the language-free stage-1 statistic ranks the true column order first on a transposed
    repetitive text, and stage=two reads it end to end."""
    text = ("the quick brown fox jumps over the lazy dog and then the dog sleeps under the old oak tree while the fox "
            "runs into the green forest to find another place to rest ") * 40
    plain = "".join(c for c in text if c.isalpha())[:600]
    letters = sorted(set(plain)); sid = {a: i for i, a in enumerate(letters)}
    w, order = 5, [3, 0, 4, 1, 2]
    c = np.array(F.transpose([sid[a] for a in plain], w, order))
    true = F.bigram_stat(c, len(letters), F.untranspose_index(len(c), w, order))
    got = F.stage1_orders(c, len(letters), len(c), w, random.Random(1), restarts=20, iters=500, keep=2)
    assert got[0][0] >= true and true > F.bigram_stat(c, len(letters), F.untranspose_index(len(c), w, [0, 1, 2, 3, 4]))
    signs = [f"s{i}" for i in range(len(letters))]; random.Random(3).shuffle(signs); key = dict(zip(letters, signs))
    cmsg = F.transpose([key[a] for a in plain], w, order)
    dec, sc, info = F.solve([cmsg], {}, 1, 1, [text], {"widths": "4-6", "iters": "15000", "stage": "two",
                                                       "s1_restarts": "20", "s1_iters": "500"})
    assert info["width"] == 5 and F.score_recovery(dec, plain) > 0.9, (info["width"], F.score_recovery(dec, plain))


if __name__ == "__main__":
    test_roundtrip(); test_shift_recovery(); test_widths(); test_width1_reads(); test_stage1_finds_order(); print("ok")
