#!/usr/bin/env python3
"""AUD2-LEDGER-24 (9 Oct 2026, second-audit verifier): letters-only phrase grep of E305/E306 over IA djvu texts given as argv
(Plum, Military Telegraph vols 1-2 `militarytelegraph01plumrich`/`02plumrich`; Bates, Lincoln in the Telegraph Office `lincolnintelegra00bates`;
OR I/36 pt 3 `warofrebellion363unit`; OR I/40 pt 2 `warofrebellion402unit`), plus KWIC for the line's names and places.
A miss is a search result, never a novelty verdict (rule 10)."""
import os, re, sys
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E305 5740/0': ['impossible to save all the wire', 'as many pieces as possible', 'with axes or otherwise', 'cable at West Point',
                 'line from there to Gloucester', 'no trouble from guerrillas', 'no trouble from guerillas', 'shorter and more direct route',
                 'save what he can', 'join the force at Jamestown', 'getting cable', 'between White House and West Point',
                 "between White House and Wilson", 'act upon your own judgment'],
 'E306 5744/1': ['only protect line from City Point', 'City Point to Fort Powhatan', 'Perkins and party', 'closing out', 'Abercrombie wishes',
                 'office kept open', 'come out right', 'circumstances will allow', 'cable about one mile', 'headquarters are removed',
                 'unable to find them', 'report to OBrien', "report to O'Brien", 'two operators'],
}
KW = ['Bickford', 'Sheldon', 'Perkins', 'Abercrombie', 'Gloucester', 'Wilson', 'Powhatan', 'Jamestown', 'Gaughey']
texts = {os.path.basename(p)[:-4]: open(p, errors='ignore').read() for p in sys.argv[1:]}
N = {k: norm(v) for k, v in texts.items()}
print('volumes searched:', ', '.join(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [f'{v}[{t.count(norm(ph))}]' for v, t in N.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
for v, t in texts.items():
    if not v.startswith(('militarytelegraph', 'lincolnintelegra')): continue
    t = ' '.join(t.split())
    for name in KW:
        ms = list(re.finditer(name, t))
        print(f'KWIC {name} {v} n={len(ms)}')
        for m in ms[:6]:
            print('   ::', t[max(0, m.start()-160):m.start()+220])
