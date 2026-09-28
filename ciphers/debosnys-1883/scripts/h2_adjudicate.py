#!/usr/bin/env python3
"""H2 adjudication (rule in scripts/PROMPTS_c1.md, written before any crop was read).

Inputs: passA_c1.tsv, passB_c1.tsv (GOLD-4C / GOLD-4E), passC_c1.tsv (the third blind pass, disputed positions only,
columns line, position, sign, confidence, alt), glyphs/inventory.tsv (family), glyphs/base_mark.tsv (base fold).
Outputs: ciphertext_c1_draft.tsv rewritten (136 rows, one per box: line, position, sign, confidence, alt, why) and the
numbers of rule 5 printed. --check exits non-zero if the committed draft differs from what the inputs give (rule 7).
"""
import csv, sys, os, collections
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
def load(p, key=('line', 'position')):
    return {(r['line'], int(r['position'])): r for r in csv.DictReader(open(os.path.join(root, p)), delimiter='\t')}
A, B, C = load('passA_c1.tsv'), load('passB_c1.tsv'), load('passC_c1.tsv')
fam = {r['sign']: r['family'] for r in csv.DictReader(open(os.path.join(root, 'glyphs/inventory.tsv')), delimiter='\t')}
base = {r['sign']: r['base'] for r in csv.DictReader(open(os.path.join(root, 'glyphs/base_mark.tsv')), delimiter='\t')}
def F(s): return fam.get(s, s)
def Bs(s): return base.get(F(s), base.get(s, F(s)))
rows = []; n = collections.Counter()
for k in sorted(A):
    a, b = A[k]['sign'], B[k]['sign']
    if a == b:
        rows.append(dict(line=k[0], position=k[1], sign=a, confidence='H' if A[k]['confidence'] == 'H' and B[k]['confidence'] != 'L' else 'M', alt='', why='agree-AB')); n['agree-AB'] += 1; continue
    if k not in C:
        rows.append(dict(line=k[0], position=k[1], sign=a, confidence='M', alt='B:' + b, why='differ-noC')); n['unsettled'] += 1; continue
    c, cc, calt = C[k]['sign'], C[k]['confidence'], C[k].get('alt', '')
    n['C-read'] += 1
    if c == a: n['AC-full'] += 1
    if c == b: n['BC-full'] += 1
    if F(c) == F(a): n['AC-fam'] += 1
    if F(c) == F(b): n['BC-fam'] += 1
    if c in ('MULTI', '_') and a not in ('MULTI', '_') and b not in ('MULTI', '_'):
        rows.append(dict(line=k[0], position=k[1], sign=a, confidence='M', alt=f'B:{b};C:{c}', why='seg-flag-C')); n['unsettled'] += 1; n['seg-flag'] += 1; continue
    votes = collections.Counter([a, b, c]); top, cnt = votes.most_common(1)[0]
    if cnt >= 2:
        g = 'H' if (cnt == 3 or cc == 'H') else 'M'
        rows.append(dict(line=k[0], position=k[1], sign=top, confidence=g, alt=';'.join(f'{t}:{v}' for t, v in (('A', a), ('B', b), ('C', c)) if v != top), why='settled-majority')); n['settled-full'] += 1; continue
    fv = collections.Counter([F(a), F(b), F(c)]); ftop, fcnt = fv.most_common(1)[0]
    if fcnt >= 2:
        rows.append(dict(line=k[0], position=k[1], sign=ftop, confidence='M', alt=f'A:{a};B:{b};C:{c}', why='family-settled')); n['settled-family'] += 1; continue
    bv = collections.Counter([Bs(a), Bs(b), Bs(c)]); btop, bcnt = bv.most_common(1)[0]
    if bcnt >= 2:
        rows.append(dict(line=k[0], position=k[1], sign=btop, confidence='M', alt=f'A:{a};B:{b};C:{c}', why='base-settled')); n['settled-base'] += 1; continue
    rows.append(dict(line=k[0], position=k[1], sign=a, confidence='M', alt=f'B:{b};C:{c}', why='three-way')); n['unsettled'] += 1; n['three-way'] += 1
N = len(rows); disputed = N - n['agree-AB']
out = 'line\tposition\tsign\tconfidence\talt\twhy\n' + ''.join('\t'.join(str(r[c]) for c in ('line', 'position', 'sign', 'confidence', 'alt', 'why')) + '\n' for r in rows)
p = os.path.join(root, 'ciphertext_c1_draft.tsv')
if '--check' in sys.argv:
    if open(p).read() != out: print('STALE: ciphertext_c1_draft.tsv differs from the passes'); sys.exit(1)
else: open(p, 'w').write(out)
full = n['agree-AB'] + n['settled-full']; famlvl = full + n['settled-family']; baselvl = famlvl + n['settled-base']
print(f"boxes {N}; agreed A=B {n['agree-AB']}; disputed {disputed}; C read {n['C-read']}")
print(f"(a) pairwise on disputed, full id: A-C {n['AC-full']}/{n['C-read']} = {n['AC-full']/max(1,n['C-read']):.3f}, B-C {n['BC-full']}/{n['C-read']} = {n['BC-full']/max(1,n['C-read']):.3f}; family: A-C {n['AC-fam']}/{n['C-read']}, B-C {n['BC-fam']}/{n['C-read']}")
print(f"(b) settled by majority full id {n['settled-full']}, family {n['settled-family']}, base {n['settled-base']}; agreement over {N}: full {full}/{N} = {100*full/N:.1f} pct, family {famlvl}/{N} = {100*famlvl/N:.1f} pct, base {baselvl}/{N} = {100*baselvl/N:.1f} pct")
print(f"(c) unsettled {n['unsettled']} (three-way {n['three-way']}, seg-flag {n['seg-flag']}, no C read {n['unsettled']-n['three-way']-n['seg-flag']})")
print(f"(d) type-noise estimate: floor {n['unsettled']}/{N} = {100*n['unsettled']/N:.1f} pct, ceiling {(n['unsettled']+n['settled-family']+n['settled-base'])}/{N} = {100*(n['unsettled']+n['settled-family']+n['settled-base'])/N:.1f} pct (GOLD-D2 base curve: 0.816 at 2.5 pct, 0.385 at 5 pct)")
print(f"gate 80 pct full id: {'MET' if full/N >= 0.8 else 'NOT MET'}")
# rule 6: the gate met licenses writing cryptogram 1 into ciphertext.txt from the draft (unsettled boxes carry a trailing ?)
if full / N >= 0.8:
    lines = collections.OrderedDict()
    for r in rows: lines.setdefault(r['line'], []).append(r['sign'] + ('' if r['why'] in ('agree-AB', 'settled-majority') else '?'))
    sec = "=== Cryptogram 1 ===\n# 28 Sept 2026 (H2): 160-id inventory ids (glyphs/inventory.tsv), three passes adjudicated by scripts/PROMPTS_c1.md;\n# a trailing ? marks a box unsettled at full id (family- or base-settled value, or pass A's value on a three-way split; alts in ciphertext_c1_draft.tsv)\n" + "".join(" ".join(v) + "\n" for v in lines.values()) + "\n"
    cp = os.path.join(root, 'ciphertext.txt'); ct = open(cp).read(); i = ct.index('=== Cryptogram 1 ==='); j = ct.index('=== Cryptogram 2')
    new = ct[:i] + sec + ct[j:]
    if '--check' in sys.argv:
        if new != ct: print('STALE: ciphertext.txt cryptogram 1 section differs from the draft'); sys.exit(1)
    else: open(cp, 'w').write(new)
