#!/usr/bin/env python3
"""Reformat pass_a/pass_b TSVs (page, block, line, pos, token) into the 'line pos sign'
convention tools/reconcile_passes.py's long_fmt detection requires (head[0] == 'line').
One block per leaf here, so the pass's own 'line' column is already a unique per-leaf id.
Usage: python3 reformat_for_reconcile.py IN.tsv OUT.tsv
"""
import csv, sys

def main(argv):
    inp, out = argv[1], argv[2]
    with open(inp, encoding='utf-8') as f:
        rows = list(csv.reader(f, delimiter='\t'))
    head = rows[0]
    i_line, i_pos, i_tok = head.index('line'), head.index('pos'), head.index('token')
    with open(out, 'w', encoding='utf-8') as f:
        f.write('line\tpos\tsign\n')
        for r in rows[1:]:
            f.write(f'{r[i_line]}\t{r[i_pos]}\t{r[i_tok]}\n')
    print(f'wrote {out}: {len(rows) - 1} rows')

if __name__ == '__main__':
    main(sys.argv)
