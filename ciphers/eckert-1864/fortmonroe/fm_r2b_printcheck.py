#!/usr/bin/env python3
"""FM-R2b (8 Oct 2026): letters-only phrase grep of the FM-R2b entries' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5824/2': ['send the Saugus down at once', 'Saugus down at once', 'Onondaga Dutch Gap', 'Commodore Parker Onondaga'],
 'F2 5635/0': ['one ironclad here yet', 'one ironclad has arrived', 'Colonel Rowley', 'Gillmore will not be here before'],
 'F3 5799/1': ['signed by or addressed to Schoonmaker', 'copy of each message received at this office', 'Schoonmaker'],
 'F4 5584/0': ['clearing out land pirates', 'land pirates in Middlesex and Mathews', 'Wistar Middlesex Mathews prisoners', 'returned from Gloucester with prisoners'],
 'F5 5748/1': ['Pitkin wants me to send all forage', 'Captain Pitkin forage Jamestown Island', 'forage to Jamestown Island', 'tow two schooners'],
 'F6 5831/0': ['Grove Wharf', 'first New York Mounted Rifles', 'Captain Obethner', 'Hicks Sixteenth New York Artillery'],
 'F7 5589/2': ['Corner of South and Pratt streets', 'hold him safe', 'confidential member of your staff', 'send me by tomorrow nights boat'],
 'F8 5643/0': ['flag of truce boat just in', 'all quiet flag of truce boat', 'receipt of dispatch before'],
 'F9 5784/0': ['sick prisoners to be exchanged', 'exact point and destination unknown to me at present', 'destination unknown to me'],
 'F10 5805/2': ['open your own letter of instructions', 'vessels which have no letters', 'letter of instructions give corresponding order', 'Captain Langdon'],
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
