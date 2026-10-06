#!/usr/bin/env python3
"""R9-WVOALIGN descriptive checks (a) 'worden sei' C05 vs C10, (b) 'zweimahl' C06 vs C07: for each letter of the word,
the label aligned to it in each of the two rows (same alignment parameters as the PREREG), and the count that agree.
Imports tools/interlinear_align.py (no copy). Run from the repo root."""
import os, sys
sys.path.insert(0, 'tools')
import interlinear_align as ia
ia.FOLD_FS = False
D = os.path.dirname(os.path.abspath(__file__))
for name in sys.argv[1:] or ['piles', 'passA', 'passB']:
    pairs = ia.load_pairs(os.path.join(D, 'pairs_%s.tsv' % name))
    prep, res, _c, _s = ia.run_align(pairs, code_prefix='@', null_cost=-1.0, seg_bonus=0.0)
    lab = {}
    for (p, raw, toks, letters, *_), chunks in zip(prep, res):
        m = {}
        for t, c in zip(raw, chunks):
            if c and c[1] > c[0]:
                m[c[0]] = t
        lab[p['cipher_line']] = (letters, m)
    for word, a, b in (('wordensei', 'C05', 'C10'), ('zweimahl', 'C06', 'C07')):
        out, same = [], 0
        cols = []
        for r in (a, b):
            letters, m = lab[r]
            k = letters.rfind(word) if r != 'C10' else letters.find(word)
            cols.append([m.get(k + i, '-') for i in range(len(word))])
        for ch, x, y in zip(word, *cols):
            same += (x == y and x != '-')
            out.append('%s:%s/%s' % (ch, x.lstrip('@'), y.lstrip('@')))
        print('%s %s %s vs %s: %d/%d same  %s' % (name, word, a, b, same, len(word), ' '.join(out)))
