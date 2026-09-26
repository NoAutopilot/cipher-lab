#!/usr/bin/env python3
"""ARM3-COR overlap screen (26 Sept 2026): top-20 value overlap + matched control.

Per the ARM3-COR job brief (.claude/briefs/runs/2026-09-26-lane-arm3-j1-correspondents.md, unit
U2-U7 step b): for a candidate letter that shows numeral groups, count how many of the target's
20 most frequent group values occur in the candidate. This is meaningless on its own (rule 3) --
report it beside two controls that CAN differ from the candidate's number:

  (1) the same overlap count computed on the known THE=972 letters already on file (pooled
      sample groups from ARM-POOL/ARM-POOL2/ARM-CODES screens -- see THE972_SAMPLE below).
  (2) 200 random draws of the same N groups, uniform over the target's own value range 1-1899;
      report the fraction of draws with >=3 shared (the "chance rate").

A "pool candidate" (brief's own definition) is a letter with >=3 shared top-20 values AND an
overlap above the THE=972 sample's own rate AND the target-like digit shape (0/1-heavy,
2/3/5/9-rare -- see pool/signature_test.py for the digit-shape screen, run separately).

Usage:
    python3 overlap_test.py --groups 622 550 1653 1105 587 --label "15 Feb 1808 sample"
    python3 overlap_test.py --the972-control          # baseline: the pooled THE=972 sample vs itself
"""
import argparse
import random
import sys

# Target's own top-20 most frequent group values, computed from ciphertext.txt (369 tokens,
# 216 distinct values), this job, 26 Sept 2026:
TARGET_TOP20 = [17, 18, 38, 1, 14, 12, 47, 170, 1480, 1267, 48, 176, 11, 240, 760, 1340, 76, 45, 671, 41]
TARGET_VALUE_RANGE = (1, 1899)

# Known THE=972 letters already on file, pooled numeral-group samples (explicit values recorded
# in this job's sources -- not full letters, the screens NOTES.md/pool/*.tsv already recorded):
#   15 Feb 1808 (SURVEY.tsv frame 0025, 12 groups)
#   22 Feb 1808, two embedded passages (DOCKET-0645.tsv item 2, 13+13 groups)
#   9 March 1808 / frame 0643 duplicate (DOCKET-0645.tsv item 3, first 16 groups)
#   27 Dec 1807, two interlinear-gloss runs (DOCKET-0645.tsv item 1, 12+15 groups)
THE972_SAMPLE = (
    [622, 550, 1653, 1105, 587, 541, 899, 972, 1413, 1116, 1131, 1481]
    + [972, 1394, 1090, 1354, 914, 985, 608, 899, 1482, 1228, 1492, 297, 1001]
    + [76, 736, 1587, 910, 369, 630, 1478, 860, 1090, 758, 1282, 1284, 823]
    + [276, 962, 972, 676, 1354, 395, 1701, 1248, 1482, 988, 1092, 1268, 1090, 1013, 734, 967]
    + [578, 1101, 1001, 626, 1105, 1090, 590, 386, 1105, 1482, 646, 1369]
    + [582, 1165, 910, 178, 584, 687, 249, 759, 1105, 750, 1379, 1587, 697, 958, 1467]
)


def overlap(groups, top20=None):
    top20 = set(top20 or TARGET_TOP20)
    nums = [g for g in groups if isinstance(g, int)]
    return sum(1 for v in nums if v in top20), len(nums)


def random_draw_chance(n, top20=None, value_range=None, trials=200, seed=26092026):
    top20 = set(top20 or TARGET_TOP20)
    lo, hi = value_range or TARGET_VALUE_RANGE
    rng = random.Random(seed)
    hits_ge3 = 0
    shared_counts = []
    for _ in range(trials):
        draw = [rng.randint(lo, hi) for _ in range(n)]
        shared = sum(1 for v in draw if v in top20)
        shared_counts.append(shared)
        if shared >= 3:
            hits_ge3 += 1
    return hits_ge3 / trials, shared_counts


def report(groups, label):
    shared, n = overlap(groups)
    the972_shared, the972_n = overlap(THE972_SAMPLE)
    chance_rate, shared_counts = random_draw_chance(n)
    print(f"# ARM3-COR overlap screen{' -- ' + label if label else ''}")
    print(f"n groups: {n}")
    print(f"shared with target top-20: {shared}/{n}")
    print(f"CONTROL 1 (THE=972 pooled sample, N={the972_n}): shared {the972_shared}/{the972_n} "
          f"({100*the972_shared/the972_n:.1f}%)")
    print(f"CONTROL 2 (200 random draws of N={n}, uniform 1-1899): "
          f"chance rate of >=3 shared = {chance_rate*100:.1f}%  "
          f"(mean shared {sum(shared_counts)/len(shared_counts):.2f})")
    if n >= 3:
        the972_rate = the972_shared / the972_n
        this_rate = shared / n
        if shared >= 3 and this_rate > the972_rate:
            verdict = "ABOVE both controls -- pool candidate (pending digit-shape screen)"
        else:
            verdict = "at or below controls -- not a pool candidate on this test"
    else:
        verdict = "n<3, screen not meaningful"
    print(f"verdict: {verdict}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--groups", nargs="+", help="numeral groups from the candidate letter")
    ap.add_argument("--label", default="")
    ap.add_argument("--the972-control", action="store_true",
                     help="report the THE=972 pooled sample against the random-draw control (baseline run)")
    args = ap.parse_args()

    if args.the972_control:
        report(THE972_SAMPLE, "THE=972 pooled sample (baseline)")
        return

    if not args.groups:
        print("--groups or --the972-control required", file=sys.stderr)
        sys.exit(1)
    nums = []
    for g in args.groups:
        try:
            nums.append(int(g))
        except ValueError:
            continue
    if not nums:
        print("no numeral groups parsed", file=sys.stderr)
        sys.exit(1)
    report(nums, args.label)


if __name__ == "__main__":
    main()
