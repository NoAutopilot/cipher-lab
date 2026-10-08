#!/usr/bin/env python3
"""LS3-R9 (8 Oct 2026): letters-only phrase grep of the LS3-R9 entries' plain phrases in the OR/ORN djvu texts (cached
sources/ia-fulltext/print-check/*.gz plus any scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10).
Usage: ls3_r9_printcheck.py [extra_djvu.txt ...]"""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'O9-AK': ['will have a regiment of militia at Johnson', 'as soon as relieved send', 'to the field as previously ordered', 'by Friday next he will have'],
 'O9-AL': ['has been directed to give you all the assistance possible', 'assistance possible from his department'],
 'E76': ['special car for self and staff', 'first through train to New York', 'for self and staff for the first through train'],
 'E77': ['fleet were inactive at their destination', 'on account of continued bad weather', 'you may be in time yet'],
 '8893/1/1': ['two brigades of Ewell', 'expected raid by Morgan through Stone'],
 '8919/27/2': ['occupy and hold the line of that river'],
 '9054/162/2': ['possible at present to send you re-enforcements'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*warofrebellion*_djvu.txt.gz')) + glob.glob(os.path.join(D, 'officialrecords*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = norm(gzip.open(p, 'rt', errors='ignore').read())
for p in sys.argv[1:]:
    texts[os.path.basename(p)[:-4]] = norm(open(p, errors='ignore').read())
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in texts.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
