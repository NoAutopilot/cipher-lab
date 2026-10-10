#!/usr/bin/env python3
"""L14-A (10 Oct 2026): letters-only phrase grep of the four filed L14-A rows' decoded phrases in the cached OR/ORN djvu texts (sources/ia-fulltext/print-check),
plus a date+addressee window search (as ms18_r8_date.py). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'Y1 9835/1': ['very important to watch', 'who he associates with', 'means mischief on the Pacific coast'],
 'Y2 9877/1': ['of sufficient time to enable them to go home and vote', 'without prejudice to the public service', 'furlough'],
 'Y3 9793/0': ['moving out by the Rockville road', 'encumbered with a large amount of plunder', 'Wright moved out to Offutt'],
 'Y4 9826/0': ['capable of bearing arms', 'exempt from', 'Mosby can'],
 'Y5 9806/2': ['any rebel force at', 'We trust mainly to you and General Couch', 'Whatever is received here is sent to you'],
 'Y6 9777/1': ['will begin to arrive at Baltimore', 'ready to forward them', 'without ambulances and wagons'],
 'Y7 9823/3': ['Muddy Branch wharf', 'start immediately on their scout', 'provisional battalion of cavalry'],
 'Y8 9865/1': ['old regiments from General Pope', 'be prepared to meet Hood', 'present himself on the Tennessee'],
}
Q = [('Y1 6 Sep 1864 Washington/Armond', r'Sept(ember|\.)?\s+[67]\W{1,4}\s*1864', ['Pacific'], ['mischief|watch']),
     ('Y2 27 Oct 1864 furlough vote Wallace/Hurlbut', r'Oct(ober|\.)?\s+2[78]\W{1,4}\s*1864', ['furlough'], ['vote|Wallace|Hurlbut']),
     ('Y3 14 July 1864 Halleck/Hunter Edwards Ferry', r'July\s+1[45]\W{1,4}\s*1864', ['Hunter'], ['Edwards|Offutt|Rockville']),
     ('Y4 25 Aug 1864 Sheridan/Mosby', r'Aug(ust|\.)?\s+2[56]\W{1,4}\s*1864', ['Mosby'], ['Sheridan|Wait']),
     ('Y5 31 July 1864 Couch/Hancock/Nolan', r'July\s+(31|Aug\.? 1)\W{1,4}\s*1864', ['Couch'], ['Hancock|Nolan']),
     ('Y6 7 July 1864 (header June 7) Ricketts/Baltimore', r'July\s+[678]\W{1,4}\s*1864', ['Ricketts'], ['Baltimore|Vinton|Thomas']),
     ('Y7 19 Aug 1864 Muddy Branch', r'Aug(ust|\.)?\s+(19|20)\W{1,4}\s*1864', ['Muddy Branch'], ['scout|cavalry']),
     ('Y8 13 Oct 1864 Van Duzer/Thomas/Hood', r'Oct(ober|\.)?\s+1[34]\W{1,4}\s*1864', ['Thomas'], ['Hood|Pope|Schofield'])]
raw, texts = {}, {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    k = os.path.basename(p)[:-12]; raw[k] = gzip.open(p, 'rt', errors='ignore').read(); texts[k] = norm(raw[k])
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        print(e, '|', ph, '|', ','.join(v for v, t in texts.items() if norm(ph) in t) or 'none')
for k, t in raw.items():
    t2 = re.sub(r'\s+', ' ', t)
    for lab, dre, a, b in Q:
        n = h = 0; ex = []
        for m in re.finditer(dre, t2, flags=re.I):
            n += 1; w = t2[m.start()-150: m.end()+450]
            if all(re.search(x, w, re.I) for x in a) and all(re.search(x, w, re.I) for x in b): h += 1; ex.append(w[:260])
        if n: print(f'{k} | {lab} | date headings {n} | with terms {h}')
        for e in ex[:2]: print('    ', e)
