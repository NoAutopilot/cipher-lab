#!/usr/bin/env python3
"""FM-S1 (9 Oct 2026): letters-only phrase grep of the FM-S1 entries' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5785/1': ['yellow fever is prevailing to considerable extent at Newbern', 'yellow fever is prevailing', 'Surgeon Charles McDougall', 'I have thought best to notify you at once'],
 'F2 5799/0': ['copy of all dispatches sent north from your office', 'dispatches sent north from your office signed Schoonmaker', 'directed to request you to forward to me a copy of all dispatches', 'Schoonmaker'],
 'F3 5816/2': ['Mr Baird will arrive tomorrow morning', 'please have him sent here with his instruments', 'Baird will arrive'],
 'F4 5583/2': ['if the operator at Cherry Stone is the same W A Dunn', 'Cherry Stone', 'Cherrystone', 'W A Dunn formerly employed'],
 'F5 5827/0': ['U S S Saugus', 'will start down at early', 'Saugus above City Point'],
 'F6 5647/0': ['what is the latest news from Gillmore', 'what number of his force is yet to arrive'],
 'F7 5793/1': ['dont fail to be at wharf when the', 'dont mention his coming to any one', 'Manhattan arrives from'],
 'F8 5636/2': ['Captain Clarke of my staff has just returned from North Carolina', 'Clarke of my staff has just returned', 'Culpepper Court House Beckwith'],
 'F9 5822/2': ['every thing is shipped', 'the Demolay leave here at day light', 'Demolay leave here'],
 'F10 5731/0': ['is an office needed at West Point', 'I want Rand here', 'keep Cowan and Ryan at West Point', 'some other office is ready for them'],
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
