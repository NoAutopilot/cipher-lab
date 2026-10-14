"""Offline test for tools/families/transposition.py (FAIR-TRANS, 14 Oct 2026). No network.
Checks: every route permutation is a permutation; a keyed columnar (both orientations), a rail fence, a spiral and a
reversed boustrophedon of a known English window are read back exactly; the `?` mask lands at the target's position.
Run: python3 tools/tests/test_transposition_family.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import numpy as np  # noqa: E402
from families import transposition as T  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
corp = [open(os.path.join(ROOT, "tools/data/en/pg1342_pride.txt"), encoding="utf-8", errors="ignore").read()]
for name, p in T.route_perms(67, 34):
    assert sorted(p.tolist()) == list(range(67)), name
params = {"N": 67, "K": 0, "target_msgs": [list("ces?" + "a" * 63)], "iters": "4000"}
for seed, design in [(1, "colK:6"), (2, "colKi:9"), (3, "rail:3"), (4, "spiral:8"), (5, "boustro:5 rev")]:
    params["ctrl_designs"] = design
    msgs, plain, train = T.make_control({}, seed, corp, params)
    assert msgs[0][3] == "?" and msgs[0].count("?") == 1
    dec, sc, info = T.solve(msgs, {}, seed, 4, train, params)
    rec = T.score_recovery(dec, plain)
    print(design, round(rec, 3), info["best"])
    assert rec >= 0.9, (design, rec, dec, plain)
print("ok")
