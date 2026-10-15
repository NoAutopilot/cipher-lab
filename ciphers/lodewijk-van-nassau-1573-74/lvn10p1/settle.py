#!/usr/bin/env python3
"""LVN-3R (15 Oct 2026): score the blind per-token read of 4610 p1 (lvn10p1/reads.tsv) against lvn10p1/key.tsv under
lvn10p1/PREREG-LVN-3R.md -- control gate >= 8/10 exact; then a target settles when the read equals A150 or B150 exactly
(no '?'), H only when the value is a key_full.tsv code (else M kept). Writes lvn10p1/settle.tsv, which lvn10/apply.py
applies last. --check: exit 1 if settle.tsv is stale (rule 7)."""
import csv, io, os, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
key = rd(os.path.join(H, 'key.tsv')); rs = {r['tid']: r['read'] for r in rd(os.path.join(H, 'reads.tsv'))}
codes = {r['code'] for r in rd(os.path.join(T, 'key_full.tsv'))}
ctl = [rs[k['tid']] == k['sign'] for k in key if k['role'] == 'control']
gate = sum(ctl) >= 8
print('control %d/%d, gate %s' % (sum(ctl), len(ctl), 'PASS' if gate else 'FAIL'))
rows = []
for k in sorted((k for k in key if k['role'] == 'target'), key=lambda k: (k['line'], int(k['position']))):
    rd_ = rs[k['tid']]; ok = gate and '?' not in rd_ and rd_ in (k['A150'], k['B150'])
    conf = ('H' if rd_ in codes else 'M') if ok else 'M'
    act = ('settled' if rd_ != k['sign'] else 'confirmed') if ok and conf == 'H' else ('read-confirmed-not-key-code' if ok else 'stays')
    rows.append([k['line'], k['position'], k['sign'], rd_ if ok else k['sign'], conf, act,
                 f"lvn3r per-token 300-dpi read {rd_} (A150 {k['A150']}, B150 {k['B150']}; {k['tid']}; control {sum(ctl)}/10)"])
s = io.StringIO(); s.write('line\tpre_pos\told\tnew\tconfidence\taction\tnote\n')
for r in rows: s.write('\t'.join(r) + '\n')
p = os.path.join(H, 'settle.tsv')
if '--check' in sys.argv:
    st = not os.path.exists(p) or open(p).read() != s.getvalue(); print('STALE' if st else 'up to date'); sys.exit(1 if st else 0)
open(p, 'w').write(s.getvalue())
from collections import Counter; print(Counter(r[5] for r in rows))
