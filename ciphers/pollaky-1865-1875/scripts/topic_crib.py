#!/usr/bin/env python3
"""Gap 1, GAPS174 (3 Oct 2026): topic crib from sibling clear ad Clay 1465 against ad 1 under Laura's rule.

Pre-registered in NOTES.md ("GAPS174 ... topic-crib test") before scoring (commit 587ce6ea).
Sign 04 = 1 dash + 4 dots, from the 1881 print (Clay item 1459, IA leaf n280). Statistic M: max positional matches of X
against any 10-letter word-start window of the crib set. Controls A shuffled-sign, B random-sign, C 104 sibling rules;
positives P1 exact crib, P2 crib with 3 letters replaced. Descriptive: ABCDEAFGHI pattern fit share.
Deterministic (seed 174). Usage: python3 topic_crib.py [--out topic_crib.tsv]
"""
import argparse, os, random, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from laura_rule import rule, load, CELLS, L

SIGNS = [(1, 2), (1, 5), (3, 2), (1, 4), (1, 1), (1, 2), (0, 3), (1, 3), (2, 2), (3, 4)]
C1465 = "Citation duly served, all in best order. You may rely on my returning about the middle of June."
PARA = ["serve the citation", "have the citation served", "get the citation served", "the citation served",
        "citation served", "serve it on him", "serve it on her", "serve the summons", "serve the writ",
        "serve the papers", "have it served", "it was served", "it is served", "duly served"]


def windows(text):
    words = re.findall(r"[a-z]+", text.lower())
    out = []
    for k in range(len(words)):
        s = "".join(words[k:])
        if len(s) >= 10:
            out.append(s[:10])
    return out


def pattern_fit(w):
    return w[0] == w[5] and len(set(w)) == 9


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "topic_crib.tsv"))
    a = ap.parse_args()
    rng = random.Random(174)
    S1 = windows(C1465); S2 = [w for p in PARA for w in windows(p)]
    crib = sorted(set(S1 + S2))

    def M(x):
        best = max(crib, key=lambda c: (sum(u == v for u, v in zip(x, c)), c))
        return sum(u == v for u, v in zip(x, best)), best

    def p95(v):
        v = sorted(v); return v[int(0.95 * len(v))]

    x = rule(SIGNS); mx, bw = M(x)
    A = []
    for _ in range(2000):
        s2 = SIGNS[:]; rng.shuffle(s2); A.append(M(rule(s2))[0])
    B = [M(rule([rng.choice(CELLS) for _ in range(10)]))[0] for _ in range(2000)]
    fam = [M(rule(SIGNS, o, r, sh))[0] for o in "SP" for r in (False, True) for sh in range(26)]
    rankC = 1 + sum(1 for t in fam if t > mx); tiesC = sum(1 for t in fam if t == mx)
    enc = set(L[:21]); ok = [c for c in crib if set(c) <= enc]
    P1 = [M(rng.choice(ok))[0] for _ in range(2000)]
    P2 = []
    for _ in range(2000):
        c = list(rng.choice(ok))
        for i in rng.sample(range(10), 3):
            c[i] = rng.choice(L[:21])
        P2.append(M("".join(c))[0])
    bp = p95(B)
    pow1 = sum(m > bp for m in P1) / 2000; pow2 = sum(m > bp for m in P2) / 2000
    letters, _ = load()
    rnd = [letters[i:i + 10] for i in (rng.randrange(len(letters) - 10) for _ in range(2000))]
    fitC = sum(map(pattern_fit, crib)); fitR = sum(map(pattern_fit, rnd)) / 2000
    with open(a.out, "w") as f:
        f.write("item\tvalue\n")
        for k, v in [("X", x), ("crib_windows", len(crib)), ("encodable_windows", len(ok)), ("M_target", mx),
                     ("best_window", bw), ("A_p95", p95(A)), ("A_tail", sum(m >= mx for m in A) / 2000),
                     ("B_p95", bp), ("B_tail", sum(m >= mx for m in B) / 2000), ("C_rank", f"{rankC}/104 (ties {tiesC})"),
                     ("P1_median", sorted(P1)[1000]), ("P1_power", pow1), ("P2_median", sorted(P2)[1000]),
                     ("P2_power", round(pow2, 3)), ("pattern_fit_crib", f"{fitC}/{len(crib)}"),
                     ("pattern_fit_random_share", round(fitR, 4))]:
            f.write(f"{k}\t{v}\n")
    print(open(a.out).read())


if __name__ == "__main__":
    main()
