#!/usr/bin/env python3
"""LS3-R18b (8 Oct 2026): pre-filter of the seven last A3V3-ECK18 keyed entries against OR ser. I vols. 46-49 (fetched to a scratch dir,
archive.org djvu, ids in eckert-1862/ec18/or_volumes.tsv) and the cached Butler / Lincoln-in-the-Telegraph-Office texts.
Letters only, spaces removed, so line breaks and hyphens do not matter. A miss is a search result for the log, not a verdict (rule 10).
Usage: ls3_r18b_printcheck.py OR_DIR   (OR_DIR holds <ia id>.txt for vols 46.1-49.2)"""
import gzip, re, sys, os, glob
OR_DIR = sys.argv[1]
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'sources', 'ia-fulltext', 'print-check')
PH = {
 '9943.494': ['does not know for what purpose these are intended', 'will take months to prepare', 'those on board the stromboli',
              'sent to the ordnance yard', 'will not the torpedoes on hand', 'torpedoes on hand or those on board'],
 '9948.507': ['at your earliest convenience', 'very fine day'],
 '10002.578': ['suspend preparations for campaign west of the mississippi', 'attempts to hold out a force will be sent to overrun'],
 '10026.621': ['to enable you to carry out the order for mustering out', 'have rolls prepared as far as practicable'],
 '10027.623': ['authorize the issuing of arms to all persons connected', 'will not be lost to the government'],
 '10028.625': ['suppress all sale of liquor on the lines traveled by troops', 'returning to be mustered out and at rendezvous'],
 '10031.632': ['you can send the whips from the', 'send the whips for', 'chief of staff'],
}
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
texts = {}
for p in sorted(glob.glob(os.path.join(OR_DIR, '*.txt'))):
    texts[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
for v in ['privateofficialc04butl', 'privateofficialc05butl', 'lincolnintelegra00bates']:
    p = os.path.join(D, v + '_djvu.txt.gz')
    if os.path.exists(p):
        texts[v] = gzip.open(p, 'rt', errors='ignore').read()
    else:
        print('missing', v, file=sys.stderr)
normtexts = {v: norm(t) for v, t in texts.items()}
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in normtexts.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
