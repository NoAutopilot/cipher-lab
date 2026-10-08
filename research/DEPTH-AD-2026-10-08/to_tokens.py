#!/usr/bin/env python3
"""DEPTH-AD (8 Oct 2026): convert a folder's reading-tokens TSV into tools/depth_stats.py's column order
(line, pos, sign, conf, value, grade). Header names are matched case-insensitively; --line joins several columns
(e.g. folio,line). Values in --null (default NULL, null, nulle, -) become '' (a null carries no letters).
Usage: to_tokens.py IN.tsv OUT.tsv [--line folio,line] [--sign sign] [--value value] [--grade grade] [--filter col=prefix]
       [--keys K1.tsv,K2.tsv --key-out KEY.tsv]  (merge key files, first wins, nulls blanked)
"""
import argparse, csv, sys
ap = argparse.ArgumentParser()
ap.add_argument('inp'); ap.add_argument('out')
ap.add_argument('--line', default='line'); ap.add_argument('--sign', default='sign')
ap.add_argument('--value', default='value'); ap.add_argument('--grade', default='grade')
ap.add_argument('--filter', action='append', default=[])
ap.add_argument('--null', default='NULL,null,nulle,Null,NUL,nul')
ap.add_argument('--keys'); ap.add_argument('--key-out')
ap.add_argument('--drop-grade', default='', help='comma list of grades (e.g. clear) dropped; each dropped row starts a new segment in the line id')
a = ap.parse_args()
nulls = set(a.null.split(','))
rows = [r for r in csv.reader(open(a.inp, encoding='utf-8'), delimiter='\t') if r and not r[0].startswith('#')]
hdr = [h.strip().lower() for h in rows[0]]
ix = lambda n: hdr.index(n.lower())
lc = [ix(c) for c in a.line.split(',')]
flt = [(ix(f.split('=')[0]), f.split('=', 1)[1]) for f in a.filter]
n = 0
drop = set(filter(None, a.drop_grade.split(','))); seg = 0
with open(a.out, 'w', encoding='utf-8') as f:
    f.write('line\tpos\tsign\tconf\tvalue\tgrade\n')
    for r in rows[1:]:
        r = r + [''] * (len(hdr) - len(r))
        if any(not r[c].startswith(p) for c, p in flt):
            continue
        if r[ix(a.grade)].strip() in drop:
            seg += 1
            continue
        v = r[ix(a.value)]
        v = '' if v.strip() in nulls else v
        f.write('\t'.join(['.'.join(r[c] for c in lc) + (f'.s{seg:03d}' if drop else ''), str(n), r[ix(a.sign)], '', v, r[ix(a.grade)].strip()]) + '\n'); n += 1
if a.keys:
    seen = {}
    for p in a.keys.split(','):
        for i, r in enumerate(csv.reader(open(p, encoding='utf-8'), delimiter='\t')):
            if i == 0 or len(r) < 2 or r[0].startswith('#') or r[0] in seen:
                continue
            seen[r[0]] = '' if r[1].strip() in nulls else r[1]
    with open(a.key_out, 'w', encoding='utf-8') as f:
        f.write('code\tvalue\n' + ''.join(f'{k}\t{v}\n' for k, v in seen.items()))
print(f'{n} tokens -> {a.out}', file=sys.stderr)
