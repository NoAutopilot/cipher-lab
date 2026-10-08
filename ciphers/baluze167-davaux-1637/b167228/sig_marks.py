#!/usr/bin/env python3
"""SIG-B228: score the two blind numeral-mark reads (b167228/sig_num/read{A,B}.tsv) under prereg_sig.md item 6 and write
b167228/sig_marks.tsv (line, numeral occurrence, code, agreed mark) for b167228/to_pipe.py. A target (one of the 27 unmarked numerals)
takes a mark only when both reads name the same mark and it is not 'none'; the control gate (>= 3 of 4 pre-registered marked
numerals read with their transcribed mark by both reads) must pass or nothing is written. Usage: python3 b167228/sig_marks.py"""
import csv
D = 'b167228/sig_num/'
rd = lambda f: {(r['strip'], int(r['idx'])): r for r in csv.DictReader(open(D + f), delimiter='\t')}
A, B, T = rd('readA.tsv'), rd('readB.tsv'), rd('targets.tsv')
SYM = {'acute': "'", 'diaeresis': ':', 'bar': '='}
ctrl = [k for k, r in T.items() if r['role'] == 'control']
ok = sum(A[k]['mark'] == B[k]['mark'] == 'acute' for k in ctrl)
print(f'control gate: {ok}/{len(ctrl)} marked numerals read acute by both ->', 'PASS' if ok >= 3 else 'FAIL')
for k in sorted(ctrl):
    print('  control', k, T[k]['code'], 'A', A[k]['mark'], 'B', B[k]['mark'])
out = ['line\toccurrence\tcode\tmark\tA\tB']
n = {'regrade': 0, 'both_none': 0, 'split': 0}
for k, r in sorted(T.items()):
    if r['role'] != 'target':
        continue
    a, b = A[k]['mark'], B[k]['mark']
    assert A[k]['numeral'] == B[k]['numeral'] == r['code'], k
    if a == b and a in SYM:
        n['regrade'] += 1; out.append(f"{r['line']}\t{r['idx']}\t{r['code']}\t{SYM[a]}\t{a}\t{b}")
    elif a == b == 'none':
        n['both_none'] += 1
    else:
        n['split'] += 1
    print('  target', k, r['line'], r['code'], 'A', a, 'B', b)
print(n)
if ok >= 3:
    open('b167228/sig_marks.tsv', 'w').write('\n'.join(out) + '\n')
