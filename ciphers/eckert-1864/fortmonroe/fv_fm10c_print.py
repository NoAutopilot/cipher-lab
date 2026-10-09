#!/usr/bin/env python3
"""FV-FM10c (9 Oct 2026; copy of fv_fm9e_print.py): letters-only phrase grep of the clear phrases of O9-BD (5771), O9-CA/CB/CC (5570) and
O9-CD (5576) over the cached print-check djvu texts plus scratch *.txt given as argv, then KWIC for rare names in the civil-war volumes.
A miss is a search result, not a statement about print (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'O9-BD': ['between Laurel and Beltsville', 'release the rebels confined there', 'deems reliable that a force', 'precaution would do no harm',
           'precautions would do no harm', 'reported south of the railroad near the places named', 'communication is all right to Baltimore',
           'run steamers from Havre de Grace', 'painful rumors', 'one of the staff here has received information'],
 'O9-CA': ['where A F Brengle has gone', 'Brengle has gone', 'brought down on flag of truce boat', 'answer immediately to me',
           'private secretary to', 'Davenport private secretary'],
 'O9-CB': ['Brengle is in this city', 'I will find him and wait orders', 'lives in Frederick'],
 'O9-CC': ['have just found Brengle', 'will send him down tonight', 'will send him down to-night', 'prisoners not yet arrived'],
 'O9-CD': ['will try and get a description', 'put the letter in office and watch it', 'it will bring him', 'he is expecting it',
           'chief detective', 'Hays office'],
}
KW = ['Brengle', 'Davenport', 'Horner', 'Buell', 'Beltsville', 'Point Lookout', 'Havre de Grace']
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
civ = [v for v in texts if any(k in v for k in ('warofrebellion', 'officialrecords', 'privateofficial', 'privateoffice', 'butler', 'military', 'lincolnintel'))]
for k in KW:
    for v in civ:
        for m in re.finditer(re.escape(k), texts[v]):
            s = ' '.join(texts[v][max(0, m.start()-200):m.end()+200].split())
            if k == 'Davenport' and not re.search(r'secretary|Butler|Brengle', s): continue
            if k == 'Horner' and not re.search(r'detective|Lee|New York', s): continue
            if k == 'Buell' and not re.search(r'Castle|telegraph|operator|M\. ?V', s): continue
            if k in ('Point Lookout', 'Havre de Grace') and not re.search(r'July 1[234]|Ord|steamer', s): continue
            print('KWIC', k, v, '::', s)
