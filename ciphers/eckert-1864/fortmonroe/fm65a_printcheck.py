#!/usr/bin/env python3
"""FM65-A (9 Oct 2026): letters-only phrase grep of the FM65-A entries' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5847/2': ['unable to furnish anchor and chain', 'anchor and chain in time for steamer Baltic', 'will not be sent on the expedition', 'need not send to New York for them'],
 'F2 5849/0': ['I have ordered the steamers C. C. Leary, Ariel and Victor to report to Colonel Newport', 'consumed all surplus transportation', 'request of General Ingalls'],
 'F3 5849/1': ['turn them over to Colonel Morgan', 'coaling and watering under the instructions received from General Ingalls', 'what number of troops each steamer will carry'],
 'F4 5850/1': ['turn over to you all the launches and large boats', 'Please direct me in the premises'],
 'F5 5851/0': ['ordered to report to Colonel Bradley', 'Euterpe, H. Livingston', 'Prometheus, Thames, Idaho', 'Atlantic draws too much water'],
 'F6 5851/1': ['Steamers all ready coaled and loaded with proper rations', 'list will be handed you stating capacity', 'Rawlins wishes you to send to this place'],
 'F7 5852/1': ['wishes to know if the steamers named in your dispatch have started', 'been reported from Jamestown'],
 'F8 5852/2': ['steamers named had left here before 9 a. m.', 'if the steamer Russia is at Monroe', 'send here in time for a flag ship'],
 'F9 5853/1': ['She answers the description you required', 'If you can spare the Montauk we need her here', 'C. C. Leary is just in'],
 'F10 5854/0': ['Bendford is not here', 'Ainsworth has copy with him', 'no other vessel here except the Alliance', 'fully comply with the orders'],
 'F11 5854/1': ['Cuyahoga has not arrived', 'letter for Mr. Draper', 'McClellan, Atlantic, Tonawanda, and Champion', 'light boats must be put back again at Cedar Point'],
 'F12 5855/2': ['light-draft steamers not over five feet', 'suitable for going with the other vessels', 'Eliza Hancox and a Winants will answer', 'good supply of coal only will be required'],
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
