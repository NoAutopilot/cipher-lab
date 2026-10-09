#!/usr/bin/env python3
"""FV-FM9e (9 Oct 2026): letters-only phrase grep of E310-E313 clear phrases (from the holder's clear copies 10291, 10193 and the
ledger plain text of 5746, 5660) over the cached print-check djvu texts plus scratch *.txt given as argv (Plum, Military Telegraph
vols 1-2; OR I/40 pt 2 `warofrebellion402unit`), then KWIC for rare names in every volume. A miss is a search result (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E310': ['W. W. Shore', 'WW Shore', 'correspondent of the New York World at Baltimore', 'whom I sent away from this department',
          'his articles are giving aid and comfort', 'found in the Richmond papers that his articles'],
 'E311': ['outpost near Suffolk was evacuated', 'retreated to Bowers Hill', 'left his key behind', 'not thought the enemy will attack the present position'],
 'E312': ['office at White House will be kept open', 'kept open for some days yet', 'building party ready to go to Jamestown', 'can not be taken down till then',
          'cannot be taken down till then'],
 'E313': ['arbitrary words should be used', 'time should never be left out', 'careful in punctuation', 'without being timed', 'important words open'],
}
KW = ['Shore', 'Homans', 'Hornans', 'Bowers Hill', 'Bowers\' Hill', 'O\'Brien', 'punctuat', 'arbitrar']
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = gzip.open(p, 'rt', errors='ignore').read()
for p in sys.argv[1:]:
    texts[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
N = {v: norm(t) for v, t in texts.items()}
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        print(e, '|', ph, '|', ','.join(v for v, t in N.items() if norm(ph) in t) or 'none')
civ = [v for v in texts if any(k in v for k in ('warofrebellion', 'officialrecords', 'privateofficial', 'lewwallace', 'military', 'lincolnintel'))]
for k in KW:
    for v in civ:
        for m in re.finditer(re.escape(k), texts[v]):
            s = ' '.join(texts[v][max(0, m.start()-160):m.end()+160].split())
            if k in ('Shore',) and not re.search(r'W\. ?W\.|World|correspond', s): continue
            if k in ("O'Brien",) and not re.search(r'cipher|Bermuda|time', s, re.I): continue
            if k in ('punctuat', 'arbitrar') and not re.search(r'cipher|telegra', s, re.I): continue
            print('KWIC', k, v, '::', s)
