#!/usr/bin/env python3
"""MONL-LEAF power check: leaf_score.py's statistic on c268's own lines against the 4 clear lines starting where each line
truly starts (align_c268.tsv cpos), for 1-line and 2-line reads; and against a wrong window (f.140r L27-L30) as the negative."""
import json, random, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent))
import align_c268 as A, leaf_score as S
words = A.load_clear(); keys = [f'{w[0]}:{w[1]}' for w in words]
pos = []; c = 0
for w in words:
    pos.append(c); c += len(w[2])
def line_at(cp):
    k = max(i for i, p in enumerate(pos) if p <= cp); return keys[k]
order = list(dict.fromkeys(keys))
first = {}
for l in list(open(HERE.parent / 'align_c268.tsv', encoding='utf-8'))[1:]:
    f = l.rstrip('\n').split('\t')
    if f[6] == 'confirm' and f[0] not in first:
        pass
rows = [l.rstrip('\n').split('\t') for l in list(open(HERE.parent / 'align_c268.tsv', encoding='utf-8'))[1:]]
import re
res = []
for n in range(1, 30 if len(sys.argv) > 1 and sys.argv[1] == '2' else 31):
    L = f'L{n:02d}'; lines = [L] + ([f'L{n+1:02d}'] if len(sys.argv) > 1 and sys.argv[1] == '2' else [])
    # start: clear line of the first keyed token of L with a nonempty chunk -- cpos isn't in the tsv, recompute alignment on whole text
    res.append(lines)
toks_all = S.tokens(c268=None, path=None) if False else None
key = {}
for l in list(open(HERE.parent / 'key.tsv', encoding='utf-8'))[1:]:
    f = l.rstrip('\n').split('\t'); key[f[0]] = f[2]
ct = [l.rstrip('\n').split('\t') for l in open(HERE.parent / 'ciphertext_c268.tsv', encoding='utf-8')][1:]
toks = [{'line': f[0], 'pos': int(f[1]), 'sign': f[2], 'conf': f[3], 'value': A.fold(key[f[2]]) if key.get(f[2]) else None} for f in ct]
clear = ''.join(w[2] for w in words)
_, path, _, _ = A.align(toks, clear)
start = {}
for ti, a, b in path:
    if b > a and toks[ti]['line'] not in start: start[toks[ti]['line']] = a
out = []
for lines in res:
    sub = [dict(t) for t in toks if t['line'] in lines]
    k0 = order.index(line_at(start[lines[0]])); win = order[k0:k0 + 4]
    w = ''.join(x[2] for x in words if f'{x[0]}:{x[1]}' in win)
    real = S.share(sub, w); wrong = S.share(sub, S.window('f.140r:L27-f.140r:L30')[0])
    rng = random.Random(2710); ws = [x[2] for x in words]; ctl = []
    for _ in range(200):
        rng.shuffle(ws); s = ''.join(ws); st = rng.randrange(0, len(s) - len(w) + 1); ctl.append(S.share(sub, s[st:st + len(w)]))
    ctl.sort(); p95 = ctl[189]
    out.append({'lines': '+'.join(lines), 'win': f'{win[0]}-{win[-1]}', 'real': real, 'p95': p95, 'margin': round(real - p95, 3),
                'pass': real - p95 >= S.GATE, 'wrong_win': wrong, 'wrong_margin': round(wrong - p95, 3), 'wrong_pass': wrong - p95 >= S.GATE})
    print(json.dumps(out[-1]), flush=True)
print(json.dumps({'n': len(out), 'pass': sum(o['pass'] for o in out), 'wrong_pass': sum(o['wrong_pass'] for o in out)}))
