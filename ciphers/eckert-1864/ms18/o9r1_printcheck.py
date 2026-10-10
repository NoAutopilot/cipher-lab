#!/usr/bin/env python3
"""O9R-1 (10 Oct 2026): letters-only phrase grep of the ten O9R-1 rows' decoded phrases in the cached OR/ORN djvu texts (sources/ia-fulltext/print-check/*.gz, plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'G1 9709/1': ['full names of Simpson', 'Painter has absconded', 'master Painter', 'Brooklyn Yards', 'ninety three Franklin'],
 'G2 9808/2': ['blocking up the roads leading from the Cumberland', 'space could be left in the barriers', 'means to close it in case of danger', 'town and country authorities should do this', 'a new raid may immediately follow'],
 'G3 9673/0': ['special expedition may be known and reimbursed', 'Maria C. Day', 'separate and distinct account', 'victualling, manning, sailing, loading'],
 'G4 9687/1': ['accommodations on the Fulton', 'Miss Dix', 'three state-rooms for officers', 'let the Fulton sail', 'until further advised on this subject'],
 'G5 9684/1': ['H. D. Stover', 'Stover now prisoner', 'books and papers of', 'no permits will be issued until we have held consultation', 'held consultation'],
 'G6 9699/1': ['quantity of forage to be placed', 'do not fail', 'Do not use steamers very expensive', 'S. L. Brown'],
 'G7 9803/0': ['concentrate nearly all your force', 'any threatened point', 'railroad facilities you should be able', 'make your arrangements to accomplish this object'],
 'G8 9684/0': ['Is Brady connected with a Navy operation', 'Edwin L. Brady', 'Arrest Edwin L. Brady', 'place him in Fort Lafayette', 'If the latter the War Department should take it up'],
 'G10 9735/0': ['three regiments of Ohio militia', 'Parkersburg', 'You remain under', 'distribute them as you deem best', 'report directly when you have any important information'],
 'G11 9686/1': ['all troops found within the limits of your department', 'order establishing it was received', 'who interferes with your authority', 'arrest any officer within your department'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = norm(gzip.open(p, 'rt', errors='ignore').read())
for p in sys.argv[1:]:
    texts[os.path.basename(p)[:-4]] = norm(open(p, errors='ignore').read())
isor = lambda v: 'warofrebellion' in v or 'officialrecord' in v or v.startswith('navalwar') or 'privateofficial' in v
print('volumes searched:', len(texts), 'OR/ORN/Butler:', ' '.join(sorted(v for v in texts if isor(v))))
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in texts.items() if norm(ph) in t and isor(v)]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
