#!/usr/bin/env python3
"""N2R-3 (10 Oct 2026): (a) letters-only phrase grep of the No. 2 readings of ms18/n2r3_entries.txt in OR djvu texts (cached sources/ia-fulltext/print-check
plus any paths given), (b) date-window + term search (heading date within the window and all term groups inside 600 chars). A miss is a search result (rule 10).
Usage: n2r3_printcheck.py FILE...  (.txt/.gz)"""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'Z1 9791/1 13 Jul 1864': ['there have debarked here', 'Emory has also reported in person', 'remainder of his divisions are close at hand', 'The head of General Wright', 'passed Fort Reno at'],
 'Z2 9839/0 12 Sep 1864': ['Inspectors have been ordered to report here for instructions', 'inspection route to Little Rock', 'special tour of inspection', 'Colonel Bingham arrives'],
 'Z3 9807/1 2 Aug 1864': ['landed last night', 'A few companies of Torbert', 'before the Sixth Corps is all landed', 'transportation of troops in small steamers is slow'],
 'Z4 9888/1 5 Nov 1864': ['I think from present appearances that Price', 'Steele\'s effective force is now about', 'cutting the Mobile and Ohio railroad', 'by which Beauregard\'s army is now supplied'],
 'Z5 9873/3 21 Oct 1864': ['no troops can at present be taken from', 'vessels collected at Alexandria', 'demurrage', 'I can form no clear idea of the condition of affairs'],
 'Z6 9813/0 6 Aug 1864': ['steamboats in addition to what are now employed', 'flags of truce boats', 'to be kept in readiness for any necessary movement', 'capacity of 19,000'],
 'Z7 9840/0 13 Sep 1864': ['In accordance with your previous instructions', 'to take charge of the expedition against Price', 'would move by St. Louis and Rolla', 'what orders have already been given'],
 'Z8 9774/3 6 Jul 1864': ['has reached Charlestown with his command', 'most of Hunter\'s forces have reached Parkersburg', 'large amount of public stores at Martinsburg', 'without making any defense'],
 'Z9 9687/0 15 Mar 1864': ['A despatch just received from Banks', 'expects to effect a junction with Sherman', 'make a mere demonstration', 'positive orders be sent to Steele'],
 'Z10 9848/1 22 Sep 1864': ['district of West Florida', 'Key West and Tortugas', 'engineer officer to defend those works against a naval attack', 'recommended by Sherman and Thomas'],
 'Z11 9876/1 27 Oct 1864': ['Delaware Volunteers', 'leave of absence to go home for the election', 'return the day after election', 'near Petersburg'],
 'Z12 9691/0 25 Mar 1864': ['escaped from Woodstock', 'learned from reliable authority that Lee', 'in readiness by the first of April', 'The lines working so badly to Cumberland'],
}
DW = [('Z1 13 Jul Emory/Rockville/Wright debarked', r'July\s+1[234]\W{1,4}\s*1864', ['Emory|Wright|Rockville|Reno'], ['debark|landed|Fort Reno|Rockville']),
 ('Z2 12 Sep inspectors/Little Rock', r'Sept(ember|\.)?\s+1[123]\W{1,4}\s*1864', ['Inspect'], ['Little Rock|Bingham|Rutherford']),
 ('Z3 2 Aug Torbert/Grover/Sixth Corps landed', r'Aug(ust|\.)?\s+[123]\W{1,4}\s*1864', ['Torbert|Grover|Emory|Averell'], ['landed|Rockville|Torbert']),
 ('Z4 5 Nov Price/Steele/Selma/Canby', r'Nov(ember|\.)?\s+[456]\W{1,4}\s*1864', ['Price|Steele|Canby|Sherman'], ['Selma|Mobile and Ohio|Beauregard|Price']),
 ('Z5 21 Oct vessels Alexandria demurrage Rucker', r'Oct(ober|\.)?\s+2[012]\W{1,4}\s*1864', ['Rucker|demurrage|Alexandria'], ['vessels|demurrage|Rucker']),
 ('Z6 6 Aug steamers Baltimore/Philadelphia/NY Rucker', r'Aug(ust|\.)?\s+[567]\W{1,4}\s*1864', ['Rucker|steamers|transports'], ['19,000|Rucker|capacity|flag.of.truce']),
 ('Z7 13 Sep Smith/Rosecrans/Price/Rolla', r'Sept(ember|\.)?\s+1[234]\W{1,4}\s*1864', ['Rosecrans|Price|Rolla|Mower|Smith'], ['Rolla|Price|Rosecrans']),
 ('Z8 6 Jul Sigel/Hunter/Martinsburg stores', r'July\s+[567]\W{1,4}\s*1864', ['Sigel|Hunter|Martinsburg'], ['Martinsburg|Parkersburg|stores']),
 ('Z9 15 Mar Banks/Sherman/Steele/Red River', r'Mar(ch|\.)?\s+1[456]\W{1,4}\s*1864', ['Banks|Steele|Sherman'], ['Red River|Steele|junction|demonstration']),
 ('Z10 22 Sep Key West Tortugas West Florida', r'Sept(ember|\.)?\s+2[123]\W{1,4}\s*1864', ['Key West|Tortugas|West Florida'], ['Key West|Tortugas|Newton']),
 ('Z11 27 Oct Delaware election furlough', r'Oct(ober|\.)?\s+2[678]\W{1,4}\s*1864', ['Delaware'], ['election|furlough|leave of absence']),
 ('Z12 25 Mar Woodstock Triplett Lee Cumberland', r'Mar(ch|\.)?\s+2[456]\W{1,4}\s*1864', ['Woodstock|Triplett|Cumberland'], ['Woodstock|Triplett|Lee'])]
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
