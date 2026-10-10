#!/usr/bin/env python3
"""SUR-MRICH step 1 (10 Oct 2026): count gloss m (and n, letters) per line on every glossed letter page with gloss text committed in this
folder. Script only, no vision. Sources: pool units (A/ and B/ gloss_reconciled.tsv, each pass's own gloss), R13/R14 gloss_reconciled.tsv
(0702, 0730, 0746, 0758), R10 0692/0693 pass-A gloss rows (no reconciled gloss file), SUR-372 0189 right page (reconciled R gloss rows,
pass B's where R lacks one). Letters as dp_align.gletters (ij one letter). Writes counts.tsv (per line) and counts.out (per page);
--check exits 1 if either is stale."""
import os, re, sys
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, '..')
def rows(f):
    for l in open(f, encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        yield l.rstrip('\n').split('\t')
def gl(s):
    s = re.sub(r'[^A-Za-zÀ-ÿ]', '', s).lower(); out, i = [], 0
    while i < len(s):
        if s[i:i+2] == 'ij': out.append('ij'); i += 2
        else: out.append(s[i]); i += 1
    return out
SRC = []
for u, page in [('inv373_0744_blind_sb', '373_0744L'), ('inv373_0744R_blind', '373_0744R'), ('inv373_0745L_blind', '373_0745L'), ('inv373_0745R_blind', '373_0745R')]:
    for p in 'AB':
        SRC.append((page, 'pool', f'{u}/{p}', {r[0]: r[1] for r in rows(os.path.join(P, u, p, 'gloss_reconciled.tsv')) if r[0] != 'crop' and len(r) > 1}))
for u, page in [('inv373_0702_r13', '373_0702'), ('inv373_0730_r13', '373_0730'), ('inv373_0746_r14', '373_0746'), ('inv373_0758_r14', '373_0758R')]:
    SRC.append((page, 'out', u, {r[0]: r[1] for r in rows(os.path.join(P, u, 'gloss_reconciled.tsv')) if r[0] != 'crop' and len(r) > 1}))
SRC.append(('373_0692R/0693L', 'out', 'inv373_0693_r10 (pass A gloss rows)', {r[0]: r[2] for r in rows(os.path.join(P, 'inv373_0693_r10', 'passA_sonnet_blind.tsv')) if len(r) > 2 and r[1] == 'gloss'}))
g372 = {r[0]: r[2] for r in rows(os.path.join(P, 'sur372', 'passB.tsv')) if len(r) > 2 and r[1] == 'gloss'}
g372.update({r[0]: r[2] for r in rows(os.path.join(P, 'sur372', 'passR.tsv')) if len(r) > 2 and r[1] == 'gloss'})
SRC.append(('372_0189R', 'out', 'sur372 (R gloss rows, B where R lacks)', g372))
lines = ['page\tstatus\tsource\tcrop\tletters\tm\tn\tgloss']; pg = []
for page, st, src, d in SRC:
    tl = tm = tn = 0
    for c in sorted(d):
        g = gl(d[c]); m, n = g.count('m'), g.count('n'); tl += len(g); tm += m; tn += n
        lines.append(f'{page}\t{st}\t{src}\t{c}\t{len(g)}\t{m}\t{n}\t{d[c]}')
    pg.append(f'{page}\t{st}\t{src}\tlines {len(d)}\tletters {tl}\tm {tm}\tn {tn}\tm per line {tm/max(len(d),1):.2f}\tm per 100 letters {100*tm/max(tl,1):.2f}')
outs = {'counts.tsv': '\n'.join(lines) + '\n', 'counts.out': '\n'.join(pg) + '\n'}
if '--check' in sys.argv: sys.exit(0 if all(os.path.exists(os.path.join(H, f)) and open(os.path.join(H, f), encoding='utf-8').read() == t for f, t in outs.items()) else 1)
for f, t in outs.items(): open(os.path.join(H, f), 'w', encoding='utf-8').write(t)
print(outs['counts.out'], end='')
