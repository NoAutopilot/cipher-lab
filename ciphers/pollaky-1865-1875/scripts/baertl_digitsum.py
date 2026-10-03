#!/usr/bin/env python3
"""Gap 2 (c), GAPS169 (3 Oct 2026): Baertl's digit-sum rule on ad 2, with matched controls.

Pre-registered in NOTES.md ("GAPS169 ... gap 2 (c)") before scoring (commit 1ecd9062).
Rule: each digit group -> sum of its digits (27 -> 26), then a simple substitution value -> letter.
Statistic T: best mean add-one trigram log10 prob a fixed hill-climbing solver reaches (8 restarts x 1500 moves).
Null: same-shape uniform random digit strings. Positive: English windows sent through a random value map.
B: Baertl's own reading against same-length English windows. Deterministic (seed 169).
Usage: python3 baertl_digitsum.py [--out baertl_digitsum.tsv] [--null 200] [--pos 100]
"""
import argparse, math, os, random, re, statistics
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SOURCES = ["tools/data/pg1661_holmes.txt", "tools/data/en/pg76_huckfinn.txt",
           "tools/data/en/pg1342_pride.txt", "tools/data/en/pg64317_gatsby.txt"]
L = "abcdefghijklmnopqrstuvwxyz"
# ad 2's 36 groups as transcribed (ciphertext.txt; "9:77314" split, as GAPS164's 36-group form)
GROUPS = ("56 717 9362 81720 19736 14 618 9 77314 390 400 272 20 211 59 91 881 460 80 401 70 447 415 91 437 801 "
          "10031 874 92 871 2391 941 72050 67321 438921 150").split()
BAERTL = [int(x) for x in ("11 15 20 19 20 18 26 5 15 9 22 12 4 11 2 4 14 10 17 10 8 5 7 15 14 10 17 10 8 5 7 15 "
                           "10 10 14 9 5 19 11 16 15 14 14 19 27 6").split()]
READING = "namimplearyfundustothewastothebattsreingassilb"


def dsum(g):
    return sum(int(c) for c in g)


def fix27(seq):
    return [26 if v == 27 else v for v in seq]


def load():
    txt = ""
    for f in SOURCES:
        txt += open(os.path.join(ROOT, f), encoding="utf-8", errors="ignore").read().lower() + " "
    return "".join(re.findall(r"[a-z]+", txt))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "baertl_digitsum.tsv"))
    ap.add_argument("--null", type=int, default=200); ap.add_argument("--pos", type=int, default=100)
    a = ap.parse_args()
    rng = random.Random(169)
    letters = load()
    tri = Counter(letters[i:i + 3] for i in range(len(letters) - 2))
    bi = Counter(letters[i:i + 2] for i in range(len(letters) - 1))
    LP = {}
    for x in L:
        for y in L:
            d = bi[x + y] + 26
            for z in L:
                LP[x + y + z] = math.log10((tri[x + y + z] + 1) / d)

    def score(s):
        return sum(LP[s[i:i + 3]] for i in range(len(s) - 2)) / (len(s) - 2)

    def solve(seq, r):
        vals = sorted(set(seq))
        best = -99
        for _ in range(8):
            m = {v: r.choice(L) for v in vals}
            cur = score("".join(m[v] for v in seq))
            for _ in range(1500):
                v = r.choice(vals); old = m[v]; m[v] = r.choice(L)
                s = score("".join(m[x] for x in seq))
                if s >= cur:
                    cur = s
                else:
                    m[v] = old
            best = max(best, cur)
        return best

    ours = fix27([dsum(g) for g in GROUPS])
    # Baertl's 46-group shape: our groups with two inserted (copy shapes of groups 3-4) and groups 15-22 repeated
    shape_b = [len(g) for g in GROUPS[:3]] + [4, 5] + [len(g) for g in GROUPS[3:]]
    shape_b = shape_b[:24] + shape_b[16:24] + shape_b[24:]
    assert len(shape_b) == 46
    rows = []
    for name, seq, shape, dup in (("S1 our 36 sums (27->26)", ours, [len(g) for g in GROUPS], False),
                                  ("S2 Baertl's 46 (27->26)", fix27(BAERTL), shape_b, True)):
        n = len(seq); t = solve(seq, random.Random(rng.random()))
        null = []
        for _ in range(a.null):
            gs = ["".join(rng.choice("0123456789") for _ in range(k)) for k in shape]
            s = fix27([dsum(g) for g in gs])
            if dup:  # same duplicated run as Baertl's sequence
                s = s[:24] + s[16:24] + s[32:]
            null.append(solve(s, random.Random(rng.random())))
        pool = sorted(set(seq)); pos = []
        for _ in range(a.pos):
            i = rng.randrange(len(letters) - n); w = letters[i:i + n]
            if dup:
                w = w[:24] + w[16:24] + w[32:]
            mp = dict(zip(L, rng.sample(range(min(pool), max(pool) + 1 + 30), 26)))
            pos.append(solve([mp[c] for c in w], random.Random(rng.random())))
        null.sort(); p95 = null[int(0.95 * len(null)) - 1]
        tail = sum(x >= t for x in null) / len(null)
        power = sum(x > p95 for x in pos) / len(pos)
        nm, pm = statistics.median(null), statistics.median(pos)
        if pm - nm < 0.05:
            verdict = "non-test (null at positive ceiling)"
        elif power < 0.5:
            verdict = "untestable (power < 0.5)"
        else:
            verdict = "supported" if t > p95 else "not supported"
        rows.append((name, n, len(set(seq)), f"{t:.4f}", f"{p95:.4f}", f"{tail:.3f}", f"{nm:.4f}", f"{pm:.4f}",
                     f"{power:.3f}", verdict))
    # B: Baertl's reading as text, against same-length English windows
    n = len(READING); b = score(READING)
    eng = sorted(score(letters[i:i + n]) for i in (rng.randrange(len(letters) - n) for _ in range(200)))
    p05 = eng[int(0.05 * len(eng))]
    rows.append(("B Baertl's reading as text", n, "", f"{b:.4f}", f"real-English p05 {p05:.4f}",
                 f"{sum(x <= b for x in eng) / len(eng):.3f}", f"{statistics.median(eng):.4f}", "", "",
                 "inside English" if b >= p05 else "below English p05"))
    hdr = "seq\tN\tK\tT\tnull_p95\ttail\tnull_med\tpos_med\tpower\tverdict"
    with open(a.out, "w") as f:
        f.write(hdr + "\n" + "\n".join("\t".join(map(str, r)) for r in rows) + "\n")
    print(hdr); [print("\t".join(map(str, r))) for r in rows]


if __name__ == "__main__":
    main()
