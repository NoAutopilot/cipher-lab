#!/usr/bin/env python3
"""BNF-Q7-ERR: write ../ciphertext_v2.tsv from ciphertext.tsv + passC_blind.tsv + err_adj.tsv (never overwrites
ciphertext.tsv). Per op: rec -> keep reconciled; blind -> take pass C (D drops the digit); unread -> pass C digit
with '?' (S/I) or reconciled digit with '?' (D). L06's disputed head is replaced by the adjudicator's own read of the
native zoom (adj_f25_L06_zoom.jpg); L00 (cipher tail of the clear line above the block, absent from ciphertext.tsv)
is added from pass C, unadjudicated. Prints the change list. usage: make_v2.py"""
import err_measure as e
R = e.load('../ciphertext.tsv'); B = e.load('passC_blind.tsv')
adj = {}
for ln in open('err_adj.tsv'):
    if ln.startswith('#') or ln.startswith('line\t'): continue
    f = ln.rstrip('\n').split('\t'); adj.setdefault(f[0], []).append(f[3])
L06_OWN = '303?7383032193115'   # 3 0 [bold blot, 3?] 7 3 ß=8 3 0 3 2 1 9 3 1 1 5
out = {}
for L in sorted(R):
    vs = iter(adj.get(L, [])); s = ''
    for op, rpos, r, b in e.align(R[L], B[L]):
        if op == 'M': s += r; continue
        v = next(vs)
        if v == 'rec': s += '' if op == 'I' else r
        elif v == 'blind': s += '' if op == 'D' else b
        else: s += (b + '?') if op != 'D' else (r + '?')
        print(f'{L}\t{op}\trpos {rpos}\t{r}->{b}\t{v}')
    out[L] = s
out['f25_L06'] = L06_OWN
with open('../ciphertext_v2.tsv', 'w') as f:
    f.write('# BnF fr.3982 f.25, v2 (BNF-Q7-ERR, 13 Oct 2026): ciphertext.tsv corrected by adjudicating every disagreement with blind pass C against the native crops (q7test/err_adj.tsv, make_v2.py). The looped sign is read 8 (M; an alphabet question for the sign sorter). L06 is the adjudicator\'s own read. f25_L00 = digits after "gran progresso" on the clear line above the block, missing from ciphertext.tsv, pass C only, unadjudicated. ? after an uncertain digit; grade M throughout.\nline\tdigits\n')
    f.write(f"f25_L00\t{open('passC_blind.tsv').read().split('f25_L00')[1].split()[0]}\n")
    for L in sorted(out): f.write(f'{L}\t{out[L]}\n')
