#!/usr/bin/env python3
"""R10-BAL103D: enlarge the f.171r control for the ambiguous 9 (r10/PREREG.md).
Joins the R7C blind pass of f.171r L01-L04 (calib/f171r_passA.tsv) and this job's blind pass of L05-L11
(r10/f171r_L05-11_passA.tsv, crops r10/images/f366x_L01..L07 = page lines 5-11; r10/f171r_L12-18_passA.tsv, crops
f366y_L01..L07 = page lines 12-18), decodes with key_decode.tsv (first
value; c = q as published, as calib.py does), keeps clear words written in [brackets] as their own letters, and
semi-global-aligns the letter string to the period decipherment (r10/f172r_decipherment_ext.txt) with calib.py's
unit-cost DP. Writes r10/nines.tsv: every standalone 9 token with its aligned decipherment letter, the letter's
neighbourhood, and whether the neighbours on both sides match (a 9 counts as 'known' only then).
--check exits 1 if the committed nines.tsv is stale."""
import sys, os, unicodedata
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if c.isalpha() and ord(c) < 128)
    return s.replace('j', 'i').replace('v', 'u')
key = {}
for ln in open(os.path.join(T, 'key_decode.tsv')):
    if ln.startswith('#') or ln.startswith('code\t'): continue
    c, v = ln.rstrip('\n').split('\t')[:2]; key[c] = v.split('|')[0]
key['c'] = 'q'
def tokens(path, linemap):
    out_all = []
    for ln in open(path):
        if ln.startswith('#') or not ln.strip(): continue
        cid, tt = ln.rstrip('\n').split('\t', 1); parts = cid.split('_'); line = linemap(parts[-2]); seg = parts[-1]
        out, buf = [], None
        for t in tt.split(' '):
            if not t: continue
            if buf is not None:
                buf += ' ' + t
                if buf.count('{') <= buf.count('}') and buf.count('[') <= buf.count(']'): out.append(buf); buf = None
            elif (t.startswith('?{') and '}' not in t) or (t.startswith('[') and ']' not in t) or \
                 (t.startswith('|>[') and ']' not in t) or (t.startswith('|>?{') and '}' not in t): buf = t
            else: out.append(t)
        if buf: out.append(buf)
        if seg == 's2':
            i = next((k for k, t in enumerate(out) if t.startswith('|>')), None)
            out = [] if i is None else [out[i][2:]] + out[i + 1:]
        for k, t in enumerate(out): out_all.append((line, seg, k, t if t.startswith(('?', '[')) else t.split('|')[0]))
    return out_all
toks = tokens(os.path.join(T, 'calib', 'f171r_passA.tsv'), lambda L: int(L[1:])) + \
       tokens(os.path.join(H, 'f171r_L05-11_passA.tsv'), lambda L: int(L[1:]) + 4) + \
       (tokens(os.path.join(H, 'f171r_L12-18_passA.tsv'), lambda L: int(L[1:]) + 11)
        if os.path.exists(os.path.join(H, 'f171r_L12-18_passA.tsv')) else [])
E = []  # (token index, letter)
for ti, (line, seg, k, s) in enumerate(toks):
    if s.startswith('['): v = s.strip('[]')
    elif s.startswith('?'): continue
    else:
        v = key.get(s)
        if not v or v.startswith('?'): continue
    for ch in norm(v): E.append((ti, ch))
D = ''.join(c for _, c in E)
P = norm(''.join(l for l in open(os.path.join(H, 'f172r_decipherment_ext.txt')) if not l.startswith('#')))
def align(D, P):
    n, m = len(D), len(P)
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
pr = dict(align(D, P))
hits = sum(1 for i, j in pr.items() if j is not None and D[i] == P[j])
rows = ['line\ttoken_index\tsign\taligned_letter\tcontext_D\tcontext_P\tneighbours_match\tknown']
for i, (ti, ch) in enumerate(E):
    if toks[ti][3] != '9': continue
    j = pr.get(i)
    al = P[j] if j is not None else '-'
    nb = all(pr.get(i + d) is not None and D[i + d] == P[pr[i + d]] and pr[i + d] == (j or -9) + d
             for d in (-2, -1, 1, 2) if 0 <= i + d < len(D))
    cD = D[max(0, i-5):i] + '[' + D[i] + ']' + D[i+1:i+6]
    cP = (P[max(0, j-5):j] + '[' + P[j] + ']' + P[j+1:j+6]) if j is not None else '-'
    known = 'yes' if (j is not None and nb) else 'no'
    rows.append(f'{toks[ti][0]}\t{ti}\t9\t{al}\t{cD}\t{cP}\t{"yes" if nb else "no"}\t{known}')
rows.append(f'# letters D {len(D)}, decipherment span P {len(P)}, matched {hits} ({hits/len(D):.3f})')
outp = os.path.join(H, 'nines.tsv'); txt = '\n'.join(rows) + '\n'
if '--check' in sys.argv:
    sys.exit(0 if os.path.exists(outp) and open(outp).read() == txt else 1)
open(outp, 'w').write(txt); print(txt, end='')
