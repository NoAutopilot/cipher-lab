#!/usr/bin/env python3
"""FV-FM9c (9 Oct 2026, verifier): letters-only phrase grep of E305/E306 (and E304 control phrases) over the cached print-check djvu
texts plus scratch *.txt given as argv (OR I/36 pt 3 `warofrebellion363unit` = to 12 June 1864, OR I/40 pt 2 `warofrebellion402unit`
= from 13 June 1864), with KWIC for names in those two. A miss is a search result (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E304 5662/0 (control)': ['Swift Creek within two miles', 'splendid charge', 'square earthwork', 'struck the Brewster', 'Richmond extra'],
 'E305 5740/0': ['impossible to save all the wire', 'as many pieces as possible', 'with axes or otherwise', 'cable at West Point', 'line from there to Gloucester',
                 'no trouble from guerrillas', 'occupies south side', 'shorter and more direct route', 'save what he can'],
 'E306 5744/1': ['can only protect line from City Point', 'protect the line from City Point to Fort Powhatan', 'send Perkins and party',
                 'take charge of closing out', 'Abercrombie wishes', 'office kept open', 'come out right', 'circumstances will allow',
                 'cable about one mile long', 'headquarters are removed', 'unable to find them'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = gzip.open(p, 'rt', errors='ignore').read()
for p in sys.argv[1:]:
    texts[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
N = {k: norm(v) for k, v in texts.items()}
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [f'{v}[{t.count(norm(ph))}]' for v, t in N.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
for name in ['Bickford', 'Sheldon', 'Perkins', 'Abercrombie']:
    for v, t in texts.items():
        if v not in ('warofrebellion363unit', 'warofrebellion402unit'): continue
        for m in list(re.finditer(name, t))[:8]:
            print('KWIC', name, v, '::', ' '.join(t[max(0, m.start()-150):m.start()+200].split()))
