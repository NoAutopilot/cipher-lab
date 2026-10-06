#!/usr/bin/env python3
"""NA-HYDE test 1: groups-per-name-line vs name letters, against a shuffled-pairing control.
Reads ciphertext_print.txt (print transcription, not the leaf). No key applied."""
import re, random, statistics, collections, os, sys
here = os.path.dirname(os.path.abspath(__file__))
lines = [l.strip() for l in open(os.path.join(here, 'ciphertext_print.txt')) if l.strip() and not l.startswith('#')]
name_lines = []
for l in lines:
    m = re.match(r'^((?:\d+\.?\s*)+)\s*(?:Mr\.\s+)?([A-Z][a-z]+)\.?$', l)
    if m and 'pray' not in l:
        nums = re.findall(r'\d+', m.group(1)); name_lines.append((nums, m.group(2), l))
n = len(name_lines)
cnt = [len(x[0]) for x in name_lines]; let = [len(x[1]) for x in name_lines]
def agree(c, L): return sum(a == b for a, b in zip(c, L)) / len(c)
def corr(a, b):
    return statistics.correlation(a, b)
def within1(c, L): return sum(abs(a-b) <= 1 for a, b in zip(c, L)) / len(c)
t_ag, t_cr, t_w1 = agree(cnt, let), corr(cnt, let), within1(cnt, let)
random.seed(20261006)
D = 1000; ag = []; cr = []; w1 = []
for _ in range(D):
    p = cnt[:]; random.shuffle(p)
    ag.append(agree(p, let)); cr.append(corr(p, let)); w1.append(within1(p, let))
def pct(xs, v): return sum(x >= v for x in xs) / len(xs)
print(f"name lines N={n}; groups total {sum(cnt)}; letters total {sum(let)}")
print("per line (groups,letters,name):", [(c, l, x[1]) for c, l, x in zip(cnt, let, name_lines)])
print(f"count distribution groups: {sorted(collections.Counter(cnt).items())}; letters: {sorted(collections.Counter(let).items())}")
for nm, t, c in (("exact agreement", t_ag, ag), ("within-1 agreement", t_w1, w1), ("Pearson r", t_cr, cr)):
    print(f"{nm}: target {t:.3f}; control mean {statistics.mean(c):.3f} sd {statistics.stdev(c):.3f} p95 {sorted(c)[949]:.3f} max {max(c):.3f}; P(control>=target)={pct(c,t):.3f}")
# repeats by position
for v in ('670', '101', '25'):
    pos = []
    for i, (nums, nm, l) in enumerate(name_lines):
        for j, x in enumerate(nums):
            if x == v: pos.append((i, j, len(nums)))
    first = sum(1 for _, j, _ in pos if j == 0); last = sum(1 for _, j, k in pos if j == k-1)
    print(f"repeat {v}: {len(pos)} in name lines (line,pos,len)={pos}; first-in-line {first}, last-in-line {last}")
