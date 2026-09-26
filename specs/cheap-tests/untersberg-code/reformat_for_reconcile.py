#!/usr/bin/env python3
"""untersberg-code NEAR step (4), 26 Sept 2026, LANE B6 worker bUNT7.

tools/reconcile_passes.py's 'long' format detector requires a header whose
first column is literally 'line' (not 'line_number') and a position column
named one of pos/position/index (not 'token_index') and a sign column named
one of sign/token/group/code (not 'token_text'). bUNT6's blind_pass.tsv and
this pass's pass_b7.tsv both use the line_number/token_index/token_text/
confidence/note header (bUNT6's own convention, kept for continuity), which
the tool's detector does not recognize -- it would silently misparse the file
as 'wide' format instead. This script writes a field-renamed copy of a given
TSV (same rows, same values, header only remapped) so tools/reconcile_passes.py
can read it; it does not alter any transcribed content.

Usage: python3 reformat_for_reconcile.py IN.tsv OUT.tsv
"""
import csv
import sys


def main():
    in_path, out_path = sys.argv[1], sys.argv[2]
    with open(in_path, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f, delimiter="\t"))
    header = rows[0]
    idx = {name: i for i, name in enumerate(header)}
    new_header = ["line", "pos", "sign", "conf", "note"]
    out_rows = [new_header]
    for r in rows[1:]:
        out_rows.append([
            r[idx["line_number"]],
            r[idx["token_index"]],
            r[idx["token_text"]],
            r[idx["confidence"]] if "confidence" in idx and idx["confidence"] < len(r) else "",
            r[idx["note"]] if "note" in idx and idx["note"] < len(r) else "",
        ])
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerows(out_rows)
    print(f"wrote {out_path}: {len(out_rows) - 1} rows")


if __name__ == "__main__":
    main()
