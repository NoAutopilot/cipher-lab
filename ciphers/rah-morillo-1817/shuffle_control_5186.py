#!/usr/bin/env python3
"""Shuffle-consistency control for key_5186.tsv (CLAUDE.md rule 3, the Szembek lesson: a recurring-code/
recurring-gloss pairing needs a control that can actually fail, not a coverage-only number).

Real score: over every code that recurs (count >= 2) among the 13 clean KEY_WORDS groups (build_key_5186.py),
the fraction of its occurrences that agree with its own majority letter, weighted by occurrence count and
averaged. Shuffle: within each length-matched bucket (a word's gloss can only be swapped onto a cipher-token
sequence of the same token count, or the letter-per-token alignment is undefined), permute which gloss word
is read against which group's tokens, 20 times with a fixed seed list, and recompute the identical statistic.
If the shuffle mean sits near the real score, the recurring-code/recurring-gloss pairing is not discriminating
at this N (the bMAT2/AX-5799 shape CLAUDE.md warns about); if it sits far below, the pairing is a real signal.
"""
import random
import sys
from collections import Counter, defaultdict

from build_key_5186 import KEY_WORDS


def consistency(assignment):
    """assignment: list of (tokens, letters). Returns weighted-mean majority-agreement over recurring codes."""
    pairs = defaultdict(Counter)
    for toks, letters in assignment:
        for t, l in zip(toks, letters):
            pairs[t][l] += 1
    num, den = 0, 0
    for code, c in pairs.items():
        total = sum(c.values())
        if total < 2:
            continue
        top = c.most_common(1)[0][1]
        num += top
        den += total
    return num / den if den else float('nan')


def main():
    groups = [(toks, letters) for _, toks, _, letters in KEY_WORDS]
    real = consistency(groups)

    by_len = defaultdict(list)
    for i, (toks, letters) in enumerate(groups):
        by_len[len(toks)].append(i)

    scores = []
    rng = random.Random(20260926)
    for _ in range(20):
        letters_by_idx = {i: letters for i, (toks, letters) in enumerate(groups)}
        shuffled_letters = dict(letters_by_idx)
        for length, idxs in by_len.items():
            perm = idxs[:]
            rng.shuffle(perm)
            for src, dst in zip(idxs, perm):
                shuffled_letters[dst] = letters_by_idx[src]
        shuffled = [(groups[i][0], shuffled_letters[i]) for i in range(len(groups))]
        scores.append(consistency(shuffled))

    scores.sort()
    mean = sum(scores) / len(scores)
    p95 = scores[int(0.95 * (len(scores) - 1))]
    print(f"real consistency (13 clean groups, recurring codes only): {real:.3f}")
    print(f"shuffle mean over 20 permutations (length-matched): {mean:.3f}, p95 {p95:.3f}, "
          f"range {scores[0]:.3f}-{scores[-1]:.3f}")
    if real - p95 < 0.05:
        print("NON-DISCRIMINATING: shuffle p95 within 0.05 of the real score at this N")
    else:
        print(f"discriminates: real beats shuffle p95 by {real - p95:.3f}")


if __name__ == '__main__':
    main()
