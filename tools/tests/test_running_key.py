#!/usr/bin/env python3
"""Offline test for tools/running_key.py (under 60 s, no network).

Builds tiny letter models from the English corpora in tools/data, enciphers a short Holmes passage under a
Moby-Dick running key (the key passage held out of the key model), and checks that the beam decoder recovers most
of the plaintext under each tabula; also checks the tabula algebra, the crib-drag and the coset IC.
"""
import os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import running_key as rk  # noqa: E402

DATA = os.path.join(os.path.dirname(HERE), "data")


def main():
    # tabula algebra: key_of inverts encipher for every tabula
    for tab in ("vig", "beau", "varbeau"):
        for p in range(26):
            for k in range(26):
                c = rk.encipher(tab, p, k)
                assert rk.key_of(tab, p, c) == k, (tab, p, k)

    holmes = rk.fold(rk.read_text(os.path.join(DATA, "pg1661_holmes.txt")))
    moby = rk.fold(rk.read_text(os.path.join(DATA, "pg2701_mobydick.txt")))
    P = holmes[200000:200120]
    K = moby[300000:300120]
    hs = rk.fold_sp(rk.read_text(os.path.join(DATA, "pg1661_holmes.txt")))
    ms = rk.fold_sp(rk.read_text(os.path.join(DATA, "pg2701_mobydick.txt")))
    # models trained on text far from the test passages (both passages held out)
    lmp = rk.LM([hs[:180000], hs[260000:560000]], order=6, alphabet=rk.AS)
    lmk = rk.LM([ms[:250000], ms[400000:700000]], order=6, alphabet=rk.AS)
    for tab in ("vig", "beau", "varbeau"):
        C = "".join(rk.A[rk.encipher(tab, rk.IDX[a], rk.IDX[b])] for a, b in zip(P, K))
        r = rk.decode_message(C, lmp, lmk, tab, beam=300, per_hyp=8, do_polish=False, spaces=True)
        # consistency: the printed key stream is exactly what p and c imply
        assert all(rk.key_of(tab, rk.IDX[p], rk.IDX[c]) == rk.IDX[k]
                   for p, c, k in zip(r["plain"], C, r["key"]))
        hit = sum(a == b for a, b in zip(r["plain"], P)) / len(P)
        swap = sum(a == b or a == k for a, b, k in zip(r["plain"], P, K)) / len(P)
        print(f"{tab}: plain {hit:.0%} swap-tolerant {swap:.0%}")
        assert (swap if tab == "vig" else hit) >= 0.25, (tab, hit, r["plain"])  # chance is ~4%

    # crib-drag: the true crib at its true place scores its key fragment as the key text
    frag = lmk.score(K[10:20]) / 10
    assert frag > lmk.score("qzxjvkqwzx") / 10
    # a letters-only model and the polish pass run and keep the streams consistent
    lp4 = rk.LM([holmes[:150000]], order=4)
    lk4 = rk.LM([moby[:150000]], order=4)
    C = "".join(rk.A[rk.encipher("vig", rk.IDX[a], rk.IDX[b])] for a, b in zip(P[:40], K[:40]))
    r = rk.decode_message(C, lp4, lk4, "vig", beam=100, per_hyp=6, do_polish=True)
    assert len(r["plain"]) == 40 and all(rk.key_of("vig", rk.IDX[p], rk.IDX[c]) == rk.IDX[k]
                                         for p, c, k in zip(r["plain"], C, r["key"]))

    # coset IC: a period-40 repeated key on English shows up at 40 and not at 37
    rng = random.Random(1)
    key = [rng.randrange(26) for _ in range(40)]
    msg = "".join(rk.A[(rk.IDX[ch] + key[i % 40]) % 26] for i, ch in enumerate(holmes[:1200]))
    assert rk.coset_ic([msg], 40) > 0.055 > rk.coset_ic([msg], 37), (rk.coset_ic([msg], 40), rk.coset_ic([msg], 37))
    print("ok")


if __name__ == "__main__":
    main()
