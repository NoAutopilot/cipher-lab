#!/usr/bin/env python3
"""MS18-R1: proximity search -- all of the given words within WIN characters, in the cached print-check set plus scratch files. Prints volume + snippet."""
import gzip, glob, os, re, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
win = int(sys.argv[1]); words = sys.argv[2].lower().split(','); extra = sys.argv[3:]
vols = {}
for p in glob.glob(os.path.join(D, 'warofrebellion*_djvu.txt.gz')) + glob.glob(os.path.join(D, 'official*_djvu.txt.gz')) + glob.glob(os.path.join(D,'privateofficial*_djvu.txt.gz')):
    vols[os.path.basename(p)[:-12]] = gzip.open(p, 'rt', errors='ignore').read()
for p in extra: vols[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
for v, t in vols.items():
    low = re.sub(r'\s+', ' ', t.lower()); w0 = words[0]; i = 0; n = 0
    while True:
        i = low.find(w0, i)
        if i < 0 or n >= 4: break
        seg = low[max(0, i-win):i+win]
        if all(w in seg for w in words):
            print(v, '|', low[max(0, i-250):i+450]); print(); n += 1
        i += len(w0)
