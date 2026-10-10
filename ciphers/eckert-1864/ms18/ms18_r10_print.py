#!/usr/bin/env python3
"""MS18-R10: print search for the one filed row (9790/1, E420) in the cached OR/ORN djvu texts: letters-only phrase grep over
sources/ia-fulltext/print-check/*.gz, and a date + addressee window search (13 July 1864, Hunter, Wright, Early). A miss is a search result (rule 10)."""
import gzip, glob, os, re
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = ['seem to be moving toward Edwards Ferry', 'Wright will follow by river road', 'form a junction with him at that place',
      'is probably about the same as that you encountered in the valley', 'estimated at over twenty thousand', 'why so slow',
      'rebel force is probably about the same', 'left our front in the night']
T = {os.path.basename(p)[:-12]: gzip.open(p, 'rt', errors='ignore').read() for p in sorted(glob.glob(D + '/*_djvu.txt.gz'))}
print('volumes searched:', len(T))
for ph in PH:
    print('PHRASE |', ph, '|', ','.join(v for v, t in T.items() if norm(ph) in norm(t)) or 'none')
for v, t in T.items():
    if not (v.startswith('warofrebellion3') or v.startswith('warofrebellion4')): continue
    t2 = re.sub(r'\s+', ' ', t); n = h = 0; ex = []
    for m in re.finditer(r'July\s+1[34]\W{1,4}\s*1864', t2, flags=re.I):
        n += 1; w = t2[m.start()-150:m.end()+500]
        if re.search(r'Hunter', w) and re.search(r'Wright|Edwards|Early|Rebel|enemy', w, re.I): h += 1; ex.append(w[:420])
    if n: print(f'DATE | {v} | headings {n} | with Hunter+terms {h}')
    for e in ex[:3]: print('     ', e)
