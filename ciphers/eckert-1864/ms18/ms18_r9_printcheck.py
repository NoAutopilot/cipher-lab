#!/usr/bin/env python3
"""MS18-R9 (10 Oct 2026): letters-only phrase grep of the four filed MS18-R9 rows' decoded phrases in the cached OR/ORN djvu texts (sources/ia-fulltext/print-check),
plus a date+addressee window search (as ms18_r8_date.py). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'X1 9811/1': ['Grant will leave here for', 'what point he should come for that purpose', 'furnish transportation for', 'Comstock'],
 'X4 9877/3': ['Arrest Maxon', 'State agent if within the limits of your command', 'send him immediately to McHenry', 'report to this Department by telegraph'],
 'X5 9793/0': ['moving out by the Rockville road', 'probably encumbered with a large amount of plunder', 'Wright moved out to Offutt', 'supreme command of the forces operating on this expedition'],
 'X8 9882/0': ['send you all available troops in St. Louis', 'hurry forward these reinforcements', 'concentrate all you can against Hood', 'replacing the garrisons in your rear'],
}
Q = [('X1 5 Aug 1864 Comstock/Monocacy/Hunter', r'Aug(ust|\.)?\s+[456]\W{1,4}\s*1864', ['Comstock|Monocacy|Hunter'], ['Grant|Ord']),
     ('X4 28 Oct 1864 Dana/Maxon/McHenry', r'Oct(ober|\.)?\s+2[89]\W{1,4}\s*1864', ['McHenry|Maxon|Dana'], ['Maxon|agent|arrest']),
     ('X5 14 July 1864 McCaine/Hunter/Wright/Edwards Ferry', r'July\s+1[45]\W{1,4}\s*1864', ['Hunter|Wright|Couch|Stanton'], ['Edwards|Offutt|Rockville']),
     ('X8 1 Nov 1864 Van Duzer/Thomas/Hood', r'Nov(ember|\.)?\s+[12]\W{1,4}\s*1864', ['Thomas|Van Duzer|Rosecrans|Halleck'], ['Hood|Smith|Rawlins|St\\. Louis'])]
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
