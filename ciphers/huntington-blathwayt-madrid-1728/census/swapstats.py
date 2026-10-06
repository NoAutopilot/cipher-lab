#!/usr/bin/env python3
"""R7B-HUNT: classify each glossed column on the four pages by which single-digit swap (if any) makes its group's
leave-pages-out key value equal its gloss.  python3 census/swapstats.py [--list]"""
import csv, collections, os, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = ('BLA188_p4', 'BLA188_p5', 'BLA188_p6', 'BLA194_p1')
ct = list(csv.DictReader(open(os.path.join(HERE, 'ciphertext.tsv')), delimiter='\t'))
page = lambda l: l.rsplit('_', 1)[0]
norm = lambda s: s.replace("'", '')
per = collections.defaultdict(collections.Counter)
for r in ct:
    if page(r['line']) in PAGES or not r['gloss'] or r['group'] in ('?', '-') or r['conf'] != 'H':
        continue
    per[r['group']][norm(r['gloss'])] += 1
top = lambda g: per[g].most_common(1)[0][0] if g in per else None
cls = collections.Counter(); rows = []
for r in ct:
    if page(r['line']) not in PAGES or not r['gloss'] or r['group'] in ('?', '-'):
        continue
    g, gl = r['group'], norm(r['gloss'])
    if top(g) == gl:
        c = 'as-read'
    else:
        hits = sorted({f'{d}->{e}' for i, d in enumerate(g) for e in '0123456789' if e != d
                       and top(g[:i] + e + g[i+1:]) == gl})
        c = ';'.join(hits) if hits else ('unkeyed' if top(g) is None else 'other')
    cls[c] += 1; rows.append((r['line'], r['pos'], g, r['conf'], r['gloss'], c))
for k, v in cls.most_common():
    print(f'{v}\t{k}')
if '--list' in sys.argv:
    for x in rows:
        if '->' in x[5]:
            print('\t'.join(x))
