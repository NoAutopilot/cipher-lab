#!/usr/bin/env python3
"""Align passA.tsv and passB.tsv line by line (difflib on the token sequences) and list every
disagreement in token or gloss, for checking against the crops. Written 23 Sept 2026.
Usage: python3 reconcile.py [--tsv out.tsv]   prints the agreement statistics."""
import csv
import difflib
import os
import sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    rows = OrderedDict()
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        for r in csv.reader((l for l in f if not l.startswith("#") and l.strip()), delimiter="\t"):
            if r[0] == "line":
                continue
            r += [""] * (6 - len(r))
            rows.setdefault(r[0], []).append(r)
    return rows


def norm_tok(t):
    return t.strip().lower() if t.startswith("[PLAIN") else t.strip()


def main():
    a, b = load("passA.tsv"), load("passB.tsv")
    lines = sorted(set(a) | set(b), key=lambda x: (x[0] != "r", x))
    out = []
    n_rows = n_agree = n_gl = n_gl_agree = 0
    for ln in lines:
        ra, rb = a.get(ln, []), b.get(ln, [])
        ta, tb = [norm_tok(r[2]) for r in ra], [norm_tok(r[2]) for r in rb]
        sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal":
                for i, j in zip(range(i1, i2), range(j1, j2)):
                    n_rows += 1
                    n_agree += 1
                    ga, gb = ra[i][3].strip().lower(), rb[j][3].strip().lower()
                    if ga or gb:
                        n_gl += 1
                        if ga == gb:
                            n_gl_agree += 1
                        else:
                            out.append((ln, ra[i][1], rb[j][1], "gloss", ta[i], tb[j], ga, gb))
            else:
                n_rows += max(i2 - i1, j2 - j1)
                out.append((ln, ",".join(r[1] for r in ra[i1:i2]), ",".join(r[1] for r in rb[j1:j2]), op,
                            " ".join(ta[i1:i2]), " ".join(tb[j1:j2]),
                            " ".join(r[3] for r in ra[i1:i2]), " ".join(r[3] for r in rb[j1:j2])))
    print(f"aligned rows {n_rows}, token agreement {n_agree} ({n_agree / max(1, n_rows):.1%}); "
          f"gloss rows {n_gl}, gloss agreement {n_gl_agree}")
    if "--tsv" in sys.argv:
        p = sys.argv[sys.argv.index("--tsv") + 1]
        with open(p, "w", encoding="utf-8") as f:
            f.write("line\tposA\tposB\top\ttokA\ttokB\tglossA\tglossB\n")
            for r in out:
                f.write("\t".join(map(str, r)) + "\n")
        print(len(out), "disagreement blocks ->", p)


if __name__ == "__main__":
    main()
