#!/usr/bin/env python3
"""FM-R5a (9 Oct 2026): letters-only phrase grep of the FM-R5a entries' hand-read phrases in the cached OR/ORN/Butler djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments); prints volume and a 100-char context of the first hit per phrase.
A miss is a search result, not a verdict (rule 10). Usage: python3 fm_r4a_printcheck.py [extra.txt ...]"""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5801/0': ['Colonel Smith will attend to', 'I leave for Washington tonight', 'repeat this to Colonel Smith', 'Terry commanding near Varina', 'Lieutenant-Colonel Smith will attend'],
 'F2 5641/1': ['would it meet your views to have', 'one gunboat due besides', 'General Gillmore not yet arrived', 'more now due'],
 'F3 5768/2': ['none of the Nineteenth Corps arrived yet', 'none of the 19th Corps has arrived', 'General-in-Chief has telegraphed to have them sent to Washington', 'Nineteenth Corps arrived yet'],
 'F4 5724/2': ['pontoon train which I dont believe', 'the pay master is not obstructed', 'at the mouth of', 'your dispatch received the pay'],
 'F5 5645/2': ['letter just received from General Gillmore', 'would start yesterday', 'he comes with the last detachment', 'bring him here to night or tomorrow morning'],
 'F6 5824/0': ['no boots of any kind to spare', 'waiting two days for boots', 'have not yet succeeded in getting them', 'Captain Allen'],
 'F7 5582/1': ['my men will all have embarked by tomorrow', 'will report in person on Tuesday', 'Lieutenant Caldwell'],
 'F8 5802/1': ['strength of each battery and the style of gun', 'Colonel Howard chief of artillery', 'let me know the strength of each battery'],
 'F9 5829/2': ['the few remaining will get away', 'fleet left during last night', 'I do not know when the few remaining'],
 'F10 5609/0': ['no shelter tents', 'asking that I be prepared to supply him', 'the last requisition was for him', 'General Gillmore has written saying'],
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
