#!/usr/bin/env python3
"""F36-GLOSS step 4 (3 Oct 2026): a separate decode variant -- printed Ceppo-Nevers key (+ X_THETA2=r) plus ONLY those
C-grade clerk values from ../../keys/key_ceppo_f36_clerk.tsv that fill a sign the printed table lacks (note 'fills a sign
the printed table lacks', printed value '-'). Printed nulls and printed values are never overridden. Applied to fr.3251
f.11r, f.21v, f.87 and fr.3252 f.47r; per letter: positions, decoded under baseline vs variant, U -> M moves, and the
variant letters around each changed position (+-6). A filled sign is M in these letters (identified across letters by
shape; C only on f.36-37 where the clerk glossed it).
  python3 variant_decode.py [--check]   -> variant.tsv, variant_fragments.txt
"""
import csv, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
C = ROOT / 'ciphers/ceppo-nevers-fr3251-1570s/harvest'
TARGETS = [('fr3251 f.11r', C / 'ciphertext_f11.tsv', 'sign'), ('fr3251 f.21v', C / 'ciphertext_f21v.tsv', 'sign'),
           ('fr3251 f.87', C / 'ciphertext_f87.tsv', 'sign'),
           ('fr3252 f.47r', HERE.parent / 'f47' / 'recon_norm.tsv', 'sign_id')]


def main(check=False):
    base = {e['id']: e['value'] for e in json.load(open(C / 'sign_id_map.json'))}
    base['X_THETA2'] = 'r'
    fill = {}
    for r in csv.DictReader(open(HERE.parents[1] / 'keys' / 'key_ceppo_f36_clerk.tsv'), delimiter='\t'):
        if r['grade'] == 'C' and r['printed'] == '-' and r['sign'] not in base:
            fill[r['sign']] = r['clerk']
    var = dict(base); var.update(fill)
    rows = ['letter\tpositions\tbase_decoded\tvariant_decoded\tU_to_M\tfilled_signs']
    frag = [f'# filled from the clerk gloss (C on f.36-37, M elsewhere): {fill}']
    for name, path, col in TARGETS:
        seq = [r[col] for r in csv.DictReader(open(path), delimiter='\t')]
        def dec(m, s):
            v = m.get(s)
            return '' if v == 'null' else ('?' if v is None else v)
        b = [dec(base, s) for s in seq]; v = [dec(var, s) for s in seq]
        ch = [i for i in range(len(seq)) if b[i] == '?' and v[i] != '?']
        nb = sum(1 for x in b if x != '?'); nv = sum(1 for x in v if x != '?')
        rows.append(f"{name}\t{len(seq)}\t{nb}\t{nv}\t{len(ch)}\t{','.join(sorted({seq[i] for i in ch}))}")
        for i in ch:
            lo, hi = max(0, i - 6), min(len(seq), i + 7)
            frag.append(f"{name} pos {i+1} {seq[i]}={v[i]}: base '{''.join(b[lo:hi])}' -> variant '{''.join(v[lo:i])}[{v[i]}]{''.join(v[i+1:hi])}'")
    out = {HERE / 'variant.tsv': '\n'.join(rows) + '\n', HERE / 'variant_fragments.txt': '\n'.join(frag) + '\n'}
    if check:
        bad = [p.name for p, t in out.items() if not p.exists() or p.read_text() != t]
        print('stale: ' + ','.join(bad) if bad else 'ok'); sys.exit(1 if bad else 0)
    for p, t in out.items():
        p.write_text(t)
    print('\n'.join(rows))


if __name__ == '__main__':
    main('--check' in sys.argv)
