#!/usr/bin/env python3
"""FV-FM3c (8 Oct 2026): rare-name and phrase grep for E185 E187 E189 E190 E191 in the cached OR/ORN/Butler djvu texts
(sources/ia-fulltext/print-check/*.gz) plus scratch *_djvu texts given as arguments. Prints each hit with 160 chars of context.
A miss is a search result, not a statement about print (rule 10)."""
import gzip, glob, os, re, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
T = {'E185': ['Colhoun', 'Saugus down', 'send the Saugus', 'with your vessel without delay'],
     'E187': ['Schoonmaker', 'Van Rensselaer', 'Rensselaer'],
     'E189': ['forage to Jamestown', 'Pitkin wants', "Wilson's Wharf", 'tow two schooners'],
     'E190': ['Obethner', 'Bovee', 'Grove Wharf', 'Hicks'],
     'E191': ['Chesnut', 'Chestnut', 'Pratt street', 'hold him safe', 'high intelligence']}
texts = {os.path.basename(p)[:-12]: gzip.open(p, 'rt', errors='ignore').read() for p in glob.glob(os.path.join(D, '*_djvu.txt.gz'))}
for p in sys.argv[1:]:
    texts[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
print('volumes:', len(texts))
for e, ts in T.items():
    for t in ts:
        pat = re.compile(r'\s+'.join(map(re.escape, t.split())), re.I)
        for v, s in sorted(texts.items()):
            for m in list(pat.finditer(s))[:6]:
                print(e, '|', t, '|', v, '|', re.sub(r'\s+', ' ', s[max(0, m.start() - 160):m.end() + 160]))
