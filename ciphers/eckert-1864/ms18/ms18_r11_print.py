#!/usr/bin/env python3
"""MS18-R10: print search for the one filed row (9790/1, E420) in the cached OR/ORN djvu texts: letters-only phrase grep over
sources/ia-fulltext/print-check/*.gz, and a date + addressee window search (13 July 1864, Hunter, Wright, Early). A miss is a search result (rule 10)."""
import gzip, glob, os, re
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = ['has crossed the Rapidan','crossing of the Rapidan effected','whether the enemy intends giving battle this side of Richmond','forty-eight hours now will demonstrate','intends giving battle this side of Richmond','Know that we have crossed the Rapidan','General Grants army has crossed the Rapidan'] 
T = {os.path.basename(p)[:-12]: gzip.open(p, 'rt', errors='ignore').read() for p in sorted(glob.glob(D + '/*_djvu.txt.gz'))}
print('volumes searched:', len(T))
for ph in PH:
    print('PHRASE |', ph, '|', ','.join(v for v, t in T.items() if norm(ph) in norm(t)) or 'none')
for v, t in T.items():
    if not (v.startswith('warofrebellion')): continue
    t2 = re.sub(r'\s+', ' ', t); n = h = 0; ex = []
    for m in re.finditer(r'May\s+4\W{1,4}\s*1864', t2, flags=re.I):
        n += 1; w = t2[m.start()-150:m.end()+500]
        if re.search(r'Butler|Sheldon', w) and re.search(r'Rapidan', w, re.I): h += 1; ex.append(w[:420])
    if n: print(f'DATE | {v} | headings {n} | with Hunter+terms {h}')
    for e in ex[:3]: print('     ', e)
