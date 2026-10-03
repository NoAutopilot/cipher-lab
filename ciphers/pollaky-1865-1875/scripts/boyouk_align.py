#!/usr/bin/env python3
"""Gap 2 (b), GAPS164 (3 Oct 2026): Boyouk's 1867 clear ad against ad 2's digit groups.

Pre-registered in NOTES.md ("GAPS164 ... Boyouk's clear ad against ad 2's groups", commit f065906d) before scoring.
Design: one group per chunk of 1-3 consecutive words, same chunk -> same group. S = log10 share of monotone
alignments in which the two '91' groups cover identical chunks (floor -12). Controls: same-length windows of period
English prose; positive control: synthetic chunk codes from fresh windows. Deterministic (seed 164).
Usage: python3 boyouk_align.py [--out boyouk_align.tsv] [--n-ctrl 2000] [--n-pos 200]
"""
import argparse, math, os, random, re
from functools import lru_cache

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
AD2 = ("56. 717. 9362. 81720. 19736. 14. 618. 9:77314. 390. 400. 272. 20 = 211. 59. 91. 881. 460. - 80. 401. "
       "70. 447 415. 91 437. . 801 10031. 874. 92. 871. 2391. 941. 72050. 67321. 438921. 150.")
CLEAR = ("ELOPED, from here home, at T….., a YOUNG LADY 17 years of age, middle sized, slim built, wavy auburn hair of "
         "a particular golden hue, high forehead and large brown (almost black) eyes. Was dressed, when leaving, in blue "
         "silk dress and black jacket, and is supposed to be in company with a young foreign gentleman. Information of "
         "there whereabouts to be given to Mr. Pollaky, Private Inquiry Office, 13, Paddington-green. W.")
SOURCES = ["tools/data/pg1661_holmes.txt", "tools/data/en/pg76_huckfinn.txt", "tools/data/en/pg1342_pride.txt"]
FLOOR, MAXL = -12.0, 3


def groups(text, split_colon=True):
    t = text if split_colon else text.replace(":", "")
    return [g for g in re.split(r"[\s.=:\-]+", t) if g]


def words(text):
    return re.findall(r"[a-z0-9]+", text.lower())


@lru_cache(maxsize=None)
def comp(g, n):
    """ways to cover n words with g groups of 1..MAXL words"""
    if g == 0:
        return 1 if n == 0 else 0
    if n < g or n > g * MAXL:
        return 0
    return sum(comp(g - 1, n - l) for l in range(1, MAXL + 1))


def stat(w, G, i, j):
    n, tot, hit = len(w), comp(G, len(w)), 0
    if tot == 0:
        return None
    for a in range(n):
        ca = comp(i, a)
        if not ca:
            continue
        for l in range(1, MAXL + 1):
            for b in range(0, n):
                cb = comp(j - i - 1, b)
                if not cb:
                    continue
                s2 = a + l + b
                if s2 + l > n or w[a:a + l] != w[s2:s2 + l]:
                    continue
                hit += ca * cb * comp(G - j - 1, n - s2 - l)
    return FLOOR if hit == 0 else max(FLOOR, math.log10(hit / tot))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "boyouk_align.tsv"))
    ap.add_argument("--n-ctrl", type=int, default=2000)
    ap.add_argument("--n-pos", type=int, default=200)
    a = ap.parse_args()
    rng = random.Random(164)
    corpus = []
    for s in SOURCES:
        corpus.append(words(open(os.path.join(ROOT, s), encoding="utf-8", errors="ignore").read())[1000:-3000])
    def window(n):
        c = rng.choice(corpus); k = rng.randrange(len(c) - n); return c[k:k + n]
    W = words(CLEAR)
    P1, P2 = W, W[:W.index("mr")]
    rows = [("text", "groups", "words", "pos_91", "S_target", "ctrl_p95", "ctrl_tail", "ctrl_floor_share",
             "power", "verdict")]
    for gname, sc in (("split", True), ("joined", False)):
        G = groups(AD2, sc)
        rep = [k for k, g in enumerate(G) if g == "91"]
        assert len(rep) == 2 and len(set(G)) == len(G) - 1, (G, rep)
        i, j = rep
        for pname, P in (("P1 whole ad", P1), ("P2 minus address", P2)):
            n = len(P)
            st = stat(P, len(G), i, j)
            ctrl = sorted(stat(window(n), len(G), i, j) for _ in range(a.n_ctrl))
            p95 = ctrl[int(0.95 * len(ctrl))]
            tail = sum(c >= st for c in ctrl) / len(ctrl)
            floor = sum(c == FLOOR for c in ctrl) / len(ctrl)
            # positive control: true chunk code with one repeated pair, gap nearest the target's
            hits = done = 0
            while done < a.n_pos:
                w = window(n)
                lens = None
                for _ in range(200):
                    L = [rng.randint(1, MAXL) for _ in range(len(G))]
                    if sum(L) == n:
                        lens = L; break
                if lens is None:
                    # rebalance a draw to sum n
                    L = [2] * len(G); d = n - sum(L); k = 0
                    while d:
                        s = 1 if d > 0 else -1
                        if 1 <= L[k % len(G)] + s <= MAXL:
                            L[k % len(G)] += s; d -= s
                        k += 1
                    rng.shuffle(L); lens = L
                ch, p = [], 0
                for l in lens:
                    ch.append(tuple(w[p:p + l])); p += l
                pairs = [(x, y) for x in range(len(ch)) for y in range(x + 1, len(ch)) if ch[x] == ch[y]]
                if not pairs:
                    continue
                x, y = min(pairs, key=lambda q: (abs((q[1] - q[0]) - (j - i)), rng.random()))
                sp = stat(w, len(G), x, y)
                nul = sorted(stat(window(n), len(G), x, y) for _ in range(200))
                hits += sp > nul[int(0.95 * len(nul))]; done += 1
            power = hits / a.n_pos
            if power < 0.5:
                v = "untestable by this statistic at this N (power < 0.5)"
            elif st > p95:
                v = "consistent beyond chance (no reading)"
            else:
                v = "control-backed negative under the chunk-code design"
            rows.append((pname, f"{len(G)} ({gname})", n, f"{i},{j}", f"{st:.3f}", f"{p95:.3f}", f"{tail:.3f}",
                         f"{floor:.3f}", f"{power:.3f}", v))
            print("\t".join(map(str, rows[-1])), flush=True)
    with open(a.out, "w") as f:
        f.write("\n".join("\t".join(map(str, r)) for r in rows) + "\n")


if __name__ == "__main__":
    main()
