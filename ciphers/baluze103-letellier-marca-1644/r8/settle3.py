#!/usr/bin/env python3
"""R8-BAL103 step 3: apply the registered 2-of-3 settlement (r8/PREREG.md) of the blind re-read r8/reread.tsv to ciphertext.tsv.
The re-read (normalised by tx/prep_passes.py into r8/reread_long.tsv; f50v_L09 s2 had no |> marker, so its first 3 tokens
'9 12 xs', repeated from the end of s1 in the 200 px overlap, are dropped here) is aligned per line (Needleman-Wunsch) to the
line's ciphertext.tsv rows, each row carrying its candidate set {pass A, pass B} (agreed rows: the one sign; disagreement rows: the
two passes' readings from tx/r7b/rec_[rv]/disagreements.tsv). Rule: at a disagreement column, if the re-read's first-choice sign
equals A's or B's reading, that sign is the settlement (grade M; H if it also equals the current sign and A, B, C all agree is
impossible at a disagreement); a re-read matching neither is logged only. Agreed rows are never changed (A = B is already 2 of 3).
Writes r8/corrections.tsv and r8/reread_align.tsv; with --apply also rewrites ciphertext.tsv (old sign kept in alt, why 'r8-2of3').
--check exits 1 if r8/corrections.tsv is stale."""
import os, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
LINES = ['f50r_L13', 'f50v_L09', 'f50v_L03', 'f50r_L14', 'f50r_L16']
C = {}
for i, ln in enumerate(open(os.path.join(H, 'reread_long.tsv'))):
    if i: f = ln.rstrip('\n').split('\t'); C.setdefault(f[0], []).append(f[2].lstrip('|>'))
C['f50v_L09'] = C['f50v_L09'][:13] + C['f50v_L09'][16:]
DIS = {}
for p in ('tx/r7b/rec_r/disagreements.tsv', 'tx/r7b/rec_v/disagreements.tsv'):
    for i, ln in enumerate(open(os.path.join(T, p))):
        if i: f = ln.rstrip('\n').split('\t'); DIS[(f[0], int(f[1]))] = (f[2], f[3])
hdr, *rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(T, 'ciphertext.tsv'))]

def col(r):
    a = r[4]
    return int(a.split()[0][3:]) if a.startswith('col') else int(r[1])

def align(rs, cs):
    n, m = len(rs), len(cs); S = [[0] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): S[i][0] = -i; B[i][0] = 'u'
    for j in range(1, m + 1): S[0][j] = -j; B[0][j] = 'l'
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cand = rs[i - 1][1]
            d = S[i - 1][j - 1] + (2 if cs[j - 1] in cand else -1)
            u, l = S[i - 1][j] - 1, S[i][j - 1] - 1
            S[i][j], B[i][j] = max((d, 'd'), (u, 'u'), (l, 'l'))
    i, j, out = n, m, []
    while i or j:
        b = B[i][j]
        if b == 'd': out.append((i - 1, cs[j - 1])); i -= 1; j -= 1
        elif b == 'u': out.append((i - 1, None)); i -= 1
        else: j -= 1
    return dict(out)

corr, al = [], []
for L in LINES:
    idx = [k for k, r in enumerate(rows) if r[0] == L]
    rs = []
    for k in idx:
        r = rows[k]; c = col(r)
        ab = DIS.get((L, c)) if r[5] != 'agree' else None
        rs.append((k, set(ab) - {'-'} if ab else {r[2]}, ab))
    m = align(rs, C[L])
    for t, (k, cand, ab) in enumerate(rs):
        c = m.get(t); r = rows[k]
        al.append((L, r[1], r[2], ab[0] if ab else r[2], ab[1] if ab else r[2], c or '-'))
        if ab and c and c in (ab[0], ab[1]) and c != r[2]:
            corr.append((L, r[1], r[2], c, ab[0], ab[1], c, 'applied'))
        elif ab and c and c not in (ab[0], ab[1]):
            corr.append((L, r[1], r[2], r[2], ab[0], ab[1], c, 'logged: re-read matches neither pass'))
        elif ab and c == r[2]:
            corr.append((L, r[1], r[2], r[2], ab[0], ab[1], c, 'confirms current'))
ctxt = 'line\tposition\told\tnew\tA\tB\treread\taction\n' + ''.join('\t'.join(x) + '\n' for x in corr)
atxt = 'line\tposition\tcurrent\tA\tB\treread\n' + ''.join('\t'.join(x) + '\n' for x in al)
if '--check' in sys.argv:
    ok = open(os.path.join(H, 'corrections.tsv')).read() == ctxt
    print('up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(os.path.join(H, 'corrections.tsv'), 'w').write(ctxt); open(os.path.join(H, 'reread_align.tsv'), 'w').write(atxt)
if '--apply' in sys.argv:
    pos = {(x[0], x[1]): x for x in corr if x[7] == 'applied'}
    for r in rows:
        x = pos.get((r[0], r[1]))
        if x and r[2] == x[2]:
            r[4] = (r[4] + ' ' if r[4] else '') + f'r8 old={x[2]} C:{x[6]}'; r[2] = x[3]; r[3] = 'M'; r[5] = 'r8-2of3'
    open(os.path.join(T, 'ciphertext.tsv'), 'w').write('\t'.join(hdr) + '\n' + ''.join('\t'.join(r) + '\n' for r in rows))
print(ctxt)
