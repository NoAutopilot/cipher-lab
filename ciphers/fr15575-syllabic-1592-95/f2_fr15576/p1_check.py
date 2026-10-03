#!/usr/bin/env python3
"""NV05D premise test P1 (PREREG.md): share K of numeric tokens on fr.15576 f.2 L01-L04 whose value is a coded row
of ../key_no54.tsv (codes 10-99), plus err_2reader of passA vs passB. Writes p1.tsv; --check exits 1 if stale."""
import re, sys, pathlib
H = pathlib.Path(__file__).parent
codes = {l.split('\t')[0] for l in (H.parent / 'key_no54.tsv').read_text().splitlines()
         if l and not l.startswith(('#', 'code')) and l.split('\t')[2] == 'syllable' and l.split('\t')[0].isdigit()}
def toks(p): return {l.split('\t')[0]: l.split('\t')[1].split() for l in p.read_text().splitlines() if l and not l.startswith('line')}
def num(t): return re.sub(r'[^0-9]', '', t)
rec = toks(H / 'ciphertext_L01-04.tsv')
nums = [num(t) for ts in rec.values() for t in ts if num(t)]
inkey = [n for n in nums if n in codes]
A, B = toks(H / 'passA.tsv'), toks(H / 'passB.tsv')
al = sum(len(A[k]) for k in A if len(A[k]) == len(B[k]))
dv = sum(num(a) != num(b) for k in A for a, b in zip(A[k], B[k]))
dall = sum(a.rstrip('?') != b.rstrip('?') for k in A for a, b in zip(A[k], B[k]))
lens = sorted({len(n) for n in nums})
out = (f"numeric_tokens\t{len(nums)}\nin_key_no54_syllabary\t{len(inkey)}\nK\t{len(inkey)/len(nums):.3f}\n"
       f"digit_lengths\t{','.join(map(str, lens))}\ngate_K>=0.50\t{'PASS' if len(inkey)/len(nums) >= 0.5 else 'FAIL'}\n"
       f"aligned_tokens_AB\t{al}\nerr_2reader_digits\t{dv}/{al}={dv/al:.3f}\nerr_2reader_incl_marks\t{dall}/{al}={dall/al:.3f}\n")
f = H / 'p1.tsv'
if '--check' in sys.argv:
    sys.exit(0 if f.exists() and f.read_text() == out else 1)
f.write_text(out); print(out, end='')
