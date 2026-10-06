#!/usr/bin/env python3
"""D4-15576: pairs.tsv (gloss G_n over cipher C_n) from gloss_reconciled.tsv + ciphertext_body.tsv.
Marks above groups (¨ ² ^ +) and a trailing '.' are dropped from the value for the alignment only.
--check exits 1 if the committed pairs.tsv differs."""
import csv, sys, os
H = os.path.dirname(os.path.abspath(__file__))
g = {r['line'][1:]: r['gloss'] for r in csv.DictReader(open(os.path.join(H, 'gloss_reconciled.tsv')), delimiter='\t')}
rows = ['plain_line\tplain_raw\tcipher_line\tcipher_raw']
for r in csv.DictReader(open(os.path.join(H, 'ciphertext_body.tsv')), delimiter='\t'):
    n = r['line'][1:]
    toks = []
    for t in r['tokens'].split():
        c = t.lstrip('¨²^').rstrip('.')
        if c.startswith('+') and len(c) > 1:
            c = c[1:]
        toks.append(c)
    rows.append('G%s\t%s\tC%s\t%s' % (n, g[n], n, ' '.join(toks)))
out = '\n'.join(rows) + '\n'
# decode inputs for tools/decode_key.py: long-format ciphertext (unsettled '?' groups conf M) and the
# alignment key with every value graded M (the pre-registered gate FAILed; PREREG-D4-15576.md, NOTES.md D4-15576)
lng = ['line\tpos\ttoken\tconf']
for r in rows[1:]:
    f = r.split('\t')
    for i, t in enumerate(f[3].split()):
        lng.append('%s\t%d\t%s\t%s' % (f[2], i + 1, t if t[0].isdigit() else 'w:' + t, 'M' if '?' in t else 'H'))
key = ['code\tvalue\tgrade\tnote']
kp = os.path.join(H, 'key_f15576.tsv')
if os.path.exists(kp):
    for r in csv.DictReader(open(kp), delimiter='\t'):
        key.append('%s\t%s\tM\tgloss alignment top chunk, n %s, agree %s; gate FAIL' % (r['value'], r['meaning'], r['n'], r['agree']))
files = {'pairs.tsv': out, 'ciphertext_long.tsv': '\n'.join(lng) + '\n', 'key_decode.tsv': '\n'.join(key) + '\n'}
if '--check' in sys.argv:
    sys.exit(0 if all(open(os.path.join(H, k)).read() == v for k, v in files.items()) else 1)
for k, v in files.items():
    open(os.path.join(H, k), 'w').write(v)
print('wrote', ', '.join(files), len(rows) - 1, 'pairs')
