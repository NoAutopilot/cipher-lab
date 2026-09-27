#!/usr/bin/env python3
"""Write back SALV2-J1's settled code+mark readings into the real ciphertext_<leaf>.tsv files (27 Sept 2026,
LANE SALV2 job 1). Reads recon_split_<leaf>/settled.tsv (line, pos, code, marks, grade, how) and, for each row,
replaces that exact (line,pos) row's code/marks/grade in ciphertext_<leaf>.tsv -- grade gets '|split2' appended
so the change is traceable. Every other row is left byte-identical. Does not touch .split-candidate files, the
spec, ciphertext.txt or ciphertext_with_plain.txt (job 2's job).

Usage: python3 apply_split2_writeback.py f54r f54v
"""
import csv, sys


def main():
    leaves = sys.argv[1:]
    if not leaves or "-h" in leaves or "--help" in leaves:
        print(__doc__); sys.exit(0)
    for leaf in leaves:
        settled = {}
        with open(f"recon_split_{leaf}/settled.tsv", newline="") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                settled[(r["line"], r["pos"])] = (r["code"], r["marks"], r["grade"])

        path = f"ciphertext_{leaf}.tsv"
        with open(path, newline="") as f:
            reader = csv.reader(f, delimiter="\t")
            header = next(reader)
            rows = list(reader)

        n_changed = 0
        for row in rows:
            line, pos = row[0], row[1]
            key = (line, pos)
            if key in settled:
                code, marks, grade = settled[key]
                assert row[2] == "_", f"expected plain '_' at {leaf} {key}, found {row[2]!r}"
                row[2] = code
                row[3] = marks
                row[4] = grade + "|split2"
                n_changed += 1
                del settled[key]

        if settled:
            print(f"WARNING: {leaf} unmatched settled rows (no plain '_' row found): {list(settled.keys())}", file=sys.stderr)

        with open(path, "w", newline="") as f:
            w = csv.writer(f, delimiter="\t", lineterminator="\n")
            w.writerow(header)
            w.writerows(rows)

        print(f"{leaf}: {n_changed} rows updated in {path} (of {len(rows)} total rows)")


if __name__ == "__main__":
    main()
