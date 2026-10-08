#!/usr/bin/env python3
"""LS5-R1c (8 Oct 2026): letters-only phrase grep of the LS5-R1c entries' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'Y1': ['transfer to Baltimore all mail matter', 'all mail matter', 'mail matter for General Sherman', 'mail for Sherman'],
 'Y2': ['send cavalry down to Fredericksburg', 'any force this side of the Rappahannock', 'on the Northern Neck', 'dispatch in relation to'],
 'Y3': ['will meet you at Fortress Monroe', 'will meet you at Fort Monroe', 'unless you shall notify me that it will be inconvenient', 'at 8 p. m. Saturday'],
 'Y5': ['proposed movement should be made as early as possible', 'occupied by General Sheridan near Winchester'],
 'Y6': ['bogus dispatches', 'for electioneering purposes', 'true condition of things', 'representing a great disaster'],
 'Y9': ['without the special orders of General Grant', 'no reinforcements can be sent to your department', 'all available troops have been ordered elsewhere'],
 'Y10': ['authorized to divest', 'hundred-days men', 'hundred days men as may be en route', 'put on duty in Kentucky'],
 'Y12': ['crossing at Antietam Ford and Shepherdstown', 'for forty hours in large force', 'troops be brought forward as rapidly as possible'],
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
