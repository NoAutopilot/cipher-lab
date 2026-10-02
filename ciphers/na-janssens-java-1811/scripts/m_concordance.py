#!/usr/bin/env python3
"""Concordance of every M-graded code on leaf 188 across the gloss sources on disk (GAPS3, 2 Oct 2026).

Usage: python3 scripts/m_concordance.py [--codes 140,190,...]
Reads reading_tokens.tsv (which codes are M on leaf 188), combined_passA.tsv / combined_passB.tsv (leaves 190, 191,
199, 200 and 500 = No.5 leaves 210-212, two blind passes), leaf192_reconciled.tsv, leaf201_reconciled.tsv, and prints,
per code, every glossed occurrence with two glosses of context on each side (pass A's gloss, pass B's where it
differs), then the leaf-188 contexts of the code. Disk only; a report, writes nothing.
"""
import argparse, csv, os
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
def load(p): return list(csv.DictReader(open(os.path.join(T, p), encoding='utf-8'), delimiter='\t'))
ap = argparse.ArgumentParser(); ap.add_argument('--codes'); a = ap.parse_args()
toks = load('reading_tokens.tsv')
m_tokens = [t for t in toks if t['grade'] == 'M']
codes = a.codes.split(',') if a.codes else sorted({t['sign'] for t in m_tokens}, key=int)
# sources: list of (name, rows) where rows have leaf, order, code, gloss, note
A = load('combined_passA.tsv'); B = load('combined_passB.tsv')
Bmap = {(r['leaf'], r['order']): r for r in B}
sources = [('AB', A)] + [(n, load(n)) for n in ('leaf192_reconciled.tsv', 'leaf201_reconciled.tsv')]
byleaf = defaultdict(list)
for name, rows in sources:
    for r in rows:
        byleaf[(name, r['leaf'])].append(r)
def ctx(rows, i, w=3):
    out = []
    for j in range(max(0, i - w), min(len(rows), i + w + 1)):
        g = rows[j]['gloss'] or '_'
        cell = f"{rows[j]['code']}={g}"
        if j == i: cell = f"[[{cell}]]"
        out.append(cell)
    return ' '.join(out)
lines = defaultdict(list)
for t in toks: lines[t['line']].append(t)
for c in codes:
    print(f"\n##### code {c}")
    for (name, leaf), rows in byleaf.items():
        for i, r in enumerate(rows):
            if r['code'] != c: continue
            if name == 'AB':
                b = Bmap.get((leaf, r['order']))
                bg = f"  | B: {b['code']}={b['gloss'] or '_'}{(' ('+b['note']+')') if b and b['note'] else ''}" if b and (b['gloss'] != r['gloss'] or b['code'] != r['code']) else ''
                note = f"  (A note: {r['note']})" if r['note'] else ''
                print(f"  leaf {leaf} #{r['order']}: {ctx(rows, i)}{bg}{note}")
            else:
                note = f"  (note: {r['note']})" if r['note'] else ''
                print(f"  leaf {leaf} #{r['order']}: {ctx(rows, i)}{note}")
    for t in m_tokens:
        if t['sign'] != c: continue
        L = lines[t['line']]; i = int(t['pos']) - 1
        s = ' '.join((f"[[{x['value']}]]" if k == i else (x['value'] if x['grade'] != 'U' else f"[{x['sign']}]")) for k, x in enumerate(L))
        print(f"  >> leaf 188 {t['line']}:{t['pos']} value {t['value']!r}: {s}")
