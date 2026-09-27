#!/usr/bin/env python3
"""Compare two blind atlas-coded passes over the same numbered strips, box by box (campaign H10/H3).

Usage: python3 compare_box_passes.py passA.tsv passB.tsv [--out disagreements.tsv]
Each pass TSV has columns line, pos, code, note, conf (pos is the strip's printed box number, or e.g. "8a" for an
unboxed sign the pass added; a merged box carries codes joined by "+"). Reports: boxes coded by both, exact code
agreement (the rule-3-style pooled agreement figure, against the transcription brief's 60% gate), agreement
counting a "+" merge as agreeing when the first code matches, additions made by one pass and not the other, and
writes the disagreement rows for a reconciler to settle from the strips. tools/reconcile_passes.py is for
line-aligned free-text passes; a box-numbered pass pair aligns by pos, which is what this does.
"""
import csv, sys, argparse
def load(p):
    d={}
    for r in csv.DictReader(open(p), delimiter='\t'):
        if not r.get('pos'): continue
        d[(r['line'].strip().lstrip('L').lstrip('0') or '0', r['pos'].strip())]=r
    return d
ap=argparse.ArgumentParser(); ap.add_argument('a'); ap.add_argument('b'); ap.add_argument('--out')
a_=ap.parse_args(); A=load(a_.a); B=load(a_.b)
both=sorted(set(A)&set(B), key=lambda k:(int(k[0]), int(''.join(ch for ch in k[1] if ch.isdigit()) or 0), k[1]))
exact=sum(1 for k in both if A[k]['code'].strip().upper()==B[k]['code'].strip().upper())
first=sum(1 for k in both if A[k]['code'].split('+')[0].strip().upper()==B[k]['code'].split('+')[0].strip().upper())
print(f"boxes in both: {len(both)}; exact agreement {exact}/{len(both)} = {exact/max(1,len(both)):.1%}; first-code agreement {first}/{len(both)} = {first/max(1,len(both)):.1%}")
onlyA=sorted(set(A)-set(B)); onlyB=sorted(set(B)-set(A))
print(f"only in A: {len(onlyA)} {[k[0]+':'+k[1]+'='+A[k]['code'] for k in onlyA]}")
print(f"only in B: {len(onlyB)} {[k[0]+':'+k[1]+'='+B[k]['code'] for k in onlyB]}")
rows=[(k[0],k[1],A[k]['code'],A[k].get('conf',''),B[k]['code'],B[k].get('conf','')) for k in both if A[k]['code'].strip().upper()!=B[k]['code'].strip().upper()]
for r in rows: print('  DIS', *r)
if a_.out:
    with open(a_.out,'w') as f:
        f.write('line\tpos\tcodeA\tconfA\tcodeB\tconfB\tsettled\n')
        for r in rows: f.write('\t'.join(r)+'\t\n')
    print('wrote', a_.out, len(rows), 'rows')
