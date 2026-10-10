#!/usr/bin/env python3
"""FM-S65A (9 Oct 2026): letters-only phrase grep of the FM-S65A entries' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5845/2': ['Butler\'s headquarters all ready', 'all ready'],
 'F2 5857/2': ['I expect to leave this afternoon for Monroe and thence to Savannah', 'thence to Savannah with', 'instructions given to General Sheridan'],
 'F3 5858/2': ['steamer Martin', 'left for Monroe about 11.30', 'it is for General Grant who left'],
 'F4 5862/0': ['River Queen left about', 'told me he had gone up the James', 'himself was going the same way', 'General Butler on board'],
 'F5 5862/2': ['to relieve General Foster', 'either would be good', 'Ord or'],
 'F6 5872/0': ['goes to sea at eleven o\'clock', 'Illinois goes to sea', '1,200 men'],
 'F7 5872/1': ['nothing has arrived to-day and the end is not yet', 'nothing has arrived today', 'the end is not yet'],
 'F8 5872/2': ['has but 40 rounds of ammunition', 'Shall I take more', 'Division has but forty rounds'],
 'F9 5874/1': ['you need not wait to get more', 'forty rounds will answer', 'will answer you need not wait'],
 'F10 5883/2': ['wait at Monroe until I get there', 'General Palmer wait at', 'I will leave an'],
 'F11 5892/0': ['arrived at ten this evening', 'Richmond party not here', 'I remain here'],
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
