#!/usr/bin/env python3
"""goldbar-1933 cheap test 1: per-letter frequency chi-squared vs a random-sampling control.

Spec: specs/goldbar-1933.json cheap_tests_in_order[0] ("confirm or refute the commenter's 'every
letter ~10 times' claim independently... report the design implication"). A literal permutation of
the SAME fixed letter multiset is a DEGENERATE control for a whole-corpus letter-frequency
chi-squared statistic: any permutation of a fixed multiset has, by definition, the identical letter
counts and therefore the identical chi-squared value (confirmed empirically the first run of this
script: control mean == control min == control max == target, 1000/1000 shuffles). Discovered this
pass, so recorded here rather than silently fixed: the correct matched-random-sampling control for
"how unusual is a chi-squared this low if the near-uniformity happened by chance" is 1000 FRESH
random N-letter strings, each letter drawn i.i.d. uniformly from the 26-letter alphabet -- NOT
preserving the observed multiset -- which is what actually produces a chi-squared null distribution.
This matches Bourdeau's own Monte Carlo design in dbourdeau/cyphersolver's goldbar/NOTES.md ("200,000
random 263-letter strings"), a fresh random draw, at 1000 draws instead of 200,000 per the brief's
size. Stdlib only, no network, no third-party dependencies (numpy/scipy not required).

Runs two readings: as-printed (McCurley/Schmeh transcription) and the Bret Bowen / dbourdeau
line-8 correction (UGMNCBXCFLDBEY -> UGMNCBXCFLDBY), the correction applied in memory only --
ciphertext.txt on disk is never silently repaired (CLAUDE.md rule 2).

Usage: python3 freq_test.py > freq_test_output.json
"""
import json
import random
import string

AS_PRINTED = [
    "SKCDKJCDJCYQSZKTZJPXPWIRN",
    "MQOLCSJTLGAJOKBSSBOMUPCE",
    "RHZVIYQIYSXVNQXQWIOVWPJO",
    "FEWGDRHDDEEUMFFTEEMJXZR",
    "XLYPISNANIRUSFTFWMIY",
    "HFXPCQYZVATXAWIZPVE",
    "YQHUDTABGALLOWLS",
    "UGMNCBXCFLDBEY",
    "ABRYCTUGVZXUPB",
    "JKGFIJPMCWSAEK",
    "KOWVRSRKWTMLDH",
    "HLMTAHGBGFNIV",
    "MVERZRLQDBHQ",
    "VIOHIKNNGUAB",
    "GKJFHYXODIE",
    "ZUQUPNZN",
]

CORRECTED = list(AS_PRINTED)
CORRECTED[7] = "UGMNCBXCFLDBY"  # Bret Bowen comment #10 / dbourdeau goldbar/NOTES.md photograph check

ALPHABET = string.ascii_uppercase
SEED = 20260925  # today's date (UTC), fixed for reproducibility
N_SHUFFLES = 1000


def chi_squared_uniform(letters):
    n = len(letters)
    expected = n / 26.0
    counts = {c: 0 for c in ALPHABET}
    for ch in letters:
        counts[ch] += 1
    chi2 = sum((counts[c] - expected) ** 2 / expected for c in ALPHABET)
    return chi2, counts


def run_reading(name, lines, rng):
    letters = list("".join(lines))
    n = len(letters)
    target_chi2, counts = chi_squared_uniform(letters)

    control_stats = []
    for _ in range(N_SHUFFLES):
        # fresh i.i.d. uniform random draw of N letters over the 26-letter alphabet --
        # NOT a permutation of the fixed multiset, see module docstring
        draw = [rng.choice(ALPHABET) for _ in range(n)]
        chi2, _ = chi_squared_uniform(draw)
        control_stats.append(chi2)

    control_stats.sort()
    below = sum(1 for x in control_stats if x <= target_chi2)
    percentile = 100.0 * below / N_SHUFFLES
    mean = sum(control_stats) / len(control_stats)
    p5 = control_stats[int(0.05 * N_SHUFFLES)]
    p95 = control_stats[int(0.95 * N_SHUFFLES) - 1]

    return {
        "reading": name,
        "n_letters": n,
        "letter_counts": counts,
        "target_chi_squared_25df": round(target_chi2, 4),
        "control_n_shuffles": N_SHUFFLES,
        "control_mean": round(mean, 4),
        "control_min": round(control_stats[0], 4),
        "control_max": round(control_stats[-1], 4),
        "control_p5": round(p5, 4),
        "control_p95": round(p95, 4),
        "target_below_n_shuffles": below,
        "target_percentile_of_control": round(percentile, 4),
    }


def main():
    rng = random.Random(SEED)
    results = [
        run_reading("as_printed", AS_PRINTED, rng),
        run_reading("bowen_bourdeau_line8_correction", CORRECTED, rng),
    ]
    print(json.dumps({"seed": SEED, "results": results}, indent=2))


if __name__ == "__main__":
    main()
