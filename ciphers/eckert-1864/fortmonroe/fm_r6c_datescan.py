#!/usr/bin/env python3
"""FM-R6c (9 Oct 2026): date + keyword window scan (30 lines) of cached OR/ORN/Butler djvu texts plus scratch texts for each FM-R6c entry's date
and rare words; the phrase grep (fm_r5c_printcheck.py) can miss a printed telegram whose wording differs from the decode, this catches it by date.
Control: none that must fire (see NOTES). A miss is a search result (rule 10). Usage: fm_r5c_datescan.py [scratch.txt ...]"""
import gzip, glob, os, re, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
E = {
 'F1 5777/2': (r'Aug\w*\.?\s+9,?\s+1864', ['Sheldon','Eckert','Chambersburg','Gaughey','Newbern','Monroe']),
 'F1b 5777/2': (r'Aug\w*\.?\s+6,?\s+1864', ['Sheldon','Gaughey','Newbern','Chambersburg','Morehead']),
 'F2 5659/0': (r'May\s+[5-9],?\s+1864', ['Albemarle','Sheldon','Christian Advocate','Roanoke','Wallace','Sassacus']),
 'F3 5786/0': (r'Oct\w*\.?\s+4,?\s+1864', ['Rucker','Sheldon','Eckert','Illinois','steamers','Knox']),
}
texts = {os.path.basename(p)[:-12]: gzip.open(p, 'rt', errors='ignore').read() for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz')))}
for p in sys.argv[1:]: texts[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
print('volumes searched:', len(texts))
for e, (dre, kws) in E.items():
    rx = re.compile(dre.replace(r'\s+', r'\s+'), re.I); n = 0
    for v, t in texts.items():
        lines = [re.sub(r'\s+', ' ', l) for l in t.split('\n')]
        for i, l in enumerate(lines):
            if rx.search(l):
                w = ' '.join(lines[i-3:i+30]).lower(); hit = [k for k in kws if k.lower() in w]
                if len(hit) >= 2: print(e, '|', v, '| line', i+1, '|', ','.join(hit), '|', l[:70]); n += 1
    if not n: print(e, '| none')
