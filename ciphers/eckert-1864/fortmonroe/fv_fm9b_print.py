#!/usr/bin/env python3
"""FV-FM9b (9 Oct 2026): letters-only phrase grep of E300-E303 phrases over the cached print-check djvu texts plus scratch
*.txt given as argv (OR I/39 pt 3 `warofrebellion393unit`, OR I/36 pt 3 `warofrebellion363unit`, fetched to scratch).
Prints volume, hit count and the nearest running-head page numbers. A miss is a search result (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E300 5639/1': ['I am just informed by General Butler that he has information that Plymouth is evacuated', 'please let me know what I am to do'],
 'E301 5764/0': ['No change in the naval situation. Report from the army', 'taking on board sand in bags'],
 'E302 5697/1': ['If White House is made the base of supplies', 'chestnut poles', 'have not rotted down', 'very little wire on hand',
                 'Confer with Sheldon as to plans and route', 'across the York at Gloucester Point, thence up to West Point', 'old road from Williamsburg'],
 'E303 5797/1': ['We took Ship', 'obstructed Snake Creek Pass to delay our trains', 'first positive fact that Hood',
                 'The necessary orders have been given for the repair of the railroad', 'Deserters from Hood', 'Same to Lieut. Gen. U. S. Grant'],
}
texts = {os.path.basename(p)[:-12]: gzip.open(p, 'rt', errors='ignore').read() for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz')))}
for p in sys.argv[1:]:
    texts[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
print('volumes searched:', len(texts))
for v, t in texts.items():
    idx = [i for i, c in enumerate(t) if c.isalpha()]; n = ''.join(t[i].lower() for i in idx)
    for e, phs in PH.items():
        for ph in phs:
            for m in re.finditer(norm(ph), n):
                o = idx[m.start()]; w = ' '.join(t[max(0, o - 6000):o].split())
                heads = re.findall(r'(?<![\d,.])(\d{2,3})(?= (?:[A-Z]{2,}[A-Z.,;: ]+|NORTH ATLANTIC|OPERATIONS|KY\.|CORRESPONDENCE)|\s*\]?\s*$)', w)[-1:]
                print(e, '|', ph, '|', v, '| page near', heads, '|', ' '.join(t[o:o + 160].split()))
