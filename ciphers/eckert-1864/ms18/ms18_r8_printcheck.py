#!/usr/bin/env python3
"""MS18-R8 (9 Oct 2026): letters-only phrase grep of the ten MS18-R8 rows' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments, e.g. OR I/36 pt 3, 41 pt 4, 47 pt 3, 49 pt 2). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'X1 10003/2': ['Joseph E. Brown', 'close custody under sufficient and secure guard', 'hold no communication, verbal or written', 'acknowledge by telegraph the hour'],
 'X2 10048/1': ['Sharkey', 'formation of militia companies', 'countermanding this proclamation', 'detect criminals, prevent crime'],
 'X3 9885/1': ['Inspectors and other officers of election', 'register of the names and residence', 'soldiers\' proxies', 'fraudulent votes'],
 'X4 9887/0': ['immediate command under you', 'apprehension that his troops were to be taken from him', 'limiting or controlling your authority', 'peculiar form of the order'],
 'X5 9841/0': ['Ames guns', 'under promise to pay', 'extraordinary price without the testing', 'provided they bear the test'],
 'X6 10055/0': ['Alberger', 'competent and reliable officer in charge', 'permission to visit Washington', 'Jno. Odell'],
 'X7 9694/1': ['consolidated into the first', 'will command the Fourth Corps', 'Relieve General Granger', 'assign General Slocum'],
 'X8 9903/1': ['sacks suitable for holding', 'each sack to hold', 'Procure immediately', 'flour sacks will probably answer'],
 'X9 9880/2': ['directing General McNeil to Rolla', 'pursuit must be continued', 'ordered the troops back', 'These orders must be obeyed'],
 'X10 9772/0': ['safety of General Sigel\'s trains', 'movement of the enemy in the valley', 'keep me posted as well as you can', 'under orders three days ago to move his forces'],
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
