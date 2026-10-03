#!/usr/bin/env python3
"""GAPS38 (3 Oct 2026): apply the reconciler's verdicts (rec/settled.tsv) to reconcile_passes.py's aligned draft
(rec/ciphertext_draft.tsv, Bourdeau = A, blind Opus pass = B) and write ciphertext_reconciled.tsv.
Settled columns get the verdict sign at the reconciler's confidence; a '-' verdict drops the column.
--check regenerates in memory and exits 1 if the committed file differs (rule 7)."""
import csv, sys, os
D = os.path.dirname(os.path.abspath(__file__))
def build():
    settled = {(r['line'], r['col']): r for r in csv.DictReader(open(f'{D}/rec/settled.tsv'), delimiter='\t')}
    out, pos, cur = [], 0, None
    for r in csv.DictReader(open(f'{D}/rec/ciphertext_draft.tsv'), delimiter='\t'):
        if r['line'] != cur: cur, pos = r['line'], 0
        s = settled.pop((r['line'], r['position']), None)
        sign, conf, why = r['sign'], r['confidence'], r['why']
        if s:
            if s['sign'] == '-': continue
            sign, conf, why = s['sign'], s['conf'], 'settled:' + s['verdict']
        pos += 1
        out.append(f"{r['line']}\t{pos}\t{sign}\t{conf}\t{why}")
    assert not settled, settled
    return 'line\tpos\tsign\tconf\twhy\n' + '\n'.join(out) + '\n'
txt = build(); f = f'{D}/ciphertext_reconciled.tsv'
if '--check' in sys.argv:
    sys.exit(0 if open(f).read() == txt else 1)
open(f, 'w').write(txt)
