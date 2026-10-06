#!/usr/bin/env python3
"""R7B-HUNT (6 Oct 2026): list every glossed column on BLA188 p4-p6 and BLA194 p1 whose digit 3/5/7/9 could be the
descending z-form, with the key value of each one-digit swap (key built from the OTHER items only, leave-pages-out).
  python3 census/candidates.py > census/candidates.tsv"""
import csv, collections, os, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = ('BLA188_p4', 'BLA188_p5', 'BLA188_p6', 'BLA194_p1')
ct = list(csv.DictReader(open(os.path.join(HERE, 'ciphertext.tsv')), delimiter='\t'))
page = lambda l: l.rsplit('_', 1)[0]
per = collections.defaultdict(collections.Counter)
for r in ct:
    if page(r['line']) in PAGES or not r['gloss'] or r['group'] in ('?', '-') or r['conf'] != 'H':
        continue
    per[r['group']][r['gloss']] += 1
def kv(g):
    c = per.get(g)
    return ','.join(f'{v}:{n}' for v, n in c.most_common()) if c else ''
print('line\tpos\tgroup\tconf\tgloss\tkey_as_read\tswaps')
for r in ct:
    if page(r['line']) not in PAGES or r['group'] in ('?', '-'):
        continue
    g = r['group']; sw = []
    for i, d in enumerate(g):
        if d in '3579':
            for e in '3579':
                if e != d:
                    h = g[:i] + e + g[i+1:]
                    if kv(h):
                        sw.append(f'{h}={kv(h)}')
    print('\t'.join([r['line'], r['pos'], g, r['conf'], r['gloss'], kv(g), ' '.join(sw)]))
