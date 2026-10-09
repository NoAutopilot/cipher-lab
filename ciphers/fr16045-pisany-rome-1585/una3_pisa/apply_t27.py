#!/usr/bin/env python3
"""UNA3-PISA commit (una3_pisa/PREREG-UNA3-PISA.md gate PASS, 9 Oct 2026): derive the committed tx86e/ciphertext_f275r.tsv,
tx87/ciphertext_f301v.tsv and tx87b/ciphertext_f302v.tsv from the byte-identical pre-edit copies *_preT27.tsv (themselves derived by
tx86e/apply_t32.py and una2_pisa/apply_t32.py) by relabelling the 3 tokens una_pisa/result.tsv marks SETTLED-T27, T47 -> T27
(una3_pisa.relabel, which asserts each is T47 at its una_pisa/tokens_pos.tsv pos).
    python3 una3_pisa/apply_t27.py [--check]   (--check exits 1 if any committed file differs from the derivation)"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, H)
import una3_pisa as V
bad = 0
for pg, d, *_ in V.PAGES:
    picks = V.picks_of(pg); assert len(picks) == 1, (pg, picks)
    txt = ''.join('\n' if x is None else f'{x[0]}\t{x[1]}\n'
                  for x in V.relabel(V.U.read(f'{d}/ciphertext_{pg}_preT27.tsv'), pg, picks))
    dst = f'{d}/ciphertext_{pg}.tsv'
    if '--check' in sys.argv:
        ok = open(os.path.join(T, dst)).read() == txt; bad += not ok; print(dst, 'up to date' if ok else 'STALE')
    else:
        open(os.path.join(T, dst), 'w').write(txt); print('wrote', dst, ', '.join(f'{l} o{o} T47->T27' for l, o in sorted(picks)))
sys.exit(1 if bad else 0)
