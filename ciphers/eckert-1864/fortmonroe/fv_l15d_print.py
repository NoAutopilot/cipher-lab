#!/usr/bin/env python3
"""FV-L15d (10 Oct 2026): letters-only phrase grep of E539 E528 E500 E573 E557 E517 decoded phrases over the cached print-check djvu texts
(sources/ia-fulltext/print-check, incl. OR I/46 pt 2, I/47 pt 2 = warofrebellion431unit, Butler V) plus scratch *.txt given as argv (ORN I/11,
ORN I/12 = officialrecords10librgoog, Google scan, title page "VOLUME 12"), then KWIC for rare names in the argv volumes and OR I/46 pt 2.
A miss is a search result, not a novelty verdict (rule 10). Usage: fv_l15d_print.py SCRATCH/*.txt"""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E539 5885/1': ['large torpedoes of 900', 'torpedoes of nine hundred', 'insulating wire', 'by the Phlox the', 'I have immediate use for them',
                 'send immediately by the Phlox'],
 'E528 5870/0': ['No forage vessels since', 'Ariel and General Sedgwick', 'Ariel and Sedgwick', 'what others are to come', 'any reason for delay',
                 'nor any reason for delay'],
 'E500 5847/2': ['anchor and chain in time', 'anchor and chain', 'will not be sent on the expedition', 'need not send to New York for them',
                 'unable to furnish anchor'],
 'E573 5930/1': ['No news of the Montauk', 'in possession of Kinston', 'Lehigh in from Charleston', 'will go up the James River immediately'],
 'E557 5907/1': ['submarine torpedoes', 'letter of the 25th ultimo', 'have not been received', 'immediate use on James River',
                 'in addition to these', 'are also required'],
 'E517 5861/1': ['consider the order countermanded', 'consider the order as countermanded', 'Let her embark troops', 'as before ordered',
                 'If the Baltic has been ordered'],
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
kw = extra + ['warofrebellion014602rootrich', 'warofrebellion431unit']
for name in ['Phlox', 'Lynch', 'St. Lawrence', 'Ariel', 'Sedgwick', 'anchor', 'Baltic', 'countermand', 'Montauk', 'submarine', 'Glisson']:
    for v in kw:
        t = texts.get(v, '')
        for m in list(re.finditer(re.escape(name), t))[:12]:
            ctx = ' '.join(t[max(0, m.start()-220):m.start()+260].split())
            if not re.search(r'Jan|January|Feb|February|March|Monroe|City Point|Sheldon|Newport|Ingalls|Wise|Parker|Glisson', ctx):
                continue
            print('KWIC', name, v, m.start(), '::', ctx)
