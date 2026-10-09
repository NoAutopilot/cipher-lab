#!/usr/bin/env python3
"""FV-MS18b (9 Oct 2026): letters-only phrase grep of E322-E325's decoded phrases (as corrected by FV-MS18b: Canby = 'can be',
hopper paddle = 'operate', shady = forage, Galway = Richmond) in OR djvu texts fetched to scratch (dir argument) plus the cached
ser. II vol. 7 (sources/ia-fulltext/print-check/warofrebellion0207rootrich). Prints volume, phrase, and 300 chars around each hit."""
import gzip, os, re, sys, glob
def norm(s): return re.sub(r'[^a-z]+', '', s.lower())
PH = {
 'E322': ['plenty of forage at Port Royal', 'leaves New York today with funds', 'remain with that part of your command', 'garrison what you deem necessary',
          'competent officer', 'returned to Tennessee', 'temporary wants', 'send your estimates', 'means of transportation to get it to you'],
 'E323': ['breaking up', 'west of the Mississippi south of the Arkansas', 'receive orders from Sheridan', 'can be spared from Arkansas',
          'operate against the enemy south of him', 'If Reynolds can be replaced'],
 'E324': ['Fort Pulaski', 'Judge Campbell', 'held in close custody', 'until further orders', 'Seddon', 'safe custody'],
 'E325': ['rebel agents', 'Kendall', 'Ritchie', 'Cape Girardeau', 'New Madrid', 'seizure of their papers', 'Monday morning next', 'Tunstall', 'Kennerly'],
}
vols = {}
for p in sorted(glob.glob(os.path.join(sys.argv[1], '*.txt'))):
    vols[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
c = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check', 'warofrebellion0207rootrich_djvu.txt.gz')
vols['warofrebellion0207rootrich'] = gzip.open(c, 'rt', errors='ignore').read()
for v, raw in vols.items():
    n = norm(raw)
    # map normalised offsets back to raw
    idx = [i for i, ch in enumerate(raw) if ch.isalpha()]
    for e, ps in PH.items():
        for ph in ps:
            q = norm(ph); k = 0; hits = []
            while True:
                j = n.find(q, k)
                if j < 0: break
                hits.append(j); k = j + 1
            if hits:
                print(f"{e}\t{v}\t{ph}\t{len(hits)}")
                if len(hits) <= 4:
                    for j in hits:
                        r = idx[j]; print('    ', re.sub(r'\s+', ' ', raw[max(0, r-250):r+250]))
