#!/usr/bin/env python3
"""Offline test for tools/partial_key_test.py (H31, 28 Sept 2026). A 300-letter Italian window under a random
substitution (its own held-out text): the TRUE key restricted to 15 codes must score above the shuffled-key p95 on
bigrams; the same 15 letters under a random wrong assignment must not beat the p95 (the must-NOT case: a wrong key
is not flagged). Run: python3 tools/tests/test_partial_key_test.py"""
import os, random, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import homophonic_anneal as ha  # noqa: E402
import judge_plaintext as jp  # noqa: E402
import partial_key_test as pk  # noqa: E402


def main():
    texts = [jp.read_corpus(str(p)) for p in jp.LANG_CORPORA["it"]]
    folded = ha.fold(texts[0])
    rng = random.Random(4)
    s = rng.randrange(20000, len(folded) - 5000)
    plain = folded[s:s + 300]
    lm = pk.LM(texts[1:])  # held out: the window's own file is not in the model
    letters = sorted(set(plain))
    codes = {a: f"C{i}" for i, a in enumerate(letters)}
    seq = [codes[a] for a in plain]
    top = [a for a, _ in __import__("collections").Counter(plain).most_common(15)]
    true_key = {codes[a]: a for a in top}
    rb, _, _, _, _, _ = pk.stats([seq], true_key, lm)
    sb = [pk.stats([seq], k2, lm)[0] for k2 in pk.shuffled_keys(true_key, 200, 1)]
    p95 = sorted(sb)[int(round(0.95 * 199))]
    assert rb > p95, (rb, p95)
    wrong = dict(zip(true_key, rng.sample(list(true_key.values()), len(true_key))))
    wb = pk.stats([seq], wrong, lm)[0]
    assert wb <= p95 or wrong == true_key, (wb, p95)
    print(f"ok: true partial key bigram {rb:.3f} > shuffled-key p95 {p95:.3f}; a wrong assignment {wb:.3f} is not flagged")


if __name__ == "__main__":
    main()
    print("all ok")
