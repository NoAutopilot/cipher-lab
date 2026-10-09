#!/usr/bin/env python3
"""TXE2-COST2: convert ceppo-f87 reader TSVs (blind_pass_brief format: passage pos sign_id ...) to tx_bench format, as
build_ceppo.write_out with prefix f87, except that prose-split runs L03.1, L03.2 ... are joined in order into L03 (the truth
has one row set per physical line). Rows sorted by (line, run, pos); nothing else edited.
    python3 convert87.py READ.tsv [READ2.tsv ...] --out OUT.tsv --label 'arm a'"""
import argparse, csv
from collections import defaultdict
ap = argparse.ArgumentParser(); ap.add_argument('reads', nargs='+'); ap.add_argument('--out', required=True)
ap.add_argument('--label', default=''); a = ap.parse_args()
runs = defaultdict(list)
for p in a.reads:
    with open(p, newline='') as f:
        for r in csv.DictReader((l for l in f if not l.startswith('#') and l.strip()), delimiter='\t'):
            ps = r['passage'].strip(); ln, _, run = ps.partition('.')
            runs[(ln, int(run or 0))].append((int(r['pos']), (r.get('sign_id') or '').strip()))
lines = defaultdict(list)
for (ln, run) in sorted(runs):
    lines[ln] += [s for _, s in sorted(runs[(ln, run)])]
out = ['# TXE2-COST2 %s of fr.3251 f.87 (Opus 5.5, blind, crops + sheet + brief only)' % a.label, 'line\tpos\tsign']
for ln in sorted(lines):
    out += ['f87_%s\t%d\t%s' % (ln, i + 1, s) for i, s in enumerate(lines[ln])]
open(a.out, 'w').write('\n'.join(out) + '\n')
print(a.out, {k: len(v) for k, v in sorted(lines.items())})
