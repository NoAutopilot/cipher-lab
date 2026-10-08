#!/usr/bin/env python3
"""LS5-R1e (8 Oct 2026): letters-only phrase grep of the LS5-R1e entries' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'X1 8984/1': ['continue you to hold the bridge across the Pamunkey', 'facilitate the junction of yourself and Sheridan', 'junction of yourself and General Sheridan with the Army of the Potomac', 'Grant is about to move his army to the James'],
 'X2 9034/1': ['should be immediately reinforced by cavalry', "Sheridan's cavalry is beginning to arrive", 'seen Mask\'s dispatch to you of last evening'],
 'X3 9124/0': ['directed to arrest Beverly Tucker', 'Beverly Tucker wherever found within the United States', 'confined in Fort Lafayette'],
 'X4 8992/1': ['fit to bring from New Orleans', 'not necessary to take up ocean steamers not already in service', 'steamers now in service fit to bring'],
 'X5 9034/0': ['Stoneman and 500 prisoners', 'Stoneman with seventy-five officers', 'Richmond dispatch of to-day contains the following'],
 'X6 9044/1': ["Fitz Hugh Lee's cavalry was at Orange", 'Longstreet is in the Valley and his corps supposed to be with him', 'brigade of Hill\'s corps was sent to Early last Friday'],
 'X10 9139/1': ['take immediate possession of the Louisville and Nashville Railroad', 'Louisville and Nashville Rail Road as vitally necessary to sustain the army', 'be instructed to take immediate possession'],
 'X11 9144/0': ['remounting the wrecks of Hood\'s army', 'supplies for remounting the wrecks of Hood', 'Stoneman\'s dispatch is received'],
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
