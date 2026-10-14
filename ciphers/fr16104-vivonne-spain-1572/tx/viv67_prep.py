#!/usr/bin/env python3
"""VIV-67: tokenisation fix before tools/reconcile_passes.py -- a multi-word [PLAIN:...] group in a blind pass is joined
into one token ([PLAIN:w1_w2_...]) so the whitespace tokenizer cannot leak plain words into the cipher stream. Nothing else
in the pass changes.   python3 tx/viv67_prep.py   (writes tx/f201r_passA_c.tsv, tx/f201r_passB_c.tsv)"""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ('A', 'B'):
    s = open(os.path.join(HERE, f'f201r_pass{p}.tsv'), encoding='utf-8').read()
    s = re.sub(r'\[PLAIN:([^\]]*)\]', lambda m: '[PLAIN:' + '_'.join(m.group(1).split()) + ']', s)
    open(os.path.join(HERE, f'f201r_pass{p}_c.tsv'), 'w', encoding='utf-8').write(s)
