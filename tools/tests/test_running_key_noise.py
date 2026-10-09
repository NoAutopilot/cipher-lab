"""Offline test: running_key family's noise param redraws about the asked share of control letters and leaves the
plaintext and the noise=0 control unchanged (LAG-NEXT, 9 Oct 2026)."""
import os, sys, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from families import running_key as f


def _corpus(seed):
    r = random.Random(seed)
    words = ["le", "roy", "de", "france", "prince", "orange", "lettre", "monsieur", "pour", "avec", "gand", "faict"]
    return " ".join(r.choice(words) for _ in range(6000))


def test_noise():
    corpora = [_corpus(i) for i in range(3)]
    base = {"N": 400, "lengths": [200, 200]}
    m0, p0, _ = f.make_control({}, 1, corpora, dict(base))
    m0b, _, _ = f.make_control({}, 1, corpora, dict(base, noise=0))
    assert m0 == m0b
    m1, p1, _ = f.make_control({}, 1, corpora, dict(base, noise=0.2))
    assert p1 == p0 and [len(m) for m in m1] == [200, 200]
    diff = sum(a != b for x, y in zip(m0, m1) for a, b in zip(x, y)) / 400
    assert 0.08 < diff < 0.3, diff


if __name__ == "__main__":
    test_noise(); print("ok")
