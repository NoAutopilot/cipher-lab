#!/usr/bin/env python3
"""Classify DECODE R9590 p1 (lines 1-8, 90 groups) against the main code and the R9586/R9588 second code.

Control (rule 3): 200 random 90-group windows from each known code (seed 1). Statistics: share of groups carrying a
main key.tsv value; hits on each code's 20 most frequent groups. All three depend on the group values, so a window of
either code CAN score like or unlike the target (the control is not orthogonal to the statistic).
Usage: python3 ciphers/castelcicala-1816/r9590/classify.py   (A2-CAS3, 2 Oct 2026)
"""
import collections, os, random, re, statistics as st
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(D)
g = [x for l in open(os.path.join(D, 'p1_lines1-8.txt')) if not l.startswith('#') for x in l.split()]
key = {}
for l in open(os.path.join(T, 'key.tsv')):
    if l.startswith('#') or not l.strip(): continue
    p = l.rstrip('\n').split('\t'); key[p[0]] = p[1]
main = [x for l in open(os.path.join(T, 'ciphertext.txt')) if '|' in l for x in l.split('|')[1].split() if x != 'NULL']
sc = []
for f in ('R9586.txt', 'R9588.txt'):
    for l in open(os.path.join(T, 'second_code', f)):
        s = l.strip()
        if s and not l.startswith(('#', 'P:', 'C:')) and re.fullmatch(r'[\d\s?^.]+', s): sc += re.findall(r'\d+', s)
mtop = {x for x, _ in collections.Counter(main).most_common(20)}
stop = {x for x, _ in collections.Counter(sc).most_common(20)}
stats = lambda w: (sum(x in key for x in w) / len(w), sum(x in mtop for x in w), sum(x in stop for x in w))
random.seed(1)
for name, seq in (('main-code windows', main), ('second-code windows', sc)):
    w = [stats(seq[i:i + 90]) for i in (random.randrange(len(seq) - 90) for _ in range(200))]
    for k, lab in enumerate(('mainkey_cov', 'main_top20_hits', 'second_top20_hits')):
        v = sorted(t[k] for t in w); print(f'{name}\t{lab}\tmean {st.mean(v):.3f}\tp05 {v[10]:.3f}\tp95 {v[189]:.3f}')
print('R9590 p1 (%d groups)\tmainkey_cov %.3f\tmain_top20_hits %d\tsecond_top20_hits %d' % ((len(g),) + stats(g)))
