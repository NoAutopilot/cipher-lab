#!/usr/bin/env python3
"""A1-BIR-EYE (3 Oct 2026): fix the changed and decoy positions and each position's two candidates before any crop is
shown (PREREG.md beside this). Run from this folder: python3 prereg_positions.py  -> positions.tsv (with the hidden
truth column `kind`/`key_side`) and blind_<leaf>.tsv (what the reader gets: id, passage, pos, A, B; no kind)."""
import csv, random
LEAVES = ['f117', 'f168', 'f144r']
rows_out = []
for L in LEAVES:
    dec = list(csv.DictReader(open(f'../{L}_lam4.decode.tsv'), delimiter='\t'))
    lat = {}
    for r in csv.DictReader(open(f'../{L}_topk.tsv'), delimiter='\t'):
        lat.setdefault((r['line'], r['pos']), []).append((float(r['score']), r['cand']))
    changed = [r for r in dec if r['changed'] == '1']
    pool = []
    for r in dec:
        if r['changed'] == '1':
            continue
        c = [x for _, x in sorted(lat[(r['line'], r['pos'])], reverse=True) if x != r['top1']]
        if c:
            pool.append((r, c[0]))
    rng = random.Random(20261003)
    decoys = rng.sample(pool, len(changed))
    items = [(r, 'changed', r['chosen']) for r in changed] + [(r, 'decoy', alt) for r, alt in decoys]
    rng.shuffle(items)
    for i, (r, kind, alt) in enumerate(items, 1):
        pair = [r['top1'], alt]; rng.shuffle(pair)
        rows_out.append(dict(leaf=L, qid=f'{L}-{i:02d}', passage=r['line'], pos=r['pos'], A=pair[0], B=pair[1],
                             kind=kind, original=r['top1'], other=alt))
with open('positions.tsv', 'w') as f:
    w = csv.DictWriter(f, list(rows_out[0]), delimiter='\t'); w.writeheader(); w.writerows(rows_out)
for L in LEAVES:
    with open(f'blind_{L}.tsv', 'w') as f:
        f.write('qid\tpassage\tpos\tA\tB\n')
        for r in rows_out:
            if r['leaf'] == L:
                f.write(f"{r['qid']}\t{r['passage']}\t{r['pos']}\t{r['A']}\t{r['B']}\n")
    print(L, sum(r['leaf'] == L and r['kind'] == 'changed' for r in rows_out), 'changed +',
          sum(r['leaf'] == L and r['kind'] == 'decoy' for r in rows_out), 'decoys')

# orientation: the lattice top-1 label sequence per passage, every question position masked as [qid]
for L in LEAVES:
    dec = list(csv.DictReader(open(f'../{L}_lam4.decode.tsv'), delimiter='\t'))
    q = {(r['passage'], r['pos']): r['qid'] for r in rows_out if r['leaf'] == L}
    with open(f'orient_{L}.txt', 'w') as f:
        cur = None
        for r in dec:
            if r['line'] != cur:
                f.write(('\n' if cur else '') + r['line'] + ':'); cur = r['line']
            k = (r['line'], r['pos'])
            f.write(' ' + (f'[{q[k]}]' if k in q else r['top1']))
        f.write('\n')
