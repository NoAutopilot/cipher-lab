#!/usr/bin/env python3
"""N2R-4 (10 Oct 2026): (a) letters-only phrase grep of the No. 2 readings of ms18/n2r4_entries.txt in OR djvu texts (cached sources/ia-fulltext/print-check
plus any paths given), (b) date-window + term search (heading date within the window and all term groups inside 600 chars). A miss is a search result (rule 10).
Usage: n2r4_printcheck.py FILE...  (.txt/.gz)"""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'Z1 9701/0 9 Apr 1864': ['has been detained in Baltimore a few days for a special purpose', 'it would save transportation', 'will be given another battery in place of that now in the'],
 'Z2 9850/1 25 Sep 1864': ['remove Heintzelman from any function', 'have you any objection to General Hooker being assigned', 'no vacant major-generalship for Crook', 'muster out Heintzelman and make a vacancy'],
 'Z3 9755/0 7 Jun 1864': ['What is the gauge of the Vicksburg and Monroe', 'no grading between Monroe and Shreveport', 'not likely that any work has been done upon it since this rebellion'],
 'Z4 9898/2 23 Nov 1864': ['hotels in this city and Georgetown have been searched', 'detectives and patrols will make every effort to find', 'Buyers'],
 'Z5 9759/0 13 Jun 1864': ['expediency of expense is so much doubted', 'repair of the railroad from Vicksburg to Monroe', 'it has been referred to General Grant'],
 'Z6 9685/1 10 Mar 1864': ['by Executive order of this date has assigned you', 'by Executive order of this date has assigned to you', 'the command of the Armies of the United States', 'Pursuant to the authority of the act of Congress approved'],
 'Z7 9906/0 5 Dec 1864': ['Should they not be assembled at Bridgeport', 'cause General Rucker to be notified', 'instead of at Monroe'],
 'Z8 9739/2 19 May 1864': ['It is Canby and not Hurlbut', 'combined departments of the Gulf and Arkansas', 'Hurlbut is not on duty', 'Banks is to be relieved'],
 'Z9 9782/0 9 Jul 1864': ['arrival of Morgan', 'remainder of the Sixth Corps should be sent to this place', 'ordered all troops to be stopped at Baltimore', 'remainder of Wright'],
 'Z10 9880/0 31 Oct 1864': ['telegram just received from General Curtis states', 'Rosecrans has recalled his troops from the pursuit of Price', 'contrary to repeated orders', 'pursuit must be continued'],
}
DW = [('Z1 9 Apr Baltimore/Maryland regiment/12th Corps', r'April\s+(8|9|10)\W{1,4}\s*1864', ['Baltimore|Maryland|Slocum|Twelfth'], ['detained|veteran|transportation']),
 ('Z2 25 Sep Heintzelman/Hooker/Crook', r'Sept(ember|\.)?\s+2[456]\W{1,4}\s*1864', ['Heintzelman|Hooker'], ['Crook|vacancy|muster out']),
 ('Z3 7 Jun Vicksburg-Monroe railroad gauge', r'June\s+[678]\W{1,4}\s*1864', ['Monroe|Vicksburg'], ['gauge|rail']),
 ('Z4 23 Nov hotels Georgetown Buyers', r'Nov(ember|\.)?\s+2[234]\W{1,4}\s*1864', ['Georgetown|Buyers|detective'], ['hotel|search']),
 ('Z5 13 Jun Vicksburg-Monroe railroad repair', r'June\s+1[234]\W{1,4}\s*1864', ['Monroe|Vicksburg'], ['rail|expense|repair']),
 ('Z6 10 Mar Grant assigned command of armies', r'March\s+(9|10|11)\W{1,4}\s*1864', ['Grant'], ['assigned|command of the Armies']),
 ('Z7 5 Dec Ingalls/Rucker/Bridgeport', r'Dec(ember|\.)?\s+[456]\W{1,4}\s*1864', ['Rucker|Ingalls'], ['Bridgeport|assembled|Monroe']),
 ('Z8 19 May Canby/Hurlbut/Banks relieved', r'May\s+(18|19|20)\W{1,4}\s*1864', ['Canby|Hurlbut'], ['Banks|relieved|Gulf']),
 ('Z9 9 Jul Wallace/Sixth Corps/Baltimore', r'July\s+(8|9|10)\W{1,4}\s*1864', ['Baltimore|Wallace'], ['Sixth Corps|Wright|Morgan|stopped']),
 ('Z10 31 Oct Curtis/Rosecrans/Price pursuit', r'(Oct(ober|\.)?\s+(30|31)|Nov(ember|\.)?\s+1)\W{1,4}\s*1864', ['Curtis|Rosecrans'], ['Price|pursuit'])]
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    if 'warofrebellion' in p or 'official' in p or 'butl' in p: texts[os.path.basename(p)[:-12]] = gzip.open(p, 'rt', errors='ignore').read()
for p in sys.argv[1:]:
    op = gzip.open if p.endswith('.gz') else open
    texts[os.path.basename(p).split('_djvu')[0].split('.')[0]] = op(p, 'rt', errors='ignore').read()
print('volumes searched:', len(texts), ' '.join(sorted(texts)))
nt = {v: norm(t) for v, t in texts.items()}
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in nt.items() if norm(ph) in t]
        print('PH', e, '|', ph, '|', ','.join(hits) or 'none')
for v, t in texts.items():
    t2 = re.sub(r'\s+', ' ', t)
    for lab, dre, a, b in DW:
        n = h = 0; ex = []
        for m in re.finditer(dre, t2, flags=re.I):
            n += 1; w = t2[max(0, m.start()-150): m.end()+600]
            if all(re.search(x, w, re.I) for x in a) and all(re.search(x, w, re.I) for x in b): h += 1; ex.append(w[:350])
        if h: print(f'DW {v} | {lab} | date headings {n} | with terms {h}')
        for e in ex[:2]: print('     ', e)
