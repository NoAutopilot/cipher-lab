#!/usr/bin/env python3
"""FM-R4a (9 Oct 2026): letters-only phrase grep of the FM-R4a entries' hand-read phrases in the cached OR/ORN/Butler djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments); prints volume and a 100-char context of the first hit per phrase.
A miss is a search result, not a verdict (rule 10). Usage: python3 fm_r4a_printcheck.py [extra.txt ...]"""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5770/1': ['all told including Ricketts', 'eleven thousand troops all told', 'telegraph communication with you was intact', 'whether telegraph communication with you was intact', 'Seventh Street road near Silver Spring'],
 'F2 5816/0': ['Bartonsville', 'Barton, of Bartonsville', 'Tell Colonel Saunders', 'books and papers taken from', 'without attracting any observation', 'make these reports without attracting'],
 'F3 5781/1': ['One hundred and fourth Pennsylvania', '104th Pennsylvania', 'Hilton Head', 'arrival of the One hundred and fourth', 'Lieutenant-Colonel Hart'],
 'F4 5789/1': ['Kent is dead', 'Waterhouse very ill', 'risking the health', 'no operators needed here for some weeks', 'prominent officers have died', 'Morehead City'],
 'F5 5829/0': ['Binney', 'make you whole immediately for this outlay', 'money is difficult', 'Acting Paymaster-General', 'such officers as you may designate'],
 'F6 5797/0': ['Taylor\'s Ridge', 'Van Duzer', 'four hundred wagon loads', 'garrison entirely', 'railroad is all right from Atlanta to Resaca', 'foraging parties'],
 'F7 5752/1': ['pontoon bridge is probably by this time taken up', 'all the army have crossed', 'Channing Clapp', 'W. H. Pettus', 'Jamestown Island'],
 'F9 5774/0': ['Purviance', 'keeper of the light-ship', 'keeper of light-ship at the mouth of York River', 'obstructions in Elizabeth River', 'moved back to the obstructions'],
 'F10 5781/0': ['One hundred and fourth Pennsylvania', 'steamer Fulton', 'proceed direct to Alexandria', 'march thence to Washington', 'report by telegraph from Fort Monroe', 'Fulton, I send'],
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
