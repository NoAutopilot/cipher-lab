#!/usr/bin/env python3
"""SFZ-R5323 scorer (PREREG-SFZ-R5323.md). Reads blind reader TSVs (letter<TAB>labels) and scores the 7 C pairs.

usage: score_r5323.py PASS_A PASS_B CTL1 [CTL2 ...]
Exact label tokens only ('^' marks stripped); 'A/B?' tokens are reported separately as a sensitivity line, not scored."""
import random, sys

PAIRS = [("O", "a"), ("Y", "o"), ("N8", "d"), ("N2", "h"), ("N11", "r"), ("ce", "r"), ("cu", "n")]


def read(path, loose=False):
    cols = {}
    for line in open(path, encoding="utf-8"):
        if "\t" not in line:
            continue
        letter, labs = line.rstrip("\n").split("\t", 1)
        out = set()
        for t in labs.split():
            t = t.rstrip("^")
            if "/" in t and t.endswith("?"):
                if loose:
                    out.update(x.rstrip("^") for x in t[:-1].split("/"))
                continue
            out.add(t)
        cols[letter.strip().lower()] = out
    return cols


def score(cols):
    return sum(1 for lab, let in PAIRS if lab in cols.get(let, set()))


def hits(cols):
    return [f"{lab}={let}" for lab, let in PAIRS if lab in cols.get(let, set())]


def main(argv):
    a, b, ctls = argv[0], argv[1], argv[2:]
    for loose in (False, True):
        A, B = read(a, loose), read(b, loose)
        agreed = {k: A[k] & B[k] for k in A if k in B}
        tag = "loose (A/B? counted)" if loose else "strict"
        s = score(agreed)
        print(f"[{tag}] R5323 S_A={score(A)} {hits(A)}  S_B={score(B)} {hits(B)}  S_agreed={s} {hits(agreed)}")
        cs = []
        for c in ctls:
            C = read(c, loose)
            cs.append(score(C))
            print(f"[{tag}]   control {c.split('/')[-1]}: S={cs[-1]} {hits(C)}")
        letters = sorted(agreed)
        rng = random.Random(5323)
        ge = 0
        for _ in range(10000):
            perm = letters[:]
            rng.shuffle(perm)
            ge += score({perm[i]: agreed[letters[i]] for i in range(len(letters))}) >= s
        p = ge / 10000
        mx = max(cs) if cs else None
        ok = s >= 4 and (mx is None or s > mx) and p <= 0.01
        print(f"[{tag}] max control S={mx}  shuffled p={p:.4f}  GATE {'PASS' if ok else 'FAIL'}"
              f"{'' if not loose else ' (sensitivity only; the strict line is the registered result)'}")


if __name__ == "__main__":
    main(sys.argv[1:])
