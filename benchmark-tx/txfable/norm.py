#!/usr/bin/env python3
"""TX-FABLE (4 Oct 2026): normalise the raw blind Fable passes (benchmark-tx/txfable/raw/) to the benchmark output format
(line, pos, sign) at benchmark-tx/outputs/<item>/passF_fable.tsv, with the rules each item's build script applies to pass A:
no.87 as benchmark-tx/txsheet/norm_passE.py (leaf_Lnn, prose-split runs joined in order); dint as build_dint128.py (CLEAR
rows dropped, '-' dropped, signs joined per line); Ceppo as build_ceppo.write_out (passage kept, f36v only v36top_L01).
Missing raw files are skipped and reported. Run from the repo root."""
import csv, os, sys
from collections import defaultdict
D = os.path.dirname(os.path.abspath(__file__)); RAW = os.path.join(D, 'raw'); BT = os.path.dirname(D)
sys.path.insert(0, BT)
import build_ceppo  # noqa: E402


def rd(p):
    with open(p, newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def wr(item, rows):
    p = os.path.join(BT, 'outputs', item, 'passF_fable.tsv')
    with open(p, 'w') as f:
        f.write('line\tpos\tsign\n')
        for r in rows:
            f.write('\t'.join(map(str, r)) + '\n')
    print(item, len(rows), 'signs ->', os.path.relpath(p, os.path.dirname(BT)))


def have(*fs):
    miss = [f for f in fs if not os.path.exists(os.path.join(RAW, f))]
    if miss:
        print('missing:', ', '.join(miss))
    return not miss


if have('passF_f178r.tsv', 'passF_f178v_L01-10.tsv', 'passF_f178v_L11-23.tsv', 'passF_f179r.tsv'):
    out = []
    for leaf, fn in [('f178r', 'passF_f178r.tsv'), ('f178v', 'passF_f178v_L01-10.tsv'), ('f178v', 'passF_f178v_L11-23.tsv'),
                     ('f179r', 'passF_f179r.tsv')]:
        n = {}
        for r in rd(os.path.join(RAW, fn)):
            ln = '%s_%s' % (leaf, r['passage'].split('.')[0])
            n[ln] = n.get(ln, 0) + 1
            out.append((ln, n[ln], r['sign_id']))
    wr('birago1572-no87', out)
if have('passF_dint_f128.tsv'):
    lines = defaultdict(list)
    for r in rd(os.path.join(RAW, 'passF_dint_f128.tsv')):
        if r['gloss'].startswith('CLEAR:'):
            continue
        lines[r['line']] += [x for x in r['signs'].split() if x != '-']
    wr('dint-f128-print', [('f128_%s' % ln, i + 1, s) for ln in sorted(lines) for i, s in enumerate(lines[ln])])
od = lambda it: os.path.join(BT, 'outputs', it)
if have('passF_f21v_L01-06.tsv', 'passF_f21v_L07-11.tsv'):
    build_ceppo.write_out(od('ceppo-f21v-S'), 'passF_fable', [os.path.join(RAW, 'passF_f21v_L01-06.tsv'),
                          os.path.join(RAW, 'passF_f21v_L07-11.tsv')], 'f21v'); print('ceppo-f21v-S written')
if have('passF_f87.tsv'):
    build_ceppo.write_out(od('ceppo-f87-S'), 'passF_fable', [os.path.join(RAW, 'passF_f87.tsv')], 'f87'); print('ceppo-f87-S written')
if have('passF_v36.tsv'):
    build_ceppo.write_out(od('ceppo-f36v-gloss'), 'passF_fable', [os.path.join(RAW, 'passF_v36.tsv')], only_lines={'v36top_L01'})
    print('ceppo-f36v-gloss written')
