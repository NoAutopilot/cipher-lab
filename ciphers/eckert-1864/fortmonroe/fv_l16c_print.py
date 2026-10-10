#!/usr/bin/env python3
"""FV-L16c (10 Oct 2026; copied from fv_l15c_print.py): letters-only phrase grep of E558 E564 E566 E569 E574 E577 decoded phrases over the cached print-check djvu texts
(sources/ia-fulltext/print-check) plus scratch *.txt given as argv (OR I/46 pts 1 and 3, ORN I/11; I/46 pt 2 and I/47 pt 2 are in the cache), then KWIC for rare
names in the argv volumes. A miss is a search result, not a novelty verdict (rule 10). Usage: fv_fm65a_print.py SCRATCH/*.txt"""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E558 5912/1': ['requires an office at Yorktown', 'office at Yorktown', 'can you supply these operators', 'considered imperative',
                 'anxious inquiry', 'Quartermaster Department here'],
 'E564 5918/1': ['entirely out of pilots', 'out of pilots', 'furnish the Navy with two pilots', 'monitors to go up', 'pilots for monitors',
                 'compelled to furnish the Navy'],
 'E566 5919/2': ['ordered to join my regiment', 'joined the expedition', 'Am I right', 'First New York Mounted Rifles', 'get quick answer',
                 'E. V. Sumner'],
 'E569 5924/0': ['regarding moving office', 'moving the office', 'precedent is once established', 'accommodation of any commanding officer',
                 'wants the room', 'purpose of her own'],
 'E574 5931/0': ['left here 1 p.m. for City Point', 'will reach Fort Monroe about 11', 'go on board the boat', 'deliver anything you may receive',
                 'River Queen', 'name of boat'],
 'E577 5933/2': ['matters still pending', 'continue in command of the district', 'not be relieved by', 'order about to issue',
                 'District of Eastern Virginia', 'relieved by General Hartsuff'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = gzip.open(p, 'rt', errors='ignore').read()
extra = []
for p in sys.argv[1:]:
    k = os.path.basename(p)[:-4]; texts[k] = open(p, errors='ignore').read(); extra.append(k)
N = {k: norm(v) for k, v in texts.items()}
print('volumes searched:', len(texts), '(argv:', ' '.join(extra) + ')')
for e, phs in PH.items():
    for ph in phs:
        hits = [f'{v}[{t.count(norm(ph))}]' for v, t in N.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
KV = [k for k in texts if any(x in k for x in ('014602rootrich', '463unit', '461unit', '431unit_djvu', 'officialrecordso0011', 'plumrich', 'telegraphinginba', 'lincolnintelegra'))] + extra
FILT = {'Sumner': r'Mounted Rifles|expedition|Turner|March', 'Hartsuff': r'Gordon|Norfolk|relieve|Eastern Virginia', 'River Queen': r'March|Stanton|Secretary|City Point',
        'Yorktown': r'telegraph|operator|office|Ord', 'pilots': r'monitor|James|Bradley|Navy', 'Bradley': r'pilot|quartermaster|March',
        'Emerick': r'.', 'Dealy': r'.', 'Mounted Rifles': r'Sumner|March|expedition', 'Gordon': r'Hartsuff|relieve|continue in command'}
for name, rx in FILT.items():
    for v in KV:
        t = texts[v]; k = 0
        for m in re.finditer(re.escape(name), t):
            ctx = ' '.join(t[max(0, m.start()-220):m.start()+260].split())
            if not re.search(rx, ctx) or not re.search(r'March|Mar\.|1865', ctx): continue
            print('KWIC', name, v, m.start(), '::', ctx); k += 1
            if k >= 8: break
