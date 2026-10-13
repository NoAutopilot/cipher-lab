#!/usr/bin/env python3
"""BAL-WL adoption (PREREG-BAL-WL.md 'Adoption'): f.228 tokens of the shape classes CONFIRMED by balshape/wl/score1.out (both gates
PASS) move M -> S; values never change (asserted against reading_tokens_b170f228.tsv). Writes balshape/wl/exceptions_b170f228.tsv,
read by tools/decode_key.py through decode.json. Class-wide for the fixed-value shapes; per token for the u4/4u family, whose value
is decided per token (SIG-B228B sig2_shape_map.tsv), so only the tiled tokens are regraded. Run from the target folder."""
import csv, re
TOK = re.compile(r'\{[^}]*\}|\S+')
CLASS = {'q': 'c', 'll': 'l', 'll|u4': 'l', '?(ff_crossed_double_long_s)': 's', 'y+': 'r', 'h': 'n'}
PER_TOKEN = {('v_b_L06', 6): 'a', ('v_a_L02', 4): 'a', ('v_b_L05', 8): 'a', ('v_b_L01', 10): 'a',  # target:u4|4u
             ('v_a_L01', 5): 'a', ('v_b_L04', 1): 't'}                                           # ANCHOR 4u=a, u4=t
cur = {(r['line'], int(r['pos'])): r for r in []}
rows, tokfile = [], list(csv.reader(open('reading_tokens_b170f228.tsv'), delimiter='\t'))
# reading_tokens lines repeat across r and v; index them in file order per folio by walking the ciphertext the same way
cipher = [l for l in open('ciphertext_b170f228.txt') if not l.startswith('#') and l.strip()]
seen = set()
for f in ('passes/reconciled_b170f228r.tsv', 'passes/reconciled_b170f228v.tsv'):
    folio = f.split('_')[1].split('.')[0]
    for ln in open(f, encoding='utf-8'):
        if ln.startswith('#') or ln.startswith('line\t') or not ln.strip():
            continue
        lid, toks = ln.rstrip('\n').split('\t'); line = lid.split('_', 1)[1]; lkey = lid.replace('b170f228', '').lstrip('_')
        ct = next(c for c in cipher if c.startswith(f'{folio} {line} |')).split('|', 1)[1].split()
        pos = ncol = 0
        for t in TOK.findall(toks):
            if t.startswith('{'):
                pos += len(t[1:-1].split()); continue
            ncol += 1; sh = t.rstrip('?')[2:] if t.startswith('s:') else None
            val = PER_TOKEN.get((lkey, ncol)) if sh in ('u4', '4u', 'u4|4u') else CLASS.get(sh)
            if val:
                assert ct[pos] == f'L:{val}?', (folio, line, pos, ct[pos], t, val)
                why = 'per-token u4/4u tile' if sh in ('u4', '4u', 'u4|4u') else f'class {sh}'
                rows.append((folio, line, pos, val, 'S', f'BAL-WL: {why} CONFIRMED (PREREG-BAL-WL, G1 0.917 G2 0.000, score1.out)'))
                seen.add((lkey, ncol)) if (lkey, ncol) in PER_TOKEN else None
            pos += 1
assert seen == set(PER_TOKEN), set(PER_TOKEN) - seen
with open('balshape/wl/exceptions_b170f228.tsv', 'w') as o:
    o.write('folio\tline\tpos\tvalue\tgrade\treason\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in rows))
import collections
print(len(rows), 'tokens M -> S', dict(collections.Counter(r[5].split(': ')[1].split(' CONF')[0] for r in rows)))
