#!/usr/bin/env python3
"""GAPS11 2 Oct 2026: apply the native-resolution blind pair (g11_passA.tsv, g11_passB.tsv, look on images/lines/g11/g11_reconcile_composite.jpg,
settled in g11_settled.tsv) to ciphertext.tsv, key.tsv and exceptions.tsv. Idempotent from the *_before_GAPS11.tsv snapshots.
A position changes only where both blind passes agree (and the look, where one was taken, agrees); see g11_settled.tsv class column."""
import csv, os
IP = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(os.path.dirname(IP))
def rd(p):
    with open(p, encoding='utf-8') as f: return list(csv.DictReader(f, delimiter='\t'))
def wr(p, rows, hdr):
    with open(p, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=hdr, delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(rows)
G = 'GAPS11 2 Oct 2026 native-resolution blind pair (body/image_pass/g11_settled.tsv): '
ct = rd(os.path.join(IP, 'ciphertext_before_GAPS11.tsv')); h = list(ct[0].keys())
for r in ct:
    k = (r['line'], r['pos'])
    if k == ('L01', '6'): r['conf'] = 'H'; r['gloss'] = '23.'
    if k == ('L09', '0'): r['group'] = '[L]'
    if k == ('L10', '0'): r['group'] = '[curl]'
    if k == ('L12', '2'): r['gloss'] = 'l'
    if k == ('L14', '10'): r['gloss'] = 't'
wr(os.path.join(T, 'ciphertext.tsv'), ct, h)
ky = rd(os.path.join(IP, 'key_before_GAPS11.tsv')); h = list(ky[0].keys())
for r in ky:
    if r['code'] == '18': r['grade'] = 'C'; r['note'] += ' | ' + G + 'L04 pos0 read 18 under gloss g by both passes -> C | was: g M'
    if r['code'] == '58': r['value'] = 'l'; r['note'] += ' | ' + G + 'both passes and the look read a tall looped l over 58 at L12 pos2 (not j/i); value -> l, still M (single occurrence; sense wanted c) | was: i M'
    if r['code'] == '20': r['note'] += ' | ' + G + 'no occurrence left: L09 pos0 is an L-shaped looped symbol, not 20 (both passes, as GAPS10)'
    if r['code'] == ')3': r['note'] += ' | ' + G + 'L14 pos10 gloss t confirmed (both passes + look; the old o was a one-place slip), L05 pos1 split e/t (look t); held M, L14 by exception at C'
    if r['code'] == '36': r['note'] += ' | ' + G + 'gloss over 36: L04 e, L06 c, L14 e (both passes each), L10 c/e split; c and e look alike in the gloss hand; stays M'
wr(os.path.join(T, 'key.tsv'), ky, h)
ex = rd(os.path.join(IP, 'exceptions_before_GAPS11.tsv')); h = list(ex[0].keys())
for r in ex:
    if (r['line'], r['pos']) == ('L06', '17'): r['grade'] = 'C'; r['reason'] += ' | ' + G + 'both native-resolution passes read s again (four blind reads s vs the one VX-RD01 r) -> C'
    if (r['line'], r['pos']) == ('L10', '0'): r['reason'] += ' | ' + G + 'the group is a curl/tilde symbol with a dot in its loop, not )2 (both passes); NULL kept M'
have = {(r['line'], r['pos']) for r in ex}
if ('L14', '10') not in have:
    ex.append({'line': 'L14', 'pos': '10', 'value': 't', 'grade': 'C', 'reason': G + 'gloss t over )3 read by both passes and the look (key )3 is M on one settled occurrence)'})
if ('L09', '0') not in have:
    ex.append({'line': 'L09', 'pos': '0', 'value': 'a', 'grade': 'M', 'reason': G + 'group is an L-shaped looped symbol, not 20 (both passes); gloss A (pass A) or a flourish (pass B); a kept at M'})
wr(os.path.join(T, 'exceptions.tsv'), ex, h)
print('applied: ciphertext %d rows, key %d, exceptions %d' % (len(ct), len(ky), len(ex)))
