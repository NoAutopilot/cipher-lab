#!/usr/bin/env python3
"""onepart_test.py: test the one-part hypothesis for d'Estaing's code (Tomokiyo
codebreaking.htm "Partial Encoding", "Andre Langie's Example"; LESSONS-TOMOKIYO.md C2)
against a shuffled-range control (CLAUDE.md rule 3).

A one-part code lists its vocabulary alphabetically, so the most frequent groups --
mostly function words in any language -- should fall in the numeric bands their
initial letters occupy in a period dictionary. This script:

1. Loads ciphertext.tsv's CODE tokens and takes the 12 most frequent distinct values.
2. Builds fr18 (French diplomatic/official prose c.1680-1790, tools/data/fr18 -- era-
   matched to this 1779 letter) initial-letter bands via tools/freq.py's
   onepart_dict_bands() (distinct word TYPES, not raw token counts -- see that
   function's docstring and berthier-napoleon-1812 NOTES.md's function-word caveat).
3. Counts how many of the 12 target groups land in a band whose letter is the initial
   of one of {de, la, le, les, que, et, a, en, il, ne, pour, vous} -- common French
   function words, folded (a covers both "a" and "a with accents removed").
4. Runs a matched control: 1000 trials, each drawing 12 DISTINCT integers uniformly
   from the same range (2-597, this letter's own min/max code value) and counting how
   many of those 12 land in a consistent band by chance.
5. Reports both numbers side by side with a pre-registered gate: target count above the
   control's 95th percentile is "support for one-part at this N"; at or below it is "no
   support for one-part at this N" (CLAUDE.md rule 3 -- a target inside the control band
   is a non-test, not a negative on the code).

The same control also stands for the two-part null (position carries no information):
under a two-part code, a group's relative position in the number range is unrelated to
its meaning, which is exactly what the uniform-random draw models. So one control run
answers both framings -- there is no second, different null to build.

This is a lead-generating structural test, not a decode: even a target count above the
control's 95th percentile would only mean the 12 groups' positions are collectively more
consistent with a one-part ordering than chance, not which group means which word.

Reproducible (rule 7): ciphertext.tsv is read fresh from disk each run; the fr18 corpus
is read fresh via tools/freq.py's onepart_dict_bands() (no cached intermediate file).

Usage: python3 onepart_test.py [--trials 1000] [--seed 1] [--lang fr18] [--range 2,597]
"""
import argparse
import os
import random
import statistics
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CIPHERTEXT_TSV = os.path.join(HERE, "ciphertext.tsv")

sys.path.insert(0, os.path.join(ROOT, "tools"))
import freq  # noqa: E402

# Common French function words a one-part alphabetical code's most frequent groups
# would plausibly represent (the brief's own list, CLAUDE.md rule 3 pre-registration --
# fixed before this script's first real run, not adjusted after seeing the result).
TARGET_WORDS = ["de", "la", "le", "les", "que", "et", "à", "en", "il", "ne", "pour", "vous"]


def load_destaing_codes():
    codes = []
    with open(CIPHERTEXT_TSV, encoding="utf-8") as f:
        next(f)
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if parts[2] == "CODE":
                codes.append(parts[3])
    return codes


def consistent_initials(words):
    return {freq.fold_word(w)[0] for w in words if freq.fold_word(w)}


def count_consistent(values, lo, hi, bands, initials):
    n = 0
    for v in values:
        frac = (v - lo) / (hi - lo) if hi > lo else 0.0
        if freq.band_for_frac(bands, frac) in initials:
            n += 1
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trials", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--lang", default="fr18")
    ap.add_argument("--range", default="2,597")
    ap.add_argument("--top", type=int, default=12)
    args = ap.parse_args()
    lo, hi = (int(x) for x in args.range.split(","))

    codes = load_destaing_codes()
    counts = Counter(codes)
    top = counts.most_common(args.top)
    top_values = [int(tok) for tok, _ in top]

    bands, total_types = freq.onepart_dict_bands(args.lang)
    initials = consistent_initials(TARGET_WORDS)

    real_count = count_consistent(top_values, lo, hi, bands, initials)

    rng = random.Random(args.seed)
    control_counts = []
    for _ in range(args.trials):
        draw = set()
        while len(draw) < args.top:
            draw.add(rng.randint(lo, hi))
        control_counts.append(count_consistent(draw, lo, hi, bands, initials))
    mean = statistics.mean(control_counts)
    sd = statistics.pstdev(control_counts)
    sorted_counts = sorted(control_counts)
    p05 = sorted_counts[int(0.05 * args.trials)]
    p95 = sorted_counts[int(0.95 * args.trials) - 1]

    gate_met = real_count > p95
    label = "support for one-part at this N" if gate_met else "no support for one-part at this N"

    print(f"corpus: {args.lang} ({total_types} distinct word types)")
    print(f"target words (folded initials): {sorted(initials)}")
    print(f"top {args.top} groups: {top}")
    print(f"range: {lo}-{hi}")
    print(f"TARGET consistent-band count: {real_count} of {args.top}")
    print(f"CONTROL ({args.trials} draws of {args.top} distinct values, seed={args.seed}): "
          f"mean {mean:.2f} (sd {sd:.2f}), 5-95pct [{p05},{p95}]")
    print(f"GATE (target > control p95): {gate_met} -- {label}")
    print("Same control also stands for the two-part null (position carries no information): "
          "the uniform-random draw IS that null, so this one control answers both framings.")


if __name__ == "__main__":
    main()
