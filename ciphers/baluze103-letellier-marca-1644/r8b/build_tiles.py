#!/usr/bin/env python3
"""R8-BAL103B: build tools/lookalike_pass.py inputs for f.50 from the R7B reconciliation.
passC = ciphertext.tsv as it stood BEFORE R8-BAL103's 10 '-r8-2of3' corrections (their old sign is restored from alt), so the
look-alike pass re-decides those columns too. A tile = a ciphertext row whose column split A/B in tx/r7b/rec_[rv]/disagreements.tsv
(both readers gave a sign; gap columns are not look-alike questions) AND whose unordered pair {A, B} sits inside one of the named
confusable families (r8 notes: m/mm/mt, venus/P/q2, x/xc/xs/xbar, 6/sigma, hz/hbar, tt/venus; plus the next two swap pairs of r8b/confusion.tsv, mm/tt and 9/venus).
Writes r8b/agreement_split.tsv (confusion input), r8b/passC.tsv (line, pos, sign), r8b/tiles.tsv (packet-format columns)."""
import os, sys, collections
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
FAM = [{'m', 'mm', 'mt'}, {'venus', 'P', 'q2', 'q'}, {'x', 'xc', 'xs', 'xbar'}, {'6', 'sigma'}, {'hz', 'hbar'}, {'tt', 'venus'}, {'mm', 'tt'}, {'9', 'venus'}]
DIS = {}
for p in ('tx/r7b/rec_r/disagreements.tsv', 'tx/r7b/rec_v/disagreements.tsv'):
    for i, ln in enumerate(open(os.path.join(T, p))):
        if i: f = ln.rstrip('\n').split('\t'); DIS[(f[0], int(f[1]))] = (f[2], f[3])
hdr, *rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(T, 'ciphertext.tsv'))]
for r in rows:
    if r[5] == 'r8-2of3':
        r[2] = r[4].split('r8 old=')[1].split()[0]
def col(r):
    return int(r[4].split()[0][3:]) if r[4].startswith('col') else int(r[1])
def first(s): return s.split('|')[0].lstrip('=') if s not in ('-', '') else s
open(os.path.join(H, 'passC.tsv'), 'w').write('line\tpos\tsign\n' + ''.join(f'{r[0]}\t{r[1]}\t{r[2]}\n' for r in rows))
al, tiles = [], []
seq = collections.defaultdict(list)
for r in rows: seq[r[0]].append(r[2])
for r in rows:
    ab = DIS.get((r[0], col(r))) if r[5] != 'agree' else None
    if not ab: continue
    a, b = ab
    al.append(dict(passage=r[0], posA=r[1], idA=a, idB=b, status='split'))
    if '-' in (a, b): continue
    sa = {x.lstrip('=') for x in a.split('|')}; sb = {x.lstrip('=') for x in b.split('|')}
    fam = [F for F in FAM if (sa & F) and (sb & F)]
    if not fam: continue
    pos = int(r[1]); s = seq[r[0]]
    cand = sorted(({x for x in a.split('|') + b.split('|') + [r[2]]} | (fam[0] - {'q'})) - {'-', ''})
    tiles.append(dict(run='bal103b', passage=r[0], pos=r[1], passC=r[2], A=first(a) if '|' not in a else a.split('|')[0], B=b.split('|')[0],
                      status='split', why='split', candidates=','.join(cand), before=' '.join(s[max(0, pos - 4):pos - 1]),
                      after=' '.join(s[pos:pos + 3]), noteA=a, noteB=b))
def w(name, rs):
    ks = list(rs[0]); open(os.path.join(H, name), 'w').write('\t'.join(ks) + '\n' + ''.join('\t'.join(str(x[k]) for k in ks) + '\n' for x in rs))
w('agreement_split.tsv', al); w('tiles.tsv', tiles)
print(f'rows {len(rows)} split columns {len(al)} family tiles {len(tiles)}', file=sys.stderr)
