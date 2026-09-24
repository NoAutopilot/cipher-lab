#!/usr/bin/env python3
"""Test whether a printed cipher passage in Birch's Thurloe carries an interlinear
decipherment, using only the extraction files (<Pn>/ciphertext.txt).

Birch set the contemporary decipherment on its own line next to each numeral line.
If a numeral line's neighbouring [PLAIN:...] line has as many letters as the line
has groups, the plain line is a letter-for-group decipherment of it. For every row
this prints how many cipher lines have a neighbour within +-3 letters (OCR drops or
splits some groups) and within 0. For the rows given with --votes it pairs letters
and groups on the exact-length lines and prints, per group, the letters the print
sets over it: consistent votes mean one substitution system with a printed key.

This does not decode anything; it measures what the 1742 print already contains.
Usage: python3 check_interlinear.py [--votes P19 P21 P22 P23]
"""
import argparse, collections, re
from pathlib import Path

HERE = Path(__file__).resolve().parent


def items(row):
    out = []
    for l in (HERE / row / "ciphertext.txt").read_text(encoding="utf-8").split("\n"):
        if l.startswith("#"):
            continue
        m = re.search(r'PLAIN:"(.*)"', l)
        if m:
            out.append(("P", re.sub(r"[^a-z]", "", m.group(1).lower())))
            continue
        m = re.search(r"CLEANED: (.*)$", l)
        if m:
            out.append(("C", [t.rstrip(".,;:") for t in m.group(1).split()]))
    return out


def pairs(its, tol):
    for i, (k, v) in enumerate(its):
        if k != "C":
            continue
        best = None
        for j in (i - 1, i + 1):
            if 0 <= j < len(its) and its[j][0] == "P":
                d = abs(len(its[j][1]) - len(v))
                if d <= tol and (best is None or d < best[0]):
                    best = (d, its[j][1])
        yield v, best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--votes", nargs="*", default=[])
    a = ap.parse_args()
    rows = sorted((p.parent.name for p in HERE.glob("P*/ciphertext.txt")), key=lambda s: int(s[1:]))
    print("row\tcipher_lines\tneighbour_len_pm3\tneighbour_len_exact")
    for r in rows:
        ps = list(pairs(items(r), 3))
        print(f"{r}\t{len(ps)}\t{sum(b is not None for _, b in ps)}\t{sum(b is not None and b[0] == 0 for _, b in ps)}")
    if a.votes:
        votes = collections.defaultdict(collections.Counter)
        for r in a.votes:
            for v, b in pairs(items(r), 0):
                if b:
                    for ch, t in zip(b[1], v):
                        if t.isdigit():
                            votes[int(t)][ch] += 1
        print("\ngroup\tletters set over it in the print (exact-length lines of " + " ".join(a.votes) + ")")
        for k in sorted(votes):
            print(f"{k}\t" + " ".join(f"{c}:{n}" for c, n in votes[k].most_common()))


if __name__ == "__main__":
    main()
