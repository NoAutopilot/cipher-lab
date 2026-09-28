#!/usr/bin/env python3
"""Offline test for tools/families/homophonic.py's wild=<sign> solver option (H25, 28 Sept 2026). No network; one
short anneal. Builds a merge=4 nulls=0.15 control at N=240 K=20 from the Holmes corpus (the merged sign is sM) and
solves it twice with 2 restarts and 8000 iterations: without wild, and with wild=sM. Must catch: with wild=sM the
decode is still N letters long, the merged sign's positions are read as at least two different letters (a
per-position letter, not one letter for the whole sign), the info dict carries wild_letters for sM, and no
pseudo-sign leaks into info["key"]. Must NOT change: params without wild give the old (score, key) shape, and every
sM position reads as ONE letter there. Recovery numbers are printed, not asserted (an 8000-iteration anneal is not a
calibration). Run: python3 tools/tests/test_homophonic_wild.py"""
import os, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, os.path.join(ROOT, "tools", "families"))
import judge_plaintext as jp  # noqa: E402
from families import homophonic as hf  # noqa: E402


def main():
    corpora = [jp.read_corpus(os.path.join(ROOT, "tools", "data", "pg1661_holmes.txt"))]
    N, K = 240, 20
    toks = ["HOOK"] * 50 + [f"t{i}" for i in range(19) for _ in range(10)]
    base = {"N": N, "K": K, "target_msgs": [toks], "merge": "4", "nulls": "0.15", "iters": "8000"}
    cm, plain, train = hf.make_control({}, 11, corpora, dict(base))
    seq = cm[0]
    assert "sM" in seq
    dec0, sc0, info0 = hf.solve(cm, {}, 11, 2, train, dict(base))
    assert len(dec0) == N and "wild_letters" not in info0
    l0 = {dec0[i] for i, x in enumerate(seq) if x == "sM"}
    assert len(l0) == 1, l0
    dec1, sc1, info1 = hf.solve(cm, {}, 11, 2, train, dict(base, wild="sM"))
    assert len(dec1) == N
    l1 = Counter(dec1[i] for i, x in enumerate(seq) if x == "sM")
    assert len(l1) >= 2, l1
    assert "sM" in info1["wild_letters"] and all("#" not in k for k in info1["key"])
    r0, r1 = hf.score_recovery(dec0, plain), hf.score_recovery(dec1, plain)
    print(f"ok: wild=sM reads the merged sign as {len(l1)} letters {dict(l1)}; recovery no-wild {r0:.3f} wild {r1:.3f} "
          f"(8000 iters, 2 restarts -- shape test, not a calibration)")


if __name__ == "__main__":
    main()
    print("all ok")
