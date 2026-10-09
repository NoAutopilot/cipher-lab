#!/usr/bin/env python3
"""ES132-LOOK (9 Oct 2026): adapter from this folder's wide passes to tools/lookalike_pass.py's long formats.

For each page with passes/<page>_passA.tsv, _passB.tsv and ciphertext_<page>.tsv (C, the committed reconciled read), the passes are
normalised by test2.load_pass (the scorer's own notation) and each is aligned per line to C by lookalike_pass._align (edit distance).
Writes lookalike/<page>/agreement.tsv (passage posA idA confA posB idB confB status merged merged_conf; one row per C token; status
'agree' when A, B and C carry the same label, 'split' when A and B both have a label and differ, 'split-gap' when one reader has
nothing aligned there, 'split-c' when A == B != C) and lookalike/<page>/passC.tsv (passage pos sign_id conf; a trailing '?' on a C
token is dropped from the label and gives conf M). No label is changed here.
  python3 lookalike/build_agreement.py [page ...]       (default: every page with all three files)
"""
import sys, csv
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(HERE), str(HERE.parent.parent / 'tools')]
from test2 import load_pass
from test0 import load_lines
from lookalike_pass import _align

def build(page):
    pa, pb, pc = HERE / f'passes/{page}_passA.tsv', HERE / f'passes/{page}_passB.tsv', HERE / f'ciphertext_{page}.tsv'
    if not (pa.exists() and pb.exists() and pc.exists()): return None
    A, B, C = load_pass(pa), load_pass(pb), load_lines(pc)
    out = HERE / 'lookalike' / page; out.mkdir(parents=True, exist_ok=True)
    ag, pcr = [], []
    for ln in sorted(C):
        ref = [t.rstrip('?') for t in C[ln]]
        a = _align(ref, [t.rstrip('?') for t in A.get(ln, [])])
        b = _align(ref, [t.rstrip('?') for t in B.get(ln, [])])
        for i, (t, x, y) in enumerate(zip(C[ln], a, b), 1):
            lab = t.rstrip('?'); conf = 'M' if t.endswith('?') else 'H'
            st = ('agree' if x == y == lab else 'split-gap' if x is None or y is None
                  else 'split-c' if x == y else 'split')
            ag.append([ln, i, x or '', 'H', i, y or '', 'H', st, lab, conf])
            pcr.append([ln, i, lab, conf])
    for name, hdr, rows in (('agreement.tsv', ['passage', 'posA', 'idA', 'confA', 'posB', 'idB', 'confB', 'status', 'merged',
                                               'merged_conf'], ag), ('passC.tsv', ['passage', 'pos', 'sign_id', 'conf'], pcr)):
        with open(out / name, 'w', newline='') as f:
            w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(hdr); w.writerows(rows)
    n = len(ag); s = sum(r[7] != 'agree' for r in ag)
    return page, n, s

if __name__ == '__main__':
    pages = sys.argv[1:] or sorted(p.name[:-10] for p in (HERE / 'passes').glob('*_passA.tsv'))
    for p in pages:
        r = build(p)
        if r: print(f'{r[0]}\tC tokens {r[1]}\tnot-agree {r[2]} ({r[2]/r[1]:.3f})')
