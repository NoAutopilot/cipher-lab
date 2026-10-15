#!/usr/bin/env python3
"""MONL-L16 (15 Oct 2026): parse the c268 L16-L20 blind passes A and B (passes/c268d_pass{A,B}_raw.txt) into token files and a
draft reconciliation table (sequence match; 'both passes' where they agree, every other position listed for the eye decision).
Writes passes/c268d_passA.tsv, c268d_passB.tsv and prints per-line agreement plus the disagreement spans. The eye decisions
themselves live in passes/c268d_reconciled.tsv (written by hand from the crops, `how` column per token)."""
import difflib, re
from pathlib import Path
P = Path(__file__).resolve().parent

def parse(fn):
    out = {}
    for l in (P / fn).read_text().splitlines():
        m = re.match(r'LINE (L\d+): (.*)', l)
        if m:
            out[m.group(1)] = [t.replace(' ', '_') for t in re.findall(r'\?x\[[^\]]*\]|\S+', m.group(2))]
    return out

A, B = parse('c268d_passA_raw.txt'), parse('c268d_passB_raw.txt')
for n, d in (('A', A), ('B', B)):
    (P / f'c268d_pass{n}.tsv').write_text(''.join(f'{k}\t{" ".join(v)}\n' for k, v in sorted(d.items())))
tot = agr = 0
for lab in sorted(A):
    a, b = A[lab], B.get(lab, [])
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    eq = sum(i2 - i1 for t, i1, i2, _, _ in sm.get_opcodes() if t == 'equal')
    tot += max(len(a), len(b)); agr += eq
    print(f'{lab}: A {len(a)} B {len(b)} agree {eq}')
    for t, i1, i2, j1, j2 in sm.get_opcodes():
        if t != 'equal':
            print(f'   {t:7s} A[{i1+1}-{i2}] {" ".join(a[i1:i2]) or "-"}  |  B[{j1+1}-{j2}] {" ".join(b[j1:j2]) or "-"}')
print(f'total agree {agr}/{tot} = {agr/tot:.3f}')
