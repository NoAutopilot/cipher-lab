#!/usr/bin/env python3
"""GOLD-4B form test: cryptogram line-length profile vs the c3 clear poem.

Reads lines.tsv (signs per cryptogram line) and clear_poems.tsv (letters and
syllables per poem line, from count_syllables.py), and:
  1. For every cryptogram, reports mean/line and, where the line COUNT
     matches the 14-line c3 poem exactly, the Pearson r between the
     cryptogram's per-line sign counts and the poem's per-line letters and
     syllables (in reading order -- the only pairing that could mean
     "encodes this poem line for line").
  2. Matched control: shuffle the poem's per-line lengths 1000 times and
     recompute r each time against the fixed cryptogram sequence; report the
     percentile of the observed r within that null distribution.
  3. signs/letter and signs/syllable ratios, and a letters-per-12-syllable
     estimate derived from the poem's own data (no external alexandrine
     corpus available -- CLAUDE.md's fr19 is prose).

Output: form_test_result.json (all numbers) plus a printed summary.
"""
import csv
import json
import random
import statistics
import sys

random.seed(20260925)


def read_lines_tsv(path):
    by_page = {}
    order = []
    with open(path) as f:
        r = csv.DictReader(f, delimiter="\t")
        for row in r:
            page = row["page"]
            by_page.setdefault(page, []).append(int(row["signs_per_line"]))
            if page not in order:
                order.append(page)
    return by_page, order


def read_poem(path):
    letters, syll = [], []
    with open(path) as f:
        r = csv.DictReader(f, delimiter="\t")
        for row in r:
            if row["page"] != "c3":
                continue
            if row["line"] in ("title", "banner", "signature"):
                continue
            letters.append(int(row["letters"]))
            syll.append(int(row["syllables"]))
    return letters, syll


def pearson(a, b):
    n = len(a)
    if n < 2:
        return None
    ma, mb = statistics.mean(a), statistics.mean(b)
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    da = sum((x - ma) ** 2 for x in a) ** 0.5
    db = sum((y - mb) ** 2 for y in b) ** 0.5
    if da == 0 or db == 0:
        return None
    return num / (da * db)


def shuffle_control(fixed, to_shuffle, trials=1000):
    obs = pearson(fixed, to_shuffle)
    null = []
    pool = list(to_shuffle)
    for _ in range(trials):
        random.shuffle(pool)
        r = pearson(fixed, pool)
        if r is not None:
            null.append(r)
    below = sum(1 for r in null if r <= obs)
    pct = 100.0 * below / len(null)
    return obs, pct, (min(null), max(null), statistics.mean(null))


def main():
    by_page, order = read_lines_tsv("lines.tsv")
    poem_letters, poem_syll = read_poem("clear_poems.tsv")
    n_poem = len(poem_letters)
    tot_letters = sum(poem_letters)
    tot_syll = sum(poem_syll)
    letters_per_syll = tot_letters / tot_syll
    letters_per_12syll = letters_per_syll * 12

    cryptograms = {
        "c1": ["c1"],
        "c2": ["c2a", "c2b"],
        "c3": ["c3"],
        "c4": ["c4a", "c4b"],
        "c4a_only": ["c4a"],
    }

    result = {
        "poem": {
            "n_lines": n_poem,
            "letters_per_line": poem_letters,
            "syllables_per_line": poem_syll,
            "mean_letters_per_line": tot_letters / n_poem,
            "mean_syllables_per_line": tot_syll / n_poem,
            "letters_per_syllable": letters_per_syll,
            "letters_per_12_syllable_line_estimate": letters_per_12syll,
        },
        "cryptograms": {},
    }

    for name, pages in cryptograms.items():
        signs = []
        for p in pages:
            signs.extend(by_page.get(p, []))
        n = len(signs)
        entry = {
            "n_lines": n,
            "signs_per_line": signs,
            "mean_signs_per_line": sum(signs) / n if n else None,
            "total_signs": sum(signs),
        }
        if n:
            entry["signs_per_letter_ratio_vs_poem_mean"] = (sum(signs) / n) / (tot_letters / n_poem)
            entry["signs_per_syllable_ratio_vs_poem_mean"] = (sum(signs) / n) / (tot_syll / n_poem)
        if n == n_poem:
            obs_r_letters, pct_letters, null_range_l = shuffle_control(signs, poem_letters)
            obs_r_syll, pct_syll, null_range_s = shuffle_control(signs, poem_syll)
            entry["line_count_matches_poem"] = True
            entry["pearson_r_vs_letters_per_line"] = obs_r_letters
            entry["shuffle_control_percentile_letters"] = pct_letters
            entry["shuffle_null_range_letters"] = null_range_l
            entry["pearson_r_vs_syllables_per_line"] = obs_r_syll
            entry["shuffle_control_percentile_syllables"] = pct_syll
            entry["shuffle_null_range_syllables"] = null_range_s
            entry["signs_per_letter_ratio_paired"] = sum(signs) / tot_letters
        else:
            entry["line_count_matches_poem"] = False
            entry["note"] = f"line count {n} != poem's {n_poem}; no per-line pairing possible"
        result["cryptograms"][name] = entry

    with open("form_test_result.json", "w") as f:
        json.dump(result, f, indent=1)

    print(json.dumps(result, indent=1))


if __name__ == "__main__":
    main()
