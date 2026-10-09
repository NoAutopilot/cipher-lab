#!/usr/bin/env python3
"""FV-FM10a (9 Oct 2026): letters-only phrase grep of E314 E315 E318 decoded phrases and rare names over the cached print-check djvu
texts (sources/ia-fulltext/print-check) plus scratch *.txt given as argv, with KWIC for named words in OR/ORN volumes.
A miss is a search result (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E314 5666/1': ['porous cups', 'relay was torn to pieces', 'spools burnt', 'taking off battery', 'connected wires', 'when will operators be here',
                 'without any apparent result', 'considerable firing yesterday', 'office at Gillmore'],
 'E315 5750/1': ['Deserters from rebel ironclads confirm previous information', 'fired a shot or two in this direction', 'sprinkle of rain'],
 'E318 5709/1': ['Gloucester route', 'route is the best', 'one hundred men can guard', '100 men can guard', 'where a regiment could not',
                 'Mackintosh arrives', 'building party', 'Logue', 'Embree', 'Collings to Yorktown', 'Homan to Gloucester', 'Cowans',
                 'come in circuit', 'north side of York River is', 'guarded by a small force', 'Bickford has some operators'],
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
        hits = [f'{v}[{t.count(norm(ph))}]' for v, t in N.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
for name in ['Gloucester route', 'Mackintosh', 'porous', "O'Brien", 'Embree', 'Logue']:
    for v, t in texts.items():
        if not (v.startswith('warofrebellion3') or v.startswith('warofrebellion4') or v.startswith('privateofficialc0') or v.startswith('officialrecordso001')): continue
        for m in list(re.finditer(re.escape(name), t))[:4]:
            print('KWIC', name, v, '::', ' '.join(t[max(0, m.start()-200):m.start()+250].split()))
