#!/usr/bin/env python3
"""R8-PIS gl275: score the f.275v L17-L20 interlinear gloss alignment (gl275/gloss_align.tsv) against the committed
transcription (tx86h/ciphertext_f275v.tsv) and key86.tsv; writes gl275/gl275_result.json. --check exits 1 if stale.
PREREG: gl275/PREREG_gl275.md."""
import json, os, sys
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(D)
key = {}
for l in open(os.path.join(T, 'key86.tsv')):
    p = l.rstrip('\n').split('\t')
    if p[0].startswith('T'): key[p[0]] = p[1]
lines = {}
for l in open(os.path.join(T, 'tx86h/ciphertext_f275v.tsv')):
    a, b = l.rstrip('\n').split('\t'); lines[a] = b.split()
alt = {}
for l in open(os.path.join(T, 'tx86i/local_ciphertext.tsv')):
    a, b = l.rstrip('\n').split('\t'); alt[a] = b.split()
rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(D, 'gloss_align.tsv'))][1:]
out = {'per_line': {}, 'C': 0, 'M_glossed': 0, 'agree_key': 0, 'conflicts': [], 'rows': []}
for L in ('L17', 'L18', 'L19', 'L20'):
    n = sum(1 for t in lines[L] if t != '/')
    out['per_line'][L] = {'sign_tokens': n, 'C': 0}
for r in rows:
    L, idx, exp, gl, grade = r[0], r[1], r[2], r[3], r[7]
    if exp == '/': continue
    i = int(idx); tok = lines[L][i]
    assert tok == exp, (L, idx, tok, exp)
    alt_tok = alt.get(L, [None] * 999)[i] if L in alt and -len(alt[L]) <= i < len(alt[L]) else None
    kv = key.get(tok, '?')
    rec = {'line': L, 'idx': i, 'token': tok, 'key': kv, 'gloss': gl, 'grade': grade, 'tx86i_token': alt_tok}
    out['rows'].append(rec)
    if grade == 'C':
        out['C'] += 1; out['per_line'][L]['C'] += 1
        if kv == gl: out['agree_key'] += 1
        else: out['conflicts'].append(rec)
    else:
        out['M_glossed'] += 1
out['sign_tokens_L17_L20'] = sum(v['sign_tokens'] for v in out['per_line'].values())
out['M_total'] = out['sign_tokens_L17_L20'] - out['C']
s = json.dumps(out, indent=1, ensure_ascii=False) + '\n'
p = os.path.join(D, 'gl275_result.json')
if '--check' in sys.argv:
    ok = os.path.exists(p) and open(p).read() == s
    print('gl275_result.json up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(p, 'w').write(s)
print(f"C {out['C']} (agree key86 {out['agree_key']}, conflicts {len(out['conflicts'])}); glossed-M {out['M_glossed']}; "
      f"L17-L20 sign tokens {out['sign_tokens_L17_L20']}, M {out['M_total']}")
for c in out['conflicts']: print('conflict', c)
