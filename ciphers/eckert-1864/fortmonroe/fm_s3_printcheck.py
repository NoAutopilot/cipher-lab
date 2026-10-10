#!/usr/bin/env python3
"""FM-S3 (9 Oct 2026): letters-only phrase grep of the FM-S3 entries' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5720/2': ['all pontoon bridging at Yorktown', 'pontoon bridging at Fort Monroe', 'which may arrive at these places will be sent to', 'pontoon'],
 'F2 5547/1': ['I await your orders by telegraph', 'will leave at once if you deem it necessary', 'J J Peck'],
 'F3 5569/1': ['effort to obtain a map of the City of Richmond', 'map of the city of Richmond but regret', 'unable to procure one'],
 'F4 5546/0': ['in regard to any cooperation', 'telegraph directly to', 'now in command of'],
 'F5 5577/0': ['send no ciphers till cable is repaired', 'till cable is repaired', 'nothing heard from Patrick'],
 'F6 5673/1': ['you used the wrong route', 'corrected it here and sent forward'],
 'F7 5672/1': ['desires that you will have the Richmond and Danville', 'Richmond and Danville Railroad cut if possible', 'Danville Rail Road cut if possible'],
 'F8 5641/0': ['have any more ironclads reached you', 'has General Gillmore arrived', 'any more iron clads reached you'],
 'F9 5804/2': ['do you need more transportation', 'do you need more transportation to New York'],
 'F10 5669/1': ['telegraph General Butler to have the Richmond and Danville', 'to have the Richmond and Danville Railroad cut', 'Richmond and Danville'],
 'F11 5664/2': ['erase the name of General Hurlbut and insert', 'insert in its place the name of Major General Canby'],
 'F12 5679/0': ['has Sheridan left the James', 'must we forage him', 'by the other line'],
 'F13 5830/0': ['I shall leave here for Beaufort', 'leave here for Beaufort in an hour'],
 'F14 5633/1': ['why publish Edgars name', 'stop your exchanges', 'this was against orders'],
 'F15 5798/1': ['make following addition in number', 'rest Halifax and hospital'],
 'F16 5833/2': ['Birney message too late', 'has gone to sea left here about'],
 'F17 5828/1': ['not away will return', 'Shepley'],
 'F18 5829/1': ['has the fleet left yet', 'chief quartermaster Ingalls fleet'],
 'F19 5800/2': ['received will start in an hour', 'Beckwith City Point received will start'],
 'F20 5590/0': ['deliver this to General Grant now at Monroe or Norfolk', 'now at Monroe or Norfolk'],
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
