#!/usr/bin/env python3
"""FM-R7b (9 Oct 2026): letters-only phrase grep of the FM-R7b entries' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5639/2': ['Adrian Terry assistant adjutant general', 'light battery one forty three', 'Adrian Terry', 'First Connecticut Light Battery', 'Fifth New Jersey Light Battery', 'Fourth New Jersey Battery'],
 'F2 5709/1': ['Gloucester route is the best', 'Gloucester route', 'Embree to Jamestown', 'Mackintosh arrives with his party', 'Bickford has some operators', 'send Collings'],
 'F3 5648/2': ['Colonel B G Onderdonk', 'Onderdonk', 'planted torpedo', 'Charles City Court House on Friday', 'party of the enemys cavalry came down from Charles City'],
 'F4 5695/2': ['cannot string wire across at either point', 'navigation must remain open for vessels', 'some of which have high masts', 'favorable for building line as the route up peninsula', 'West Point three quarters of a mile'],
 'F5 5702/0': ['I regret having ordered OBrien away from', 'Caldwell will attend to all cipher work', 'direct Mackintosh to bring with him all builders', 'Nichols can remain with him'],
 'F6 5782/0': ['cable should be laid on north side', 'dragged up by anchors', 'channel most of way is nearest south shore', 'nearest south shore'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = norm(gzip.open(p, 'rt', errors='ignore').read())
for p in sys.argv[1:]:
    texts[os.path.basename(p)[:-4]] = norm(open(p, errors='ignore').read())
print('volumes searched:', len(texts), ' '.join(sorted(texts)))
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in texts.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
