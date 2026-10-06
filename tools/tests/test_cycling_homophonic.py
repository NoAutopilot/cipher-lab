#!/usr/bin/env python3
"""Offline test for tools/families/cycling_homophonic.py (R11-SCORPCYC, 6 Oct 2026). No network, about a minute.
Must catch: a control that is not cyclic (each letter's signs must repeat with period = its homophone count), a
violation count that is not zero on the true key or that misses a broken cycle, and a solver that cannot read an
easy cycling control (N=400, K=40) or reads it worse with the cycle term on (lam=2) than off (lam=0).
Must NOT change: any other family (the registry only gains a name).
Run: python3 tools/tests/test_cycling_homophonic.py"""
import os, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import judge_plaintext as jp  # noqa: E402
import families  # noqa: E402
from families import cycling_homophonic as f  # noqa: E402


def main():
    assert "cycling_homophonic" in families.REGISTRY
    corp = [jp.read_corpus(os.path.join(ROOT, "tools", "data", "pg1661_holmes.txt"))]
    params = {"N": 400, "K": 40, "target_msgs": [["x"] * 400], "lengths": [400]}
    msgs, plain, train = f.make_control({}, 1, corp, dict(params))
    seq = msgs[0]
    assert len(seq) == 400 and len(plain) == 400
    _, truth, homs = f.encipher(plain, 40, 1)
    assert f.violations(seq, truth) == 0, "true key must have no cycle violations"
    for a, ss in homs.items():  # every letter's signs cycle with period len(ss)
        got = [x for x, p in zip(seq, plain) if p == a]
        assert all(got[i] == got[i + len(ss)] for i in range(len(got) - len(ss))), a
    broken = list(seq)
    i, j = next((i, j) for i in range(400) for j in range(i + 1, 400)
                if plain[i] == plain[j] and seq[i] != seq[j] and Counter(seq)[seq[i]] > 1)
    broken[i], broken[j] = broken[j], broken[i]
    assert f.violations(broken, truth) > 0, "a swapped pair must break the cycle"
    assert f.score_recovery(plain, plain) == 1.0
    rec = {}
    for lam in ("0", "2.0"):
        dec, sc, info = f.solve(msgs, {}, 1, 4, train, dict(params, lam=lam, iters="30000"))
        rec[lam] = f.score_recovery(dec, plain)
        print("easy cycling control N=400 K=40 lam=%s recovery %.3f violations %d" % (lam, rec[lam], info["violations"]))
    assert rec["2.0"] > 0.8, rec
    assert rec["2.0"] >= rec["0"] - 0.02, rec
    print("ok")


if __name__ == "__main__":
    main()
