#!/usr/bin/env python3
"""MS18-R5: loose co-occurrence search (all terms inside a 600-character window, case-folded) of decoded content words of rows X3, X4, X5, X9, X10 in the cached OR/ORN/other djvu texts plus scratch OR volumes given as arguments.
A miss is a search result (rule 10). Usage: ms18_r3_loose.py [scratch.txt ...]"""
import gzip, glob, os, re, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
Q = {'X1 habeas corpus minors Hancock': ['habeas corpus', 'minors', 'Hancock'],
 'X1b minors discharged illegally enlisted': ['minors', 'illegally enlisted'],
 'X2 hostages Wentz Harpers Ferry': ['hostages', 'Wentz', 'Harper'],
 'X2b hostages negroes Weldon Railroad prominent citizens': ['hostages', 'prominent citizens', 'raiders'],
 'X3 Wilson Macon reward Davis seized': ['Wilson', 'Macon', 'reward', 'Davis'],
 'X3b prominent rebel reorganizing seized sent to Washington under guard': ['reorganiz', 'seized', 'under guard'],
 'X4 Sampson Edwards Ferry guerrillas Baltimore': ['Edwards Ferry', 'guerrillas', 'Baltimore'],
 'X5 Stiner reporter': ['Stiner', 'reporter'],
 'X5b written accounts Fox Fortress Monroe navy vessels': ['written accounts', 'Fox'],
 'X6 Olcott Boston witnesses Goodman Judge Advocate': ['Goodman', 'Judge Advocate', 'Boston'],
 'X7 Early Wednesday rumored Lee cavalry beaten Beckwith Bowers': ['Early', 'Wednesday', 'Bowers', 'prisoners'],
 'X8 Memphis Barton prisoner papers publication Canada': ['Barton', 'prisoner', 'papers', 'Memphis'],
 'X9 Maryland veteran cavalry Augur Wallace': ['Augur', 'Maryland', 'Veteran', 'Wallace'],
 'X10 Hunter Kanawha Harpers raid Maryland McCaine': ['Kanawha', 'raid into Maryland'],
 'X11 furlough governors authority Stokes': ['furlough', 'Governors', 'Stokes'],
 'X12 Rawlins Missouri troops Thomas Hood Wheeler': ['Rawlins', 'Missouri', 'Hood', 'Wheeler']}
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
