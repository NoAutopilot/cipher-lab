#!/usr/bin/env python3
"""PIS-246 (13 Oct 2026): tally every T40 token on f.246r (tx246/ciphertext_f246r.tsv vs kp246/colbert_f246r.txt) into the
D1A-PIS T40 alignment table, with d1apis/t40_align.py's own witness() (masked token = one neutral slot, band_dp against the
copy) UNCHANGED. Descriptive only: D1A-PIS's power control failed (a pure cell reads its own letter at ~0.43), so no gate
is run here and key86.tsv is not touched. The seven-page result.json / t40_witness.tsv stay as committed; this writes
d1apis/t40_witness_f246r.tsv (f.246r rows) and d1apis/t40_tally_8pages.json (seven pages + f.246r pooled).
    python3 d1apis/t40_f246r.py [--check]"""
import os, sys, json
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, H)
import t40_align as ta

toks, where, clear = ta.load('tx246/ciphertext_f246r.tsv', 'kp246/colbert_f246r.txt')
m = {i for i, t in enumerate(toks) if t == 'T40'}
w = ta.witness(toks, clear, m)
rows = [f'f246r\t{where[i][0]}\t{where[i][1]}\t{w[i]}' for i in sorted(m)]
seven = [ln.rstrip('\n').split('\t')[3] for ln in open(os.path.join(H, 't40_witness.tsv')).readlines()[1:]]
new = [w[i] for i in sorted(m)]
out = {'f246r': dict(N=len(new), tokens_on_page=len(toks), letters=dict(Counter(new).most_common())),
       'seven_pages_committed': dict(N=len(seven), letters=dict(Counter(seven).most_common())),
       'pooled_8pages': dict(N=len(seven) + len(new), letters=dict(Counter(seven + new).most_common()))}
v, n, s = ta.top(seven + new)
out['pooled_8pages'].update(top=v, count=n, share=round(s, 3))
out['note'] = 'descriptive; D1A-PIS power control 0/50 (pure cell ~0.43), so no gate; key86.tsv unchanged'
js = json.dumps(out, indent=1, sort_keys=True) + '\n'
tsv = 'page\tline\tpos\taligned\n' + '\n'.join(rows) + '\n'
rp, wp = os.path.join(H, 't40_tally_8pages.json'), os.path.join(H, 't40_witness_f246r.tsv')
if '--check' in sys.argv:
    ok = os.path.exists(rp) and open(rp).read() == js and open(wp).read() == tsv
    print('up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(rp, 'w').write(js); open(wp, 'w').write(tsv); print(js)
