#!/usr/bin/env python3
"""FM-R5c (9 Oct 2026): letters-only phrase grep of the FM-R5c entries' decoded phrases AND rare names/numbers in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5662/0': ['made a splendid charge driving the enemy from their rifle pits', 'splendid charge driving the enemy', 'checked in their advance by a square earthwork', 'advanced to Swift Creek within two miles of Petersburg', 'Heckman made a splendid charge', 'blowing the boat up', 'struck the Shokokon', 'above Port Walthall', 'serious wounding of Longstreet and the death of General Jenkins', 'extra announces the serious wounding of Longstreet', 'will be promulgated to the troops tomorrow morning', 'greatest enthusiasm', 'Samuel Wilkeson', 'tore up the railroad effectually', 'had no engagement', 'Let this go over wires from Monroe'],
 'F2 5740/0': ['impossible to save all the wire between White House and West Point', 'save all the wire between White House', 'cutting it into as many pieces as possible with axes', 'cable at West Point should be taken up', 'Jamestown', 'wire between White House and West Point', 'no trouble from guerillas', 'shorter and more direct route', 'sorry weather has prevented your getting cable', 'Bickford'],
 'F3 5744/1': ['can only protect line from City Point to Fort Powhatan', 'protect the rest very soon', 'important that line be built to that point immediately', 'asked Bickford to send Perkins and party', 'Bickford to remain and take charge of closing out that line', 'General Abercrombie wishes', 'Abercrombie wishes White House office kept open', 'teams and a good guard left Yorktown this morning for West Point', 'Grants headquarters are removed', 'last two orderlies have been unable to find them', 'Bickford reports that General Grants headquarters', 'Burr Moody'],
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
