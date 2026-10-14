#!/usr/bin/env python3
"""VIV-67: tokenisation fix before tools/reconcile_passes.py -- a multi-word [PLAIN:...] group in a blind pass is joined
into one token ([PLAIN:w1_w2_...]) so the whitespace tokenizer cannot leak plain words into the cipher stream. Nothing else
in the pass changes.   python3 tx/viv67_prep.py [PAGE]   (default f201r: writes tx/f201r_passA_c.tsv, tx/f201r_passB_c.tsv;
VIV-67B: PAGE f201v)"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = sys.argv[1] if len(sys.argv) > 1 else 'f201r'
for p in ('A', 'B'):
    s = open(os.path.join(HERE, f'{PAGE}_pass{p}.tsv'), encoding='utf-8').read()
    s = re.sub(r'\[PLAIN:([^\]]*)\]', lambda m: '[PLAIN:' + '_'.join(m.group(1).split()) + ']', s)
    open(os.path.join(HERE, f'{PAGE}_pass{p}_c.tsv'), 'w', encoding='utf-8').write(s)
