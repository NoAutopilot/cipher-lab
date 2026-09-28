#!/usr/bin/env python3
"""Reconcile the Opus blind pass pairs into the v4 coded transcription (campaign H30, 28 Sept 2026).

Inputs: p1_L1-4_v3_passG/H.tsv, p1_L5-8_v3_passI/J.tsv (p.[1], H15's montage boxes), p2_v3_passK/L.tsv (p.[2], the
atlas-v2 p2L1/p2L2 boxes as lines 1-2), and opus_settled.tsv (unit, line, pos, code, grade, note): the runner's
direct-look decision for every box the pair disagreed on (and for the two NEW shapes both readers agreed on).
Rule: pair agrees -> that code at grade AB; pair disagrees -> the settled code at the settled grade (R unless the
settled row says AB); a box with no settled row that disagrees is an error (exit 1). A code "A+B" (two signs in one
box) becomes two rows with the same box and consecutive pos. "_" rows (fragments) are kept here and dropped by
build_letter_codes.py. Output columns match p1_reconciled.tsv: line, box, pos, code, grade, note.
  python3 passes/reconcile_opus.py            writes p1_reconciled_v4.tsv, p2_reconciled_v4.tsv
  python3 passes/reconcile_opus.py --check    exit 1 if either committed file differs from a rebuild"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
PAIRS = {"p1": [("p1_L1-4_v3_passG.tsv", "p1_L1-4_v3_passH.tsv"), ("p1_L5-8_v3_passI.tsv", "p1_L5-8_v3_passJ.tsv")],
         "p2": [("p2_v3_passK.tsv", "p2_v3_passL.tsv")]}


def load(name):
    with open(os.path.join(HERE, name), newline="", encoding="utf-8") as f:
        return {(r["line"].strip(), r["pos"].strip()): r["code"].strip() for r in csv.DictReader(f, delimiter="\t") if r.get("pos")}


def settled():
    out = {}
    with open(os.path.join(HERE, "opus_settled.tsv"), newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            out[(r["unit"], r["line"], r["pos"])] = (r["code"], r["grade"], r["note"])
    return out


def build(unit):
    S = settled()
    rows = []
    for a, b in PAIRS[unit]:
        A, B = load(a), load(b)
        assert set(A) == set(B), (a, b)
        for k in sorted(A, key=lambda k: (int(k[0]), int(k[1]))):
            ca, cb = A[k].upper(), B[k].upper()
            if ca == cb and not ca.startswith("NEW"):
                code, grade, note = A[k], "AB", ""
            else:
                key = (unit, k[0], k[1])
                if key not in S:
                    sys.exit(f"unsettled disagreement {key}: {A[k]} / {B[k]}")
                code, grade, note = S[key]
            rows.append((k[0], k[1], code, grade, note))
    out, pos, cur = [], 0, None
    for line, box, code, grade, note in rows:
        if line != cur:
            cur, pos = line, 0
        for c in code.split("+"):
            pos += 1
            out.append((line, box, str(pos), c, grade, note))
    return out


def text(out):
    return "line\tbox\tpos\tcode\tgrade\tnote\n" + "".join("\t".join(r) + "\n" for r in out)


def main():
    check = "--check" in sys.argv
    bad = 0
    for unit in ("p1", "p2"):
        t = text(build(unit))
        p = os.path.join(HERE, f"{unit}_reconciled_v4.tsv")
        if check:
            if not os.path.exists(p) or open(p, encoding="utf-8").read() != t:
                print(f"STALE: {p}"); bad += 1
            else:
                print(f"ok: {unit}_reconciled_v4.tsv")
        else:
            open(p, "w", encoding="utf-8").write(t)
            n = t.count("\n") - 1
            print(f"wrote {unit}_reconciled_v4.tsv: {n} rows")
    if bad:
        sys.exit(1)


if __name__ == "__main__":
    main()
