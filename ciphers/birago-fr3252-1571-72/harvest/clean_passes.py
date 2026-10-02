#!/usr/bin/env python3
"""NEVBIR-3252, 2 Oct 2026: clean the two f.47r L01-L04 blind passes before value-blind reconciliation.
The --follow-slope cut put L02 on line 1 (both readers saw it): L02 is dropped (line 2 is still unread).
The s2 crops repeat the last few signs of s1 (both readers flagged it): for each line, the s2 head of k signs
(k = 2..6) that best matches the s1 tail (>= k-1 equal ids) is dropped. Pass B's seam note broke one row
(non-numeric pos) per line: dropped. Positions renumbered. No sign value is read."""
import csv, re, sys
def load(p):
    rows=[r for r in csv.DictReader(open(p),delimiter='\t')]
    return [r for r in rows if r['pos'] and r['pos'].strip().isdigit() and ' ' not in (r['sign_id'] or ' ')]
def s2start(rows):
    for i,r in enumerate(rows):
        if 's2' in (r.get('note') or '') and 'start' in (r.get('note') or ''): return i
    return None
def clean(p, out):
    rows=load(p); res=[]; log=[]
    for L in ['L01','L03','L04']:
        lr=[r for r in rows if r['passage']==L]
        i=s2start(lr); drop=0
        if i is not None:
            best=0
            for k in range(2,7):
                if i-k<0 or i+k>len(lr): continue
                a=[r['sign_id'] for r in lr[i-k:i]]; b=[r['sign_id'] for r in lr[i:i+k]]
                if sum(x==y for x,y in zip(a,b))>=k-1: best=k
            drop=best
            lr=lr[:i]+lr[i+drop:]
        log.append(f"{L}: s2 at row {i}, dropped {drop}")
        for n,r in enumerate(lr,1): r['pos']=str(n); res.append(r)
    w=csv.DictWriter(open(out,'w'),fieldnames=['passage','pos','sign_id','alt','conf','note'],delimiter='\t',extrasaction='ignore')
    w.writeheader(); [w.writerow(r) for r in res]
    print(p, '; '.join(log), len(res),'signs')
clean('passA_L01-04.tsv','passA_clean.tsv'); clean('passB_L01-04.tsv','passB_clean.tsv')
