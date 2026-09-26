#!/usr/bin/env python3
"""ARM-S2: check the reconciled top-12 shorthand shape shares against (a) an
English letter-frequency hypothesis and (b) a Zipf word/syllable-sign hypothesis.
Reads INVENTORY_reconciled.tsv, no network. Usage: python3 profile_check.py"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# Mayzner/Norvig-style English single-letter frequencies (percent of letters), top 12.
ENGLISH_LETTER_FREQ = [
    ("e", 12.7), ("t", 9.1), ("a", 8.2), ("o", 7.5), ("i", 7.0), ("n", 6.7),
    ("s", 6.3), ("h", 6.1), ("r", 6.0), ("d", 4.3), ("l", 4.0), ("c", 2.8),
]

# Approximate share of running-text word tokens taken by the top English words
# (Brown-corpus-order-of-magnitude figures: the, of, and, a, to, in, ...).
ZIPF_TOP_WORDS = [
    ("the", 7.0), ("of", 3.5), ("and", 2.9), ("to", 2.6), ("a", 2.3),
    ("in", 2.1), ("that", 1.1), ("is", 1.0), ("was", 0.9), ("he", 0.9),
    ("for", 0.8), ("it", 0.8),
]


def load_reconciled(path):
    rows = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            rows.append(row)
    rows.sort(key=lambda r: -float(r["count"]))
    return rows


# Grand total of ALL catalogued marks across both passes (INVENTORY.tsv count
# column: pass A 105.5 [treating S11's "1-2 uncertain" as 1.5] + pass B 116),
# NOT just the sum of the reconciled top-12 (189) -- shares must be "of all
# marks" per the brief, so the ~32.5-mark hapax/pair tail (shapes seen 1-2
# times, excluded from the reconciled top-12 as individually too rare to test
# a frequency claim) still counts in the denominator.
TOTAL_ALL_MARKS = 221.5


def main():
    path = os.path.join(HERE, "INVENTORY_reconciled.tsv")
    rows = load_reconciled(path)
    top12_sum = sum(float(r["count"]) for r in rows)
    total = TOTAL_ALL_MARKS
    print(f"reconciled top-12 shapes: {len(rows)}, marks covered by them: {top12_sum:.0f}, "
          f"grand total (all marks, both passes): {total}")
    print()
    print(f"{'rank':<5}{'id':<5}{'count':<7}{'share%':<9}{'top eng letter':<18}{'top word':<14}")
    for i, r in enumerate(rows):
        share = 100.0 * float(r["count"]) / total
        letter, lfreq = ENGLISH_LETTER_FREQ[i] if i < len(ENGLISH_LETTER_FREQ) else ("-", 0)
        word, wfreq = ZIPF_TOP_WORDS[i] if i < len(ZIPF_TOP_WORDS) else ("-", 0)
        print(f"{i+1:<5}{r['id']:<5}{r['count']:<7}{share:<9.1f}"
              f"{letter+' '+str(lfreq)+'%':<18}{word+' '+str(wfreq)+'%':<14}")

    top = rows[0]
    top_share = 100.0 * float(top["count"]) / total
    max_letter_freq = ENGLISH_LETTER_FREQ[0][1]
    max_word_freq = ZIPF_TOP_WORDS[0][1]
    print()
    print(f"Top shape ({top['id']}) share = {top_share:.1f}%.")
    print(f"  vs. max single English letter frequency ('e') = {max_letter_freq}% "
          f"-> ratio {top_share/max_letter_freq:.2f}x")
    print(f"  vs. max single common-word share ('the') = {max_word_freq}% "
          f"-> ratio {top_share/max_word_freq:.2f}x")
    if top_share > 2 * max_letter_freq and top_share > 2 * max_word_freq:
        print("  VERDICT: fits neither hypothesis (a letter alphabet or a Zipf "
              "word/syllable sign) -- too high a share for any single letter or "
              "common word in continuous English prose. Consistent with a "
              "structural/connector stroke (a vowel mark, syllable joiner, or "
              "line-filler) rather than a phonetic letter or lexical sign.")
    core_only = 61.0  # A-S5 + B-Sh.1 only, excluding the two "partial" family variants
    core_share = 100.0 * core_only / total
    print(f"  If only the visually-confirmed core of the top shape is counted "
          f"(excluding the two 'partial' family variants), share = {core_share:.1f}% "
          f"-- still {core_share/max_letter_freq:.2f}x the top English letter and "
          f"{core_share/max_word_freq:.2f}x the top common word.")

    print()
    print("Ranks 2-3 (13.1%, 10.8%) sit closer to the range of mid/high-frequency "
          "English letters ('t' 9.1%, 'a' 8.2%) but on the high side; the low-tail "
          "shapes (ranks 8-12, 0.9-2.3%) are compatible with either a rare letter "
          "or a rare word/syllable sign and are not individually diagnostic at "
          "these counts (rule 3: too few occurrences to test a frequency claim).")


if __name__ == "__main__":
    main()
