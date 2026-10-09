#!/usr/bin/env python3
"""PISA-T32 commit (pisa_t32/PREREG-PISA-T32.md gate PASS, 9 Oct 2026): derive tx86e/ciphertext_f275r.tsv from the byte-identical
pre-edit copy tx86e/ciphertext_f275r_preT32.tsv (itself derived by tx86e/apply_t36.py) by relabelling the 4 f.275r tokens
una_pisa/result.tsv marks SETTLED-T32, T57 -> T32 (una2_pisa.relabel, which asserts each is T57 at its una_pisa/tokens_pos.tsv pos).
    python3 tx86e/apply_t32.py [--check]   (--check exits 1 if the committed file differs from the derivation)"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, os.path.join(T, 'una2_pisa'))
import una2_pisa as U
picks = {(l, o) for (p, l, o), v in U.SETTLED.items() if p == 'f275r' and v == 'SETTLED-T32'}
assert len(picks) == 4, picks
txt = ''.join('\n' if x is None else f'{x[0]}\t{x[1]}\n'
              for x in U.relabel(U.read('tx86e/ciphertext_f275r_preT32.tsv'), 'f275r', picks))
dst = os.path.join(H, 'ciphertext_f275r_preT27.tsv')  # UNA3-PISA: the T27 relabel now derives the committed file from this copy (una3_pisa/apply_t27.py)
if '--check' in sys.argv:
    ok = open(dst).read() == txt; print('tx86e/ciphertext_f275r_preT27.tsv', 'up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(dst, 'w').write(txt); print('wrote tx86e/ciphertext_f275r_preT27.tsv:', ', '.join(f'{l} o{o} T57->T32' for l, o in sorted(picks)))
