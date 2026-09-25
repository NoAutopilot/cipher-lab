#!/usr/bin/env python3
"""untersberg-code cheap test 1: abbreviation hypothesis (specs/untersberg-code.json
cheap_tests_in_order[0]).

Schmeh's own text leans toward a scribal-abbreviation reading over a substitution cipher
("some knowledge of ancient German or Latin might be more helpful than codebreaking
skills"). The six transcribed lines mix short letter groups closed with a period (typical
of a 16th-century suspension abbreviation, e.g. "S." "d." "occo.") with a handful of longer
unpunctuated runs that read as full words (Satrnrop, missm, ariu, alto, mvraco, mic, pymi).
A real abbreviation convention should show short (<=3-letter) alphabetic tokens
disproportionately closed with a period, compared to what the same character frequencies
would produce by chance.

Pattern counted (identically in target and control): a maximal run of 1-3 ASCII letters,
delimited by whitespace on the left, immediately followed by a period.

Control (LANE B3 orchestrator's brief, 25 Sept 2026): a synthetic string of the same length
as the target, drawn i.i.d. per-character from the target's own unigram character
distribution (letters, digits, '.', ',', whitespace -- exactly the characters that occur in
the transcription), tokenised and counted the same way. This asks whether the short-token/
period clustering is more than what the target's own character frequencies would produce by
chance -- not whether it matches an external abbreviation corpus (none is on file; CLAUDE.md
rule 3, matching the *design* under test, here means matching the null model to the same
alphabet and length, since no abbreviation-convention corpus exists to draw a positive
control from).

CLAUDE.md rule 7: reproducible, exits non-zero if it cannot regenerate its own numbers.
"""
import argparse
import json
import random
import re
import sys
from pathlib import Path

TARGET_LINES = [
    "S. d. d. occo. x.",
    "Satrnrop, 5. a. f. 5. l. d.",
    "P. 6. m. 6. a. t. 5. q. o. t. m. 5. r. u. a t.",
    "m. 519. r. l. v. e. p. 55. a. tt. tt. l. x. missm",
    "ariu. a. o. u st g c x 5. l. 19. alto mvraco",
    "mic r l y. pymi. l o p m i. v m l t. t g",
]

PATTERN = re.compile(r"(?<![A-Za-z.])[A-Za-z]{1,3}\.")


def count_pattern(s):
    return len(PATTERN.findall(s))


def build_text(lines=TARGET_LINES):
    return " ".join(lines)


def unigram_distribution(text):
    chars = list(text)
    from collections import Counter

    counts = Counter(chars)
    total = len(chars)
    symbols = list(counts.keys())
    weights = [counts[c] / total for c in symbols]
    return symbols, weights, total


def synthetic_control(symbols, weights, length, n_trials, seed):
    rng = random.Random(seed)
    counts = []
    for _ in range(n_trials):
        s = "".join(rng.choices(symbols, weights=weights, k=length))
        counts.append(count_pattern(s))
    return counts


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--trials", type=int, default=500)
    ap.add_argument("--seed", type=int, default=20260925)
    ap.add_argument("--check", action="store_true",
                     help="exit non-zero if the committed output.json is stale")
    ap.add_argument("--out", default=str(Path(__file__).parent / "test1_output.json"))
    args = ap.parse_args(argv)

    text = build_text()
    target_count = count_pattern(text)
    symbols, weights, length = unigram_distribution(text)
    control_counts = synthetic_control(symbols, weights, length, args.trials, args.seed)
    control_counts_sorted = sorted(control_counts)
    mean = sum(control_counts) / len(control_counts)
    lo, hi = control_counts_sorted[0], control_counts_sorted[-1]
    pctile = sum(1 for c in control_counts if c <= target_count) / len(control_counts) * 100

    result = {
        "target_length_chars": length,
        "target_pattern_count": target_count,
        "control_trials": args.trials,
        "control_seed": args.seed,
        "control_mean": round(mean, 3),
        "control_min": lo,
        "control_max": hi,
        "target_percentile_in_control": round(pctile, 1),
        "verdict": (
            "target ABOVE control range -- short-token/period clustering exceeds chance"
            if target_count > hi else
            "target BELOW control range -- short-token/period clustering is less than chance"
            if target_count < lo else
            "target WITHIN control range -- not distinguishable from the target's own character frequencies by chance"
        ),
    }

    out_path = Path(args.out)
    if args.check:
        if not out_path.exists():
            print(f"STALE: {out_path} does not exist", file=sys.stderr)
            return 1
        on_disk = json.loads(out_path.read_text())
        # only compare the reproducible numeric fields (seed/trials pinned, so exact)
        keys = ["target_length_chars", "target_pattern_count", "control_trials",
                "control_seed", "control_mean", "control_min", "control_max",
                "target_percentile_in_control", "verdict"]
        stale = [k for k in keys if on_disk.get(k) != result[k]]
        if stale:
            print(f"STALE: fields differ: {stale}", file=sys.stderr)
            return 1
        print(f"OK: {out_path} matches regenerated output")
        return 0

    out_path.write_text(json.dumps(result, indent=1) + "\n")
    print(json.dumps(result, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
