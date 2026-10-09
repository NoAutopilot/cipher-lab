#!/usr/bin/env python3
"""FV-FM4 (9 Oct 2026): phrase/stem grep for E193 (5784) and E194 (5805) in the cached print-check texts (sources/ia-fulltext/print-check)
plus scratch *.txt given as arguments; prints letters-only hits and a context window for raw-text hits. A miss is a search result (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())
PH = {'E193': ['sick prisoners to be exchanged', 'destination unknown to me', 'transportation for about 5700', '5700 sick', '5,700 sick',
               'R. C. Webster', 'Capt. R. C. Webster', 'about 5,700', 'transportation for sick prisoners'],
      'E194': ['open your own letter of instructions', 'vessels which have no letters', 'If General Hawley is gone', 'Captain Langdon',
               'Langdon, First U', 'use all possible despatch', 'corresponding orders to the vessels', 'letter of instructions']}
raw = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    raw[os.path.basename(p)[:-12]] = gzip.open(p, 'rt', errors='ignore').read()
for p in sys.argv[1:]:
    raw[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
texts = {k: norm(v) for k, v in raw.items()}
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in texts.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits[:12]) or 'none', f'({len(hits)})')
