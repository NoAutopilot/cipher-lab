#!/usr/bin/env python3
"""LS5-R1d (8 Oct 2026): letters-only phrase grep of the LS5-R1d entries' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'X1': ["Longstreet's corps was passing north through Staunton", 'left Gordonsville yesterday morning', 'could give no information as to number but was certain the whole corps', 'old man whom he met at'],
 'X2': ['discharge of the Ohio militia leaves West Virginia much exposed to raids', 'no troops that Canby sent for its defense', 'much exposed to raids and there are no troops'],
 'X3': ['I doubt if a hundred men are sufficient for the work they are undertaking', 'rounds of ammunition for them will be sent you at once', 'doubt if a hundred men are sufficient'],
 'X4': ['plot to seize the sound steamers', 'can render any service to owners or shippers', 'cheerfully given and you may so inform them', 'plot to seize the Sound steamers'],
 'X5': ["supposed to be Kershaw's was sent by rail from Richmond to Gordonsville", 'marched from Gordonsville to join Early', 'officer in charge of scouts says the above came to him'],
 'X6': ['preparatory to the evacuation of Richmond', 'Richmond cannot be held a month longer', 'have not been running on the Central railroad since last Saturday', 'all being used to convey government property from Richmond to Danville'],
 'X7': ['Rosser is at Leesburg with a brigade', 'dispositions made to prevent him from crossing the river', 'Rosser is at Leesburg'],
 'X8': ['Indiana militia have been ordered to Nashville', 'left Indianapolis yesterday', 'more will soon follow', 'militia have been ordered to Nashville'],
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
