#!/usr/bin/env python3
"""FM-R1 (8 Oct 2026): letters-only phrase grep of the FM-R1 entries' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5802/2': ['strength of each battery', 'Napoleons officers men', 'batteries Army of the James strength officers men'],
 'F2 5772/0': ['I arrived at Annapolis', 'save invalids', 'light draft ferry boat', 'Annapolis this morning'],
 'F3 5802/0': ['Third New York Artillery', 'first United States Artillery Army of the James', 'Battery E third United States'],
 'F4 5823/1': ['large sized', 'loaded with subsistence', 'ought to be loaded with subsistence'],
 'F5 5664/0': ['cipher of ten columns', 'cant translate your cipher', 'compare with yours'],
 'F6 5808/2': ['make following additions to No. 1 cipher', 'following additions to No. 1', 'Pulaski Godfrey', 'Paducah Goslin'],
 'F7 5780/0': ['Arago and Cosmopolitan', 'the steamers Arago and Cosmopolitan', 'to await at Fort Monroe', 'Von Weitzel'],
 'F8 5818/0': ['Mattawan not the craft', 'not the craft for your services', 'have not seen Sanborne', 'Mattawan'],
 'F9 5584/1': ['additional arbitraries', 'add additional arbitraries', 'orphan'],
 'F10 5782/1': ['make the following additions and insert the same in all copies', 'in all copies in use in your departments', 'additions and insert the same'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = norm(gzip.open(p, 'rt', errors='ignore').read())
for p in sys.argv[1:]:
    texts[os.path.basename(p)[:-4]] = norm(open(p, errors='ignore').read())
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in texts.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
