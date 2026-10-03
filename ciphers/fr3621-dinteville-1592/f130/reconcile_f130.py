#!/usr/bin/env python3
"""Normalize passA/passB (default: list disagreements; --write: write ciphertext.tsv) to the f.128 label set and list where they still disagree (A2-DIN2, 3 Oct 2026).

Label normalization (checked against images/f128_L03_s1.jpg beside f128/gloss_pairs.tsv L03):
  x -> p      the looped x glyph is the sign f.128's reconciliation labels p ("deux millions": z p 4 plus L)
  + / t / t' -> plus   the cross written as a sign (f.128 'plus', in "millions")
  2 -> z, ÷ -> div, D' -> D, 4' -> 4   spelling variants of one label
  0' kept as 0' (o with a stem); f.128's reconciliation wrote this glyph as 0 (L03 "sq 0 0 f" over "□ o ō ≠"),
     so score_f130.py reads 0' with 0's key value at grade M.
"""
import csv, difflib
NORM = {"x": "p", "+": "plus", "t": "plus", "t'": "plus", "2": "z", "÷": "div", "D'": "D", "4'": "4"}
def load(f):
    d = {}
    for r in csv.DictReader(open(f), delimiter="\t"):
        d[(r["line"], r["seg"])] = [NORM.get(s, s) for s in (r["signs"] or "").split() if not s.startswith("CLEAR:")]
    return d
def report():
    A, B = load("passA.tsv"), load("passB.tsv"); tot = ed = 0
    for k in sorted(set(A) | set(B)):
        a, b = A.get(k, []), B.get(k, [])
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        for t, i1, i2, j1, j2 in sm.get_opcodes():
            if t != "equal":
                ed += max(i2 - i1, j2 - j1)
                print(k, t, f"A[{i1}:{i2}]", " ".join(a[i1:i2]) or "-", "| B", " ".join(b[j1:j2]) or "-",
                      "| ctx", " ".join(a[max(0, i1 - 3):i1]))
        tot += max(len(a), len(b))
    print("cipher signs", tot, "A-B edit after normalization", ed)


# --- reconciliation (A2-DIN2, Opus, 3 Oct 2026): base = pass A normalized; A/B disagreement spans -> conf M;
# segments re-read by the reconciler from 1.6x zooms (images/zoom/f130_*_z.jpg) replace the pass text.
OVERRIDE = {  # (line, seg): list of (sign, conf)
    ("L01", "s2"): [(s, "M") for s in "4 1 m y".split()],  # tail cut at the crop top; B's reading, A saw only 4 1
    ("L02", "s1"): [(s, "H") for s in "v' o c y p m sq L plus r p o 0' v'".split()] + [("NEW:e-hook", "M")]
                   + [(s, "H") for s in "L m 0' y".split()] + [("al", "M"), ("c", "H")],
    ("L11", "s1"): [(s, "H") for s in "h y m w".split()] + [("al", "M")]
                   + [(s, "H") for s in "y L w # 1 z 0 f w 0 v' L c 0 w # v m 4 v' v f v' a m L 4 p".split()],
}
A_TAIL = {("L02", "s1"): 23}  # pass A tokens [0:23] replaced by the override; the rest of A's segment is kept
PATCH = {("L10", "s1"): ("w 0 0 0' L x 0", "w v sq 0' L p o")}  # reconciler's zoom read, conf M


def reconcile():
    rowsA = list(csv.DictReader(open("passA.tsv"), delimiter="\t"))
    B = load("passB.tsv"); out = []
    for r in rowsA:
        k = (r["line"], r["seg"])
        raw = (r["signs"] or "").split()
        if k in PATCH:
            raw = " ".join(raw).replace(PATCH[k][0], PATCH[k][1]).split()
        clear = [s for s in raw if s.startswith("CLEAR:")]
        a = [NORM.get(s, s) if s != "t'" else "v'" for s in raw if not s.startswith("CLEAR:")]
        conf = ["H"] * len(a)
        sm = difflib.SequenceMatcher(None, a, B.get(k, []), autojunk=False)
        for t, i1, i2, j1, j2 in sm.get_opcodes():
            if t != "equal":
                for i in range(max(0, i1 - (1 if i1 == i2 else 0)), max(i2, i1 + (1 if i1 == i2 else 0))):
                    if i < len(conf):
                        conf[i] = "M"
        if k in PATCH:
            lo = " ".join(a).find(PATCH[k][1])
            i0 = len(" ".join(a)[:lo].split()); conf[i0:i0 + len(PATCH[k][1].split())] = ["M"] * len(PATCH[k][1].split())
        seq = list(zip(a, conf))
        if k in OVERRIDE:
            seq = OVERRIDE[k] + (seq[A_TAIL[k]:] if k in A_TAIL else [])
        # clear words keep their place: leading ones before, trailing ones after the signs (as on the leaf)
        lead = []
        for s in raw:
            if s.startswith("CLEAR:"):
                lead.append(s)
            else:
                break
        trail = [s for s in clear if s not in lead]
        out += [(k[0], s, "H") for s in lead] + [(k[0], s, c) for s, c in seq] + [(k[0], s, "H") for s in trail]
    pos = {}
    with open("ciphertext.tsv", "w") as f:
        f.write("line\tpos\tsign\tconf\n")
        for ln, s, c in out:
            pos[ln] = pos.get(ln, 0) + 1
            f.write(f"{ln}\t{pos[ln]}\t{s}\t{c}\n")
    return out


if __name__ == "__main__":
    import sys
    if "--write" in sys.argv:
        reconcile(); print("wrote ciphertext.tsv")
    else:
        report()
