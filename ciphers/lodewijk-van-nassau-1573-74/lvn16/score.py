#!/usr/bin/env python3
"""R12-LVN16: align blind 300-dpi passes A3/B3 to ciphertext_4616.tsv (p1_L05-L17 = crop L01-L13), score the
pre-registered H-row control (lvn16/PREREG.md), list target-row reads. Writes lvn16/aligned.tsv. Offline."""
import csv, difflib, os
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
ct = list(csv.DictReader(open(os.path.join(T, 'ciphertext_4616.tsv')), delimiter='\t'))
def load(n):
    d = {}
    for r in csv.DictReader(open(os.path.join(H, n)), delimiter='\t'):
        d.setdefault(r['line'], []).append(r['token'].strip())
    return d
P = {'A3': load('passA3.tsv'), 'B3': load('passB3.tsv')}
tg = {(r['line'], r['position']) for r in csv.DictReader(open(os.path.join(H, 'targets.tsv')), delimiter='\t')}
out = []; ctl = {k: [0, 0] for k in P}
for i in range(13):
    ln = 'p1_L%02d' % (i + 5); cl = 'L%02d' % (i + 1)
    rows = [r for r in ct if r['line'] == ln]
    sig = [r['sign'] for r in rows]
    reads = {}
    for k, d in P.items():
        toks = d.get(cl, [])
        m = {}
        sm = difflib.SequenceMatcher(None, sig, toks, autojunk=False)
        for op, a0, a1, b0, b1 in sm.get_opcodes():
            if op == 'equal' or (op == 'replace' and a1 - a0 == b1 - b0):
                for j in range(a1 - a0): m[a0 + j] = toks[b0 + j]
            elif op == 'replace':  # unequal block: map 1:1 from the left, rest unaligned
                for j in range(min(a1 - a0, b1 - b0)): m[a0 + j] = toks[b0 + j] + '~'
        reads[k] = m
    for j, r in enumerate(rows):
        a, b = reads['A3'].get(j, '-'), reads['B3'].get(j, '-')
        is_t = (ln, r['position']) in tg
        if not is_t and r['confidence'] == 'H':
            for k, v in (('A3', a), ('B3', b)):
                ctl[k][1] += 1; ctl[k][0] += (v == r['sign'])
        out.append([ln, r['position'], r['sign'], r['confidence'], r['alt'], a, b, 'target' if is_t else 'control' if r['confidence'] == 'H' else ''])
with open(os.path.join(H, 'aligned.tsv'), 'w') as f:
    f.write('line\tposition\tsign\tconfidence\talt\tA3\tB3\trole\n')
    for o in out: f.write('\t'.join(o) + '\n')
for k, (c, n) in ctl.items(): print('control %s: %d/%d = %.3f (gate 0.90)' % (k, c, n, c / n))
