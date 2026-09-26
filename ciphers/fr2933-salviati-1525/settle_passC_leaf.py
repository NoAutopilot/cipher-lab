#!/usr/bin/env python3
"""bSALC (26 Sept 2026): 2-of-3 majority of pass A / pass B / pass C on one leaf's disagreement boxes, any leaf.

  python3 settle_passC_leaf.py <leaf>

Reads passA_<leaf>.tsv, passB_<leaf>.tsv, passC_<leaf>.tsv and recon_box_<leaf>/disagreements.tsv. At each row: if two of
the three base codes agree, that code wins (marks from an agreeing pass, preferring one that gives a mark); a three-way
split (all three differ) is taken from THREE_WAY.tsv (leaf, line, pos, code, marks, reason -- settled on the crop, grade M)
when a row exists there, else provisionally to pass B's call (the leaf's prior settle policy) and flagged 'split'.
Writes recon_box_<leaf>/settled_passC.tsv (line,pos,code,marks,source,reason) and prints the counts. The earlier
recon_box_<leaf>/settled.tsv (one reader's settle) is left untouched for comparison.
"""
import csv, os, sys
from collections import Counter

LEAF = sys.argv[1]


def load(path):
    rows = {}
    for r in csv.DictReader(open(path), delimiter='\t'):
        rows[(r['line'].strip(), r['pos'].strip())] = {k.strip(): (v or '').strip() for k, v in r.items() if k}
    return rows


def main():
    A, B, C = (load(f'pass{p}_{LEAF}.tsv') for p in 'ABC')
    tw = {}
    if os.path.exists('THREE_WAY.tsv'):
        for r in csv.DictReader(open('THREE_WAY.tsv'), delimiter='\t'):
            if r['leaf'] == LEAF:
                tw[(r['line'], r['pos'])] = r
    dis = list(csv.DictReader(open(f'recon_box_{LEAF}/disagreements.tsv'), delimiter='\t'))
    out, src = [], Counter()
    missing_c = 0
    for r in dis:
        k = (r['line'].strip(), r['pos'].strip())
        a, b, c = A.get(k), B.get(k), C.get(k)
        ca = a['code'] if a else 'MISSING'
        cb = b['code'] if b else 'MISSING'
        if c is None:
            missing_c += 1
        cc = c['code'] if c else 'NO_C'
        ma, mb, mc = (x['marks'] if x else '' for x in (a, b, c))
        if cc == ca and cc == cb:
            code, marks, s = cc, mc or ma or mb, 'ABC'
        elif ca == cb:
            code, marks, s = ca, ma or mb, 'AB'
        elif cc == ca:
            code, marks, s = ca, ma or mc, 'AC'
        elif cc == cb:
            code, marks, s = cb, mb or mc, 'BC'
        elif k in tw:
            code, marks, s = tw[k]['code'], tw[k]['marks'], 'split-M'
        else:
            code, marks, s = cb, mb, 'split'
        src[s] += 1
        reason = f'A={ca} B={cb} C={cc}' + (f'; C note: {c["note"]}' if c else '') + (f'; settled on crop: {tw[k]["reason"]}' if s == 'split-M' else '')
        out.append((k[0], k[1], code, marks, s, reason.replace('\t', ' ')))
    with open(f'recon_box_{LEAF}/settled_passC.tsv', 'w') as f:
        f.write('line\tpos\tcode\tmarks\tsource\treason\n')
        for row in out:
            f.write('\t'.join(row) + '\n')
    n = len(dis)
    print(f'{LEAF}: {n} rows, C missing {missing_c}; sources {dict(src)}; '
          f'C sided with A {src["AC"]}, B {src["BC"]}, neither {src["split"] + src["split-M"]}')


if __name__ == '__main__':
    main()
