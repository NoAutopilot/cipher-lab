#!/usr/bin/env python3
"""PISA-MERGE commit (pisa_merge/PREREG-PISA-MERGE.md): derive tx86/ciphertext_f244r.tsv from the byte-identical pre-edit copy
tx86/ciphertext_f244r_preMERGE.tsv (itself derived by pisa_rs244/apply_rs244.py) by deleting only the tokens of the groups
pisa_merge/result.json marks commit=true (gate PASS; G-X and G-M5alt never); merge.delete asserts the label at each position.
    python3 pisa_merge/apply_merge.py [--check]   (--check exits 1 if the committed file differs from the derivation)"""
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, H)
import merge as M
res = json.load(open(os.path.join(H, 'result.json')))
lines = M.U.read('tx86/ciphertext_f244r_preMERGE.tsv'); dels = {}
for g in res["committable_groups"]:
    assert res[g]["commit"] and M.GROUPS[g][3]; dels.update(M.GROUPS[g][0])
lines = M.delete(lines, dels)
txt = ''.join('\n' if x is None else f'{x[0]}\t{x[1]}\n' for x in lines)
dst = os.path.join(T, 'tx86/ciphertext_f244r.tsv')
if '--check' in sys.argv:
    ok = open(dst).read() == txt; print('tx86/ciphertext_f244r.tsv', 'up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(dst, 'w').write(txt); print('wrote tx86/ciphertext_f244r.tsv:', ', '.join(res["committable_groups"]) or 'no group')
