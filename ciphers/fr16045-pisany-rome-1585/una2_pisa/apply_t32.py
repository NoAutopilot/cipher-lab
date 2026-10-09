#!/usr/bin/env python3
"""UNA2-PISA commit (una2_pisa/PREREG-UNA2-PISA.md gate PASS, 9 Oct 2026): derive the committed tx87/ciphertext_f301v.tsv and
tx87b/ciphertext_f302v.tsv from the byte-identical pre-edit copies *_preT32.tsv by relabelling the 11 SETTLED-T32 tokens T57 -> T32.
    python3 una2_pisa/apply_t32.py [--check]   (--check exits 1 if either committed file differs from the derivation)"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, H)
import una2_pisa as U

bad = 0
for pg, d, *_ in U.PAGES:
    picks = {(l, o) for (p, l, o), v in U.SETTLED.items() if p == pg and v == 'SETTLED-T32'}
    lines = U.read(f'{d}/ciphertext_{pg}_preT32.tsv')
    txt = ''.join('\n' if x is None else f'{x[0]}\t{x[1]}\n' for x in U.relabel(lines, pg, picks))
    dst = os.path.join(T, f'{d}/ciphertext_{pg}_preT27.tsv')  # UNA3-PISA: una3_pisa/apply_t27.py now derives the committed file from this copy
    if '--check' in sys.argv:
        ok = open(dst).read() == txt; bad += not ok; print(dst, 'up to date' if ok else 'STALE')
    else:
        open(dst, 'w').write(txt); print('wrote', dst, len(picks), 'labels')
sys.exit(1 if bad else 0)
