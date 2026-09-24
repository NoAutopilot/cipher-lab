#!/usr/bin/env python3
"""Per-line agreement between the two blind transcription passes of the folio 9 letter
(canvas 24/25, f9r/f9v). Same method as agreement.py (folio 1-2 letter): a line "agrees"
if both passes have the same number of cipher-group tokens at each position AND the same
raw group string (ignoring confidence). Reports per-line and overall agreement, plus a
token-level agreement rate for lines with matching counts.
"""
import csv
import sys
from collections import defaultdict


def load(path):
    lines = defaultdict(list)
    clear = defaultdict(list)
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if row["position"] == "clear":
                clear[row["line"]].append(row["group"])
            else:
                lines[row["line"]].append(row["group"])
    return lines, clear


def line_key(s):
    side, rest = s.split("_L")
    return (side, int(rest))


def main():
    a_groups, a_clear = load("passA_f9.tsv")
    b_groups, b_clear = load("passB_f9.tsv")
    all_lines = sorted(set(a_groups) | set(b_groups) | set(a_clear) | set(b_clear), key=line_key)

    line_agree = 0
    tok_total = tok_agree = 0
    print(f"{'line':10} {'A_n':>4} {'B_n':>4} {'count_match':>12} {'tok_agree':>10} {'rate':>7}")
    for line in all_lines:
        a = a_groups.get(line, [])
        b = b_groups.get(line, [])
        count_match = len(a) == len(b)
        agree = 0
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

    same_count = sum(1 for l in all_lines if len(a_groups.get(l, [])) == len(b_groups.get(l, [])))
    print()
    print(f"Lines: {len(all_lines)}  same-count: {same_count}  fully-agreeing: {line_agree}")
    if tok_total:
        print(f"Token-level agreement (lines with matching counts only): {tok_agree}/{tok_total} = {tok_agree/tok_total:.1%}")
    else:
        print("Token-level agreement: no count-matched lines")

    clear_lines = sorted(set(a_clear) | set(b_clear), key=line_key)
    print()
    print("Clear-French lines (A vs B):")
    for line in clear_lines:
        av = " / ".join(a_clear.get(line, ["<absent>"]))
        bv = " / ".join(b_clear.get(line, ["<absent>"]))
        flag = "SAME" if av == bv else "differs"
        print(f"  {line}: [{flag}] A={av!r} B={bv!r}")


if __name__ == "__main__":
    sys.exit(main())
