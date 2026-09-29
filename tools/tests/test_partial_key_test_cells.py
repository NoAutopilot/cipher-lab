#!/usr/bin/env python3
"""Offline test for tools/partial_key_test.py's polyphonic order mode (--cells; H354, 29 Sept 2026). No network.
Known answer: about 480 letters of 16th-century French (tools/data/fr16) enciphered with a pair-cell key (13 classes, each
the cipher sign for two letters, fixed seed) and cut into lines of 40 signs. (1) The true key shows an order gain above the
binned-permuted keys' p95. (2) The same draft with its signs shuffled across the whole text shows no order signal (the
ARM-C1 shape: the statistic must be able to fail). (3) order_runs breaks runs at unkeyed signs and line ends.
Small beam and few keys keep it fast.   Run: python3 tools/tests/test_partial_key_test_cells.py"""
import os, random, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import judge_plaintext as jp  # noqa: E402
import partial_key_test as pk  # noqa: E402
FR = os.path.join(ROOT, "tools", "data", "fr16", "lettresindites00marg_djvu.txt.gz")
def build(seed=7, n=480, start=20000):
    txt = jp.fold(jp.read_corpus(FR))[start:start + n]
    letters = sorted(set("abcdefghilmnopqrstuxz") | set(txt)); rng = random.Random(seed); rng.shuffle(letters)
    cls = {}; cells = {}
    for i in range(0, len(letters), 2):
        name = f"K{i // 2:02d}"; pair = letters[i:i + 2]; cells[name] = frozenset(pair)
        for ch in pair: cls[ch] = name
    draft = [(f"L{j // 40:02d}", cls[ch]) for j, ch in enumerate(txt)]
    return draft, cells
def test_runs():
    cells = {"A": frozenset("a"), "B": frozenset("b")}
    d = [("L1", "A"), ("L1", "B"), ("L1", "A"), ("L1", "B"), ("L1", "X"), ("L1", "A"), ("L2", "A"), ("L2", "B"), ("L2", "A"), ("L2", "B")]
    assert pk.order_runs(d, cells, 4) == [["A", "B", "A", "B"], ["A", "B", "A", "B"]]
def test_known_and_shuffled():
    draft, cells = build(); lp = pk.make_lp("fr"); kw = dict(keys=40, within=5, width=60)
    r = pk.order_gain_test(draft, cells, lp, **kw)
    assert r["signal"], r
    sg = [s for _, s in draft]; random.Random(11).shuffle(sg)
    rs = pk.order_gain_test([(l, s) for (l, _), s in zip(draft, sg)], cells, lp, **kw)
    assert not rs["signal"], rs
    return r, rs
if __name__ == "__main__":
    test_runs(); r, rs = test_known_and_shuffled()
    print(f"ok: true key gain {r['gain']:.4f} > p95 {r['p95']:.4f}; shuffled draft gain {rs['gain']:.4f} <= p95 {rs['p95']:.4f}")
