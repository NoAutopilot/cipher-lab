#!/usr/bin/env python3
"""Gap 1, GAPS160 (3 Oct 2026): Laura's bars-x-dots component rule on ad 1, with matched N=10 controls.

Pre-registered in NOTES.md ("GAPS160 ... gap 1 component test") before scoring (commit 577aeea6).
Rule: letter = alphabet[(S-1)*6 + P - 1] for S bars/dashes, P dots; parenthesised k dots = s/t/u.
Statistic T: mean add-one bigram log10 prob of "timeto"+X+"shall"; W: word-segmentation coverage of X.
Controls: A shuffled-sign, B random-sign, C 104 sibling rules, plus a positive control for power.
Deterministic (seed 160). Usage: python3 laura_rule.py [--out laura_rule.tsv] [--right shall]
GAPS178 (3 Oct 2026): --right ishall re-scores with the 1881 print's frame "I shall" (PREREG-GAPS178 in NOTES.md).
"""
import argparse, math, os, random, re
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SOURCES = ["tools/data/pg1661_holmes.txt", "tools/data/en/pg76_huckfinn.txt",
           "tools/data/en/pg1342_pride.txt", "tools/data/en/pg64317_gatsby.txt"]
L = "abcdefghijklmnopqrstuvwxyz"
# (S, P) per sign; S=0 marks a parenthesised dot group. Sign table: ciphertext.txt.
OURS = [(1, 2), (1, 5), (3, 2), (1, 3), (1, 1), (1, 2), (0, 3), (1, 3), (2, 2), (3, 4)]
LAURA = [(1, 2), (1, 5), (3, 2), (1, 4), (1, 1), (1, 2), (0, 3), (1, 3), (2, 2), (3, 4)]
CELLS = [(s, p) for s in (1, 2, 3) for p in range(1, 7)] + [(0, 1), (0, 2), (0, 3)]


def idx(sp, order="S"):
    s, p = sp
    if s == 0:
        return 18 + p - 1
    return (s - 1) * 6 + p - 1 if order == "S" else (p - 1) * 3 + s - 1


def rule(signs, order="S", rev=False, shift=0):
    out = []
    for sp in signs:
        i = (idx(sp, order) + shift) % 26
        out.append(L[25 - i] if rev else L[i])
    return "".join(out)


def load():
    txt = ""
    for f in SOURCES:
        txt += open(os.path.join(ROOT, f), encoding="utf-8", errors="ignore").read().lower() + " "
    words = re.findall(r"[a-z]+", txt)
    return "".join(words), Counter(words)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "laura_rule.tsv"))
    ap.add_argument("--right", default="shall", help="right-hand clear frame (GAPS178: ishall)")
    a = ap.parse_args()
    rng = random.Random(160)
    letters, wc = load()
    bg = Counter(letters[i:i + 2] for i in range(len(letters) - 1)); uni = Counter(letters)
    lp = {x + y: math.log10((bg[x + y] + 1) / (uni[x] + 26)) for x in L for y in L}
    vocab = {w for w, c in wc.items() if c >= 5 and (len(w) >= 2 or w in ("a", "i"))}

    def T(x):
        s = "timeto" + x + a.right
        return sum(lp[s[i:i + 2]] for i in range(len(s) - 1)) / (len(s) - 1)

    def W(x):
        best = [0] * (len(x) + 1)
        for j in range(1, len(x) + 1):
            best[j] = best[j - 1]
            for i in range(max(0, j - 12), j):
                if x[i:j] in vocab:
                    best[j] = max(best[j], best[i] + j - i)
        return best[-1] / len(x)

    def p95(v):
        v = sorted(v); return v[int(0.95 * len(v))]

    rows = []
    for name, signs in (("target-ours", OURS), ("target-laura", LAURA)):
        x = rule(signs)
        A = []
        for _ in range(2000):
            s2 = signs[:]; rng.shuffle(s2); A.append(rule(s2))
        B = [rule([rng.choice(CELLS) for _ in range(10)]) for _ in range(2000)]
        fam = [rule(signs, o, r, sh) for o in "SP" for r in (False, True) for sh in range(26)]
        tA, tB, tC = [T(y) for y in A], [T(y) for y in B], [T(y) for y in fam]
        wA, wB = [W(y) for y in A], [W(y) for y in B]
        rankC = 1 + sum(1 for t in tC if t > T(x))
        rows.append((name, x, T(x), p95(tA), sum(t >= T(x) for t in tA) / 2000, p95(tB),
                     sum(t >= T(x) for t in tB) / 2000, rankC, len(fam), W(x), p95(wA), p95(wB), tB, wB))
    # positive control: corpus windows restricted to a-u (encodable), identity under the rule
    enc = set(L[:21]); pos = []
    while len(pos) < 2000:
        i = rng.randrange(len(letters) - 10); w = letters[i:i + 10]
        if set(w) <= enc:
            pos.append(w)
    tP, wP = [T(y) for y in pos], [W(y) for y in pos]
    tB, wB = rows[0][12], rows[0][13]
    powT = sum(t > p95(tB) for t in tP) / 2000; powW = sum(w > p95(wB) for w in wP) / 2000
    medP = sorted(tP)[1000]
    with open(a.out, "w") as f:
        f.write("text\tX\tT\tA_p95\tA_tail\tB_p95\tB_tail\tC_rank\tC_n\tW\tWA_p95\tWB_p95\n")
        for r in rows:
            f.write("\t".join(str(round(v, 4)) if isinstance(v, float) else str(v) for v in r[:12]) + "\n")
        f.write(f"positive\tcorpus a-u windows\tmedian {medP:.4f}\tpowerT {powT:.3f}\t\tpowerW {powW:.3f}\n")
    print(open(a.out).read())


if __name__ == "__main__":
    main()
