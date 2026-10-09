#!/usr/bin/env python3
"""MS18-R5 (9 Oct 2026): letters-only phrase grep of the ten MS18-R5 rows' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments, e.g. OR I/36 pt 3, 41 pt 4, 47 pt 3, 49 pt 2). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'X1 10065/2': ['writ of habeas corpus in case of minors', 'minors is not to be resisted', 'names of officers by whom minors', 'illegally enlisted', 'defend the case as well as possible'],
 'X2 9821/1': ['E. L. Wentz', 'held as hostages for', 'guided the raiders in their late raid', 'hand over to'],
 'X3 10004/1': ['reward of $100,000 for his arrest', 'sent to Washington under guard', 'any steps towards reorganizing rebels', 'Instructions have been sent you in regard to'],
 'X4 9791/0': ['rebels have no troops in the direction of Baltimore', 'except mounted guerrillas', 'move out of Baltimore as soon as it becomes evident', 'seems to be moving toward Edwards Ferry'],
 'X5 9863/0': ['these written accounts of such a character', 'are about all the information the enemy wants', 'what use is it to the northern reader', 'Stiner'],
 'X6 9729/2': ['bring back any witness discharged', 'President of the court ordered to get new rooms', 'Judge Advocate ordered to report to you', 'cases in Boston and New York navy yards'],
 'X7 9825/1': ['no other troops than those already reported', 'it was rumored at Orange C. H. Wednesday', 'losing all his artillery', 'They bring no other information'],
 'X8 10043/1': ['keep the prisoner in close and secure custody', 'secure his papers', 'telegraph in cipher briefly the substance or purport', 'publication signed'],
 'X9 9753/1': ['First Maryland Veteran Cavalry', 'will be sent to Washington to report to General Augur', 'is much weakened it will be necessary to concentrate it', 'occupying only the more important points'],
 'X10 9770/1': ['such of your forces as are not required to hold the Kanawha', 'prevent any raid into Maryland', 'Ewell\'s corps has returned', 'hears nothing of Breckenridge'],
 'X11 9674/0': ['Governors of States have no authority to furlough', 'authority to furlough troops', 'Please report any cases that have occurred'],
 'X12 9886/1': ['all the troops you can lay hand on in Missouri', 'sent forward with the least possible delay', 'opposed by Hood\'s entire army', 'satisfied that all the troops'],
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
