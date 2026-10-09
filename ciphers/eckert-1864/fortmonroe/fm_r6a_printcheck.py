#!/usr/bin/env python3
"""FM-R6a (9 Oct 2026): letters-only phrase grep of the FM-R6a entries' hand-read phrases in the cached OR/ORN/Butler djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments); prints volume and a 100-char context of the first hit per phrase.
A miss is a search result, not a verdict (rule 10). Usage: python3 fm_r6a_printcheck.py [extra.txt ...]"""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5639/1': ['Plymouth is evacuated', 'rebels are leaving North Carolina', 'Plymouth evacuated rebels leaving', 'informed by General Butler that he has information that Plymouth', 'let me know what I am to do in this movement'],
 'F2 5764/0': ['rebel ironclads are taking on board sand in bags', 'no change in the naval situation', 'taking on board sand in bags', 'Flag-Ship Malvern Farrars Island'],
 'F3 5697/1': ['if White House is made the base of supplies', 'West Point will also be made a depot', 'the old line was all destroyed last year', 'fine large chestnut poles and have not rotted down', 'have asked OBrien about material', 'I have very little wire on hand now', 'cross at Yorktown to Glouster Point', 'Gloucester Point thence by a direct road to the Mattapony'],
 'F4 5797/1': ['we took Ships Gap', 'obstructed Snake Creek Pass to delay our trains', 'I can move in any direction I want', 'reoccupy the railroad and put the construction corps to work', 'repair the break from the tunnel to Resaca', 'Roddys force moved from Tuscumbia yesterday', 'Hoods strength of his cavalry not known', 'no additional move from the Tennessee River except that Roddys force', 'the first positive fact that Hood contemplated an invasion of Tennessee', 'the necessary orders have been given for the repair of the railroad'],
}

texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = gzip.open(p, 'rt', errors='ignore').read()
for p in sys.argv[1:]:
    texts[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
N = {v: norm(t) for v, t in texts.items()}
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in N.items() if norm(ph) in t]
        ctx = ''
        if hits and len(norm(ph)) > 14 and len(hits) <= 3:
            v = hits[0]; i = N[v].find(norm(ph)); ctx = ' ~ ' + N[v][max(0, i-30):i+60]
        print(e, '|', ph, '|', (','.join(hits[:6]) + (' +%d' % (len(hits)-6) if len(hits) > 6 else '')) or 'none', ctx)
