#!/usr/bin/env python3
"""Offline test for tools/families/permuted_tableau.py (GOLD-B2D, 25 Sept 2026; under 30 s, no network).
(1) perm_tabula inverts for random S1, S2, S3 under vig/beau/varbeau (key_of(encipher(p, k)) == k) and the identity
tabula equals the standard vig tableau; (2) letters_correct counts exact and shift-aligned matches; (3) the sum-stream
proxy anneal recovers a random cipher-side permutation on an English control long enough to identify it (Holmes plain
x Moby-Dick key, 8000 letters, order 3, best of two chains, proxy tables from the rest of both books) -- at the Koehler length (924) the
same proxy cannot (measured in HYPOTHESES.md), which is the point of the number; (4) family_run.py lists the family.
Run: python3 tools/tests/test_permuted_tableau.py"""
import os, random, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(HERE)
sys.path.insert(0, TOOLS)
import running_key as rk  # noqa: E402
import families  # noqa: E402

DATA = os.path.join(TOOLS, "data")


def main():
    t0 = time.time()
    pt = families.load("permuted_tableau")
    rng = random.Random(7)
    for ar in ("vig", "beau", "varbeau"):
        S = [rng.sample(range(26), 26) for _ in range(3)]
        t = pt.perm_tabula(*S, arith=ar)
        for p in range(26):
            for k in range(26):
                assert rk.key_of(t, p, rk.encipher(t, p, k)) == k, (ar, p, k)
        assert t["alphabet"] == "".join(rk.A[c] for c in S[2])
    t = pt.perm_tabula(None, None, None, "vig")
    assert all(rk.encipher(t, p, k) == rk.encipher("vig", p, k) for p in range(26) for k in range(26))
    S3 = rng.sample(range(26), 26)
    assert pt.inverse(pt.inverse(S3)) == S3
    assert pt.letters_correct(S3, S3) == (26, 26, 0)
    shifted = [S3[(s + 3) % 26] for s in range(26)]
    e, bs, sh = pt.letters_correct(shifted, S3)
    assert bs == 26 and sh == 23 and e < 26, (e, bs, sh)

    holmes = rk.fold(rk.read_text(os.path.join(DATA, "pg1661_holmes.txt")))
    moby = rk.fold(rk.read_text(os.path.join(DATA, "pg2701_mobydick.txt")))
    N = 8000
    S = random.Random(N).sample(range(26), 26)
    tab = pt.perm_tabula(None, None, S, "vig")
    P, K = holmes[200000:200000 + N], moby[300000:300000 + N]
    msgs = [[rk.A[rk.encipher(tab, rk.IDX[x], rk.IDX[y])] for x, y in zip(P, K)]]
    ptrain, ktrain = [holmes[:150000], holmes[260000:]], [moby[:250000], moby[400000:]]
    counts = pt.sum_stream_counts(ptrain, ktrain, 3, 3, 1)
    proxy = pt.Proxy(msgs, pt.sum_table(counts, 3, 0.5), 3)
    cc = [msgs[0].count(x) for x in rk.A]
    start = pt.inverse(pt.sort_match_start(cc, pt.unigram(ptrain), pt.unigram(ktrain)))
    best = None
    for chain in range(2):   # best of two chains: sort-match start, then a uniform-random start
        s0 = start if chain == 0 else pt.inverse(random.Random(chain).sample(range(26), 26))
        inv, sc, ne, T0 = pt.anneal(proxy, s0, 20000, 6000, random.Random(N + chain))
        if best is None or sc > best[0]:
            best = (sc, inv, ne)
    sc, inv, ne = best
    e, bs, sh = pt.letters_correct(pt.inverse(inv), S)
    assert bs >= 22, (e, bs, sh, ne)
    assert sc >= proxy.score(pt.inverse(S)) - 1e-6, (sc, proxy.score(pt.inverse(S)))

    r = subprocess.run([sys.executable, os.path.join(TOOLS, "family_run.py"), "--help"], capture_output=True, text=True)
    assert "permuted_tableau" in r.stdout, r.stdout[-500:]
    print(f"ok permuted_tableau: tabula algebra 3/3 arithmetics, shift test, English N={N} proxy anneal S3 letters "
          f"{e}/26 exact {bs}/26 shifted after {ne} evals; {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
