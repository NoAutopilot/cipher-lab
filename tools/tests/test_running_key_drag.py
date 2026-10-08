#!/usr/bin/env python3
"""Offline test for tools/running_key.py --drag (TT-DRAG, 8 Oct 2026; Tomokiyo runningkey.htm, Brown's dictionary drag).

Must catch: a long word of the plaintext (or of the key) at its true offset when the key is a book text (vig: the word is
found whichever side it sits on; beau: role 'key' finds a key-side word). Must NOT flag: the same plaintext word when the
key is a uniform random one-time key or a short periodic key (bcdefg, the hessen-1824 design) -- the true word then
ranks like a decoy. Offline, under 60 s; corpora from tools/data (Holmes, Moby-Dick), test windows held out of the model.
"""
import os, random, re, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import running_key as rk  # noqa: E402

DATA = os.path.join(os.path.dirname(HERE), "data")


def toks(path):
    return [w for w in (rk.fold(t) for t in re.findall(r"[^\W\d_]+", rk.read_text(path))) if w]


def window(tk, start, n):
    s, i, longs = "", start, []
    while len(s) < n:
        if len(tk[i]) >= 10 and len(s) + len(tk[i]) <= n:
            longs.append((len(s), tk[i]))
        s += tk[i]
        i += 1
    return s[:n], longs


def run(tmp, C, P, K, cribs, lm, extra=()):
    f = lambda n, t: (open(os.path.join(tmp, n), "w").write(t + "\n"), os.path.join(tmp, n))[1]
    argv = [f("c.txt", C), "--drag", "10", "--drag-cribs", f("cribs.txt", "\n".join(cribs)), "--pcorpus", lm,
            "--top", "20", "--truth", f("p.txt", P), f("k.txt", K), *extra]
    rows = rk.main(argv)["rows"]
    return next((i + 1 for i, r in enumerate(rows) if r["true"] == "yes"), None), rows


def main():
    ht, mt = toks(os.path.join(DATA, "pg1661_holmes.txt")), toks(os.path.join(DATA, "pg2701_mobydick.txt"))
    n = 150
    start = next(i for i in range(30000, len(ht)) if window(ht, i, n)[1])
    P, plongs = window(ht, start, n)
    kstart = next(i for i in range(60000, len(mt)) if window(mt, i, n)[1])
    K, klongs = window(mt, kstart, n)
    decoys = sorted({w for w in ht[:20000] + mt[:20000] if len(w) >= 10})[:400]
    cribs = sorted(set(decoys) | {w for _, w in plongs + klongs})
    with tempfile.TemporaryDirectory() as tmp:
        lm = os.path.join(tmp, "lm.txt")
        open(lm, "w").write(" ".join(ht[:25000] + mt[:40000]))   # both test windows lie outside the model text
        enc = lambda tab, key: "".join(rk.A[rk.encipher(tab, rk.IDX[a], rk.IDX[b])] for a, b in zip(P, key))
        # 1. catch: book key under vig, true words of either stream rank at the top
        first, rows = run(tmp, enc("vig", K), P, K, cribs, lm)
        print("vig book key: first true rank", first, rows[0]["word"], rows[0]["pos"])
        assert first is not None and first <= 3, first
        # 2. catch under beau: a key-side word is found with role 'key' (its fragment is the plaintext)
        first, rows = run(tmp, enc("beau", K), P, K, cribs, lm, ("--tabula", "beau"))
        hit = [r for r in rows if r["true"] == "yes"]
        print("beau book key: first true rank", first, [(r["word"], r["role"]) for r in hit[:3]])
        assert first is not None and first <= 5, first
        assert all(r["role"] in ("plain", "key") for r in rows)
        for r in hit:   # the role and fragment are consistent with the truth
            lo = r["pos"]
            assert (r["role"] == "plain" and r["word"] == P[lo:lo + len(r["word"])] and r["fragment"] == K[lo:lo + len(r["word"])]) or \
                   (r["role"] == "key" and r["word"] == K[lo:lo + len(r["word"])] and r["fragment"] == P[lo:lo + len(r["word"])]), r
        # 3. must NOT flag: random one-time key and short periodic key -- the plaintext words rank like decoys
        rng = random.Random(3)
        R = "".join(rng.choice(rk.A) for _ in range(n))
        per = ("bcdefg" * 40)[:n]
        for name, key in (("random key", R), ("periodic bcdefg", per)):
            first, rows = run(tmp, enc("vig", key), P, key, cribs, lm)
            print(f"{name}: first true rank", first)
            assert first is None or first > 10, (name, first)
    # NgramTable scores agree with the LM it was built from
    lm4 = rk.LM([" ".join(ht[:5000])], order=4)
    import numpy as np
    t = rk.NgramTable(lm4)
    s = "thequickbrownfox"
    v = t.score_rows(np.array([[rk.IDX[c] for c in s]]))[0]
    assert abs(v - lm4.score(s)) < 1e-6, (v, lm4.score(s))
    print("ok")


if __name__ == "__main__":
    main()
