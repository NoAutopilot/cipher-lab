#!/usr/bin/env python3
"""TXE3-6 UNIT step 2: the frozen exemplar labels (PREREG-txeng3-6.md 'Classifier'). Round 0: a TRAIN line whose
sign-unit (seg/sign) box count equals its truth position count is labelled 1:1 in order; scored position -> ref_sign if in
the truth set else the truth set's first member; excluded position -> ref_sign if it is a key code, else dropped.
Writes labels_train.tsv (box, code) and labels_report.txt. Test lines are never read here."""
import csv, collections, os
ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(ROOT, '..', '..', '..'))
from seg import TRAIN, TRUTH
key = {r['code'] for r in csv.DictReader(open(os.path.join(REPO, 'ciphers/fr16104-vivonne-spain-1572/key.tsv')), delimiter='\t')}
truth = collections.defaultdict(list)
for r in csv.DictReader((l for l in open(TRUTH) if not l.startswith('#')), delimiter='\t'):
    truth[r['line'].split('_')[1]].append(r)
boxes = collections.defaultdict(list)
for r in csv.DictReader(open(os.path.join(ROOT, 'seg/sign/boxes.tsv')), delimiter='\t'):
    boxes[r['line'].split('_')[1]].append(r)
lab, rep = [], []
for ln in TRAIN:
    t, b = truth[ln], sorted(boxes[ln], key=lambda r: int(r['pos']))
    if len(t) != len(b):
        rep.append(f'{ln}: boxes {len(b)} truth {len(t)} -> skipped (round 0)')
        continue
    n = 0
    for tr, bx in zip(t, b):
        ts = tr['truth'].split('|') if tr['truth'] else []
        if tr['status'] == 'scored':
            code = tr['ref_sign'] if tr['ref_sign'] in ts else ts[0]
        elif tr['ref_sign'] in key:
            code = tr['ref_sign']
        else:
            continue
        lab.append((bx['sid'], code)); n += 1
    rep.append(f'{ln}: boxes {len(b)} = truth {len(t)} -> {n} labelled')
with open(os.path.join(ROOT, 'labels_train.tsv'), 'w') as f:
    f.write('box\tcode\n')
    for s, c in lab:
        f.write(f'{s}\t{c}\n')
cnt = collections.Counter(c for _, c in lab)
rep.append(f'TOTAL labelled boxes {len(lab)} on {sum("labelled" in r for r in rep)} train lines; codes {len(cnt)}: ' + ', '.join(f'{c}:{n}' for c, n in cnt.most_common()))
open(os.path.join(ROOT, 'labels_report.txt'), 'w').write('\n'.join(rep) + '\n')
print('\n'.join(rep))
