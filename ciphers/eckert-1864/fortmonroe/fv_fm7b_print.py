#!/usr/bin/env python3
"""FV-FM7b (9 Oct 2026): letters-only phrase grep for E260 E261 E262 E263 E266 over the cached print-check volumes
(sources/ia-fulltext/print-check/*.txt.gz) plus OR volumes fetched to a scratch dir (plain _djvu.txt). Prints hits with context.
Usage: fv_fm7b_print.py SCRATCH_DIR. A miss is a search result, not a statement about print (rule 10)."""
import glob, gzip, os, re, sys
P = {
 'E260': ['city of hudson', 'destitute of water transportation', 'no such orders were received', 'shall i comply', 'answered him to this effect', 'almost destitute of water'],
 'E261': ['requisition for one hundred', 'requisition for 100', '140 mules', 'pontoon train', 'two hundred additional wagons', '200 additional wagons', 'wagons and teams complete', 'saddle horses for quartermaster'],
 'E262': ['cable for the james', 'cable for the appomattox', 'arriving here in considerable numbers', 'work for us this side of the james', 'men and material ready', 'none on hand at present'],
 'E263': ['empty steamers to washington', 'all empty steamers', 'bring down troops', 'as fast as they arrive and become light', 'estimates are prepared of material', 'process of erection', 'tell colonel bradley'],
 'E266': ['additional shelter tents', 'instead of 20000', 'instead of twenty thousand', '500 artillery horses', 'artillery horses are also needed', 'as required by lieutenant webster', 'water transportation i asked for'],
}
def norm(s): return re.sub(r'[^a-z0-9]+', ' ', s.lower())
files = glob.glob(os.path.join(os.path.dirname(__file__), '../../../sources/ia-fulltext/print-check/*.txt.gz')) + glob.glob(os.path.join(sys.argv[1], '*.txt'))
print('volumes', len(files))
for f in files:
    raw = (gzip.open(f, 'rt', errors='ignore') if f.endswith('.gz') else open(f, errors='ignore')).read()
    t = norm(raw)
    for e, ps in P.items():
        for p in ps:
            q = norm(p).strip()
            for m in re.finditer(r'\b' + re.escape(q) + r'\b', t):
                print(f'{e}\t{p!r}\t{os.path.basename(f)}\t...{t[max(0, m.start()-300):m.end()+300]}...')
