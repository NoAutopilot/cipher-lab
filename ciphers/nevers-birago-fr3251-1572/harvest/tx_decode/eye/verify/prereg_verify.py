#!/usr/bin/env python3
"""A1-BIR-VERIFY (3 Oct 2026): verifier's question sets, fixed before any crop is shown. Run from this folder:
python3 prereg_verify.py -> vpositions.tsv (hidden truth) and vblind_<leaf>.tsv / vorient_<leaf>.txt (reader files).
Per leaf: the A1-BIR-EYE changed + decoy questions unchanged (same positions, same A/B order; arm 'orig') plus an
ambiguity-matched decoy arm ('mdecoy'): every unused unchanged position whose lattice alt/top1 score ratio >= 0.3,
seeded sample capped at the leaf's changed count. Questions renumbered and reshuffled (seed 20261003+1) so the reader
cannot map them to A1-BIR-EYE's qids."""
import csv, random
EYE = '..'; LEAVES = ['f117', 'f168', 'f144r']; THR = 0.3
pos = list(csv.DictReader(open(f'{EYE}/positions.tsv'), delimiter='\t'))
rng = random.Random(20261004)
out = []
for L in LEAVES:
    lat = {}
    for r in csv.DictReader(open(f'../../{L}_topk.tsv'), delimiter='\t'):
        lat.setdefault((r['line'], r['pos']), {})[r['cand']] = float(r['score'])
    dec = list(csv.DictReader(open(f'../../{L}_lam4.decode.tsv'), delimiter='\t'))
    mine = [p for p in pos if p['leaf'] == L]
    used = {(p['passage'], p['pos']) for p in mine}
    items = []
    for p in mine:
        d = lat[(p['passage'], p['pos'])]
        items.append(dict(arm='orig', kind=p['kind'], passage=p['passage'], pos=p['pos'], A=p['A'], B=p['B'],
                          original=p['original'], other=p['other'], ratio=round(d.get(p['other'], 0) / d[p['original']], 4),
                          eye_qid=p['qid']))
    pool = []
    for r in dec:
        k = (r['line'], r['pos'])
        if r['changed'] == '1' or k in used:
            continue
        alt = sorted(((s, c) for c, s in lat[k].items() if c != r['top1']), reverse=True)
        if alt and alt[0][0] / lat[k][r['top1']] >= THR:
            pool.append((r, alt[0][1], alt[0][0] / lat[k][r['top1']]))
    n = sum(p['kind'] == 'changed' for p in mine)
    for r, alt, ratio in rng.sample(pool, min(n, len(pool))):
        pair = [r['top1'], alt]; rng.shuffle(pair)
        items.append(dict(arm='mdecoy', kind='mdecoy', passage=r['line'], pos=r['pos'], A=pair[0], B=pair[1],
                          original=r['top1'], other=alt, ratio=round(ratio, 4), eye_qid=''))
    rng.shuffle(items)
    for i, it in enumerate(items, 1):
        it.update(leaf=L, qid=f'v{L}-{i:02d}'); out.append(it)
    print(L, {k: sum(it['kind'] == k for it in items) for k in ('changed', 'decoy', 'mdecoy')})
cols = ['leaf', 'qid', 'arm', 'kind', 'passage', 'pos', 'A', 'B', 'original', 'other', 'ratio', 'eye_qid']
with open('vpositions.tsv', 'w') as f:
    w = csv.DictWriter(f, cols, delimiter='\t'); w.writeheader(); w.writerows(out)
for L in LEAVES:
    with open(f'vblind_{L}.tsv', 'w') as f:
        f.write('qid\tpassage\tpos\tA\tB\n')
        for r in out:
            if r['leaf'] == L:
                f.write(f"{r['qid']}\t{r['passage']}\t{r['pos']}\t{r['A']}\t{r['B']}\n")
    dec = list(csv.DictReader(open(f'../../{L}_lam4.decode.tsv'), delimiter='\t'))
    q = {(r['passage'], r['pos']): r['qid'] for r in out if r['leaf'] == L}
    with open(f'vorient_{L}.txt', 'w') as f:
        cur = None
        for r in dec:
            if r['line'] != cur:
                f.write(('\n' if cur else '') + r['line'] + ':'); cur = r['line']
            k = (r['line'], r['pos'])
            f.write(' ' + (f'[{q[k]}]' if k in q else r['top1']))
        f.write('\n')
