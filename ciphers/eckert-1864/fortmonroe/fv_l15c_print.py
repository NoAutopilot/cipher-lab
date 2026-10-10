#!/usr/bin/env python3
"""FV-L15c (10 Oct 2026; copied from fv_fm65a_print.py): letters-only phrase grep of E513 E515 E529 E549 E551 E552 decoded phrases over the cached print-check djvu texts
(sources/ia-fulltext/print-check) plus scratch *.txt given as argv (OR I/46 pts 1 and 3, ORN I/11; I/46 pt 2 and I/47 pt 2 are in the cache), then KWIC for rare
names in the argv volumes. A miss is a search result, not a novelty verdict (rule 10). Usage: fv_fm65a_print.py SCRATCH/*.txt"""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E513 5857/1': ['orders payment to company', 'second expedition', 'not mustered for December', 'opposed to law and general orders',
                 'except on muster rolls', 'Amos Binney'],
 'E515 5858/1': ['Ariel Victor Illinois', 'Ariel, Victor, Illinois', 'were sent to report to you', 'by order of the Quartermaster',
                 'William L. James', 'Sedgwick and Baltic'],
 'E529 5871/0': ['Ericsson writes', 'approbation for', 'Puritan', 'shaft being put in', 'Shall I get ours out', 'blockade runner Julia',
                 'leave Beaufort Wednesday', 'buoys to be lighted', 'weather here favorable'],
 'E549 5896/2': ['called on Colonel Stager', 'cipher operator', 'construction corps and some operators', 'refers the matter to you',
                 'party selected', 'Mack and party', 'together with the material'],
 'E551 5898/1': ['exclusive of the Rhode Island', 'two vessels exclusive', 'patrol from Cape Henry', 'Cape Henry to Cape Fear',
                 'whilst troops are moving', 'at the yard or in the Roads'],
 'E552 5899/0': ['Dumbarton', 'promised to Commodore Bell', 'up the James River', 'Cambridge will be available', 'but one vessel',
                 'available on Tuesday next'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = gzip.open(p, 'rt', errors='ignore').read()
extra = []
for p in sys.argv[1:]:
    k = os.path.basename(p)[:-4]; texts[k] = open(p, errors='ignore').read(); extra.append(k)
N = {k: norm(v) for k, v in texts.items()}
print('volumes searched:', len(texts), '(argv:', ' '.join(extra) + ')')
for e, phs in PH.items():
    for ph in phs:
        hits = [f'{v}[{t.count(norm(ph))}]' for v, t in N.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
for name in ['Dumbarton', 'Berrien', 'Binney', 'Ericsson', 'Puritan', 'Rhode Island', 'Cambridge', 'Stager', 'Mack', 'construction corps',
             'Sedgwick', 'Victor', 'Commodore Bell']:
    for v in extra:
        t = texts[v]
        for m in list(re.finditer(re.escape(name), t))[:6]:
            ctx = ' '.join(t[max(0, m.start()-220):m.start()+260].split())
            if name in ('Sedgwick', 'Victor', 'Cambridge', 'Mack', 'Rhode Island', 'Stager') and not re.search(r'Jan|January|Feb|February|Monroe|Norfolk|Sheldon|Eckert|Newport', ctx):
                continue
            print('KWIC', name, v, m.start(), '::', ctx)
