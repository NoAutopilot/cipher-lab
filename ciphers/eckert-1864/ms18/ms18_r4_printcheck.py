#!/usr/bin/env python3
"""MS18-R4 (9 Oct 2026): letters-only phrase grep of the ten MS18-R4 rows' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments, e.g. OR I/36 pt 3, 41 pt 4, 47 pt 3, 49 pt 2). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'X1 9892/1': ['ranks General Stanley as', 'assign General Stanley to', 'placing General Stanley under', 'ranks Stanley as'],
 'X2 9835/0': ['does not deem him fit to command', 'relieve Brigadier-General E. A. Paine', 'relieve General Paine from command', 'Paine from command at Paducah'],
 'X4 9827/1': ['provisional battalion of cavalry belonging to', 'guarding the river while the', 'cannot get his regiment ready', 'Gregg'],
 'X5 9866/3': ['may understand General Grant', 'while the communication between you and General Sherman is interrupted', 'copies of the following dispatches', 'frequently advised of what transpires'],
 'X6 9825/2': ['absolutely necessary that General Hurlbut', 'on both banks of the Mississippi', 'cannot otherwise protect the navigation', 'conflict of orders'],
 'X7 9820/1': ['Gordon Bruce', 'Alexander Keith', 'machinery of some description', 'Mitchell, Kennuer'],
 'X8 9811/2': ['wishes to go to Monocacy this afternoon', 'have your car put on', 'departure of the General must be kept'],
 'X9 9779/1': ['sending State troops from', 'Shelton Howe', 'about 20,000 strong', 'moving by Urbana'],
 'X10 9843/1': ['incompatible', 'relieve Colonel Crane', 'disbursing officer', 'Inspector and of disbursing officer'],
 'X11 9895/2': ['Burnet House', 'Grierson', 'serviceable horses there for issue', 'Planters House'],
 'X3 10002/2': ['suspend preparations for', 'overrun the whole country', 'attempts to hold out'],
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
