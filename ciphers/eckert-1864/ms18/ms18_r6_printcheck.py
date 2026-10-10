#!/usr/bin/env python3
"""MS18-R6 (9 Oct 2026): letters-only phrase grep of the ten MS18-R6 rows' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments, e.g. OR I/36 pt 3, 41 pt 4, 47 pt 3, 49 pt 2). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'X1 9674/0': ['Governors of States have no authority to furlough', 'no authority to furlough', 'rank of lieutenant-colonel', 'Mr. Beckwith has been restored'],
 'X2 9886/1': ['all the troops you can lay hand on', 'sent forward with the least possible delay', 'opposed by Hood\'s entire army', 'cavalry of Wheeler'],
 'X3 9676/1': ['directed to send recruits to their regiments as fast as collected', 'send new regiments to the field as fast as organized', 'who do you want to command', 'Name several to select from'],
 'X4 9769/1': ['shall not be repaired at present', 'guage should be changed to', 'gauge should be changed to', 'are in existence'],
 'X5 9674/1': ['more than two months discussing the draft bill', 'unless it soon passes', 'furloughed', 'same or worse condition than yours'],
 'X6 10005/2': ['Boulware', 'King and Queen Court-House', 'send him here under guard', 'Judge-Advocate'],
 'X7 9801/0': ['gives no intimation', 'rebel army is down the valley', 'when you last heard from him', 'in what direction was he operating'],
 'X8 10027/2': ['issuing of arms to all persons', 'carrying of Government freight', 'on proper security that the arms will not be lost', 'freight over the plains'],
 'X9 10020/2': ['Thomas J. Campbell', 'send him under guard to Nashville', 'delivered to Major-General Thomas', 'forward by railroad'],
 'X10 9836/1': ['Masury & Whiton', 'Masury and Whiton', 'Fulton street', 'can be supplied by rail'],
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
