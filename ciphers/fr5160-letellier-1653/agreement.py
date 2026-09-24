#!/usr/bin/env python3
"""Per-line agreement between two blind transcription passes of the same leaf.

A line "agrees" if both passes have the same number of cipher-group tokens
at each position AND the same raw group string (ignoring confidence).
Reports per-line and overall agreement, plus a token-level agreement rate
for lines with matching counts.
"""
import csv
import sys
from collections import defaultdict


def load(path):
    lines = defaultdict(list)
    clear = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if row["position"] == "clear":
                clear[row["line"]] = row["group"]
            else:
                lines[row["line"]].append(row["group"])
    return lines, clear


def main():
    a_groups, a_clear = load("passA.tsv")
    b_groups, b_clear = load("passB.tsv")
    all_lines = sorted(set(a_groups) | set(b_groups), key=lambda s: (s.split("_")[0], int(s.split("L")[1])))

    line_agree = 0
    tok_total = tok_agree = 0
    print(f"{'line':10} {'A_n':>4} {'B_n':>4} {'count_match':>12} {'tok_agree':>10} {'rate':>7}")
    for line in all_lines:
        a = a_groups.get(line, [])
        b = b_groups.get(line, [])
        count_match = len(a) == len(b)
        if count_match:
            n = len(a)
            agree = sum(1 for x, y in zip(a, b) if x == y)
            tok_total += n
            tok_agree += agree
            rate = agree / n if n else 1.0
            if rate == 1.0:
                line_agree += 1
        else:
            rate = float("nan")
        print(f"{line:10} {len(a):>4} {len(b):>4} {str(count_match):>12} "
              f"{'' if not count_match else agree:>10} {'' if not count_match else f'{rate:.2f}':>7}")

    print()
    print(f"Lines: {len(all_lines)}  same-count: {sum(1 for l in all_lines if len(a_groups.get(l, [])) == len(b_groups.get(l, [])))}  "
          f"fully-agreeing: {line_agree}")
    print(f"Token-level agreement (lines with matching counts only): {tok_agree}/{tok_total} = {tok_agree/tok_total:.1%}")

    clear_lines = sorted(set(a_clear) | set(b_clear))
    print()
    print("Clear-French lines (A vs B):")
    for line in clear_lines:
        av = a_clear.get(line, "<absent>")
        bv = b_clear.get(line, "<absent>")
        flag = "SAME" if av == bv else "differs"
        print(f"  {line}: [{flag}] A={av!r} B={bv!r}")


if __name__ == "__main__":
    sys.exit(main())
