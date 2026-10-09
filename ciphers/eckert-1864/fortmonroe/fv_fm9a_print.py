#!/usr/bin/env python3
"""FV-FM9a (9 Oct 2026): letters-only phrase grep of E291 E292 E299 decoded phrases and rare names over the cached print-check djvu
texts plus scratch *.txt given as argv (OR I/36 pt 3 `warofrebellion363unit`, OR I/42 pt 2 `warofrebellion422unit`), with KWIC for
names. A miss is a search result (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E291 5722/0': ['not to build any farther', 'farther than White House', 'getting word from Caldwell', 'getting word from Coldwell', 'Bickford has a card',
                 'cipher which you can use', 'communicate with him', 'do you understand', 'I understand, and will communicate with Bickford', 'Crimea'],
 'E292 5783/1': ['raid on the cattle herd', 'cattle herd near Coggins', 'captured the entire herd', 'lines are down and you will have to order',
                 'order by telegraph from Monroe', 'twelve hundred head', '1,200 head', 'I will send 1200', 'Thomas Wilson', 'M. P. Small', 'Small, lieutenant-colonel'],
 'E299 5609/1': ['Maddox', 'confidential agent of the War Department', 'boxes of tobacco', 'have him in custody', 'what shall I do with him', 'worth some $40,000'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = gzip.open(p, 'rt', errors='ignore').read()
for p in sys.argv[1:]:
    texts[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
N = {k: norm(v) for k, v in texts.items()}
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [f'{v}[{t.count(norm(ph))}]' for v, t in N.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
for name in ['Maddox', 'Bickford', 'Coggins', 'Small']:
    for v, t in texts.items():
        if v not in ('warofrebellion363unit', 'warofrebellion422unit', 'warofrebellion33unit'): continue
        for m in list(re.finditer(name, t))[:6]:
            print('KWIC', name, v, '::', ' '.join(t[max(0, m.start()-200):m.start()+250].split()))
