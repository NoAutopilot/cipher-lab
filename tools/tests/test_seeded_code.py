#!/usr/bin/env python3
"""Offline test for tools/families/seeded_code.py (A2-CAS8, 2 Oct 2026). No network; a small Italian-like corpus built
in memory. Checks: (1) make_control returns N tokens in the target's message lengths, K codes, pinned tokens carry
"code=value" and the pinned share is at least the requested share; (2) solve keeps every pinned token's value and
score_recovery ignores pinned positions (a decode equal to the truth reads 1.0, one with every unpinned entry wrong
reads 0.0); (3) with pinshare=0.95 on a tiny repetitive text the solver reads better than a random-vocabulary floor;
(4) the same with --param lm=entry (entry-bigram scorer, A2-CAS9, 3 Oct 2026).
Run: python3 tools/tests/test_seeded_code.py"""
import os, random, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from families import seeded_code as sc  # noqa: E402

WORDS = ("il re di francia ha detto al ministro che la conferenza della spagna sopra le isole sarà tenuta presso "
         "il duca prima del ritorno del conte e il signore ambasciatore desidera sapere quale sia il favore").split()


def corpus(seed, n):
    r = random.Random(seed)
    return " ".join(r.choice(WORDS) for _ in range(n))


def main():
    corp = [corpus(1, 30000), corpus(2, 3000)]
    target = [[str(i % 90 + 1) for i in range(150)], [str(i % 70 + 5) for i in range(100)]]
    P = {"N": 250, "K": 60, "lengths": [150, 100], "target_msgs": target, "pinshare": "0.5", "words": "10",
         "iters": "3000"}
    msgs, truth, train = sc.make_control({}, 1, corp, dict(P))
    assert [len(m) for m in msgs] == [150, 100]
    toks = [t for m in msgs for t in m]
    assert sum("=" in t for t in toks) >= 0.5 * len(toks)
    assert len(truth.split("|")) == 250
    dec, s, info = sc.solve(msgs, {}, 1, 1, train, dict(P))
    for t, d in zip(toks, dec.split("|")):
        if "=" in t:
            assert d == "=" + t.split("=", 1)[1], (t, d)
    assert sc.score_recovery(truth, truth) == 1.0
    wrong = "|".join(x if x.startswith("=") else "zzz" for x in truth.split("|"))
    assert sc.score_recovery(wrong, truth) == 0.0
    P2 = dict(P, pinshare="0.95")
    msgs2, truth2, train2 = sc.make_control({}, 2, corp, dict(P2))
    dec2, _, _ = sc.solve(msgs2, {}, 2, 1, train2, dict(P2))
    rec = sc.score_recovery(dec2, truth2)
    print(f"pinned recovery on the tiny control: {rec:.2f}")
    assert rec >= 0.15, rec  # a random draw from the ~50-entry vocabulary reads about 0.02
    # (4) lm=entry (A2-CAS9, 3 Oct 2026): pinned values kept, and the entry-bigram solver beats the same floor
    P3 = dict(P2, lm="entry")
    dec3, _, info3 = sc.solve(msgs2, {}, 2, 1, train2, dict(P3))
    assert info3["lm"] == "entry"
    for t, d in zip([t for m in msgs2 for t in m], dec3.split("|")):
        if "=" in t:
            assert d == "=" + t.split("=", 1)[1], (t, d)
    rec3 = sc.score_recovery(dec3, truth2)
    print(f"pinned recovery on the tiny control, lm=entry: {rec3:.2f}")
    assert rec3 >= 0.15, rec3
    print("test_seeded_code: ok")


if __name__ == "__main__":
    main()
