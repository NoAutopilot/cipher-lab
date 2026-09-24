#!/usr/bin/env python3
"""French 16th-c. corpus for tools/nomenclator_anneal.py (LANE R4 N, 24 Sept 2026).
Paragraphs of tools/data/fr16 (Catherine de Medicis letters t.1-2, Marguerite de Valois) that look like French
letter prose, normalised with tools/italian_ngram.norm; every 10th kept paragraph is held out for controls.
usage: python3 fr_corpus.py OUTDIR"""
import gzip, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'tools'))
from italian_ngram import norm, paragraphs
FR = set('que les vous pour qui est des une nous mais estre avoir faire aussi leur mesme'.split())
out = sys.argv[1]; train, held = [], []; k = 0
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'tools', 'data', 'fr16')
for fn in sorted(os.listdir(base)):
    if not fn.endswith('_djvu.txt.gz'): continue
    for par in paragraphs(gzip.open(os.path.join(base, fn)).read().decode('utf-8', 'replace')):
        w = re.findall(r'[a-zéèêàùç]+', par.lower())
        if len(w) < 25 or sum(x in FR for x in w) < 0.12 * len(w): continue
        z = norm(par).strip('#')
        (held if k % 10 == 9 else train).append(z); k += 1
open(os.path.join(out, 'fr16_train.txt'), 'w').write('\n'.join(train) + '\n')
open(os.path.join(out, 'fr16_heldout.txt'), 'w').write('\n'.join(held) + '\n')
print(len(train), len(held), sum(map(len, train)), sum(map(len, held)))
