#!/usr/bin/env python3
"""FV-FM7c (9 Oct 2026): phrase grep for E267 (5790), E268 (5742), E269 (5775) in the cached print-check
texts (sources/ia-fulltext/print-check) plus scratch *.txt given as arguments (letters-only match; context window with --ctx).
A miss is a search result, not a statement about print (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())
PH = {'E267': ['on the Keyport', 'steamer Keyport', 'Keyport for City Point', 'meet him at the wharf', 'at the wharf on arrival',
               'see him in person', 'tell him that I directed you', 'Dealy', 'Secretary of War left here', 'Secretary left here'],
      'E268': ['put afloat all the', 'scantling', 'inch plank', '100,000 feet', 'hurry me an operator', 'until you get further orders',
               'dont start vessel', 'Shaffer, chief of staff'],
      'E269': ['York River light vessel', 'York River light-vessel', 'light vessel', 'light-vessel', 'McGarvey', 'Garvey',
               'light-house inspector', 'lighthouse inspector', 'remove York River', 'J. W. Sampson']}
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
