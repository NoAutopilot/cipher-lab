#!/usr/bin/env python3
"""TXE2-COUNT (PREREG-txeng2-3 X12) helpers, job-local.

  python3 count_score.py gate      # step 1 read-free score: share of lines whose blind count is within +-1 of the
                                   # truth line length (rows per line in the item's *.truth.tsv); gate >= 0.8 pooled
  python3 count_score.py convert   # step 2: blind reads -> tx_bench format (outputs/<item>/passCOUNT.tsv), the same
                                   # joining rules as build_dint128.py (CLEAR rows dropped, segments joined per line)
                                   # and build_ceppo.py write_out (passage -> f87_Lnn)
The truth is read only by 'gate', run after count_*.tsv are committed; never by a reader.
"""
import csv, os, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
BT = os.path.normpath(os.path.join(HERE, '..', '..'))
ITEMS = {  # item: (count file, truth file, line-id prefix, step-2 read file)
    'dint-f128-print': ('count_dint.tsv', 'dint-f128-print.truth.tsv', 'f128_', 'read_dint.tsv'),
    'ceppo-f87-S': ('count_f87.tsv', 'ceppo-f87-S.truth.tsv', 'f87_', 'read_f87.tsv'),
}


def rd(p):
    with open(p) as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def gate():
    tot = ok = 0
    print('item\tline\tcount\ttruth_len\tdiff\twithin1')
    for item, (cf, tf, pre, _) in ITEMS.items():
        tl = Counter(r['line'] for r in rd(os.path.join(BT, tf)))
        for r in rd(os.path.join(HERE, cf)):
            if '_s' in r['line']:
                continue
            ln = pre + r['line']
            c = int(r['count']); t = tl[ln]; w = abs(c - t) <= 1
            tot += 1; ok += w
            print('%s\t%s\t%d\t%d\t%+d\t%s' % (item, ln, c, t, c - t, 'yes' if w else 'no'))
    share = ok / tot
    print('pooled within +-1: %d/%d = %.3f; gate >= 0.8: %s' % (ok, tot, share, 'MET' if share >= 0.8 else 'FAIL read-free'))
    return 0 if share >= 0.8 else 3


def convert():
    for item, (_, _, pre, rf) in ITEMS.items():
        p = os.path.join(HERE, rf)
        if not os.path.exists(p):
            print('missing', rf); continue
        lines = defaultdict(list)
        for r in rd(p):
            if 'gloss' in r:  # dint format (pass_instructions.md)
                if r['gloss'].startswith('CLEAR:'):
                    continue
                lines[pre + r['line']] += [x for x in r['signs'].split() if x != '-']
            else:  # f87 format (blind_pass_brief.md)
                lines[pre + r['passage']].append(r['sign_id'])
        od = os.path.join(BT, 'outputs', item); os.makedirs(od, exist_ok=True)
        with open(os.path.join(od, 'passCOUNT.tsv'), 'w') as f:
            f.write('# TXE2-COUNT step-2 blind Opus read with counts in the brief (PREREG-txeng2-3 X12), from %s\n' % rf)
            f.write('line\tpos\tsign\n')
            for ln in sorted(lines):
                for i, s in enumerate(lines[ln]):
                    f.write('%s\t%d\t%s\n' % (ln, i + 1, s))
        print(item, {k: len(v) for k, v in sorted(lines.items())})


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
        print(__doc__); sys.exit(0)
    sys.exit({'gate': gate, 'convert': convert}[sys.argv[1]]() or 0)
