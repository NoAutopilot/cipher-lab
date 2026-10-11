#!/usr/bin/env python3
"""TXE3-7 PROPAGATE step 1: the training-label TSVs (box, code) for the arms of benchmark-tx/PREREG-txeng3-7.md.
owner.tsv  = settled_corrected.tsv new_sign (the owner's final pile, family suffix stripped) on the 445 tiles that map 1:1 to an
             atlas box (sorter/no87/owner_map.tsv);  machine.tsv = the same boxes with old_sign (the start pile, the reconciled
             machine read); null_<seed>.tsv = owner codes permuted among the same boxes (seeds 1-20).
Run from the repo root: python3 benchmark-tx/txeng3/7/make_labels.py"""
import csv, os, random, collections, json
B = 'ciphers/nevers-birago-fr3251-1572'; W = 'benchmark-tx/txeng3/7/labels'
fam = lambda s: s.split('-')[0]
lab = {r['sid']: r for r in csv.DictReader(open(f'{B}/harvest/bir87align/settled_corrected.tsv'), delimiter='\t')}
m = {r['sid']: r for r in csv.DictReader(open(f'{B}/sorter/no87/owner_map.tsv'), delimiter='\t')}
rows = []
drop = collections.Counter()
for sid, r in lab.items():
    mm = m.get(sid)
    if not mm or not mm['box'] or mm['dup'] == '1':
        drop['no 1:1 box'] += 1; continue
    if r['status'] in ('aside', 'bad-cut') or not r['new_sign'] or not r['old_sign']:
        drop['aside/bad-cut/empty'] += 1; continue
    rows.append((mm['box'], fam(r['old_sign']), fam(r['new_sign']), r['status']))
rows.sort()
os.makedirs(W, exist_ok=True)
with open(f'{W}/owner.tsv', 'w') as f:
    f.write('box\tcode\n' + ''.join(f'{b}\t{n}\n' for b, o, n, s in rows))
with open(f'{W}/machine.tsv', 'w') as f:
    f.write('box\tcode\n' + ''.join(f'{b}\t{o}\n' for b, o, n, s in rows))
codes = [n for b, o, n, s in rows]
for seed in range(1, 21):
    rnd = random.Random(seed); p = codes[:]; rnd.shuffle(p)
    with open(f'{W}/null_{seed}.tsv', 'w') as f:
        f.write('box\tcode\n' + ''.join(f'{b}\t{c}\n' for (b, o, n, s), c in zip(rows, p)))
diff = sum(1 for b, o, n, s in rows if o != n)
info = dict(boxes=len(rows), dropped=dict(drop), owner_ne_machine=diff, moved=sum(1 for r in rows if r[3] == 'moved'),
            by_page=dict(collections.Counter(b.rsplit('_', 2)[0] for b, *_ in rows)),
            owner_codes=dict(collections.Counter(codes).most_common()), machine_codes=dict(collections.Counter(o for b, o, n, s in rows).most_common()))
json.dump(info, open(f'{W}/labels_info.json', 'w'), indent=1)
print(json.dumps({k: v for k, v in info.items() if k not in ('owner_codes', 'machine_codes')}))
