#!/usr/bin/env python3
"""OLD-PASS2: per-sign disagreement between the committed B/C1 rows of ciphertext.tsv and a blind pass,
after the normalisation pre-registered in PREREG_OLD-PASS2.md (both sides alike). Agreement, not accuracy.

  python3 diff_pass2.py ../ciphertext.tsv blind_pass2.tsv [--norm-out DIR]
"""
import csv, re, sys, os
from collections import defaultdict

def norm_tok(t):
    t = t.strip().lower()
    t = re.sub(r"[,;:\-|' ]", '', t).replace('.^', '^')  # punctuation inside a V.Sa group (PREREG item 2)
    for pat in ('v.sa', 'vsa', '2s^a', '25^a', '2sa', '25a'):
        t = t.replace(pat, '@')
    t = re.sub(r"[,.;:\-|' ]", '', t)
    t = t.replace('^', '')
    if t.endswith('5'):
        t = t[:-1] + 's'
    return t.replace('6', 'b')

def lines(path):
    d = defaultdict(list)
    with open(path) as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r['block'] in ('B', 'C1'):
                n = norm_tok(r['raw_token'])
                if n:
                    d[(r['block'], int(r['line']))].append(n)
    return d

def lev(a, b):
    p = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        c = [i]
        for j, y in enumerate(b, 1):
            c.append(min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (x != y)))
        p = c
    return p[-1]

def main():
    ref, bl = lines(sys.argv[1]), lines(sys.argv[2])
    tot = defaultdict(lambda: [0, 0])
    for k in sorted(set(ref) | set(bl)):
        a, b = ''.join(ref.get(k, [])), ''.join(bl.get(k, []))
        e = lev(a, b)
        tot[k[0]][0] += e; tot[k[0]][1] += len(a)
        print(f"{k[0]}\t{k[1]}\t{e}/{len(a)}\tref={' '.join(ref.get(k, []))}\tblind={' '.join(bl.get(k, []))}")
    E = N = 0
    for blk, (e, n) in sorted(tot.items()):
        print(f"BLOCK {blk}: {e}/{n} = {100*e/n:.1f}% per-sign disagreement"); E += e; N += n
    print(f"TOTAL B+C1: {E}/{N} = {100*E/N:.1f}% per-sign disagreement (agreement, not accuracy)")
    if '--norm-out' in sys.argv:
        out = sys.argv[sys.argv.index('--norm-out') + 1]
        for name, d in (('ref', ref), ('blind', bl)):
            with open(os.path.join(out, f'norm_{name}.tsv'), 'w') as f:
                f.write('line\tpos\ttoken\tconf\n')
                for k in sorted(d):
                    for i, t in enumerate(d[k], 1):
                        f.write(f"{k[0]}_L{k[1]:02d}\t{i}\t{t}\thigh\n")

if __name__ == '__main__':
    main()
