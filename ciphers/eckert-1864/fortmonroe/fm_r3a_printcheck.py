#!/usr/bin/env python3
"""FM-R3a (9 Oct 2026): letters-only phrase grep of the FM-R3a entries' hand-read phrases in the cached OR/ORN/Butler djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments); prints volume and a 100-char context of the first hit per phrase.
A miss is a search result, not a verdict (rule 10). Usage: python3 fm_r3a_printcheck.py [extra.txt ...]"""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5637/2 E210': ['Captain Tafft', 'H. S. Tafft', 'Sergeant Royer', 'Royer with my desk', 'best maps of the peninsula', 'maps of the peninsula and south side', 'L. B. Norton', 'chief signal officer'],
 'F2 5649/2 E211': ['little party of pleasure', 'party of pleasure to which you were invited', 'will come off Wednesday evening', 'marriage can hardly be celebrated without you', 'friends most earnestly desire your presence'],
 'F3 5767/2 E212': ['directs that all available transportation be sent to City Point', 'all available transportation', 'send up such steamers as you have suited for this service', 'Lieutenant-Colonel Biggs', 'move troops thence to Washington'],
 'F4 5607/1 E213': ['material which will become surplus', 'surplus by the new arrangements', 'material and the superintendent go with the Tenth Corps', 'I came here by General Turner', 'instructions concerning material'],
 'F5 5703/1 E214': ['Bickford has', 'insulators and', 'send to West Point with him enough material', 'material to make out twenty miles', 'operators sufficient are ordered to report to you', 'advise me often about the work'],
 'F6 5734/0 E215': ['no change in the naval situation', 'Richmond Examiner says General Grant will cross', 'Grant will cross the James River and operate against Richmond on the south side', 'Richmond Examiner', 'Agawam, Trent\'s Reach', 'Trent\'s Reach June 7'],
 'F7 5743/1 E216': ['every vessel fitted to aid in this movement', 'send to that place immediately every vessel fitted', 'removing stores and wounded to a new base', 'is to embark at White House', 'sixteen thousand', 'wounded to a new base or hospital'],
 'F8 5770/0 E217': ['transports here now for seven thousand men', 'General Wright has eleven thousand men', 'transports enough for his command', 'Wright has 11,000', 'there will be transports enough'],
 'F9 5768/0 E218': ['inform me by telegraph of the arrival of the first transport', 'arrival of the first transport of the advance of the Nineteenth', 'first transport of the advance of the 19th', 'advance of the Nineteenth Army Corps from New Orleans', 'Nineteenth Corps from New Orleans'],
 'F10 5780/1 E219': ['place the steamer Greyhound at his disposal', 'steamer Greyhound at his disposal', 'to meet his family at Fort Monroe', 'meet his family at Fortress Monroe', 'General Grant leaves here at', 'Greyhound at his disposal'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = gzip.open(p, 'rt', errors='ignore').read()
for p in sys.argv[1:]:
    texts[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
N = {v: norm(t) for v, t in texts.items()}
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in N.items() if norm(ph) in t]
        ctx = ''
        if hits and len(norm(ph)) > 14 and len(hits) <= 3:
            v = hits[0]; i = N[v].find(norm(ph)); ctx = ' ~ ' + N[v][max(0, i-30):i+60]
        print(e, '|', ph, '|', (','.join(hits[:6]) + (' +%d' % (len(hits)-6) if len(hits) > 6 else '')) or 'none', ctx)
