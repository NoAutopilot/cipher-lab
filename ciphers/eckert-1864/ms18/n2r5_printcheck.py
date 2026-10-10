#!/usr/bin/env python3
"""N2R-5 (10 Oct 2026): (a) letters-only phrase grep of the No. 2 readings of ms18/n2r5_entries.txt in OR djvu texts (cached sources/ia-fulltext/print-check
plus any paths given), (b) date-window + term search (heading date within the window and all term groups inside 600 chars). A miss is a search result (rule 10).
Usage: n2r5_printcheck.py FILE...  (.txt/.gz)"""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'Z1 9678/0 20 Feb 1864': ['no law authorizing an Inspector to send for persons', 'order of a Court of Inquiry by the President', 'to send for persons and take evidence'],
 'Z2 9757/1 11 Jun 1864': ['McCook and Hurlbut will be ordered to report to you', 'authorizes you to assign them to any duty you wish', 'has been temporarily abolished', 'open the railroad further west than Monroe'],
 'Z3 9724/0 27 Apr 1864': ['return yourself immediately to New Orleans', 'carry out his previous instructions', 'secure Red River to Shreveport', 'see the gunboats safely out of Red River', 'Hurry this to General Banks'],
 'Z4 9771/0 3 Jul 1864': ['Early and Breckinridge', 'repeated to Hunter', 'has replied to none of my telegrams', 'good defense if the enemy should attack the line', 'Max Weber'],
 'Z5 9804/1 30 Jul 1864': ['informs me that the enemy commenced crossing at McCoy', 'camp fires of the enemy are about four miles south of Greencastle', 'was forced to fall back to Greencastle', 'moving in three columns'],
 'Z6 9727/0 30 Apr 1864': ['Trans-Mississippi affairs are definitely decided', 'modifying my telegram of the 27th', 'Special Orders No. 150', 'do not relieve him from command of the Sixteenth', 'repair to his home in Illinois'],
 'Z7 9765/2 25 Jun 1864': ['all the ocean steamers in service at New York and Philadelphia', 'not actively employed be sent to the James', 'repair at once to New Orleans and report to the quartermaster', 'steamers are now at Hampton Roads and City Point'],
 'Z8 9780/0 8 Jul 1864': ['Wallace reports tonight that the enemy are moving in strong force near Urbana', 'Urbana is about thirty miles from Washington', 'has not yet left Parkersburg', 'pressure of business in the department requires your assistance'],
 'Z9 9876/0 24 Oct 1864': ['do come within the principle involved', 'give the act of Congress the most liberal construction', 'meritorious service', 'finally determined by the Senate on the confirmation'],
 'Z10 9764/2 24 Jun 1864': ['was sent back by Hunter to collect', 'Stahel is nearly ready to start but has no information', 'too perilous to be undertaken', 'proceed the best he can up the Shenandoah Valley'],
}
DW = [('Z1 20 Feb Inspector/Court of Inquiry', r'Feb(ruary|\.)?\s+(19|20|21)\W{1,4}\s*1864', ['Inspector|Inquiry'], ['send for persons|Court of Inquiry']),
 ('Z2 11 Jun McCook/Hurlbut/Canby', r'June\s+(10|11|12)\W{1,4}\s*1864', ['McCook|Hurlbut|Canby'], ['abolished|Monroe|Hurlbut']),
 ('Z3 27 Apr Banks/Steele/Shreveport', r'Apr(il|\.)?\s+(26|27|28)\W{1,4}\s*1864', ['Banks|Steele'], ['Shreveport|Little Rock|Red River']),
 ('Z4 3 Jul Sigel/Hunter/Early', r'July\s+(2|3|4)\W{1,4}\s*1864', ['Sigel|Hunter|Stahel'], ['Early|Breckinridge|Moorefield|Romney']),
 ('Z5 30 Jul Chambersburg crossing', r'July\s+(29|30|31)\W{1,4}\s*1864', ['Chambersburg|Averell'], ['Greencastle|Mercersburg|McCoy|Falling Waters']),
 ('Z6 30 Apr Trans-Mississippi/Canby/Washburn', r'Apr(il|\.)?\s+(29|30)\W{1,4}\s*1864', ['Canby|Washburn'], ['Special Orders|Sixteenth|relieved|Illinois']),
 ('Z7 25 Jun steamers/James', r'June\s+(24|25|26)\W{1,4}\s*1864', ['steamers|Quartermaster'], ['New Orleans|James|Hampton|City Point']),
 ('Z8 8 Jul Urbana/Wallace/Hunter', r'July\s+(7|8|9)\W{1,4}\s*1864', ['Wallace|Urbana'], ['Parkersburg|Urbana|Early']),
 ('Z9 24 Oct appointments/law/Senate', r'Oct(ober|\.)?\s+(23|24|25)\W{1,4}\s*1864', ['appointments'], ['Senate|Congress|liberal construction']),
 ('Z10 24 Jun Stahel/Hunter/Shenandoah', r'June\s+(23|24|25)\W{1,4}\s*1864', ['Stahel|Hunter'], ['Shenandoah|Stahel|perilous'])]
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
