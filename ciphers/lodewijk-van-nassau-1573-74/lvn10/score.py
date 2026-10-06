#!/usr/bin/env python3
"""R12-LVN10: align blind 300-dpi passes A4/B4 (22 physical-line crops of WVO 4610 p3) to the numeral rows of
lvn10/ciphertext_4610_pre.tsv p3_L12-p3_L31 as one page sequence (clear '=' rows and '|' tokens dropped; the
transcription's line breaks do not follow the physical lines), score the pre-registered H-row control
(lvn10/PREREG.md), list target-row reads. Writes lvn10/aligned.tsv. Offline."""
import csv, difflib, os, sys
H = os.path.dirname(os.path.abspath(__file__))
# --round b (R13-LVN10B, 6 Oct 2026, lvn10/PREREG_B.md): passes A5/B5 (each two 11-crop calls, concatenated) -> aligned_b.tsv
RB = '--round' in sys.argv and sys.argv[sys.argv.index('--round') + 1] == 'b'
PA, PB, ALN = ('A5', 'B5', 'aligned_b.tsv') if RB else ('A4', 'B4', 'aligned.tsv')
ct = [r for r in csv.DictReader(open(os.path.join(H, 'ciphertext_4610_pre.tsv')), delimiter='\t')
      if 'p3_L12' <= r['line'] <= 'p3_L31' and not r['sign'].startswith('=')]
def load(n):
    return [r['token'].strip() for r in csv.DictReader(open(os.path.join(H, n)), delimiter='\t')
            if r['token'].strip() not in ('|', '')]
P = {PA: load('pass%s.tsv' % PA), PB: load('pass%s.tsv' % PB)}
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
    a, b = reads[PA].get(j, '-'), reads[PB].get(j, '-')
    is_t = (r['line'], r['position']) in tg
    if not is_t and r['confidence'] == 'H':
        for k, v in ((PA, a), (PB, b)):
            ctl[k][1] += 1; ctl[k][0] += (v == r['sign'])
    out.append([r['line'], r['position'], r['sign'], r['confidence'], r['alt'], a, b,
                'target' if is_t else 'control' if r['confidence'] == 'H' else ''])
with open(os.path.join(H, ALN), 'w') as f:
    f.write('line\tposition\tsign\tconfidence\talt\t%s\t%s\trole\n' % (PA, PB))
    for o in out: f.write('\t'.join(o) + '\n')
for k, (c, n) in ctl.items(): print('control %s: %d/%d = %.3f (gate 0.90)' % (k, c, n, c / n))
