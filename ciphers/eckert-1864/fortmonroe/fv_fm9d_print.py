#!/usr/bin/env python3
"""FV-FM9d (9 Oct 2026): letters-only phrase grep of E307 E308 E309 decoded phrases and rare names over the cached print-check djvu
texts plus scratch *.txt given as argv (Plum, Military Telegraph vols 1-2 `militarytelegraph01plumrich`/`02plumrich`; OR I/42 pt 3
`warofrebellion423unit`), with KWIC for names in the argv volumes. A miss is a search result (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E307 5777/2': ['terrible affair at Chambersburg', 'my mother nearly insane', 'without home, clothes or money', 'Newport office closed',
                 'Waterhouse', 'dangerously ill', 'McGaughey can take charge', 'as much of my back pay', 'J. R. Gilmore', 'Gilmore, J. R.'],
 'E308 5659/0': ['Emory Round', 'Providence Conference', 'Chaplain White', 'terrific naval engagement', 'piercing the boiler',
                 'retired to the Roanoke', 'apparently uninjured', 'land attack upon New Berne', 'land attack upon Newbern', 'Daily Christian Advocate',
                 'Carlton and Porter', 'Carlton & Porter'],
 'E309 5786/0': ['no spare boats', 'excepting the Illinois', 'collected by order of', 'all the steamers that can possibly be spared',
                 'give the names of those you send', 'R. C. Webster', 'Webster, chief quartermaster', 'Illinois is nearly discharged'],
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
ARGV = {os.path.basename(p)[:-4] for p in sys.argv[1:]}
for name in ['Gilmore', 'Waterhouse', 'Gaughey', 'Rucker', 'Webster', 'Emory Round', 'Sheldon']:
    for v, t in texts.items():
        if v not in ARGV: continue
        for m in list(re.finditer(name, t))[:8]:
            print('KWIC', name, v, '::', ' '.join(t[max(0, m.start()-200):m.start()+250].split()))
