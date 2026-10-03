#!/usr/bin/env python3
"""READ2-ROELL: score the inv. 164 function-word codes against the letter (PREREG.md).

python3 inv164/score.py [--codes inv164/function_codes.tsv] [--sets 1000] [--seed 1]
Reads function_codes.tsv (word, code, grade...; rows with grade 'x' are skipped), the letter's groups
(decode_transcription/R1469_groups.txt + R1470_groups.txt), and prints S1/S2 for the target and for two
random-code-set controls: (a) uniform from the integers the read sheets cover, (b) uniform from 1..3000.
"""
import argparse, collections, os, random, statistics
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
ap = argparse.ArgumentParser()
ap.add_argument('--codes', default=os.path.join(here, 'function_codes.tsv'))
ap.add_argument('--sets', type=int, default=1000)
ap.add_argument('--seed', type=int, default=1)
ap.add_argument('--covered', default='1-1000,2001-3000', help='integer ranges the read sheets cover')
a = ap.parse_args()
groups = []
for f in ('R1469_groups.txt', 'R1470_groups.txt'):
    groups += [int(x) for x in open(os.path.join(root, 'decode_transcription', f)).read().split() if x.isdigit()]
freq = collections.Counter(groups)
top20 = {c for c, _ in freq.most_common(20)}
codes = {}
for line in open(a.codes):
    p = line.rstrip('\n').split('\t')
    if not p or p[0] in ('word', '') or p[0].startswith('#'):
        continue
    if len(p) > 2 and p[2].strip().lower() == 'x':
        continue
    codes[int(p[1])] = p[0]
k = len(codes)
S1 = sum(freq[c] for c in codes); S2 = sum(1 for c in codes if c in top20)
print(f'letter groups {len(groups)}, distinct {len(freq)}; read function-word codes k={k}')
for c in sorted(codes):
    print(f'  {codes[c]:>6} {c:>5}  letter freq {freq[c]}' + ('  TOP20' if c in top20 else ''))
print(f'TARGET S1={S1} ({100*S1/len(groups):.2f}% of groups)  S2={S2}')
def ranges(s):
    out = []
    for r in s.split(','):
        lo, hi = r.split('-'); out += range(int(lo), int(hi) + 1)
    return out
rng = random.Random(a.seed)
for name, pool in (('covered ' + a.covered, ranges(a.covered)), ('1-3000', list(range(1, 3001)))):
    s1s, s2s = [], []
    for _ in range(a.sets):
        st = rng.sample(pool, k)
        s1s.append(sum(freq[c] for c in st)); s2s.append(sum(1 for c in st if c in top20))
    s1s.sort(); s2s.sort()
    p99 = s1s[int(0.99 * a.sets) - 1]; p992 = s2s[int(0.99 * a.sets) - 1]
    ge = sum(1 for x in s1s if x >= S1)
    print(f'CONTROL {name}: S1 mean {statistics.mean(s1s):.1f} p95 {s1s[int(.95*a.sets)-1]} p99 {p99} max {s1s[-1]}; '
          f'S2 mean {statistics.mean(s2s):.2f} p99 {p992}; sets with S1>=target {ge}/{a.sets}; '
          f'{"PASS" if S1 > p99 else "FAIL"} (S1 > p99)')
