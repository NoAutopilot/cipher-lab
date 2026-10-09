#!/usr/bin/env python3
"""TXE2-COST: convert a reader TSV (pass_instructions format) to tx_bench format, the PREREG-dint128 rule:
per physical line, every non-CLEAR row's signs in order, '-' dropped, nothing else edited
(a NEW: label whose description holds spaces inside parentheses is kept as one sign).
    python3 convert.py READ.tsv [READ2.tsv ...] --out OUT.tsv --label 'arm a'"""
import argparse, csv
from collections import defaultdict
ap = argparse.ArgumentParser(); ap.add_argument('reads', nargs='+'); ap.add_argument('--out', required=True)
ap.add_argument('--label', default=''); a = ap.parse_args()
lines = defaultdict(list)
for p in a.reads:
    with open(p, newline='') as f:
        for r in csv.DictReader((l for l in f if not l.startswith('#') and l.strip()), delimiter='\t'):
            if (r.get('gloss') or '').startswith('CLEAR:'):
                continue
            toks = []
            for x in (r.get('signs') or '').split():
                # a NEW:<description> with spaces inside parentheses is one sign (reader wrote "NEW:B-like (B with crossbar)")
                if toks and toks[-1].startswith('NEW:') and toks[-1].count('(') > toks[-1].count(')'):
                    toks[-1] += ' ' + x
                else:
                    toks.append(x)
            lines[r['line'].strip()] += [x for x in toks if x != '-']
out = ['# TXE2-COST %s of fr.3621 f.128r (Opus 5.5, blind, crops + brief only), rows joined per line' % a.label, 'line\tpos\tsign']
for ln in sorted(lines):
    out += ['f128_%s\t%d\t%s' % (ln, i + 1, s) for i, s in enumerate(lines[ln])]
open(a.out, 'w').write('\n'.join(out) + '\n')
print(a.out, {k: len(v) for k, v in sorted(lines.items())})
