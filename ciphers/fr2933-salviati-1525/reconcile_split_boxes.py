#!/usr/bin/env python3
"""Reconcile two blind per-box code+mark passes for SALV2-J1 (27 Sept 2026, LANE SALV2 job 1).

tools/reconcile_passes.py aligns two full-line sign sequences with Needleman-Wunsch; the per-box
passes here sample only the SALV-SPLIT-confirmed (line,pos) boxes, scattered a handful per line, not
a line's full sequence -- there is nothing to align, so this compares by the (line,pos) key directly,
per the job brief's own fallback clause ("if --rows does not fit the per-box shape, compare by
(line,pos) key in a few lines of Python and say so").

Usage: python3 reconcile_split_boxes.py passA_split_<leaf>.tsv passB_split_<leaf>.tsv --out-dir recon_split_<leaf>

Reads both passes (header line, pos, sign, conf, marks, note, id), one row per confirmed box, joins
on (line,pos), and writes:
  agreement.tsv       line, pos, code_agree (0/1), marks_agree (0/1), both_agree (0/1)
  disagreements.tsv    line, pos, A_code, A_marks, A_conf, A_id, B_code, B_marks, B_conf, B_id
Also prints the overall code/marks/both agreement fractions (the transcription-error control figure
for NOTES.md, beside bSALC's 6.4% per-sign measured error).
"""
import csv, os, sys


def load(path):
    rows = {}
    with open(path, newline="") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            rows[(int(r["line"]), r["pos"])] = r
    return rows


def main():
    if len(sys.argv) < 3 or "-h" in sys.argv or "--help" in sys.argv:
        print(__doc__)
        sys.exit(0)
    a_path, b_path = sys.argv[1], sys.argv[2]
    out_dir = sys.argv[sys.argv.index("--out-dir") + 1] if "--out-dir" in sys.argv else "."
    os.makedirs(out_dir, exist_ok=True)

    A, B = load(a_path), load(b_path)
    if set(A.keys()) != set(B.keys()):
        missing_a = set(B.keys()) - set(A.keys())
        missing_b = set(A.keys()) - set(B.keys())
        print(f"WARNING: key mismatch -- only in B: {missing_a}, only in A: {missing_b}", file=sys.stderr)

    keys = sorted(set(A.keys()) & set(B.keys()))
    agree_rows, disagree_rows = [], []
    n_code = n_marks = n_both = 0
    for k in keys:
        a, b = A[k], B[k]
        code_agree = a["sign"] == b["sign"]
        marks_agree = a["marks"] == b["marks"]
        both_agree = code_agree and marks_agree
        n_code += code_agree
        n_marks += marks_agree
        n_both += both_agree
        agree_rows.append((k[0], k[1], int(code_agree), int(marks_agree), int(both_agree)))
        if not both_agree:
            disagree_rows.append((k[0], k[1], a["sign"], a["marks"], a["conf"], a["id"],
                                   b["sign"], b["marks"], b["conf"], b["id"]))

    with open(os.path.join(out_dir, "agreement.tsv"), "w", newline="") as f:
        f.write("line\tpos\tcode_agree\tmarks_agree\tboth_agree\n")
        for row in agree_rows:
            f.write("\t".join(str(c) for c in row) + "\n")

    with open(os.path.join(out_dir, "disagreements.tsv"), "w", newline="") as f:
        f.write("line\tpos\tA_code\tA_marks\tA_conf\tA_id\tB_code\tB_marks\tB_conf\tB_id\n")
        for row in disagree_rows:
            f.write("\t".join(str(c) for c in row) + "\n")

    n = len(keys)
    print(f"{a_path} vs {b_path}: n={n} code_agree={n_code}/{n}={n_code/n:.1%} "
          f"marks_agree={n_marks}/{n}={n_marks/n:.1%} both_agree={n_both}/{n}={n_both/n:.1%} "
          f"disagreements={len(disagree_rows)} -> {out_dir}/")


if __name__ == "__main__":
    main()
