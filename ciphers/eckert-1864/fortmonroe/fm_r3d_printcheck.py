#!/usr/bin/env python3
"""FM-R3d (9 Oct 2026): letters-only phrase grep of the FM-R3d entries' hand-read phrases in the cached OR/ORN/Butler djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments); prints volume and a 100-char context of the first hit per phrase.
A miss is a search result, not a verdict (rule 10). Usage: python3 fm_r3a_printcheck.py [extra.txt ...]"""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E240 5784/1': ['yellow fever is raging', 'fever is raging in Newbern', 'Surgeon Hand reports', 'Surgeon D. W. Hand', 'William H. Freeman', 'Freeman of Philadelphia', 'rigid quarantine', 'yellow fever at Newbern', 'Surgeon-General Barnes', 'Newbern violently'],
 'E241 5663/1': ['Hicksford', 'Heckman', 'nearly into Petersburg', 'Fulton and Craig', 'J. C. Rowe', 'back three miles', 'list of wounded', 'Kautz succeeded in destroying', 'Weldon and North Carolina railroad', 'between Richmond and Petersburg'],
 'E242 5682/0': ['signal field cord', 'line to Jamestown impracticable', 'field cord to spare', 'Huyck', 'operator for outer line', 'hurried operations', 'woody country', 'Jamestown impracticable'],
 'E243 5826/1': ['steamer Brady', 'Matilda is loading', 'Matilda', 'S. Cloud', 'William L. James', 'G. W. Bradley', 'loading with cavalry at Portsmouth', 'order her here at once', 'suitable to go to sea with horses'],
 'E244 5796/0': ['main body was about LaFayette', 'Ship\'s Gap', 'Carpenter\'s Ferry', 'Tunnel Hill', 'effectually protect this place', 'Bridgeport and the intermediate', 'approaching Carpenter\'s Ferry', 'repairing the railroad below Tunnel Hill', 'attempt of Hood to cross'],
 'E245 5769/0': ['Depredations of the Florida', 'Monticello and Mount Vernon', 'Monticello and Mount', 'Shenandoah from Commodore Livingston', 'Commodore Livingston', 'State of Georgia', 'tug America', 'Malvern, Hampton Roads', 'block aids off Wilmington', 'this side Nantucket', 'Jno Toby'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = gzip.open(p, 'rt', errors='ignore').read()
for p in sys.argv[1:]:
    texts[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
N = {v: norm(t) for v, t in texts.items()}
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in N.items() if norm(ph) in t]
        ctx = ''
        if hits and len(norm(ph)) > 14 and len(hits) <= 3:
            v = hits[0]; i = N[v].find(norm(ph)); ctx = ' ~ ' + N[v][max(0, i-30):i+60]
        print(e, '|', ph, '|', (','.join(hits[:6]) + (' +%d' % (len(hits)-6) if len(hits) > 6 else '')) or 'none', ctx)
