#!/usr/bin/env python3
"""N2R-2 (10 Oct 2026): letters-only phrase grep of decoded phrases of the N2R-2 rows in cached OR djvu texts
(sources/ia-fulltext/print-check/*.gz plus plain .txt/.gz paths given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'Y2 9874/1 22 Oct 1864': ['pay masters will leave', 'paymasters will leave here', 'sufficient escort at Martinsburg', 'with funds for payment of the Nineteenth', 'for their protection'],
 'Y3 9761/1 19 Jun 1864': ['found the enemy in possession of Staunton', 'another attempt to send the despatches', 'detachment of cavalry sent from Beverly', 'sent from Beverly with despatches', 'McLaughlin'],
 'Y4 9913/0 10 Dec 1864': ['Paymasters ready to go', 'unpaid to August 31', 'unpaid to the 31st of August', 'safe guard from Relay House', 'Relay House'],
 'Y5 9800/2 24 Jul 1864': ['rear of the Sixth Corps got into', 'being supplied and paid', 'will probably embark tonight', 'Sixth Corps got in'],
 'Y7 9916/1 16 Dec 1864': ['meet him on the Gulf coast', 'ordered the supplies in vessels', 'supplies in vessels at Pensacola', 'unnecessary that you should keep'],
 'Y8 9722/1 25 Apr 1864': ['Mosby is collecting corn', 'Mosby is gathering corn', 'send a regiment of cavalry from Warrenton', 'regiment of cavalry from Warrenton', 'break up this'],
 'Y9 9680/0 27 Feb 1864': ['no immediate movement on foot', 'advices just received from Jacksonville', 'Hardee with fifteen thousand', 'no immediate movement on foot in West Virginia'],
 'Y10 9725/0 27 Apr 1864': ['column in motion will reach Fairfax', 'will reach Fairfax to-night', 'requisite ammunition and supplies', 'ammunition and supplies with the column'],
 'Y11 9914/1 14 Dec 1864': ['paymasters will leave tomorrow by river for City Point', 'payment of two regiments of the Sixth Corps', 'unpaid to the 31st of August', 'in compliance with the Secretary\'s order of'],
 'Y12 9681/0 29 Feb 1864': ['put in direct communication', 'direct communication with Washington', 'come into the telegraph office at that hour', 'telegraph office at that hour'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    if 'warofrebellion' in p or 'official' in p: texts[os.path.basename(p)[:-12]] = norm(gzip.open(p, 'rt', errors='ignore').read())
for p in sys.argv[1:]:
    op = gzip.open if p.endswith('.gz') else open
    texts[os.path.basename(p).split('_djvu')[0].split('.')[0]] = norm(op(p, 'rt', errors='ignore').read())
print('volumes searched:', len(texts), ' '.join(sorted(texts)))
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in texts.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
