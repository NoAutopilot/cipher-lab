#!/usr/bin/env python3
"""Permutation z-test (ZX-BAR, 25 Sept 2026) on thurloe-barriere-1654's gloss-derived key.

Question this answers: does the gloss-derived key (key_gloss.tsv) carry information about the UNglossed
tokens of this letter beyond what any assignment of the same code frequencies would? Answered here through a
narrower, sharper proxy: is a held-out gloss OCCURRENCE of a code predictable from that code's OTHER gloss
occurrences, more often than chance permutations of the same data predict it?

Statistic (leave-one-out over every row of key_gloss.tsv -- each row is one glossed code occurrence, grade C,
per NOTES.md s.2/s.3): hold out row i; rebuild a key from every OTHER row (group the remaining rows by code;
a code gets a key value only if every remaining observation of that code agrees on one value after
normalize() below -- exactly key_gloss.tsv's own primary/conflict rule, recomputed fresh each time instead of
reusing the file's fixed status column, since removing one observation can change which codes conflict);
predict row i's value from that key; correct if the code is in the key AND the predicted value normalizes
equal to row i's true value. The statistic is the count of held-out rows predicted correctly, out of N.

normalize(): lowercase, then fold long-s/f, u/v, i/j -- old-spelling/OCR variants that can make the same word
read as two different strings across two gloss occurrences (both sides of every comparison are folded).

Null A (key shuffle): permute the VALUE column among all N observations (codes and their run/position stay
put). This keeps every word's total occurrence count fixed across the letter -- "each word's code count" read
as how many times each word's code appears -- while destroying any real code<->word correspondence.

Null B (token shuffle): within each source_run, permute the CODE column among that run's own rows only (gloss
words stay in their printed positions/order). This tests whether the target's SEQUENTIAL alignment of codes to
gloss words (the method NOTES.md s.2 uses, since typesetting does not column-align a gloss word under its
source token) is itself informative, independent of which codes exist where -- a different question from Null A.

Usage: python3 permutation_test.py [key_gloss.tsv] [--n 1000] [--seed 0]
       python3 permutation_test.py --key key_gloss_marked.tsv [--n 1000] [--seed 0]

--key is an explicit alias for the same positional path argument (ZX-BAR2, 25 Sept 2026, added so a
code+mark key file such as key_gloss_marked.tsv can be named without relying on positional-argument order;
the statistic/nulls are byte-identical to the bare-code run -- this file is not forked, only given a second
way to name its input). key_gloss_marked.tsv uses the same code/value/grade/status/source_run/note schema as
key_gloss.tsv; its 'code' column is the code+mark unit (e.g. "61-circumflex") instead of the bare digit, so
build_key()'s existing per-code grouping automatically treats two marks of the same digit as different keys.
"""
import argparse
import collections
import math
import random


def normalize(w):
    w = w.strip().lower()
    w = w.replace('f', 's')
    w = w.replace('v', 'u')
    w = w.replace('j', 'i')
    return w


def load_observations(path):
    obs = []
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
            code = d['code'].split('(')[0]
            obs.append({'code': code, 'value': d['value'], 'source_run': d['source_run']})
    return obs


def build_key(observations):
    by_code = collections.defaultdict(set)
    for o in observations:
        by_code[o['code']].add(normalize(o['value']))
    return {code: next(iter(vals)) for code, vals in by_code.items() if len(vals) == 1}


def loo_statistic(observations):
    correct = 0
    for i in range(len(observations)):
        rest = observations[:i] + observations[i + 1:]
        key = build_key(rest)
        held = observations[i]
        pred = key.get(held['code'])
        if pred is not None and pred == normalize(held['value']):
            correct += 1
    return correct


def null_a_draw(observations, rng):
    values = [o['value'] for o in observations]
    rng.shuffle(values)
    return [{'code': o['code'], 'value': v, 'source_run': o['source_run']}
            for o, v in zip(observations, values)]


def null_b_draw(observations, rng):
    by_run = collections.defaultdict(list)
    for idx, o in enumerate(observations):
        by_run[o['source_run']].append(idx)
    codes = [o['code'] for o in observations]
    new_codes = list(codes)
    for run_id, idxs in by_run.items():
        run_codes = [codes[i] for i in idxs]
        rng.shuffle(run_codes)
        for i, c in zip(idxs, run_codes):
            new_codes[i] = c
    return [{'code': c, 'value': o['value'], 'source_run': o['source_run']}
            for c, o in zip(new_codes, observations)]


def zscore(real, nulls):
    mean = sum(nulls) / len(nulls)
    sd = math.sqrt(sum((x - mean) ** 2 for x in nulls) / len(nulls))
    z = (real - mean) / sd if sd > 0 else float('nan')
    p = sum(1 for x in nulls if x >= real) / len(nulls)
    return mean, sd, z, p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('keypath', nargs='?', default='key_gloss.tsv')
    ap.add_argument('--key', dest='key_opt', default=None,
                     help='explicit alias for keypath (e.g. --key key_gloss_marked.tsv); overrides the positional arg if given')
    ap.add_argument('--n', type=int, default=1000)
    ap.add_argument('--seed', type=int, default=0)
    args = ap.parse_args()
    if args.key_opt:
        args.keypath = args.key_opt

    observations = load_observations(args.keypath)
    real = loo_statistic(observations)
    n_obs = len(observations)

    rng_a = random.Random(args.seed)
    nulls_a = [loo_statistic(null_a_draw(observations, rng_a)) for _ in range(args.n)]
    rng_b = random.Random(args.seed + 1)
    nulls_b = [loo_statistic(null_b_draw(observations, rng_b)) for _ in range(args.n)]

    mean_a, sd_a, z_a, p_a = zscore(real, nulls_a)
    mean_b, sd_b, z_b, p_b = zscore(real, nulls_b)

    print(f'N observations ({args.keypath}): {n_obs}')
    print(f'real leave-one-out statistic: {real}/{n_obs} ({100 * real / n_obs:.1f}%)')
    print(f'Null A (key shuffle, n={args.n}): mean={mean_a:.3f} sd={sd_a:.3f} z={z_a:.3f} p={p_a:.4f}')
    print(f'Null B (token shuffle, n={args.n}): mean={mean_b:.3f} sd={sd_b:.3f} z={z_b:.3f} p={p_b:.4f}')


if __name__ == '__main__':
    main()
