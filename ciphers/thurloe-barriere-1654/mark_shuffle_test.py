#!/usr/bin/env python3
"""ZX-BAR2, 25 Sept 2026: does splitting the 9+ bare-code conflicts in key_gloss.tsv by mark resolve more of
them than pinning the SAME marks onto the SAME tokens at random would? Brief step 2's first result (before the
permutation_test.py rerun in step 3, which a near-universal singleton-per-code+mark split makes uninformative
on its own -- see NOTES.md).

Real statistic: for every bare code flagged 'conflict' in key_gloss.tsv with >1 observation (excludes the
single-observation '24' row, whose 'conflict' status is a data-entry quirk noted in its own row -- a code
cannot conflict with itself), count it RESOLVED if every one of its code+mark variants (from
key_gloss_marked.tsv) has exactly one distinct normalized value.

Null: permute the 64 marks among the 64 (code, value) pairs (fixed seed, 1000 draws) -- keeps the real mark
frequencies and the real code/value pairing, destroys which specific token got which specific mark -- and
recompute how many of the same bare codes would be "resolved" by that random pairing.

Usage: python3 mark_shuffle_test.py [--n 1000] [--seed 0]
"""
import argparse
import collections
import random


def normalize(w):
    w = w.strip().lower()
    return w.replace('f', 's').replace('v', 'u').replace('j', 'i')


def load_marked(path='key_gloss_marked.tsv'):
    rows = []
    with open(path) as f:
        header = None
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            row = line.rstrip('\n').split('\t')
            if header is None:
                header = row
                continue
            d = dict(zip(header, row))
            base = d['code'].split('(')[0]
            bare, mark = base.rsplit('-', 1)
            rows.append({'bare': bare, 'mark': mark, 'value': normalize(d['value'])})
    return rows


def conflicting_bare_codes(rows):
    by_bare = collections.defaultdict(set)
    for r in rows:
        by_bare[r['bare']].add(r['value'])
    return {b for b, v in by_bare.items() if len(v) > 1}


def count_resolved(rows, conflicting):
    by_bare_mark = collections.defaultdict(set)
    for r in rows:
        by_bare_mark[(r['bare'], r['mark'])].add(r['value'])
    by_bare_variants = collections.defaultdict(list)
    for (bare, mark), vals in by_bare_mark.items():
        by_bare_variants[bare].append(len(vals))
    return sum(1 for c in conflicting if max(by_bare_variants[c]) == 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=1000)
    ap.add_argument('--seed', type=int, default=0)
    args = ap.parse_args()

    rows = load_marked()
    conflicting = conflicting_bare_codes(rows)
    real_resolved = count_resolved(rows, conflicting)

    rng = random.Random(args.seed)
    marks = [r['mark'] for r in rows]
    null_counts = []
    for _ in range(args.n):
        shuffled = list(marks)
        rng.shuffle(shuffled)
        draw_rows = [{'bare': r['bare'], 'mark': m, 'value': r['value']} for r, m in zip(rows, shuffled)]
        null_counts.append(count_resolved(draw_rows, conflicting))

    mean = sum(null_counts) / len(null_counts)
    sd = (sum((x - mean) ** 2 for x in null_counts) / len(null_counts)) ** 0.5
    z = (real_resolved - mean) / sd if sd > 0 else float('nan')
    p = sum(1 for x in null_counts if x >= real_resolved) / len(null_counts)

    print(f'{len(conflicting)} bare codes flagged conflict in key_gloss.tsv with >1 observation: {sorted(conflicting)}')
    print(f'real: {real_resolved}/{len(conflicting)} resolved by the ACTUAL marks read from the image')
    print(f'shuffle null (marks permuted among the same 64 tokens, n={args.n}, seed={args.seed}): '
          f'mean={mean:.3f} sd={sd:.3f} z={z:.3f} p={p:.4f}')
    print(f'null distribution range: {min(null_counts)}-{max(null_counts)}')


if __name__ == '__main__':
    main()
