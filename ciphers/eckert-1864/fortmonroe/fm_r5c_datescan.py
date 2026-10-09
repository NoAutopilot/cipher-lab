#!/usr/bin/env python3
"""FM-R5c (9 Oct 2026): date + keyword window scan (30 lines) of cached OR/ORN/Butler djvu texts plus scratch texts for each FM-R5c entry's date
and rare words; the phrase grep (fm_r5c_printcheck.py) can miss a printed telegram whose wording differs from the decode, this catches it by date.
Control: F7 (Shepley 11 Dec 1864) must fire in warofrebellion423unit. A miss is a search result (rule 10). Usage: fm_r5c_datescan.py [scratch.txt ...]"""
import gzip, glob, os, re, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
E = {
 'F1 5751/2': (r'June\s+15,?\s+1864', ['Sheldon','Meigs','ferry','Monroe','vessel']),
 'F2 5722/0': (r'May\s+31,?\s+1864', ['Bickford','Coldwell','White House','Sheldon','Eckert']),
 'F3 5783/1': (r'Sept\w*\.?\s+16,?\s+1864', ['Coggins','Lawrence','Wilson','herd','Sheldon']),
 'F4 5822/0': (r'Dec\w*\.?\s+8,?\s+1864', ['Beckwith','Dodge','Sedgwick','Dupont','Rice','Webster']),
 'F5 5616/1': (r'April\s+20,?\s+1864', ['Rucker','Biggs','steamers','Port Royal','Sheldon']),
 'F6 5624/0': (r'April\s+22,?\s+1864', ['Belcher','Vinton','assistant quartermasters','Butler','Sheldon']),
 'F7 5827/2': (r'Dec\w*\.?\s+11,?\s+1864', ['Shepley','Hicksford','Blackwater','South Quay','Beckwith']),
 'F8 5632/0': (r'April\s+24,?\s+1864', ['Dana','blockade','runner','Diamond','Smith','Sheldon']),
 'F9 5794/1': (r'Oct\w*\.?\s+16,?\s+1864', ['Stanton','Hooker','Logan','Missouri','Dealy']),
 'F10 5609/1': (r'April\s+18,?\s+1864', ['Maddox','tobacco','Stanton','Butler','Biggs']),
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
