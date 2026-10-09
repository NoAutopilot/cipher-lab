#!/usr/bin/env python3
"""FV-FM10b (9 Oct 2026): letters-only phrase grep of E319-E321's decoded phrases over the 164 cached print-check volumes plus
scratch texts given as arguments (OR I/42 pt 2 `warofrebellion422unit`, Plum 1882 `militarytelegraph01plumrich`/`02plumrich`),
then KWIC in the scratch texts for the entries' names and places. A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E319': ['cannot string wire', 'can not string wire', 'navigation must remain open', 'some of which have high masts', 'high masts',
          'fully as favorable for building', 'a little over half a mile', 'three quarters of a mile', 'across York River at Yorktown'],
 'E320': ['regret having ordered', 'ordered OBrien away', 'require careful working', 'better posted with that command',
          'Caldwell will attend', 'Nichols can remain', 'Mackintosh to bring', 'all builders and building material'],
 'E321': ['dragged up by anchors', 'danger of being dragged', 'nearest south shore', 'cable should be laid', 'laid on north side',
          'take less cable', 'north side of river'],
}
KW = [r'high masts', r'Mattapony', r'string (?:the )?wire', r'O.Brien', r'Bermuda Hundred', r'Mackintosh', r'Nichols', r'Doren',
      r'Caldwell', r'anchors', r'York River', r'cable']
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = gzip.open(p, 'rt', errors='ignore').read()
raw = {}
for p in sys.argv[1:]:
    raw[os.path.basename(p)[:-4]] = texts[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
N = {k: norm(v) for k, v in texts.items()}
print('volumes searched:', len(N))
for e, phs in PH.items():
    for ph in phs:
        print(e, '|', ph, '|', ','.join(v for v, t in N.items() if norm(ph) in t) or 'none')
for v, t in raw.items():
    flat = re.sub(r'\s+', ' ', t)
    for k in KW:
        ms = list(re.finditer(k, flat, re.I))
        print(f'KWIC {v} /{k}/ {len(ms)}')
        for m in ms[:12]:
            print('   @', m.start(), '...', flat[max(0, m.start()-110):m.end()+110].replace('\n', ' '))
