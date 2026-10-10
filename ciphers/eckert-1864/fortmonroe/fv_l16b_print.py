#!/usr/bin/env python3
"""FV-L16b (10 Oct 2026; copied from fv_l15c_print.py): letters-only phrase grep of E518 E526 E527 E546 E553 E554 decoded phrases over the cached
print-check djvu texts (sources/ia-fulltext/print-check, incl. OR I/46 pt 2, I/47 pt 2 = warofrebellion431unit, ORN I/11, Gordon War Diary,
O'Brien Telegraphing in Battle, Plum vol. 2, Bates) plus scratch *.txt given as argv; then KWIC for rare names. A miss is a search result, not a
novelty verdict (rule 10). Usage: fv_l16b_print.py [SCRATCH/*.txt]"""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E518 5864/1': ['Elias Smith', 'correspondent of the New York Tribune', 'desires permission to go', 'next boat joining the expedition',
                 'will permit him to pass'],
 'E526 5867/2': ['no other vessels of forage', 'no troops arrived nor sailed', 'have not seen General Abbott', 'nor sailed', 'add to Ingalls'],
 'E527 5869/1': ['Butler is relieved', 'I think I will resign', 'what are you going to do', 'George J. Carney', 'Frank J. White',
                 'superintendent of negro affairs', 'forwarded to the War Department for approval'],
 'E546 5890/2': ['ordered to Portsmouth', 'I do not wish to go', 'have me detached here', 'executive officer', 'Lieutenant Commander Parker',
                 'can take the ship', 'Lanman', 'Senator Foster'],
 'E553 5902/1': ['respectfully suggest that the', 'purposes of the commission', 'Eastern District temporarily', 'all my time and attention',
                 'devoted to the investigation', 'hands of General Vogdes'],
 'E554 5902/2': ['take the command for the present', 'investigation can progress', 'progress quietly', 'at the same time General Vogdes'],
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
KV = ['warofrebellion014602rootrich', 'warofrebellion431unit', 'officialrecordso0011unse', 'telegraphinginba00obri'] + extra
for name in ['Lanman', 'Elias Smith', 'Carney', 'Eastville', 'Vogdes', 'Emerick', 'Frank J. White', 'Parker can', 'Portsmouth, N']:
    for v in KV:
        t = texts.get(v, '')
        for m in list(re.finditer(re.escape(name), t))[:8]:
            ctx = ' '.join(t[max(0, m.start()-220):m.start()+260].split())
            if name in ('Vogdes', 'Portsmouth, N') and not re.search(r'Jan|January|Feb|February|Gordon|Lanman|Minnesota|commission', ctx):
                continue
            print('KWIC', name, v, m.start(), '::', ctx)
