#!/usr/bin/env python3
"""Gap 1, GAPS200 (3 Oct 2026): topic crib against ad 1 under a v-z-capable component rule family.

Pre-registered in PREREG-GAPS200.md (commit 34dc70a4) before scoring. Family: letter = alpha_n[(a*S + b*P + c) mod n],
a, b, c in 0..n-1, n in {26, 25 (I=J), 24 (I=J, U=V)}, paren sign S in {0, 4}: 97,806 rules. Statistic F = max over the
family and GAPS174's 29 crib windows of positional matches. Controls A shuffled-sign, B random-sign (1000 each);
power P1 exact / P2 3-of-10 wrong synthetic positives (1000 each). Deterministic (seed 200).
Usage: python3 vz_family_crib.py [--out vz_family_crib.tsv]
"""
import argparse, os, random, sys
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from laura_rule import CELLS
from topic_crib import SIGNS, C1465, PARA, windows

ALPHA = {26: "abcdefghijklmnopqrstuvwxyz", 25: "abcdefghiklmnopqrstuvwxyz", 24: "abcdefghiklmnopqrstuwxyz"}
CONV = (0, 4)


def fold(w, n):
    if n <= 25: w = w.replace("j", "i")
    if n == 24: w = w.replace("v", "u")
    return w


CRIB = sorted(set(windows(C1465) + [w for p in PARA for w in windows(p)]))
WIN = {n: np.array([[ALPHA[n].index(ch) for ch in fold(w, n)] for w in CRIB]) for n in ALPHA}
GRID = {n: np.arange(n) for n in ALPHA}


def F(signs, detail=False):
    best, arg = -1, None
    P = np.array([p for _, p in signs])
    for n in ALPHA:
        ar = GRID[n]
        for pc in CONV:
            S = np.array([pc if s == 0 else s for s, _ in signs])
            # d[a,b,w,i] = (W - a S_i - b P_i) mod n ; max over c of count(d == c)
            base = (ar[:, None, None] * S[None, None, :] + ar[None, :, None] * P[None, None, :]) % n  # a,b,i
            d = (WIN[n][None, None, :, :] - base[:, :, None, :]) % n  # a,b,w,i
            cnt = (d[..., None] == ar).sum(axis=3)  # a,b,w,c
            m = int(cnt.max())
            if m > best:
                best = m
                if detail:
                    a, b, w, c = np.unravel_index(cnt.argmax(), cnt.shape)
                    arg = (n, pc, int(a), int(b), int(c), CRIB[w])
    return (best, arg) if detail else best


def decode(signs, n, pc, a, b, c):
    return "".join(ALPHA[n][(a * (pc if s == 0 else s) + b * p + c) % n] for s, p in signs)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "vz_family_crib.tsv"))
    ap.add_argument("--reps", type=int, default=1000)
    o = ap.parse_args(); R = o.reps
    rng = random.Random(200)
    ft, (n, pc, a, b, c, bw) = F(SIGNS, detail=True)
    xs = decode(SIGNS, n, pc, a, b, c)
    A = []
    for _ in range(R):
        s2 = SIGNS[:]; rng.shuffle(s2); A.append(F(s2))
    B = [F([rng.choice(CELLS) for _ in range(10)]) for _ in range(R)]
    P1, P2 = [], []
    while len(P1) < R:
        n2 = rng.choice(list(ALPHA)); pc2 = rng.choice(CONV)
        a2, b2, c2 = (rng.randrange(n2) for _ in range(3)); w = fold(rng.choice(CRIB), n2)
        cells = {}
        for cl in CELLS:
            cells.setdefault(decode([cl], n2, pc2, a2, b2, c2), []).append(cl)
        if not all(ch in cells for ch in w):
            continue
        sg = [rng.choice(cells[ch]) for ch in w]
        P1.append(F(sg))
        for i in rng.sample(range(10), 3):
            sg[i] = rng.choice(CELLS)
        P2.append(F(sg))
    q = lambda v: sorted(v)[int(0.95 * len(v))]
    ap95, bp95 = q(A), q(B)
    pw1 = sum(m > bp95 for m in P1) / R; pw2 = sum(m > bp95 for m in P2) / R
    if pw2 < 0.5 or bp95 >= 10:
        dec = "untestable by this instrument at N=10"
    elif ft > ap95 and ft > bp95:
        dec = "topic crib supported under the v-z family"
    else:
        dec = "crib set not read under the v-z component family"
    rows = [("rules", 2 * sum(k ** 3 for k in ALPHA)), ("crib_windows", len(CRIB)), ("F_target", ft),
            ("best_rule", f"n={n} paren_S={pc} a={a} b={b} c={c}"), ("best_window", bw), ("decoded_under_best", xs),
            ("A_p95", ap95), ("A_tail", sum(m >= ft for m in A) / R), ("B_p95", bp95), ("B_tail", sum(m >= ft for m in B) / R),
            ("A_dist", dict(sorted({k: A.count(k) for k in set(A)}.items()))),
            ("B_dist", dict(sorted({k: B.count(k) for k in set(B)}.items()))),
            ("P1_median", sorted(P1)[R // 2]), ("P1_power", pw1), ("P2_median", sorted(P2)[R // 2]), ("P2_power", round(pw2, 3)),
            ("decision", dec)]
    with open(o.out, "w") as f:
        f.write("item\tvalue\n")
        for k, v in rows:
            f.write(f"{k}\t{v}\n")
    print(open(o.out).read())


if __name__ == "__main__":
    main()
