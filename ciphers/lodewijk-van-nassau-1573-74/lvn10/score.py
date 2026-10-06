#!/usr/bin/env python3
"""R12-LVN10: align blind 300-dpi passes A4/B4 (22 physical-line crops of WVO 4610 p3) to the numeral rows of
lvn10/ciphertext_4610_pre.tsv p3_L12-p3_L31 as one page sequence (clear '=' rows and '|' tokens dropped; the
transcription's line breaks do not follow the physical lines), score the pre-registered H-row control
(lvn10/PREREG.md), list target-row reads. Writes lvn10/aligned.tsv. Offline."""
import csv, difflib, os
H = os.path.dirname(os.path.abspath(__file__))
ct = [r for r in csv.DictReader(open(os.path.join(H, 'ciphertext_4610_pre.tsv')), delimiter='\t')
      if 'p3_L12' <= r['line'] <= 'p3_L31' and not r['sign'].startswith('=')]
def load(n):
    return [r['token'].strip() for r in csv.DictReader(open(os.path.join(H, n)), delimiter='\t')
            if r['token'].strip() not in ('|', '')]
P = {'A4': load('passA4.tsv'), 'B4': load('passB4.tsv')}
tg = {(r['line'], r['position']) for r in csv.DictReader(open(os.path.join(H, 'targets.tsv')), delimiter='\t')}
sig = [r['sign'] for r in ct]
reads = {}
for k, toks in P.items():
    m = {}
    key = [t.rstrip('?') for t in toks]
    sm = difflib.SequenceMatcher(None, sig, key, autojunk=False)
    for op, a0, a1, b0, b1 in sm.get_opcodes():
        if op == 'equal' or (op == 'replace' and a1 - a0 == b1 - b0):
            for j in range(a1 - a0): m[a0 + j] = toks[b0 + j]
    reads[k] = m
out = []; ctl = {k: [0, 0] for k in P}
for j, r in enumerate(ct):
    a, b = reads['A4'].get(j, '-'), reads['B4'].get(j, '-')
    is_t = (r['line'], r['position']) in tg
    if not is_t and r['confidence'] == 'H':
        for k, v in (('A4', a), ('B4', b)):
            ctl[k][1] += 1; ctl[k][0] += (v == r['sign'])
    out.append([r['line'], r['position'], r['sign'], r['confidence'], r['alt'], a, b,
                'target' if is_t else 'control' if r['confidence'] == 'H' else ''])
with open(os.path.join(H, 'aligned.tsv'), 'w') as f:
    f.write('line\tposition\tsign\tconfidence\talt\tA4\tB4\trole\n')
    for o in out: f.write('\t'.join(o) + '\n')
for k, (c, n) in ctl.items(): print('control %s: %d/%d = %.3f (gate 0.90)' % (k, c, n, c / n))
