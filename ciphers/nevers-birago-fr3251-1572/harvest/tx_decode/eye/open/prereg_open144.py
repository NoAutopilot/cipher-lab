#!/usr/bin/env python3
"""BIR-OPEN-144 (3 Oct 2026, account-3 worker): prereg_open.py unchanged except leaf = f144r only (PREREG-OPEN-144.md).
Run from this folder: python3 prereg_open144.py -> opositions_f144r.tsv (hidden truth), oblind_f144r.tsv, oorient_f144r.txt.
Original docstring follows (f117/f168 there read f144r here; one reader part, all lines).
Per leaf (f117 = f.117r, f168 = f.168), PREREG-OPEN.md:
  * targets = every token graded M in ../verify/reading_<leaf>_verify_tokens.tsv (f117 74, f168 22);
  * H decoys = the same number of tokens graded S with transcription conf H that are not A1-BIR-VERIFY exceptions,
    ambiguity-matched: for each target, an unused decoy with the same top-1 sign if one exists (the one with the highest
    lattice alt/top-1 ratio in r2_<leaf>_topk... H rows carry one candidate there, so the TX-DECODE lattice ../../<leaf>_topk.tsv
    is used for the ratio), else the unused H position with the highest ratio; ties broken by seeded shuffle (seed 20261006).
  * reader parts: f117 L01-L05 (part f117a), f117 L06-L10 (f117b), f168 (f168). Each part's orient file shows the top-1
    sign at every position except the part's questions (targets and decoys alike), which are masked [qid]. The reader is
    never shown the current sign at a question position. Lines differ between parts, so nothing asked in one is shown in another."""
import csv, random
rng = random.Random(20261006)
T = '../../'
PARTS = {'f144r': [('f144r', None)]}
rows = []
for L, parts in PARTS.items():
    tok = list(csv.DictReader(open(f'../verify/reading_{L}_verify_tokens.tsv'), delimiter='\t'))
    exc = {(r['line'], r['pos']) for r in csv.DictReader(open(f'../verify/exceptions_{L}.tsv'), delimiter='\t')}
    lat = {}
    for r in csv.DictReader(open(T + L + '_topk.tsv'), delimiter='\t'):
        lat.setdefault((r['line'], r['pos']), {})[r['cand']] = float(r['score'])
    def ratio(k, s):
        c = lat.get(k, {}); alt = [v for a, v in c.items() if a != s]
        return max(alt) / c[s] if alt and c.get(s) else 0.0
    targets = [r for r in tok if r['grade'] == 'M']
    pool = [r for r in tok if r['grade'] == 'S' and r['conf'] == 'H' and (r['line'], r['pos']) not in exc]
    rng.shuffle(pool); pool.sort(key=lambda r: -ratio((r['line'], r['pos']), r['sign']))
    used = set(); dec = []
    for t in targets:
        same = [r for r in pool if r['sign'] == t['sign'] and id(r) not in used]
        pick = (same or [r for r in pool if id(r) not in used])[0]
        used.add(id(pick)); dec.append(pick)
    items = [dict(leaf=L, kind='target', passage=r['line'], pos=r['pos'], current=r['sign'], conf=r['conf'],
                  ratio=round(ratio((r['line'], r['pos']), r['sign']), 4)) for r in targets]
    items += [dict(leaf=L, kind='hdecoy', passage=r['line'], pos=r['pos'], current=r['sign'], conf=r['conf'],
                   ratio=round(ratio((r['line'], r['pos']), r['sign']), 4)) for r in dec]
    for part, lines in parts:
        its = [it for it in items if lines is None or it['passage'] in lines]
        rng.shuffle(its)
        for i, it in enumerate(its, 1):
            it.update(part=part, qid=f'o{part}-{i:02d}'); rows.append(it)
        q = {(it['passage'], it['pos']): it['qid'] for it in its}
        with open(f'oblind_{part}.tsv', 'w') as f:
            f.write('qid\tpassage\tpos\tanswer\tconf\tnote\n')
            for it in sorted(its, key=lambda it: it['qid']):
                f.write(f"{it['qid']}\t{it['passage']}\t{it['pos']}\t\t\t\n")
        with open(f'oorient_{part}.txt', 'w') as f:
            cur = None
            for r in tok:
                if lines is not None and r['line'] not in lines:
                    continue
                if r['line'] != cur:
                    f.write(('\n' if cur else '') + r['line'] + ':'); cur = r['line']
                k = (r['line'], r['pos']); f.write(' ' + (f'[{q[k]}]' if k in q else r['sign']))
            f.write('\n')
        print(part, 'targets', sum(it['kind'] == 'target' for it in its), 'hdecoys', sum(it['kind'] == 'hdecoy' for it in its))
    print(L, 'decoys same-sign', sum(d['sign'] == t['sign'] for d, t in zip(dec, targets)), 'of', len(targets))
cols = ['leaf', 'part', 'qid', 'kind', 'passage', 'pos', 'current', 'conf', 'ratio']
with open('opositions_f144r.tsv', 'w') as f:
    w = csv.DictWriter(f, cols, delimiter='\t', extrasaction='ignore'); w.writeheader(); w.writerows(rows)
