#!/usr/bin/env python3
"""BAL103-200 reconciliation: rec/ciphertext_draft.tsv (tools/reconcile_passes.py --keep-plain on joinA/joinB) -> f200r_rec.tsv.
Settlement by sign class, eyed on crops L01 and L05 (same hand and same rules as BAL103-189's rec_settled.tsv): on a disagreeing
column, pass A by default, except (A sigma, B 5) -> 5 (the long-s shape; 189 rule '5 over sigma'). A '-' (B-only sign) is dropped
under A default. Every settled column is listed in rec_settled.tsv. M grade throughout."""
import csv, os
H = os.path.dirname(os.path.abspath(__file__))
RULE = {('sigma', '5'): ('5', "class rule '5 over sigma' (eyed L01, L05)")}
CLASS_A = {('H', 'xs'), ('H', '8s'), ('mt', '3'), ('mt', 'z'), ('mt', '3|z'), ('mt', '3|mm'), ('q2', '2'), ('xc', 'xs')}
rows = list(csv.DictReader(open(os.path.join(H, 'rec/ciphertext_draft.tsv')), delimiter='\t'))
lines, settled = {}, ['line\tcol\tA\tB\tsettled\twhy']
for r in rows:
    if r['alt'].startswith('A:'): a, b = r['alt'][2:], r['sign']   # draft shows B's sign where A is the alt
    else: a, b = r['sign'], (r['alt'][2:] if r['alt'].startswith('B:') else '')
    out, why = a, ''
    if r['why'] in ('differ', 'gap'):
        if (a, b) in RULE: out, why = RULE[(a, b)]
        elif (a, b) in CLASS_A: why = 'class rule, A shape (eyed L01, L05; BAL103-189 rule)'
        else: why = 'A default'
        settled.append(f"{r['line'][6:9]}\t{r['position']}\t{a}\t{b or '-'}\t{out}\t{why}")
    if out != '-': lines.setdefault(r['line'], []).append(out)
hdr = '# BAL103-200 reconciliation of passA/passB (joined per line by join_lines.py; tools/reconcile_passes.py --keep-plain, 64.9% agree); settled list in rec_settled.tsv\n'
open(os.path.join(H, 'f200r_rec.tsv'), 'w').write(hdr + ''.join(f"{k}\t{' '.join(v)}\n" for k, v in lines.items()))
open(os.path.join(H, 'rec_settled.tsv'), 'w').write('\n'.join(settled) + '\n')
print(len(lines), 'lines', len(settled) - 1, 'columns settled')
