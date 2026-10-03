#!/usr/bin/env python3
"""Error figures for the fr.3019 / fr.2988 two-witness check (A1B-RANZO-2WIT, pre-registration in NOTES.md).

  python3 twowit_stats.py

Reads twowit_diff.tsv (classes settled on native crops of both copies), fr3019_no27_tokens.tsv (reconciled read),
fr3019_no27_settled.tsv and passes/*.tsv. Prints: raw two-copy agreement; per-token reader error of the reconciled
fr.3019 read ((R3019+R2)/tokens) and of Bourdeau's read ((RB+RB-sg+R2)/tokens, and without the s/g label rows), each with
Wilson 95% and the U range; and each single blind pass's error against the settled read (per line, edit operations over
settled tokens, U positions excluded). Positions where both copies' readers agree are taken as correct, so every figure
is a lower bound; the settled read inherits the passes' agreed tokens, so the single-pass figures favour the passes.
"""
import csv, difflib, math, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SKIP = {'/', '|', '/.'}


def wilson(k, n, z=1.96):
    if n == 0:
        return (0, 0)
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - h) / d, (c + h) / d)


def fmt(k, n):
    lo, hi = wilson(k, n)
    return f'{k}/{n} = {k / n:.3f} (95% {lo:.3f}-{hi:.3f})'


rd = lambda f: list(csv.DictReader(open(os.path.join(HERE, f)), delimiter='\t'))
diff = rd('twowit_diff.tsv')
ours = [r for r in rd('fr3019_no27_tokens.tsv') if r['token'] not in SKIP]
nb = sum(len([t for t in l.split() if t not in SKIP]) for f in ('ranzo_c006.txt', 'ranzo_c007.txt')
         for l in open(os.path.join(HERE, 'bourdeau', f)) if not l.startswith('#'))
cl = Counter(r['class'] for r in diff)
print(f"tokens: fr.3019 reconciled {len(ours)}, Bourdeau fr.2988 {nb}; disagreement rows {len(diff)}: " +
      ', '.join(f'{k} {v}' for k, v in sorted(cl.items())))
U = cl['U']
r3 = cl['R3019'] + cl['R2']
rb = cl['RB'] + cl['RB-sg'] + cl['R2']
print('fr.3019 reconciled read error:', fmt(r3, len(ours)), f'; if all {U} U were ours: {(r3 + U) / len(ours):.3f}')
print('Bourdeau fr.2988 read error:  ', fmt(rb, nb), f'; without the {cl["RB-sg"]} s/g label rows:', fmt(rb - cl['RB-sg'], nb),
      f'; if all {U} U were his: {(rb + U) / nb:.3f}')
print('copy variants (V):', cl['V'], f'= {cl["V"] / len(ours):.3f} per token')
# single passes vs the settled read
settled = {}
for r in rd('fr3019_no27_settled.tsv'):
    settled.setdefault(r['line'], []).append(r)
upos = {(r['line'], r['pos']) for r in diff if r['class'] == 'U' and r['line']}
for p in ('A', 'B', 'C'):
    errs = n = 0
    for f in sorted(os.listdir(os.path.join(HERE, 'passes'))):
        if not f.startswith(f'pass{p}-'):
            continue
        pl = {}
        for r in rd(os.path.join('passes', f)):
            if r['token'] not in SKIP:
                pl.setdefault(r['line'], []).append(r['token'].replace('?', '') or '?')
        for line, toks in pl.items():
            truth = [t for t in settled.get(line, []) if t['token'] not in SKIP]
            tt = [t['token'] for t in truth]
            for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, tt, toks, autojunk=False).get_opcodes():
                ks = [k for k in range(i1, i2) if (line, truth[k]['pos']) not in upos]
                if op == 'equal':
                    n += len(ks)
                elif op in ('replace', 'delete'):
                    n += len(ks); errs += min(len(ks), max(i2 - i1, j2 - j1)) if ks else 0
                    if op == 'replace' and j2 - j1 > i2 - i1:
                        errs += j2 - j1 - (i2 - i1)
                else:
                    errs += j2 - j1
    if n:
        print(f'single pass {p} vs settled read (pages it covers):', fmt(errs, n))
