#!/usr/bin/env python3
"""R9-COST (6 Oct 2026): apply the PREREG-R9-COST q split to the committed passes and report the numbers.
usage: python3 r9cost_apply.py <reads_dir>   (reads_dir holds r9cost_reads/out_{A,B}_p{1,2,4}.tsv)
Mapping (prereg): the k-th split answer in a crop goes to the k-th `q` of an earlier pass's read only if the reader's count equals that
pass's q count; a token becomes q1 (F1 closed) / q2 (F1 open) only when both split passes give the same F1; otherwise it stays `q`.
Writes r9cost_passA.tsv, r9cost_passB.tsv (P1+P2, for run_align.py) and r9cost_p4_pass{A,B}.tsv; prints F1/F2 tallies and per-page
C coverage (agreed AND C in key_n9cos2.tsv, difflib per crop for P1/P2)."""
import csv, collections, difflib, os, sys
H = os.path.dirname(os.path.abspath(__file__)); R = sys.argv[1]
def tsv(p): return list(csv.DictReader(open(p), delimiter='\t'))
split = {}
for t in 'AB':
    for p in '124':
        for r in tsv(os.path.join(R, f'out_{t}_p{p}.tsv')):
            f1 = [] if r['F1'] == '-' else r['F1'].split(','); f2 = [] if r['F2'] == '-' else r['F2'].split(',')
            split[(t, r['crop'])] = (int(r['n']), f1, f2)
f1c = collections.Counter(x for (_, _), (_, f1, _) in split.items() for x in f1)
f2c = collections.Counter(x for (_, _), (_, _, f2) in split.items() for x in f2)
print('F1 answers (both passes, all pages):', dict(f1c)); print('F2 answers:', dict(f2c))
same = [c for (t, c) in split if t == 'A' and ('B', c) in split and split[('A', c)][0] == split[('B', c)][0]]
f2agree = sum(a == b for c in same for a, b in zip(split[('A', c)][2], split[('B', c)][2]))
print(f'crops with equal split counts A/B: {len(same)} of {len({c for _, c in split})}; F2 agreeing positions there: {f2agree}/{sum(split[("A", c)][0] for c in same)}')
def label(crop, qcount, k):
    sa, sb = split.get(('A', crop)), split.get(('B', crop))
    if not sa or not sb or sa[0] != qcount or sb[0] != qcount: return 'q'
    a, b = sa[1][k], sb[1][k]
    return ('q1' if a == 'closed' else 'q2') if a == b else 'q'
def relabel(signs, crop):
    toks = [g.split('_') for g in (signs or '').split()]; n = sum(t == 'q' for g in toks for t in g); k = 0; out = []
    for g in toks:
        h = []
        for t in g:
            if t == 'q': h.append(label(crop, n, k)); k += 1
            else: h.append(t)
        out.append('_'.join(h))
    return ' '.join(out)
K = {r['sign']: r['grade'] for r in tsv(os.path.join(H, 'key_n9cos2.tsv'))}
labs = collections.Counter()
for t, src, dst in (('A', 'n9cos2_passA_W.tsv', 'r9cost_passA.tsv'), ('B', 'n9cos2_passB_W.tsv', 'r9cost_passB.tsv'),
                    ('A', 'r8cost_reads/passA.tsv', 'r9cost_p4_passA.tsv'), ('B', 'r8cost_reads/passB.tsv', 'r9cost_p4_passB.tsv')):
    rows = tsv(os.path.join(H, src)); f = rows and list(rows[0].keys())
    with open(os.path.join(H, dst), 'w') as o:
        w = csv.DictWriter(o, f, delimiter='\t', lineterminator='\n'); w.writeheader()
        for r in rows:
            c = r['crop'] if r['crop'].startswith('p') else 'p4_' + r['crop']
            r['signs'] = relabel(r['signs'], c); w.writerow(r)
            labs.update((t, x) for g in r['signs'].split() for x in g.split('_') if x in ('q', 'q1', 'q2'))
print('labels after split:', dict(sorted(labs.items())))
# per-page C coverage on P1/P2 group crops (same rule as r8cost_score.py: agreed AND C; splits/indels count as positions)
A = {r['crop']: r['signs'] for r in tsv(os.path.join(H, 'r9cost_passA.tsv'))}; B = {r['crop']: r['signs'] for r in tsv(os.path.join(H, 'r9cost_passB.tsv'))}
pg = collections.defaultdict(lambda: [0, 0])
for c in sorted(set(A) | set(B)):
    sa = [x for g in A.get(c, '').split() for x in g.split('_') if x and x not in '.,:;/|-']
    sb = [x for g in B.get(c, '').split() for x in g.split('_') if x and x not in '.,:;/|-']
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, sa, sb, autojunk=False).get_opcodes():
        if op == 'equal':
            for s in sa[i1:i2]: pg[c[:2]][0] += 1; pg[c[:2]][1] += K.get(s) == 'C'
        else: pg[c[:2]][0] += max(i2 - i1, j2 - j1)
for p, (tot, cov) in sorted(pg.items()): print(f'{p} C coverage {cov}/{tot} = {cov / tot:.3f}')
