#!/usr/bin/env python3
"""MS18-R7 (9 Oct 2026): letters-only phrase grep of the ten MS18-R7 rows' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments, e.g. OR I/36 pt 3, 41 pt 4, 47 pt 3, 49 pt 2). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'X1 9842/1': ['withdraw from', 'chief quartermaster', 'cash notes or certificates', 'credits therefor', 'now under his control'],
 'X2 9907/1': ['Mobile and Ohio', 'cut the', 'Hood\'s army can not be supplied', 'be supplied by that route', 'call on General Reynolds'],
 'X3 9878/1': ['by no means certain that he will do so', 'absent from Washington', 'send you reinforcements', 'communicate with General Rosecrans'],
 'X4 9673/1': ['should leave his present duties', 'Devereux', 'McCallum', 'has left for Nashville'],
 'X5 10061/0': ['keep a very close watch on the man', 'close watch on the man referred to'],
 'X6 10013/0': ['deliver to you at St. Louis', 'serviceable cavalry horses', 'cavalry horses'],
 'X7 9774/1': ['revoked the order that you report to him in person', 'take immediate command of operations', 'enemy\'s forces now threatening Maryland'],
 'X8 9820/3': ['may be released and allowed to proceed', 'observe the course of trade', 'whatever may transpire', 'more detectives'],
 'X9 9759/1': ['commenced last night his movement to the south side of the James', 'completely routed him', 'Morgan at Cynthiana', 'that is the way to do it'],
 'X10 9732/1': ['Marks\' Mills', 'supply this loss in provisions and transportation', 'Washita', 'Steele\'s supply train'],
 'X11 10048/1': ['Sharkey', 'formation of militia companies', 'countermanding this proclamation'],
 'X12 10003/2': ['Joseph E. Brown', 'close custody under sufficient and secure guard', 'hold no communication, verbal or written'],
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
