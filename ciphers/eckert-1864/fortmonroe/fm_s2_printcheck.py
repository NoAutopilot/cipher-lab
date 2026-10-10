#!/usr/bin/env python3
"""FM-S2 (9 Oct 2026): letters-only phrase grep of the FM-S2 entries' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5698/0': ['send me all the transportation you can', 'Colonel Biggs', 'transportation you can to Bermuda Hundred', 'telegraph what is coming'],
 'F2 5638/0': ['referred your telegram about Dunn', 'I know of none and do not believe a word against him', 'returns it endorsed'],
 'F3 5632/2': ['ready to put up at a moments notice', 'conference with Knox'],
 'F4 5627/1': ['three hundred thousand cartridges for Spencer rifles', 'cartridges for Spencer rifles with all possible dispatch', 'Theodore Edson'],
 'F5 5810/1': ['Beckwith Monroe meet you', 'Sheldon Beckwith City Point November 28'],
 'F6 5756/1': ['tell me quick if Beckwith or Caldwell have my cipher', 'have heard from Sheridan will probably get here tonight', 'Sheridan White House June 18'],
 'F7 5720/0': ['heavy and continuous firing about fifteen miles from here', 'continuous firing in direction of', 'heavy and continuous firing'],
 'F8 5814/0': ['monitors Mahopac Canonicus and Saugus', 'Mahopac Canonicus and Saugus are ready for service', 'Mahopac Saugus ready for service', 'Canonicus Saugus Mahopac with coal'],
 'F9 5768/3': ['none of the troops have arrived yet', 'New Orleans troops have arrived', 'Shaffer chief of staff', 'troops from New Orleans arrived Fort Monroe July 10'],
 'F10 5680/2': ['add to the list of extra arbitraries', 'extra arbitraries', 'mackerel and mutton'],
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
