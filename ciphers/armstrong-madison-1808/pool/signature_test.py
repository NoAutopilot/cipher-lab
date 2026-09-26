#!/usr/bin/env python3
"""ARM-POOL signature screen (26 Sept 2026): NOT a result, a screen.

Per the job brief: for a candidate coded letter found on NARA M34 roll 14, decide
office-code (THE=972) vs some other code WITHOUT transcribing it in full, by
eye-transcribing one line (about 15 groups) at native resolution and computing:
  (a) the fraction of those groups THE=972_bourdeau.tsv defines
  (b) the units-digit distribution of those groups

The 20 Feb 1808 target's signature (ARM-DESIGN, ARM-CODES): last digit 0/1
dominant (25%/18% of all 369 tokens), 2/3/5/9 rare (2-5% each), plus shorthand
marks mixed into the numeral stream. THE=972's own real usage (Armstrong's other
1808 letters, pooled 474 tokens, tools/data/uscodes-1800/README.md) is closer to
flat-with-noise (top digit 2 at 15%, not digit-0). A candidate whose one-line
sample matches the target's shape (0/1-heavy, 2/3/5/9 rare, low THE=972 coverage)
is a pool candidate for full transcription; a candidate matching THE=972's usage
(near-flat digits, high coverage) is office correspondence, not a pool candidate.

This is a screen at N~15, not a control-backed result (rule 3): a one-line sample
is too small for a shuffle test to mean anything. Say so in the report.

Usage:
    python3 signature_test.py --groups 1394 1116 1273 250 1165 1405 ...
"""
import argparse
import csv
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
THE972 = HERE.parent.parent.parent / "tools" / "data" / "uscodes-1800" / "THE972_bourdeau.tsv"

# Target's own reference shape (ARM-CODES stats.tsv, all 369 tokens):
TARGET_DIGIT_PCT = {0: 25, 1: 18, 2: 5, 3: 3, 4: 11, 5: 3, 6: 9, 7: 12, 8: 12, 9: 2}
# THE=972 real usage, pooled 474 tokens (NOTES.md ARM-CODES section): top digit 2 at 15%, near-flat.
THE972_USAGE_NOTE = "flat-with-noise, top digit 2 at ~15%, not digit-0 (NOTES.md ARM-CODES)"


def load_the972():
    values = set()
    if THE972.exists():
        with open(THE972, newline="") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                values.add(int(row["value"]))
    return values


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--groups", nargs="+", required=True, help="numeral groups from one eye-transcribed line")
    ap.add_argument("--label", default="", help="candidate letter label (date/frame) for the report")
    args = ap.parse_args()

    nums = []
    for g in args.groups:
        try:
            nums.append(int(g))
        except ValueError:
            continue  # skip shorthand marks / illegible tokens
    n = len(nums)
    if n == 0:
        print("no numeral groups parsed", file=sys.stderr)
        sys.exit(1)

    the972 = load_the972()
    covered = sum(1 for v in nums if v in the972)

    digit_counts = {d: 0 for d in range(10)}
    for v in nums:
        digit_counts[v % 10] += 1
    digit_pct = {d: round(100 * c / n) for d, c in digit_counts.items()}

    print(f"# ARM-POOL signature screen{' -- ' + args.label if args.label else ''}")
    print(f"n groups (numeral only, marks excluded): {n}")
    print(f"THE=972_bourdeau.tsv coverage: {covered}/{n} ({100*covered/n:.0f}%)")
    print(f"units digit %: {digit_pct}")
    print(f"target reference shape (369 tokens): {TARGET_DIGIT_PCT}")
    print(f"THE=972 real usage reference: {THE972_USAGE_NOTE}")
    top1 = max(digit_pct, key=digit_pct.get)
    rare = sum(digit_pct[d] for d in (2, 3, 5, 9))
    dom01 = digit_pct[0] + digit_pct[1]
    print(f"digit-0/1 share: {dom01}%  digit-2/3/5/9 share: {rare}%  top digit: {top1}")
    if covered / n > 0.5 and rare > 15:
        verdict = "looks like THE=972 office usage (high coverage, digits not 0/1-skewed) -- NOT a pool candidate"
    elif dom01 >= 30 and rare <= 15:
        verdict = "matches the target's 0/1-heavy, 2/3/5/9-rare shape -- POOL CANDIDATE (fetch at native size)"
    else:
        verdict = "ambiguous at this N -- screen only, not decisive; fetch more of the letter before deciding"
    print(f"verdict (screen, not a control-backed result): {verdict}")


if __name__ == "__main__":
    main()
