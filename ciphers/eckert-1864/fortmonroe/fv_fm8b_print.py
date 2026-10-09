#!/usr/bin/env python3
"""FV-FM8b (9 Oct 2026): letters-only phrase grep for E280 E281 E283 E284 E285 over the cached print-check volumes
(sources/ia-fulltext/print-check/*.txt.gz) plus volumes fetched to a scratch dir (plain _djvu.txt: ORN I/3, I/11; OR I/36 pt 3, I/42 pts 2-3;
Plum, Military Telegraph II). Prints hits with context. Usage: fv_fm8b_print.py SCRATCH_DIR. A miss is a search result, not a statement about
print (rule 10)."""
import glob, gzip, os, re, sys
P = {
 'E280': ['fever prevailing', 'alarming extent', 'newport barracks', 'vanderhoef', 'change of air', 'close the offices', 'not very fatal', 'encamped outside the town', 'waterhouse'],
 'E281': ['cut poles', 'gloster', 'gloucester to west point', 'bickford', 'machinery for paying', 'lay cables', 'connect through', 'detail of at least'],
 'E283': ['white shoal', 'point of shoals', 'tow them off', 'hold the persons', 'chain ready', 'ready to slip', 'anchor near shore', 'until further orders and keep', 'night and day until further', 'parker onondaga', 'commander parker'],
 'E284': ['lizzie baker', 'mulford s boats', 'boats just as they are', 'transferred here within', 'whether i shall take the boats', 'only boat that has'],
 'E285': ['tallapoosa', 'montauk point', 'latitude of new york', 'miles off shore', 'get there before the tallahassee', 'steering for halifax', 'before the tallahassee'],
}
def norm(s): return re.sub(r'[^a-z0-9]+', ' ', s.lower())
files = glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../sources/ia-fulltext/print-check/*.txt.gz')) + glob.glob(os.path.join(sys.argv[1], '*.txt'))
print('volumes', len(files))
for f in sorted(files):
    raw = (gzip.open(f, 'rt', errors='ignore') if f.endswith('.gz') else open(f, errors='ignore')).read()
    t = norm(raw)
    for e, ps in P.items():
        for p in ps:
            q = norm(p).strip()
            ms = list(re.finditer(r'\b' + re.escape(q) + r'\b', t))
            for m in ms[:6]:
                print(f'{e}\t{p!r}\t{os.path.basename(f)}\t({len(ms)})\t...{t[max(0, m.start()-220):m.end()+220]}...')
