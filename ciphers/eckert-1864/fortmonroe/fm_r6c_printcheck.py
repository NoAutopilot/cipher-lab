#!/usr/bin/env python3
"""FM-R6c (9 Oct 2026): letters-only phrase grep of the FM-R6c entries' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5777/2': ['terrible affair at Chambersburg has just reached me', 'My mother nearly insane', 'sisters are without home clothes or money', 'Newport office closed', 'Mack Gaughey can take charge', 'Gaughey', 'back pay as possible ready for me'],
 'F2 5659/0': ['terrific naval engagement in Albemarle Sound', 'Daily Christian Advocate', 'Christian Advocate Philadelphia', 'Carlton and Porter', 'Albemarle ravished', 'Chaplain White of the Providence Conference', 'J. Emory Round', 'piercing the boiler of one of them', 'disabling the rudder'],
 'F3 5786/0': ['send here immediately all the steamers that can possibly be spared', 'steamers that can possibly be spared from your place', 'no spare boats here excepting the Illinois', 'collected by order of Knox', 'The Illinois is nearly discharged', 'Illinois is nearly discharged and will be sent to you at once', 'Thayer needed at once', 'give the names of those you send'],
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
