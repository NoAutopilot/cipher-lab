#!/usr/bin/env python3
"""Compare two independent transcription passes (passA.tsv, passB.tsv) per line.

Not a reconciler: reports token counts and a rough per-line agreement ratio
(position-wise token match over the shorter of the two token lists), and does
not produce a merged reading. Grades and notes are ignored for the comparison
since the two passes used independent, non-identical note conventions.
"""
import csv
import sys
from collections import defaultdict


def load(path):
    by_line = defaultdict(list)
    with open(path, newline="") as f:
        r = csv.DictReader(f, delimiter="\t")
        for row in r:
            by_line[(row["leaf"], row["line"])].append(row["token"].strip().lower())
    return by_line


def main():
    a = load("passA.tsv")
    b = load("passB.tsv")
    keys = sorted(set(a) | set(b))
    total_tokens_a = sum(len(v) for v in a.values())
    total_tokens_b = sum(len(v) for v in b.values())
    total_compared = 0
    total_match = 0
    per_line_rows = []
    for k in keys:
        ta, tb = a.get(k, []), b.get(k, [])
        n = min(len(ta), len(tb))
        matches = sum(1 for i in range(n) if ta[i] == tb[i])
        total_compared += n
        total_match += matches
        pct = (matches / n * 100) if n else 0.0
        per_line_rows.append((k[0], k[1], len(ta), len(tb), matches, n, pct))

    print(f"passA total tokens: {total_tokens_a}")
    print(f"passB total tokens: {total_tokens_b}")
    print(f"lines compared: {len(keys)}")
    overall = (total_match / total_compared * 100) if total_compared else 0.0
    print(f"overall position-wise token agreement (shorter-list basis): "
          f"{total_match}/{total_compared} = {overall:.1f}%")
    print()
    print("leaf\tline\ttokensA\ttokensB\tmatches\tcompared\tpct")
    for row in per_line_rows:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]:.0f}%")


if __name__ == "__main__":
    sys.exit(main())
