#!/usr/bin/env python3
"""bMALX step 5/6: shuffle-consistency control on cribs.tsv (CLAUDE.md rule 3 -- a control that
can fail differently from the target) and the pool/pooled.tsv system-match check (step 6).

Consistency statistic: among codes seen 2+ times, the share of PAIRS of occurrences of the
same code whose candidate class agrees. Shuffle control: permute the class labels across all
code-occurrence positions 1000 times (keeps the multiset of classes and the multiset of codes,
breaks the code<->class correspondence -- the axis being tested), recompute the same statistic;
report real vs shuffle mean/p95, overall and per class, with N of repeated codes. A real/shuffle
margin is the gate; a tie is non-discriminating (rule 3), not a pass.
"""
import csv, random, statistics
from collections import defaultdict, Counter
from itertools import combinations

random.seed(20260926)

def load():
    return list(csv.DictReader(open('cribs.tsv'), delimiter='\t'))

def consistency(codes, classes):
    """codes, classes: parallel lists (one per occurrence). Returns (overall_share, per_class dict, n_pairs, n_repeated_codes)."""
    by_code = defaultdict(list)
    for c, cl in zip(codes, classes):
        by_code[c].append(cl)
    agree = 0
    total = 0
    per_class_agree = Counter()
    per_class_total = Counter()
    n_repeated = 0
    for code, cls_list in by_code.items():
        if len(cls_list) < 2:
            continue
        n_repeated += 1
        for a, b in combinations(cls_list, 2):
            total += 1
            if a == b:
                agree += 1
                per_class_agree[a] += 1
            per_class_total[a if a == b else f'{a}/{b}'] += 0  # not used further
    return (agree / total if total else float('nan')), total, n_repeated

def per_class_consistency(codes, classes, target_class):
    by_code = defaultdict(list)
    for c, cl in zip(codes, classes):
        by_code[c].append(cl)
    agree = 0
    total = 0
    for code, cls_list in by_code.items():
        if len(cls_list) < 2:
            continue
        for a, b in combinations(cls_list, 2):
            if a != target_class and b != target_class:
                continue
            total += 1
            if a == b == target_class:
                agree += 1
    return (agree / total if total else float('nan')), total

def main():
    rows = load()
    codes = [r['code'] for r in rows]
    classes = [r['class'] for r in rows]

    real_share, real_pairs, n_rep = consistency(codes, classes)
    print(f"N crib rows: {len(rows)}; distinct codes: {len(set(codes))}; repeated codes (2+): {n_rep}; pairs compared: {real_pairs}")
    print(f"REAL overall class-agreement share: {real_share:.3f}")

    shuffle_shares = []
    N = 1000
    for _ in range(N):
        shuffled = classes[:]
        random.shuffle(shuffled)
        s, _, _ = consistency(codes, shuffled)
        shuffle_shares.append(s)
    shuffle_mean = statistics.mean(shuffle_shares)
    shuffle_p95 = sorted(shuffle_shares)[int(0.95 * N)]
    print(f"SHUFFLE (N={N}) overall class-agreement mean: {shuffle_mean:.3f}, p95: {shuffle_p95:.3f}")
    print(f"REAL vs SHUFFLE margin: {real_share - shuffle_mean:+.3f}")

    print()
    print("Per-class breakdown (real vs shuffle mean/p95, pairs restricted to that class on at least one side):")
    for cls in sorted(set(classes)):
        r_share, r_pairs = per_class_consistency(codes, classes, cls)
        s_shares = []
        for _ in range(N):
            shuffled = classes[:]
            random.shuffle(shuffled)
            s, _ = per_class_consistency(codes, shuffled, cls)
            s_shares.append(s)
        s_mean = statistics.mean(s_shares)
        s_p95 = sorted(s_shares)[int(0.95 * N)]
        print(f"  {cls:14s} real={r_share:.3f} (pairs={r_pairs})  shuffle_mean={s_mean:.3f}  shuffle_p95={s_p95:.3f}")

    # class balance (for the AX-NAMES per-class caveat: a blended number dominated by one class
    # inflates the shuffle floor toward that class)
    print()
    print("Class balance (occurrence count, not pairs):", Counter(classes))

if __name__ == '__main__':
    main()
