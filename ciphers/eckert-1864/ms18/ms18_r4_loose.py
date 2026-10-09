#!/usr/bin/env python3
"""MS18-R4: loose co-occurrence search (all terms inside a 600-character window, case-folded) of decoded content words of rows X3, X4, X5, X9, X10 in the cached OR/ORN/other djvu texts plus scratch OR volumes given as arguments.
A miss is a search result (rule 10). Usage: ms18_r3_loose.py [scratch.txt ...]"""
import gzip, glob, os, re, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
Q = {'X4 provisional battalion Gregg Aldie': ['provisional', 'Aldie', 'Gregg'],
     'X4b forges coal cavalry Upper Potomac': ['Upper Potomac', 'provisional', 'battalion'],
     'X6 Hurlbut both banks Kirby Smith navigation': ['Hurlbut', 'both banks', 'navigation'],
     'X6b conflict of orders Hurlbut Memphis': ['Hurlbut', 'conflict of orders'],
     'X7 Gordon Bruce Halifax machinery': ['Halifax', 'machinery', 'Bruce'],
     'X8 Monocacy car Frederick refreshments': ['Monocacy', 'refreshments'],
     'X8b Grant Monocacy Relay car': ['Monocacy', 'Relay', 'Grant'],
     'X10 Crane disbursing inspector incompatible': ['Crane', 'disbursing', 'Inspector'],
     'X11 Brackett Burnet House Grierson': ['Brackett', 'Burnet', 'Grierson'],
     'X11b Brackett inspector Planters House': ['Brackett', 'Planters'],
     'X5b Lamb copies telegrams Beckwith McClellan': ['Beckwith', 'McClellan', 'Lamb'],
     'X3 Pope suspend preparations': ['suspend', 'Kirby Smith', 'Pope']}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))): texts[os.path.basename(p)[:-12]] = gzip.open(p, 'rt', errors='ignore').read()
for p in sys.argv[1:]: texts[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
print('volumes', len(texts))
for k, terms in Q.items():
    tot = 0
    for v, t in texts.items():
        t2 = re.sub(r'\s+', ' ', t); lo = t2.lower(); n = 0
        for m in re.finditer(re.escape(terms[0].lower()), lo):
            w = lo[max(0, m.start() - 300): m.end() + 300]
            if all(x.lower() in w for x in terms[1:]):
                n += 1
                if n <= 1: print(f'{k} | {v} | {t2[max(0, m.start() - 100): m.end() + 160]}')
        tot += n
    print(f'{k}: {tot} windows')
