#!/usr/bin/env python3
"""THU-1 gate G2 (pre-registered in .claude/briefs/runs/2026-10-07-acct2-st-rebuild-workers.md):
decode each glossed Birch sibling's cipher groups with the CURRENT key and score group-level agreement
with the sibling's own printed gloss (as aligned by tools/interlinear_align.py align, run with NO prior,
so the alignment does not see the key), against 200 shuffled keys (the key's value->meaning map permuted).
PASS (same key) = real >= 0.70 and real > shuffle p95.

Scored token: kind num, value in the key, non-empty plain chunk. Agreement: chunk == key meaning after
lower-casing, letters only, long-s f->s and v->u folds (the tool's own folds). The shuffle permutes which
meaning sits on which value, so it changes the statistic.

usage: g2_gate.py KEY.tsv ALIGN.tsv [ALIGN.tsv ...]   (prints one TSV row per align file)
"""
import csv, random, re, sys

def norm(s):
    s = re.sub(r'[^a-z]', '', s.lower())
    return s.replace('f', 's').replace('v', 'u')

def load_key(p):
    k = {}
    for r in csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'):
        v, m = r['value'].strip(), norm(r['meaning'])
        if v and m:
            k[v] = m
    return k

def tokens(p):
    out = []
    for r in csv.DictReader(open(p), delimiter='\t'):
        if r['kind'] != 'num' or not r['value']:
            continue
        c = norm(r['plain_chunk'])
        if c:
            out.append((r['value'], c))
    return out

def score(key, toks):
    sc = [(v, c) for v, c in toks if v in key]
    if not sc:
        return 0, 0, float('nan')
    a = sum(key[v] == c for v, c in sc)
    return a, len(sc), a / len(sc)

def main():
    key = load_key(sys.argv[1])
    vals, means = list(key), list(key.values())
    print('align\tscored\tall_num_tokens\tagree\treal\tshuffle_mean\tshuffle_p95\tverdict')
    for p in sys.argv[2:]:
        toks = tokens(p)
        a, n, real = score(key, toks)
        rng = random.Random(1656)
        draws = []
        for _ in range(200):
            m = means[:]; rng.shuffle(m)
            draws.append(score(dict(zip(vals, m)), toks)[2])
        draws.sort()
        mean = sum(draws) / len(draws); p95 = draws[int(0.95 * len(draws)) - 1]
        ok = n >= 5 and real >= 0.70 and real > p95
        print(f'{p.split("/")[-1]}\t{n}\t{len(toks)}\t{a}\t{real:.3f}\t{mean:.3f}\t{p95:.3f}\t{"PASS" if ok else "FAIL"}')

if __name__ == '__main__':
    main()
