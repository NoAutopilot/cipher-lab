#!/usr/bin/env python3
"""GAPS146 frozen mod-24 residue rule for R1411 (see PREREG-GAPS146.md).

Builds the 24-entry residue -> letter table from ../gloss/pairs.tsv (grade C pairs only) and nothing else:
  observed residue: majority gloss letter among C pairs with that residue (tie -> the alphabet letter below);
  unobserved residue: the 24-letter alphabet a b c d e f g h i k l m n o p q r s t u w x y z laid on residues with a = 5.
Prints the table; `--table OUT` writes it as TSV. Importable: table(), decode(numbers, shift=0).
"""
import collections, csv, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ALPHA = "abcdefghiklmnopqrstuwxyz"  # 24 letters, i/j and u/v merged
A_AT = 5


def alphabet_letter(r):
    return ALPHA[(r - A_AT) % 24]


def table():
    votes = collections.defaultdict(collections.Counter)
    with open(os.path.join(HERE, "..", "gloss", "pairs.tsv")) as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if row["grade"] != "C" or "?" in row["token"]:
                continue
            votes[int(row["token"]) % 24][row["gloss"]] += 1
    t = {}
    for r in range(24):
        c = votes.get(r)
        if not c:
            t[r] = (alphabet_letter(r), "alphabet", "")
            continue
        top = c.most_common()
        if len(top) > 1 and top[0][1] == top[1][1]:
            t[r] = (alphabet_letter(r), "tie->alphabet", dict(c))
        else:
            t[r] = (top[0][0], "gloss", dict(c))
    return t


def decode(numbers, shift=0, tab=None):
    tab = tab or table()
    return "".join(tab[(n + shift) % 24][0] for n in numbers)


if __name__ == "__main__":
    t = table()
    lines = ["residue\tletter\tsource\tvotes"] + [f"{r}\t{t[r][0]}\t{t[r][1]}\t{t[r][2]}" for r in range(24)]
    if "--table" in sys.argv:
        open(sys.argv[sys.argv.index("--table") + 1], "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))
