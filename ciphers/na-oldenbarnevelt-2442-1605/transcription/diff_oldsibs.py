#!/usr/bin/env python3
"""OLD-SIBS (8 Oct 2026): per-sign disagreement between the two blind passes per leaf (PREREG_OLD-SIBS item 3).
Usage: python3 diff_oldsibs.py L4 L5 L7   (reads passJ_OLDSIBS_<leaf>_A.tsv and _B.tsv beside this script)."""
import csv, os, sys
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diff_pass2 import norm_tok, lev

HERE = os.path.dirname(os.path.abspath(__file__))

def lines(path):
    d = defaultdict(str)
    for r in csv.DictReader(open(path), delimiter='\t'):
        t = r['token']
        if t in ('EMPTY',):
            continue
        d[r['line']] += norm_tok(t)
    return d

tot_e = tot_n = 0.0
for leaf in sys.argv[1:] or ['L4', 'L5', 'L7']:
    a = lines(os.path.join(HERE, f'passJ_OLDSIBS_{leaf}_A.tsv'))
    b = lines(os.path.join(HERE, f'passJ_OLDSIBS_{leaf}_B.tsv'))
    e = n = 0.0
    for k in sorted(set(a) | set(b)):
        e += lev(a.get(k, ''), b.get(k, ''))
        n += (len(a.get(k, '')) + len(b.get(k, ''))) / 2
    tot_e += e; tot_n += n
    print(f'{leaf}\tedits {e:.0f}\tmean_len {n:.0f}\tdisagreement {100*e/max(n,1):.1f}%')
print(f'pooled\tedits {tot_e:.0f}\tmean_len {tot_n:.0f}\tdisagreement {100*tot_e/max(tot_n,1):.1f}%')
