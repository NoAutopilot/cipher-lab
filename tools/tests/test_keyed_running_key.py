#!/usr/bin/env python3
"""Offline test for tools/families/keyed_running_key.py and running_key.mixed_tabula (GOLD-2C, 25 Sept 2026; under
90 s, no network). (1) every mixed tabula (4 modes x 3 arithmetics) inverts: key_of(encipher(p, k)) == k, and the
empty keyword reduces to the standard tableau; (2) an English control -- a Holmes passage (3 messages of 300 letters)
under a Moby-Dick running key through a keyword-mixed square (mode full) -- has its keyword ranked in the top 3 by
stage 1 among ~1200 candidates and is selected by stage 2 and read above the 1/26 chance level with small models (order 5, beam 100), the passages
held out of the models; (3) family_run.py lists the family. Run: python3 tools/tests/test_keyed_running_key.py"""
import os, subprocess, sys, time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(HERE)
sys.path.insert(0, TOOLS)
import running_key as rk  # noqa: E402
import families  # noqa: E402

DATA = os.path.join(TOOLS, "data")


def main():
    t0 = time.time()
    for mode in rk.MIXED_MODES:
        for ar in ("vig", "beau", "varbeau"):
            t = rk.mixed_tabula("gentleman", mode, ar)
            for p in range(26):
                for k in range(26):
                    assert rk.key_of(t, p, rk.encipher(t, p, k)) == k, (mode, ar, p, k)
    t = rk.mixed_tabula("", "full", "vig")
    assert all(rk.encipher(t, p, k) == rk.encipher("vig", p, k) for p in range(26) for k in range(26))
    assert rk.keyword_alphabet("koehler") == "koehlrabcdfgijmnpqstuvwxyz"

    fam = families.load("keyed_running_key")
    holmes = rk.read_text(os.path.join(DATA, "pg1661_holmes.txt"))
    moby = rk.read_text(os.path.join(DATA, "pg2701_mobydick.txt"))
    hf, mf = rk.fold(holmes), rk.fold(moby)
    P = [hf[200000 + i * 300:200300 + i * 300] for i in range(3)]
    K = [mf[300000 + i * 300:300300 + i * 300] for i in range(3)]
    tab = rk.mixed_tabula("gentleman", "full", "vig")
    msgs = [[rk.A[rk.encipher(tab, rk.IDX[a], rk.IDX[b])] for a, b in zip(p, k)] for p, k in zip(P, K)]
    ptrain = [holmes[:len(holmes) // 3], holmes[len(holmes) * 2 // 3:]]   # the passage sits in the middle third
    ktrain = [moby[:len(moby) // 4], moby[len(moby) // 2:]]
    params = {"N": 900, "K": 26, "lengths": [300, 300, 300], "target_msgs": msgs, "messages_independent": True,
              "order": "5", "beam": "100", "top": "3", "nwords": "300", "spaces": "1"}
    a = fam._p(params)
    words = fam.word_list([holmes, moby], a)
    assert "gentleman" in words and len(words) > 300, len(words)
    counts = Counter("".join("".join(m) for m in msgs))
    ranked = fam.stage1([counts.get(x, 0) for x in rk.A], fam.unigram(ptrain), fam.unigram(ktrain), words, a)
    pos = next(i + 1 for i, row in enumerate(ranked) if (row[1], row[2]) == ("gentleman", "full"))
    assert pos <= 3, (pos, ranked[:5])
    fam._STATE.update({"ktrain": ktrain, "words": words, "truth": ("gentleman", "full")})
    dec, score, info = fam.solve(msgs, None, 1, 1, ptrain, dict(params))
    rec = fam.score_recovery(dec, "".join(P))
    assert info["tabula"] == "mixed:gentleman:full:vig", info["tabula"]
    # small models (a third of Holmes, order 5, beam 100): the right tableau is selected; recovery is well above
    # the 1/26 chance level but not the 50% a full-size model reads (GOLD-2A control 60-79% at order 8, beam 1000)
    assert rec > 0.15, (rec, dec[:60], P[0][:60])
    assert not fam._STATE, fam._STATE  # solve() consumed the control state
    r = subprocess.run([sys.executable, os.path.join(TOOLS, "family_run.py"), "--help"], capture_output=True, text=True)
    assert "keyed_running_key" in r.stdout, r.stdout[-500:]
    print(f"ok keyed_running_key: tabula algebra 12/12, stage 1 rank {pos} of {len(ranked)}, stage 2 recovery {rec:.3f}, "
          f"score {score:.3f}; {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
