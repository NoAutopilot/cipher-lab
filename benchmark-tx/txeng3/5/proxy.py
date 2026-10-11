#!/usr/bin/env python3
"""TXE3-5 proxy for the two oracle hands without a tile pipeline (PREREG-txeng3-5 'Proxy' item 2): per-line box counts, machine vs
owner-corrected vs a reference count of units on the line, against 200 random-deletion controls. Count agreement is NOT accuracy."""
import csv, collections, random, statistics, re
O = 'benchmark-tx/txeng2/oracle1'
rd = lambda p: [r for r in csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t')]
boxes = rd(f'{O}/boxes/boxes_recut_all.tsv')
def run(hand, ans, ref, extra_drop=()):
    B = [b for b in boxes if b['hand'] == hand]
    settled = {r['sid']: r['status'] for r in rd(f'{O}/answers/{ans}/settled.tsv')}
    drop = {s for s, st in settled.items() if st in ('not-letter', 'aside')} | set(extra_drop)
    lines = sorted({b['line'] for b in B})
    mc = collections.Counter(b['line'] for b in B)
    oc = collections.Counter(b['line'] for b in B if b['box_id'] not in drop)
    stat = lambda c: sum(abs(c[l] - ref[l]) for l in lines)
    signed = lambda c: sum(c[l] - ref[l] for l in lines)
    rnd = random.Random(7); ctl = []
    ids = [b['box_id'] for b in B]
    for _ in range(200):
        d = set(rnd.sample(ids, len(drop))); ctl.append(stat(collections.Counter(b['line'] for b in B if b['box_id'] not in d)))
    print(f'## {hand}: {len(B)} machine boxes, owner removes {len(drop)} ({len(drop & set(settled))} settled not-letter/aside'
          f'{", " + str(len(set(extra_drop))) + " merge-absorbed" if extra_drop else ""}); reference units {sum(ref[l] for l in lines)}')
    print('| line | machine | owner | reference | machine-ref | owner-ref |'); print('|---|---|---|---|---|---|')
    for l in lines: print(f'| {l} | {mc[l]} | {oc[l]} | {ref[l]} | {mc[l]-ref[l]:+d} | {oc[l]-ref[l]:+d} |')
    print(f'sum|boxes-ref|: machine {stat(mc)}, owner {stat(oc)}; signed sum: machine {signed(mc):+d}, owner {signed(oc):+d}; '
          f'control (200 seeds, {len(drop)} random deletions) mean {statistics.mean(ctl):.1f} min {min(ctl)} max {max(ctl)}, '
          f'seeds <= owner: {sum(c <= stat(oc) for c in ctl)}/200\n')
# Vivonne: reference = truth positions per line (every status; = the committed read's tokens, marks included)
tv = rd('benchmark-tx/vivonne1573-f102r-dev.truth.tsv'); refv = collections.Counter(r['line'] for r in tv)
merges = rd(f'{O}/answers/vivonne/merges.tsv'); absorbed = [s for m in merges for s in m['absorbed'].split(',') if s]
run('vivonne1573-f102r', 'vivonne', refv, absorbed)
# Luzerne: reference = digits in the committed read per line (boxes are digits, truth positions are groups)
lz = rd('benchmark-tx/outputs/luzerne108a-p1/committed.tsv'); refl = collections.Counter()
odd = collections.Counter()
for r in lz:
    refl[r['line']] += sum(ch.isdigit() for ch in r['sign'])
    if not r['sign'].isdigit(): odd[r['sign']] += 1
print('luzerne committed non-digit tokens:', dict(odd))
run('luzerne108a-p1', 'luzerne', refl)
