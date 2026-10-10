#!/usr/bin/env python3
"""N2R-6 (10 Oct 2026): (a) letters-only phrase grep of the No. 2 readings of ms18/n2r6_entries.txt in OR djvu texts (cached sources/ia-fulltext/print-check
plus any paths given), (b) date-window + term search (heading date within the window and all term groups inside 600 chars). A miss is a search result (rule 10).
Usage: n2r6_printcheck.py FILE...  (.txt/.gz)"""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'KA Z4 9729/1 3 May 1864': ['telegraphed to Cairo', 'has seen your telegrams but has said nothing to me', 'Your last instructions in regard to', 'I will write to you immediately'],
 'KB Z5 9697/0 7 Apr 1864': ['asks that a regiment of heavy artillery be sent', 'will be sent to him in cipher as soon as he can be found', 'left unexpectedly last night', 'has been relieved'],
 'KC Z7 9908/2 6 Dec 1864': ['New Creek disaster', 'were ordered by General Canby', 'these orders have been repeated', 'repeated some days ago'],
 'KD Z8 9798/1 19 Jul 1864': ['another regiment of heavy artillery in addition to those with', 'should be sent here as soon as you can spare it', 'I am of opinion that another'],
 'KE Z9 9832/1 3 Sep 1864': ['The Onondaga and Atlanta', 'Prepare the Saugus and Canonicus', 'iron-clads retained in the James', 'Senior Naval Officer James River'],
}
DW = [('KA 3 May Cairo/instructions/President', r'May\s+(2|3|4)\W{1,4}\s*1864', ['Cairo|instructions'], ['President|Halleck']),
 ('KB 7 Apr heavy artillery/Harpers Ferry', r'Apr(il|\.)?\s+(6|7|8)\W{1,4}\s*1864', ['heavy artillery|Heavy Artillery'], ['Harper|Sigel|Burnside']),
 ('KC 6 Dec New Creek/Canby', r'Dec(ember|\.)?\s+(5|6|7)\W{1,4}\s*1864', ['New Creek'], ['Canby|Kelley|Wheeling']),
 ('KD 19 Jul heavy artillery/Washington', r'July\s+(18|19|20)\W{1,4}\s*1864', ['heavy artillery|Heavy Artillery'], ['Halleck|Grant|spare']),
 ('KE 3 Sep Onondaga/Saugus/Canonicus', r'Sept(ember|\.)?\s+(2|3|4)\W{1,4}\s*1864', ['Onondaga|Saugus|Canonicus'], ['James|Paulding|iron'])]
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
