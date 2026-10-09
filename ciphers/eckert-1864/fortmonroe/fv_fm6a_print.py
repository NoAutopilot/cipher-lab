#!/usr/bin/env python3
"""FV-FM6a (9 Oct 2026): phrase grep for E217 (5770), E219 (5780), E226 (5748), E227 (5808) in the cached print-check
texts (sources/ia-fulltext/print-check) plus scratch *.txt given as arguments (letters-only match; context window with --ctx).
A miss is a search result, not a statement about print (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())
PH = {'E217': ['transports here now for 7,000', 'transports here now', 'Wright has 11,000', 'transports enough for his command',
               'enough for his command', 'I think there will be transports enough', '7,000 men. General Wright'],
      'E219': ['to meet his family at', 'meet his family', 'steamer Greyhound at his disposal', 'Greyhound at his disposal',
               'place the steamer Greyhound', 'leaves here at 7', 'Webster, chief quartermaster', 'R. C. Webster'],
      'E226': ['mail boats to Charles City', 'send the mail boats', 'Seventh Street wharf', 'Seventh-street wharf', '7th street wharf',
               'mail-boats', 'H. B. Blood', 'Captain Blood'],
      'E227': ['Ninth Vermont will leave', 'steamer Perit', 'on the Perit', 'D. Stinson', 'William L. James', 'W. L. James',
               '150 men Ninth Vermont', 'John Horner']}
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
