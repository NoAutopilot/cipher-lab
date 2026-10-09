#!/usr/bin/env python3
"""FM-R7a (9 Oct 2026): letters-only phrase grep of the FM-R7a entries' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5644/1': ['W W Shore', 'Shore whom I sent away from this Department', 'arrest him and send him to me', 'found in the Richmond papers that his articles', 'aid and comfort to the enemy Butler'],
 'F2 5581/1': ['Outpost near Suffolk was evacuated in a hurry', 'retreated to Bowers Hill', 'Homans left his key behind', 'Bowers Hill'],
 'F3 5746/1': ['kept open for some days yet', 'building party ready to go to Jamestown', 'live cannot be taken down', 'work on south side of river'],
 'F4 5660/2': ['arbitrary words should be used when at all possible', 'time should never be left out', 'be very careful in punctuation', 'come here without being timed'],
 'F5 5666/1': ['ten porous cups broken', 'spools burnt through', 'relay was torn to pieces', 'taking off battery and relay in storms', 'nothing important going on considerable firing yesterday'],
 'F6 5750/1': ['deserters from rebel Ironclads confirm previous information', 'Rebel tug from bend above fired a shot or two', 'flag ship Agawam', 'sprinkle of rain'],
 'F7 5771/1': ['between Laurel and Beltsville', 'release the rebels confined there', 'force of rebel cavalry crossed the', 'Communication is all right', 'Buell New Castle'],
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
