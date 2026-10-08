#!/usr/bin/env python3
"""LS4-R1b (8 Oct 2026): letters-only phrase grep of the LS4-R1b entries' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'X1': ['come over to-night and see me', 'come over to night and see me', 'Hoffman come over'],
 'X2': ['reported on what seems trustworthy evidence', 'trustworthy evidence as a rebel agent in Baltimore', 'several persons answering to the name', 'care must be exercised'],
 'X3': ['evidence in our possession furnishes no personal description', 'no personal description of the rebel agent', 'rebel agent at St. Louis'],
 'X4': ['can you not hold on for three or four days', 'until our vessel reaches you', 'hold on for three or four days'],
 'X5': ['all troops sent from Missouri must report to', 'sent from Missouri must report to General Thomas', 'any other orders to the contrary notwithstanding'],
 'X6': ['little personal bundle for yourself', 'draft for you with package', 'send an officer down'],
 'X8': ['fully coaled and watered', 'Nelly Pentz', 'such point as General Gillmore may order', 'leave as soon as the storm is over'],
 'X9': ['no design to put Buell again in command', 'do not believe the newspapers', 'Buell again in command in Tennessee'],
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
