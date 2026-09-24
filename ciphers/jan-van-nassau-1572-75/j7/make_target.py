#!/usr/bin/env python3
"""J7 (24 Sept 2026): write the 5549 body (runs 1-61) in nomenclator_anneal's format, j7/body_5549.txt.
Tokens from ciphertext_5549.tsv (J5I image-checked; roman groups left out); in-run clear fragments as {..};
frames = Groen's clear text next to each run (groen/groen_5549.tsv left/right, cut at the nearest numeral)."""
import csv, os, re
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
g = list(csv.DictReader(open(os.path.join(T, 'groen', 'groen_5549.tsv')), delimiter='\t'))
c = [r for r in csv.DictReader(open(os.path.join(T, 'ciphertext_5549.tsv')), delimiter='\t') if not r['run'].startswith('PS')]
left, right = {}, {}
for r in g:
    if r['left'] and r['run'] not in left:
        left[r['run']] = re.split(r'\d+\.?', r['left'])[-1].strip()
    if r['right']:
        right[r['run']] = re.split(r'\d', r['right'])[0].strip()
out, runs = [], []
for r in c:
    if not runs or runs[-1][0] != r['run']:
        runs.append((r['run'], []))
    runs[-1][1].append(r)
for run, toks in runs:
    parts = ['{' + left.get(run, '') + '}']
    for r in toks:
        if r['kind'] == 'num':
            parts.append(r['token'])
        elif r['kind'] == 'clear':
            parts.append('{' + r['token'] + '}')
    parts.append('{' + right.get(run, '') + '}')
    out.append(f'# run {run}\n' + ' '.join(parts))
open(os.path.join(H, 'body_5549.txt'), 'w').write('# 5549 body runs 1-61, J7 24 Sept 2026, from ciphertext_5549.tsv + groen frames\n' + '\n'.join(out) + '\n')
print(len(runs), 'runs', sum(1 for r in c if r['kind'] == 'num'), 'numerals')
