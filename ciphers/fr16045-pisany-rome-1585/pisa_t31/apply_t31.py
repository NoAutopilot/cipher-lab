#!/usr/bin/env python3
"""PISA-T31 commit (PREREG-PISA-T31.md gate PASS, 11 Oct 2026): derive tx86e/ciphertext_f275r.tsv from the byte-identical pre-edit
copy tx86e/ciphertext_f275r_preT31.tsv (itself derived by una3_pisa/apply_t27.py) by relabelling the 5 f.275r tokens
pisa_t31/result.tsv marks SETTLED-BY-TWO on another-value cell (T31 -> T36 x4, T31 -> T45 x1; rescore.relabel asserts each is T31).
    python3 pisa_t31/apply_t31.py [--check]   (--check exits 1 if the committed file differs from the derivation)"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, H)
import rescore as R
pk = R.picks(); assert len(pk) == 5, pk
tmp = R.relabel('tx86e/ciphertext_f275r_preT31.tsv', pk, 'pisa_t31/tx/_apply.tsv')
txt = open(os.path.join(T, tmp)).read(); os.remove(os.path.join(T, tmp))
dst = os.path.join(T, 'tx86e/ciphertext_f275r.tsv')
if '--check' in sys.argv:
    ok = open(dst).read() == txt; print('tx86e/ciphertext_f275r.tsv', 'up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(dst, 'w').write(txt); print('wrote tx86e/ciphertext_f275r.tsv:', ', '.join(f'{l} i{i} T31->{v}' for (l, i), v in sorted(pk.items())))
