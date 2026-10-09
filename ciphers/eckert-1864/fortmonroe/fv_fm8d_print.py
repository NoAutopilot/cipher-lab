#!/usr/bin/env python3
"""FV-FM8d (9 Oct 2026; FV-FM8b script adapted): letters-only phrase grep for E278 E286 E288 E289 over the cached print-check volumes
(sources/ia-fulltext/print-check/*.txt.gz) plus volumes fetched to a scratch dir (plain _djvu.txt: ORN I/11; OR I/36 pt 3, I/42 pt 3). Prints hits with context. Usage: fv_fm8d_print.py SCRATCH_DIR. A miss is a search result, not a statement about
print (rule 10)."""
import glob, gzip, os, re, sys
P = {
 'E278': ['few remaining', 'remaining will get away', 'presume this evening', 'fleet left during last night', 'left during last night', 'has the fleet left', 'r c webster'],
 'E286': ['fifth new jersey battery', '5th new jersey battery', 'new jersey battery be spared', 'be spared to this department', 'defenses of washington if so', 'i should direct this to', 'pleased to have it ordered here'],
 'E288': ['two millions of rations', 'two millions rations', 'millions of rations', 'head of cattle to the white house', 'm p small', 'shall i send them'],
 'E289': ['dewey', 'court martial', 'court marshal', 'witnesses leave', 'such a time as this', 'squadron leaving', 'captain taylor'],
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
