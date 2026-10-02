"""Offline test for tools/families/phased_homophonic.py (BIRAGO-NUM3, 2 Oct 2026). Under a minute, no network.
Must catch: a control whose runs do not match the target's lengths, a pair straddling a run break, a recovery that
credits a misphased pair, and a solver that cannot read an easy (20-cell, no-stray) control. Must NOT change: the
other families (registry only gains a name)."""
import os, sys, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import glob
import families
import judge_plaintext as jp
from families import phased_homophonic as f

TEXT = ("la maesta del re ha mandato a dire al signor duca che le genti sono partite di turino et che il marescial "
        "sara qui fra pochi giorni con la compagnia per la guardia della citta et del castello et che si debbe "
        "provedere alle munitioni et alle paghe de soldati che sono molto mal contenti per la tardanza ") * 40


def main():
    assert "phased_homophonic" in families.REGISTRY
    rng = random.Random(3)
    lengths = [rng.randrange(1, 60) for _ in range(30)]
    target = [[str(rng.choice("01234589")) for _ in range(L)] for L in lengths]
    params = {"lengths": lengths, "target_msgs": target, "cells": "20", "strays": "0.0"}
    msgs, truth, train = f.make_control({}, 1, [TEXT], dict(params))
    corp = [jp.read_corpus(p) for p in sorted(glob.glob(os.path.join(os.path.dirname(HERE), "data", "it16dip", "*.txt.gz")))]
    assert [len(m) for m in msgs] == lengths, "control runs must take the target's own lengths"
    assert all(set("".join(m)) <= set("01234589") for m in msgs), "control uses only the target's own digits"
    p = 0
    for m in msgs:  # no pair straddles a break: a run never ends on a letter whose '.' would be in the next run
        seg = truth[p:p + len(m)]
        assert not seg.startswith("."), "pair straddles a run break"
        p += len(m)
    # misphased decode gets no credit
    shifted = "-" + truth[:-1]
    assert f.score_recovery(truth, truth) == 1.0
    assert f.score_recovery(shifted, truth) < 0.2
    msgs, truth, train = f.make_control({}, 1, corp, dict(params, strays="0.05"))
    dec, sc, info = f.solve(msgs, {}, 1, 4, train, dict(params, iters="40000", iters2="10000"))
    rec = f.score_recovery(dec, truth)
    print("easy control recovery", round(rec, 3), "types", info["types"])
    assert rec > 0.7, rec
    assert len(f.split_decode(dec, msgs)) == len(msgs)
    print("ok")


if __name__ == "__main__":
    main()
