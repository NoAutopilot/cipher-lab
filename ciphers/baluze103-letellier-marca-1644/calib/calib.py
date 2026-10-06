#!/usr/bin/env python3
"""R7C-BAL103K: sibling calibration of Tomokiyo's 1644 table on f.171r L01-L04 (registered in calib/PREREG.md).
Decodes the blind pass with key_decode.tsv (first value), semi-global-aligns it to the period decipherment (f.172r),
A = matched letters / len(D); control = 200 permutations of the sign->letter values (seed 1644); wrong-span null descriptive.
Writes calib/result.tsv and calib/sign_table.tsv; --check exits 1 if the committed files are stale."""
import sys, os, random, unicodedata
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if c.isalpha() and ord(c) < 128)
    return s.replace('j', 'i').replace('v', 'u')
key = {}
for ln in open(os.path.join(T, 'key_decode.tsv')):
    if ln.startswith('#') or ln.startswith('code\t'): continue
    c, v = ln.rstrip('\n').split('\t')[:2]; key[c] = v.split('|')[0]
# the registered test is of the table as published: undo this job's own licensed change (c q->p) before scoring
key['c'] = 'q'
toks = []  # (line, sign)
for ln in open(os.path.join(H, 'f171r_passA.tsv')):
    if ln.startswith('#') or not ln.strip(): continue
    cid, tt = ln.rstrip('\n').split('\t'); line = cid.split('_')[1]; seg = cid.split('_')[2]
    tt = tt.replace('?{', '?{').split(' ')
    # join brace groups
    out, buf = [], None
    for t in tt:
        if buf is not None:
            buf += ' ' + t
            if '}' in t: out.append(buf); buf = None
        elif t.startswith('?{') and '}' not in t: buf = t
        else: out.append(t)
    if seg == 's2':
        i = next((k for k, t in enumerate(out) if t.startswith('|>')), None)
        out = [] if i is None else [out[i][2:]] + out[i + 1:]
    for t in out: toks.append((line, t.split('|')[0] if not t.startswith('?') else t))
dec = [(l, s, key.get(s)) for l, s in toks]
signs = [s for l, s, v in dec if v and len(v) == 1]   # letter cells only (word codes kept separately)
D_items = [(s, v) for l, s, v in dec if v and not v.startswith('?')]
P_all = norm(''.join(l for l in open(os.path.join(H, 'f172r_decipherment.txt')) if not l.startswith('#')))
def expand(items, kmap):
    out = []
    for s, v in items:
        vv = kmap.get(s, v) if len(v) == 1 else v
        for ch in norm(vv): out.append((s, ch))
    return out
def align(D, P):
    n, m = len(D), len(P); INF = 10**9
    sc = [[0] * (m + 1) for _ in range(n + 1)]; bt = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): sc[i][0] = i; bt[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            a = sc[i-1][j-1] + (0 if D[i-1] == P[j-1] else 1); b = sc[i-1][j] + 1; c = sc[i][j-1] + 1
            sc[i][j], bt[i][j] = min((a, 0), (b, 1), (c, 2))
    j = min(range(m + 1), key=lambda j: sc[n][j]); i = n; pairs = []
    while i > 0:
        if j > 0 and bt[i][j] == 0: pairs.append((i-1, j-1)); i -= 1; j -= 1
        elif bt[i][j] == 1 or j == 0: pairs.append((i-1, None)); i -= 1
        else: j -= 1
    return pairs[::-1]
def stat(kmap, P):
    E = expand(D_items, kmap); D = ''.join(c for s, c in E)
    pr = align(D, P); hit = sum(1 for i, j in pr if j is not None and D[i] == P[j])
    return hit / len(D), E, pr, D
base = {s: v for s, v in D_items if len(v) == 1}
A, E, pr, D = stat({}, P_all[:len(D_items) * 2])
rng = random.Random(1644)
cells = [c for c, v in key.items() if len(v) == 1]; vals = [key[c] for c in cells]
perm = []
for _ in range(200):
    v2 = vals[:]; rng.shuffle(v2); km = dict(zip(cells, v2)); perm.append(stat(km, P_all[:len(D_items) * 2])[0])
perm.sort(); p95, p99 = perm[189], perm[197]; mean = sum(perm) / len(perm)
L = len(D); wrong = P_all[len(P_all) - L - 10:]
Aw = stat({}, wrong)[0]
gate = 'PASS' if A >= 0.60 and A > p99 else ('PARTIAL' if A > p99 else 'FAIL')
res = (f"N_signs\t{len(toks)}\nN_decoded_letters\t{L}\nA\t{A:.3f}\nperm_mean\t{mean:.3f}\nperm_p95\t{p95:.3f}\nperm_p99\t{p99:.3f}\n"
       f"wrong_span_A\t{Aw:.3f}\ngate\t{gate}\n")
from collections import defaultdict
st = defaultdict(list)
for i, j in pr:
    st[E[i][0]].append(P_all[j] if j is not None else '-')
rows = ['sign\tkey_value\tn\taligned_letters']
for s in sorted(st, key=lambda s: -len(st[s])): rows.append(f"{s}\t{key.get(s)}\t{len(st[s])}\t{''.join(st[s])}")
tab = '\n'.join(rows) + '\n'
files = {'result.tsv': res, 'sign_table.tsv': tab}
if '--check' in sys.argv:
    bad = [f for f, c in files.items() if open(os.path.join(H, f)).read() != c]
    print('stale: ' + ', '.join(bad) if bad else 'calib up to date'); sys.exit(1 if bad else 0)
for f, c in files.items(): open(os.path.join(H, f), 'w').write(c)
print(res + 'D: ' + D + '\nP: ' + P_all[:L + 20]); print(tab)
