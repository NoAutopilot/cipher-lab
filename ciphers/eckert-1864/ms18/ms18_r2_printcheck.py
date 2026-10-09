#!/usr/bin/env python3
"""MS18-R2 (9 Oct 2026): letters-only phrase grep of the ten MS18-R2 rows' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'X1 10009/1': ['leaves New York today with funds', 'Quartermaster Department says that there is plenty', 'plenty of forage at Port Royal', 'remain with that part of your command', 'garrison what you deem necessary points'],
 'X2 10010/2': ["breaking up Hurlbut's division", 'assigning Sheridan to the command', 'Reynolds to receive orders from Sheridan', 'Canby spared from Arkansas'],
 'X3 10058/0': ['pardon means restoration of property', 'only that portion which has been libeled', 'Van Duzer Nashville'],
 'X4 10024/2': ['Judge Campbell', 'sent to Fort Pulaski', 'held in close custody there until further orders', 'Seddon late Secretary of War', 'Fort Pulaski Hilton Head Gillmore'],
 'X5 9889/0': ['directs the arrest at 10 a.m. on Monday morning next', 'following named rebel agents and the seizure of their papers', 'William Kendall', 'Lewis Kennerly', 'Wm Ritchie'],
 'X6 9889/2': ['Thos T. Tunstall', 'Tunstall Nashville', 'seizure of his papers'],
 'X7 9813/1': ['Cavalry Bureau has requested that all unserviceable', 'depots at Gallipolis', 'Geesboro', 'every possible effort be made to mount your cavalry'],
 'X8 10016/2': ['will send you 2700 horses as fast as possible', 'cannot probably be well replaced in that state', 'need not a Co.'],
 'X9 9864/1': ['all forces that can possibly be spared from Kentucky should be sent to', 'to enable him to meet any force that Hood may send', 'send copy to Kearney'],
 'X10 9873/1': ['it is reported here that Forrest is threatening both Paris', 'if by the assistance of Kearney', 'drive him south it would relieve that part of the country'],
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
