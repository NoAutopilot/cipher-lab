#!/usr/bin/env python3
"""Collate Hs 1's six-line inscription (untersberg-code) against Herzog 1929's
spelled-out Hs 12 witness, and control the alignment against shuffled word order.

Rule 3 (CLAUDE.md): a match means nothing without a control of the same design.
This script is the control: it runs the identical initial-letter alignment
procedure on the real word order and on N random permutations of the same six
words, and reports both.

Design (see ciphers/untersberg-code/NOTES.md and witnesses.tsv for the source):
Hs 1's six lines each carry several period/space-delimited tokens; Hs 12 gives
six spelled-out Latin words (a seventh, "Orpheus", prints on its own sub-line
below the six-word list and is read as a coda/name, not a 7th line -- excluded
from the aligned set). For each Hs1 line i (i=1..6), and each candidate word
order, test whether ANY of line i's letter-tokens (digits and the two "eth"
glyph tokens excluded -- rule 2, they are not a Latin letter) shares its first
letter with the word placed at position i. Report the count of the six lines
that match (out of 6), for the real order and for 10 shuffles.

Usage: python3 align_witnesses.py
"""
import random
from itertools import permutations

# Hs1 letter-token initials per line (from witnesses.tsv; digits and the two
# "eth" abbreviation-glyph tokens excluded, per rule 2 -- eth is not a Latin
# letter and has no defensible initial to compare).
HS1_LINE_INITIALS = {
    1: ["s", "o", "x"],  # S, occo, x (the two "eth" tokens excluded)
    2: ["s", "a", "f", "l", "d"],  # Satrnrop, a, f, l, d
    3: ["p", "m", "a", "t", "q", "o", "r", "u"],
    4: ["m", "r", "l", "v", "e", "p", "a", "t", "x", "m"],  # tt->t, missm->m
    5: ["a", "o", "u", "s", "g", "c", "x", "l", "a", "m"],  # st->s, alto->a, mvraco->m
    6: ["m", "r", "l", "y", "p", "o", "p", "m", "i", "v", "m", "l", "t", "t", "g"],
}

HS12_WORDS = ["Bellum", "Famus", "Gestas", "Res", "Mores", "Amicus"]  # Orpheus excluded, see docstring


def match_count(word_order):
    """word_order: list of 6 words assigned to lines 1..6 in order. Returns
    how many of the 6 lines contain a letter-token whose initial equals the
    word's initial (case-insensitive)."""
    hits = 0
    for line_no, word in zip(range(1, 7), word_order):
        initial = word[0].lower()
        if initial in HS1_LINE_INITIALS[line_no]:
            hits += 1
    return hits


def main():
    real_hits = match_count(HS12_WORDS)
    print(f"Real Hs12 order: {HS12_WORDS}")
    print(f"Real order match count: {real_hits}/6")

    rng = random.Random(20260925)
    shuffle_hits = []
    for i in range(10):
        shuffled = HS12_WORDS[:]
        rng.shuffle(shuffled)
        h = match_count(shuffled)
        shuffle_hits.append(h)
        print(f"Shuffle {i+1}: {shuffled} -> {h}/6")

    mean = sum(shuffle_hits) / len(shuffle_hits)
    print(f"\nShuffle mean: {mean:.2f}/6, range [{min(shuffle_hits)}, {max(shuffle_hits)}]")
    print(f"Real ({real_hits}/6) vs shuffle mean ({mean:.2f}/6): "
          f"{'ABOVE' if real_hits > mean else ('AT' if real_hits == mean else 'BELOW')} the shuffle mean")
    tie_or_beat = sum(1 for h in shuffle_hits if h >= real_hits)
    print(f"{tie_or_beat}/10 shuffles tie or beat the real order's {real_hits}/6")

    # Bonus rigor (not required by the brief, cheap to compute exactly):
    # all 6! = 720 permutations of the 6 words, exact distribution.
    all_hits = [match_count(list(p)) for p in permutations(HS12_WORDS)]
    exact_mean = sum(all_hits) / len(all_hits)
    ge_real = sum(1 for h in all_hits if h >= real_hits)
    print(f"\nExact distribution over all 720 permutations: mean {exact_mean:.3f}/6, "
          f"range [{min(all_hits)}, {max(all_hits)}]")
    print(f"{ge_real}/720 permutations ({100*ge_real/720:.1f}%) tie or beat the real order's {real_hits}/6 "
          f"-- this is the real order's percentile under an exact permutation test")


if __name__ == "__main__":
    main()
