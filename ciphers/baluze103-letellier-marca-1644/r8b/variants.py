#!/usr/bin/env python3
"""R8-BAL103B: write the three ciphertext variants judged in r8b/PREREG.md, each a full ciphertext.tsv copy in a scratch folder
(r8b/v_pre, r8b/v_r8, r8b/v_look; scratch, deleted after the run -- rerun to regenerate): pre-R8 (R8's 10 corrections undone), R8 (as committed), look-alike (pre-R8 + r8b/passD.tsv's
relabels; old sign kept in alt as 'r8b old=..', why 'r8b-lookalike', grade M)."""
import os, shutil, csv
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
hdr, *rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(T, 'ciphertext.tsv'))]
for r in rows:   # after r8b/revert_r8.py: rebuild the R8 state from 'r8 tried=X' so this script reproduces all three variants
    if r[5] == 'r8-reverted':
        x = r[4].split('r8 tried=')[1].split()[0]; r[4] = r[4].replace(f'r8 tried={x}', f'r8 old={r[2]}'); r[2] = x; r[5] = 'r8-2of3'
D = {(r['passage'], r['pos']): r for r in csv.DictReader(open(os.path.join(H, 'passD.tsv')), delimiter='\t')}
def pre(r):
    r = list(r)
    if r[5] == 'r8-2of3':
        r[2] = r[4].split('r8 old=')[1].split()[0]; r[4] = r[4].split(' r8 old=')[0] if ' r8 old=' in r[4] else ''; r[5] = 'pre-r8'; r[3] = 'M'
    return r
V = {'v_r8': [list(r) for r in rows], 'v_pre': [pre(r) for r in rows], 'v_look': []}
for r in V['v_pre']:
    r = list(r); d = D[(r[0], r[1])]
    if d['sign_id'] != r[2]:
        r[4] = (r[4] + ' ' if r[4] else '') + f'r8b old={r[2]}'; r[2] = d['sign_id']; r[3] = 'M'; r[5] = 'r8b-lookalike'
    V['v_look'].append(r)
for k, rs in V.items():
    d = os.path.join(H, k); os.makedirs(d, exist_ok=True)
    for f in ('decode.json', 'key_decode.tsv', 'key.tsv'): shutil.copy(os.path.join(T, f), d)
    open(os.path.join(d, 'ciphertext.tsv'), 'w').write('\t'.join(hdr) + '\n' + ''.join('\t'.join(r) + '\n' for r in rs))
    print(k, sum(a[2] != b[2] for a, b in zip(rs, V['v_pre'])), 'signs differ from pre-R8')
