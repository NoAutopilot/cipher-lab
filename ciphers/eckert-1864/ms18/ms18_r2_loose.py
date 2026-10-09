#!/usr/bin/env python3
"""MS18-R2: loose co-occurrence search (all terms inside a 700-character window, case-folded) of the decoded content words of rows X5-X9 in the cached OR/ORN djvu texts and the scratch OR vols 39/3, 41/4, 46/3.
Usage: ms18_r2_loose.py [scratch.txt ...]. A miss is a search result (rule 10)."""
import gzip, glob, os, re, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
Q = {'X5/X6 arrest agents Nov 1864': ['arrest', 'agents', 'seizure', 'papers', 'Monday'],
     'X7 cavalry bureau depots Aug 1864': ['Cavalry Bureau', 'unserviceable', 'Gallipolis'],
     'X9 forces from Kentucky to Thomas': ['spared from Kentucky', 'Thomas', 'Hood'],
     'X9b spared from Kentucky': ['can possibly be spared', 'Nashville'],
     'X1 plenty Port Royal funds': ['Port Royal', 'funds', 'Quartermaster'],
     'X2 Hurlbut Sheridan division': ['Hurlbut', 'Sheridan', 'Reynolds', 'Canby'],
     'X8 2700 horses': ['2,700', 'horses', 'Pope'],
     'X4 Campbell Pulaski Seddon': ['Campbell', 'Pulaski', 'Seddon']}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    n = os.path.basename(p)[:-12]
    if n.startswith(('warofrebellion', 'officialrecordso', 'lincolnin', 'privateofficial', 'reportsofb')): texts[n] = gzip.open(p, 'rt', errors='ignore').read()
for p in sys.argv[1:]: texts[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
for k, terms in Q.items():
    for v, t in texts.items():
        t2 = re.sub(r'\s+', ' ', t); lo = t2.lower(); n = 0
        for m in re.finditer(re.escape(terms[0].lower()), lo):
            w = lo[max(0, m.start() - 350): m.end() + 350]
            if all(x.lower() in w for x in terms[1:]):
                n += 1
                if n <= 2: print(f'{k} | {v} | {t2[max(0, m.start() - 120): m.end() + 200]}')
        if n > 2: print(f'{k} | {v} | ... {n} windows')
