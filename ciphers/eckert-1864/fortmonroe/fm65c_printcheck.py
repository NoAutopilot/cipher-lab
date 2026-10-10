#!/usr/bin/env python3
"""FM65-C (10 Oct 2026): letters-only phrase grep of the FM65-C rows' readable phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5867/0': ['Robie and Cosgrove', 'edges of these cracks', 'brass bearings', 'danger of a break down', 'blowing gale tonight', 'main journal'],
 'F2 5868/0': ['got off for Monroe before I could countermand', 'let me know what orders you give her', 'she had better coal there and return to Annapolis', 'impossible for her to come up here'],
 'F3 5867/2': ['no other vessels of forage here', 'have not seen General Abbott', 'Emerick City Point', 'arrived nor sailed'],
 'F4 5869/1': ['Carney Superintendent Negro affairs', 'George J Carney', 'Frank J White', 'Janeway'],
 'F5 5870/0': ['Ariel and General Sedgwick have arrived from Baltimore', 'I do not know what others are to come nor any reason for delay', 'no forage vessels since'],
 'F6 5871/0': ['Ericsson writes he has Departments approbation', 'Shall I get ours out', 'buoys lighted weather here favorable', 'Niagara and Pawnee to leave'],
 'F7 5871/1': ['have sailed in perfect order', 'Sedgwick Ariel', 'ditto ditto'],
 'F8 5873/1': ['will start in half an hour', 'all as ordered', 'sailed in perfect order Mr Morgan'],
 'F9 5877/0': ['mule teams complete', 'fifteen days rations water and coal', 'what time can this transportation be here', 'G. W. Bradley Colonel and Chief Quartermaster'],
 'F10 5877/1': ['just in left off Fort Fisher yesterday morning', 'weather splendid outside', 'our troops were all landed and had entrenched', 'no attack has been made on our troops'],
 'F11 5877/2': ['Dupont Thames Haze and Sentinel', 'are all we have', 'put fifteen days rations on such vessels', 'each vessel will carry', 'Small Chief Quartermaster'],
 'F12 5878/1': ['enough are here to carry', 'every effort will be made to have all the vessels that are here ready by tomorrow noon', 'will the Fort Fisher news change your instructions', 'Quartermaster at City Point will be telegraphed when each vessel leaves here'],
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
