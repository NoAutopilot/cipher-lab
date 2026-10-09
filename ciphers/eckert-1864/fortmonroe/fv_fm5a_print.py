#!/usr/bin/env python3
"""FV-FM5a (9 Oct 2026): phrase grep for E210 (5637), E212 (5767), E213 (5607), E214 (5703), E216 (5743) in the cached print-check
texts (sources/ia-fulltext/print-check) plus scratch *.txt given as arguments (letters-only match; context window with --ctx).
A miss is a search result, not a statement about print (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())
PH = {'E210': ['maps of the Peninsula', 'best maps', 'Sergeant Royer', 'with my desk', 'from the Engineer Department and send', 'Norton, chief signal',
               'Taft, signal officer', '158 F street', 'south side of James'],
      'E212': ['all available transportation be sent to City Point', 'suited for this service', 'such steamers as you have', 'move troops thence',
               'available transportation be sent', 'Colonel Biggs, chief quartermaster', 'Biggs, chief quartermaster'],
      'E213': ['become surplus by the new arrangements', 'material and the superintendent', 'surplus by the new', 'by General Turner\'s directions',
               'receive your instructions concerning material'],
      'E214': ['Bickford has', 'miles insulators', 'enough material to make out', 'advise me often about the work', 'operators sufficient',
               'Bickford', 'send to West Point with him'],
      'E216': ['16,000 strong is to embark', 'is to embark at White House', 'to a new base or hospital', 'every vessel fitted to aid',
               'removing stores and wounded', 'new base or hospital', 'expedition of 16,000']}
ctx = '--ctx' in sys.argv
args = [a for a in sys.argv[1:] if a != '--ctx']
raw = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    raw[os.path.basename(p)[:-12]] = gzip.open(p, 'rt', errors='ignore').read()
for p in args:
    raw[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
texts = {k: norm(v) for k, v in raw.items()}
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in texts.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits[:12]) or 'none', f'({len(hits)})')
        if ctx:
            for v in hits[:4]:
                for m in list(re.finditer(re.escape(ph.split()[0]) + r'\W+' + re.escape(ph.split()[1]) if len(ph.split()) > 1 else re.escape(ph), raw[v], re.I))[:3]:
                    print('   ', v, '::', re.sub(r'\s+', ' ', raw[v][max(0, m.start()-300):m.end()+400]))
