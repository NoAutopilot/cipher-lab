#!/usr/bin/env python3
"""FV-L16d (10 Oct 2026): letters-only phrase grep of E441 E472 E442 E473 E469 E466 (Mar-May 1864, Butler / Bermuda Hundred) decoded phrases over the
cached print-check djvu texts (sources/ia-fulltext/print-check: OR I/33, I/36 pts 1-3, Butler Corr. IV-V, Plum vol. 2, J. E. O'Brien 1910 ...), then KWIC
for rare names in OR I/33, I/36 pts 2-3, Butler IV, O'Brien, Plum 2. A miss is a search result, not a novelty verdict (rule 10). Usage: fv_l16d_print.py [SCRATCH/*.txt]"""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E441 5699/1': ['Operators should have reached', 'boat probably delayed', 'the suggestions are good', 'will adopt the route', 'number 14 wire',
                 'No. 14 wire', 'stretched across at that point', 'necessity for use of cables', 'chance for poles', 'answer quick',
                 'how wide is the river at Yorktown', 'how wide is the York River'],
 'E472 5679/0': ['has Sheridan left the James', 'Has General Sheridan left', 'forage him by the other line', 'by the other line',
                 'must we forage him'],
 'E442 5707/0': ['must have office at his headquarters', 'one at Bermuda landing', 'one at Bermuda Landing', 'connected by cable', 'Homan and Collings',
                 'Homan & Collings', 'via Jamestown Island', 'one mile of cable', 'little fine wire', 'construction party'],
 'E473 5633/1': ['New Regime', 'why publish', "Edgar's name", 'Stop your exchanges', 'this was against orders', 'against orders'],
 'E469 5720/0': ['heavy and continuous firing', 'continuous firing about', 'it may be Grant', 'Grant has reached there', "Bottom's Bridge"],
 'E466 5638/0': ['I know of none', 'do not believe a word against him', 'believe a word against', 'appears settled', 'about Dunn'],
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
kw = ['warofrebellion33unit', 'warofrebellion362unit', 'warofrebellion363unit', 'privateofficialc04butl', 'telegraphinginba00obri', 'militarytelegraph02plumrich']
FILT = r'Monroe|Sheldon|Eckert|O.Brien|Butler|Bermuda|City Point|telegraph|Biggs|Norfolk|cable'
for name in ['New Regime', 'Regime', 'Homan', 'Collings', 'Jamestown Island', 'Dunn', 'Edgar', 'Biggs', 'Haxall', 'cable', 'Yorktown', 'continuous firing']:
    for v in kw:
        t = texts.get(v, '')
        for m in list(re.finditer(re.escape(name), t))[:25]:
            ctx = ' '.join(t[max(0, m.start()-220):m.start()+260].split())
            if name in ('cable', 'Yorktown', 'Biggs', 'Dunn', 'Edgar') and not re.search(r'May|April|Apr\.|1864', ctx): continue
            if not re.search(FILT, ctx): continue
            print('KWIC', name, v, m.start(), '::', ctx)
