#!/usr/bin/env python3
"""FV-FM5b (9 Oct 2026): phrase/stem grep for E220 (5811), E222 (5747), E223 (5823), E224 (5701), E225 (5626) in the cached print-check texts
(sources/ia-fulltext/print-check) plus scratch *.txt given as arguments (OR I/36 pt 3, I/40 pt 2, I/42 pts 2-3); letters-only match.
A miss is a search result for the log, not a statement about print (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())
PH = {'E220': ['will send tonight the', 'will send to-night the', 'H. Livingston', 'Weybosset', 'Louisa Moore', 'capacity in all',
               '6,600 men', 'Gen. Sedgwick', 'General Sedgwick, Massachusetts', 'every steamer and propeller', 'names of those you send'],
      'E222': ['send up all ferry', 'ferry-boats immediately', 'ferry boats immediately', 'quickest possible form', 'hurry up our telegraph',
               'telegraph party', 'lumber to Fort Powhatan', 'stop at Fort Powhatan'],
      'E223': ['Western Metropolis', 'B. Deford', 'urgent military necessity', 'Surgeon-General Barnes', 'has taken the Western',
               'Metropolis, Baltic', 'Baltic and'],
      'E224': ['Captain Farquhar', 'Farquhar', 'you are ordered to report to General Smith', 'as he passes Fort Monroe', 'large force to join',
               'as chief engineer'],
      'E225': ['Longstreet at Charlottesville', 'our man reports', 'from his own corps', 'think the number large', 'John I. Davenport',
               'Davenport', '5,000 men from']}
raw = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    raw[os.path.basename(p)[:-12]] = gzip.open(p, 'rt', errors='ignore').read()
for p in sys.argv[1:]:
    raw[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
texts = {k: norm(v) for k, v in raw.items()}
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [f'{v}:{t.count(norm(ph))}' for v, t in texts.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits[:12]) or 'none', f'({len(hits)})')
