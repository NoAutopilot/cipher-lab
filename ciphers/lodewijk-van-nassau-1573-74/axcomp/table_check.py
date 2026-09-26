#!/usr/bin/env python3
"""AX-COMP: which table does letter N use? Decode its three longest runs of consecutive codes 1-120 under
key_full.tsv and under key_5799.tsv and print them side by side, plus the share of run tokens each key covers.
    python3 axcomp/table_check.py N"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); TOP = os.path.dirname(HERE)
n = sys.argv[1]
def key(p):
    return {r['code']: r['value'] for r in csv.DictReader(open(os.path.join(TOP, p), encoding='utf-8'), delimiter='\t')}
kf, k99 = key('key_full.tsv'), key('key_5799.tsv')
toks = [r['sign'] for r in csv.DictReader(open(os.path.join(TOP, 'ciphertext_%s.tsv' % n), encoding='utf-8'), delimiter='\t')]
runs, cur = [], []
for t in toks:
    if t.isdigit() and 1 <= int(t) <= 120:
        cur.append(t)
    else:
        if cur: runs.append(cur)
        cur = []
if cur: runs.append(cur)
runs.sort(key=len, reverse=True)
for k, run in enumerate(runs[:3], 1):
    a = ''.join(kf.get(t, '?') if len(kf.get(t, '?')) == 1 else '?' for t in run)
    b = ''.join(k99.get(t, '?') if len(k99.get(t, '?')) == 1 else '?' for t in run)
    print('run %d (%d codes)\n  key_full : %s\n  key_5799 : %s' % (k, len(run), a, b))
allrun = [t for r in runs for t in r]
cov = lambda k: sum(1 for t in allrun if t in k) / max(1, len(allrun))
print('coverage of all 1-120 tokens: key_full %.3f, key_5799 %.3f (n=%d)' % (cov(kf), cov(k99), len(allrun)))
