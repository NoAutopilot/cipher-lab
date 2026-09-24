#!/usr/bin/env python3
"""One-system test (brief point 3) over tokens.tsv's cipher-line tokens only
(line_is_cipher == yes) -- inline PLAIN-line numerals are excluded here since
they are a handful of clear numeral asides (dates, counts, "the (16) sail"),
not part of the cipher stream itself, and would distort the frequency/IC
comparison. Read-only report; pasted into NOTES.md section 12 by hand.
"""
import csv
import math
from collections import Counter

LETTERS = ['P4', 'P5_P6', 'P7']


def load():
    by_letter = {l: [] for l in LETTERS}
    with open('tokens.tsv', encoding='utf-8') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            if row['line_is_cipher'] != 'yes':
                continue
            core = row['cleaned'].rstrip('.,;:')
            if row['doubtful'] == 'yes' or not core.isdigit():
                continue
            by_letter[row['letter']].append(int(core))
    return by_letter


def ic(values):
    c = Counter(values)
    n = len(values)
    if n < 2:
        return 0.0
    num = sum(v * (v - 1) for v in c.values())
    return num / (n * (n - 1))


def main():
    by_letter = load()
    all_vals = []
    for l in LETTERS:
        v = by_letter[l]
        all_vals.extend(v)
        c = Counter(v)
        n = len(v)
        distinct = len(c)
        top5 = c.most_common(5)
        three_digit = sum(1 for x in v if x >= 100)
        print(f'=== {l}: n={n} distinct={distinct} range={min(v) if v else "-"}-{max(v) if v else "-"} '
              f'IC={ic(v):.4f} 3digit={three_digit} ({three_digit/n*100:.1f}%)')
        print(f'    top5 values: {top5}')
        bigrams = Counter(zip(v, v[1:]))
        print(f'    top bigrams: {bigrams.most_common(5)}')

    print()
    print('=== cross-letter: values seen in >=2 of the 3 texts ===')
    sets = {l: set(by_letter[l]) for l in LETTERS}
    common_all3 = sets['P4'] & sets['P5_P6'] & sets['P7']
    common_any2 = (sets['P4'] & sets['P5_P6']) | (sets['P4'] & sets['P7']) | (sets['P5_P6'] & sets['P7'])
    print('shared by all 3:', sorted(common_all3))
    print('shared by >=2:', sorted(common_any2))

    print()
    print('=== combined pool (all 3 cipher texts) ===')
    c = Counter(all_vals)
    n = len(all_vals)
    print(f'n={n} distinct={len(c)} IC={ic(all_vals):.4f}')
    print('rank-frequency (top 15):')
    for val, cnt in c.most_common(15):
        print(f'  {val}: {cnt} ({cnt/n*100:.2f}%)')

    # rough English-letter IC comparison for reference (~0.0667 for English text,
    # ~1/26=0.0385 for uniform random over 26 symbols)
    print()
    print('reference: English-text letter IC ~0.0667; uniform-26 IC ~0.0385; uniform-N IC ~1/N')


if __name__ == '__main__':
    main()
