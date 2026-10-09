#!/usr/bin/env python3
"""FV-FM8c (9 Oct 2026): letters-only phrase grep of E293 E294 E295 E297 E298 decoded phrases and rare names over the cached print-check
djvu texts plus scratch *.txt (ORN I/11, OR I/42 pt 3, I/39 pt 3, I/41 pts 3-4), with KWIC context for names. A miss is a search result (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E293 5822/0': ['Rice Dupont and Sedgwick', 'Rice, Du Pont', 'Western Metropolis', 'headquarters boat', 'embarking the troops with all possible dispatch', 'remaining troops to Fort Monroe', 'river boats and transfer them', 'seagoing steamers now lying there', 'Baltic to report to you'],
 'E294 5616/1': ['no steamers now that I can send to sea', 'send to sea with 400 or 500', 'four or five hundred men', 'bound to Port Royal', 'make a short trip', 'cant send them far'],
 'E295 5624/0': ['much in need of assistant quartermasters', 'efficient and experienced assistant quartermasters', 'experienced assistant quartermasters', 'four efficient', 'assistant quartermasters be ordered to report'],
 'E297 5632/0': ['blockade runner Diamond', 'the Diamond', 'about to be sold in New York', 'in the old business', 'ought to be seized', 'so much in want of vessels', 'fast blockade runner'],
 'E298 5794/1': ['propose Logan', 'Logan for', 'Hooker go to Missouri', 'Hooker to Missouri', 'Hookers present command', 'expect to reach City Point', 'opinion in respect to this proposition', 'have just arrived and will go on'],
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
        hits = []
        for v, t in N.items():
            i = t.find(norm(ph))
            if i >= 0: hits.append(f'{v}[{t.count(norm(ph))}]')
        print(e, '|', ph, '|', ','.join(hits) or 'none')
