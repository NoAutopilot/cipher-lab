#!/usr/bin/env python3
"""MS18-R3 (9 Oct 2026): letters-only phrase grep of the ten MS18-R3 rows' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments, e.g. OR I/36 pt 3, 41 pt 4, 47 pt 3, 49 pt 2). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'X1 10016/1': ['permitted to go to Canada', 'through the States as he may select', 'not to return to the United States without first obtaining leave', 'Joseph E. Johnston'],
 'X2 9808/1': ['drove him back toward Old Town', 'can you not push forward', 'defeated the enemy last night near'],
 'X3 9745/1': ['plot to seize a steamer going from', 'Phillips is tall and thin', 'goatee wears a diamond ring', 'de Lasalle'],
 'X4 9746/0': ['immediately send down the Mississippi River to report to', 'Hurlbut the following regiments', 'Sixty-eighth United States Colored', 'Twelfth Missouri Volunteer Cavalry'],
 'X5 9693/1': ['barrels powder, part cannon and part musket', 'Berrien at Pittsburgh', 'retain it at Pittsburgh subject to your order'],
 'X6 9881/1': ['imperative that reinforcements be sent to him', 'with all possible despatch', 'by forced marches his men can rest on the steamers', 'Hudson is crossing the Tennessee'],
 'X7 9886/0': ['assume command of all troops belonging to the Department of Missouri', 'now serving on the western border', 'till he reaches the troops of'],
 'X8 9888/2': ['at Cape Girardeau and New Madrid that could be spared', 'I think every man you can possibly get should be hurried to', 'regiment at Cairo not required there'],
 'X9 9864/0': ['again tender its thanks to you', 'Torbert, Merritt, and Custer', 'the efficient arm in this war', 'brilliant victory won last Sunday'],
 'X10 10056/2': ['M. H. Alberger', 'Hall the safe key', 'bring it with you', 'leave the safe open'],
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
