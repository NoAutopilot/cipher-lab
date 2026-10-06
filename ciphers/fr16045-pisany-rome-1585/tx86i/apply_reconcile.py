#!/usr/bin/env python3
"""D2-PIS275 (PREREG kp86j step 3): rebuild tx86i/local_ciphertext.tsv = tx86h/local_ciphertext.tsv (R) with only the eye-settled
columns of tx86i/cmp/disagreements.tsv (R vs reader C) changed, per tx86i/reconcile_log.tsv (line, col, old, new, why; new '-' = drop).
--check: exit 1 if the committed tx86i/local_ciphertext.tsv differs from the rebuild; with no log rows the rebuild must equal R."""
import csv, os, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
dis = {(r['line'], int(r['col'])): r for r in csv.DictReader(open(os.path.join(H, 'cmp/disagreements.tsv')), delimiter='\t')}
log = {(r['line'], int(r['col'])): r for r in csv.DictReader(open(os.path.join(H, 'reconcile_log.tsv')), delimiter='\t')}
R = {l.split('\t')[0]: l.rstrip('\n').split('\t')[1].split() for l in open(os.path.join(T, 'tx86h/local_ciphertext.tsv'))}
# column -> R value: walk C-vs-R alignment; R value is disagreements' A, or for agree columns the next R token
out = {}
for ln, toks in R.items():
    cols = sorted(c for (l, c) in dis if l == ln); ncol = max(cols + [0]); i = 0; new = []; c = 0
    while i < len(toks) or (ln, c + 1) in dis:
        c += 1
        d = dis.get((ln, c))
        rv = d['A'] if d else toks[i]
        if rv not in ('-', ''):
            assert rv == toks[i], (ln, c, rv, toks[i]); i += 1
        e = log.get((ln, c))
        if e:
            assert e['old'] == rv, (ln, c, e['old'], rv)
            v = e['new']
        else:
            v = rv
        if v not in ('-', ''):
            new += v.split()
    out[ln] = new
txt = ''.join(f"{ln}\t{' '.join(out[ln])}\n" for ln in R)
P = os.path.join(H, 'local_ciphertext.tsv')
if '--check' in sys.argv:
    ok = os.path.exists(P) and open(P).read() == txt
    print('tx86i/local_ciphertext.tsv up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(P, 'w').write(txt); print('wrote', P, {k: len(v) for k, v in out.items()})
