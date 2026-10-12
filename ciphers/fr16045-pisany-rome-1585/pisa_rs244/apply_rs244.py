#!/usr/bin/env python3
"""PISA-RS244 commit (pisa_rs244/PREREG-PISA-RS244.md): derive tx86/ciphertext_f244r.tsv from the byte-identical pre-edit copy
tx86/ciphertext_f244r_preRS244.tsv (written by tx86/reconcile86.py) by relabelling only the groups pisa_rs244/result.json marks
commit=true (gate PASS; T57->T42 never); rs244.relabel asserts the old label at each position.
    python3 pisa_rs244/apply_rs244.py [--check]   (--check exits 1 if the committed file differs from the derivation)"""
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, H)
import rs244 as R
res = json.load(open(os.path.join(H, 'result.json')))
cands = R.candidates(); lines = R.U.read('tx86/ciphertext_f244r_preRS244.tsv'); done = []
for g in res["committable_groups"]:
    old, new = g.split('->'); assert res[g]["commit"] and (old, new) not in R.NOCOMMIT
    lines = R.relabel(lines, cands[(old, new)], old, new); done.append(f'{g} x{len(cands[(old, new)])}')
txt = ''.join('\n' if x is None else f'{x[0]}\t{x[1]}\n' for x in lines)
dst = os.path.join(T, 'tx86/ciphertext_f244r.tsv')
if '--check' in sys.argv:
    ok = open(dst).read() == txt; print('tx86/ciphertext_f244r.tsv', 'up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(dst, 'w').write(txt); print('wrote tx86/ciphertext_f244r.tsv:', ', '.join(done) or 'no group')
