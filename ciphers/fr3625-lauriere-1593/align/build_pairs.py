#!/usr/bin/env python3
"""Build PAIRS.tsv for tools/interlinear_align.py from fr3625 no.10's seven glossed runs.

Each raw cipher token (whatever its exact string -- pure numeral, symbol-only like XX/close-cross,
or a mixed numeral+letter/mark group like 54y+ or 56nDelta) is mapped to a unique 3-digit surrogate
number so that classify_token() in interlinear_align.py treats every group uniformly as a 'num'
token (1-3 digits), giving the DP full freedom (0..14 plain letters) via floor=0. Without this,
classify_token's digitish() heuristic would split our symbol-heavy groups across its 'num' /
'doubtful' / 'clear' branches inconsistently, breaking cross-run agreement counting for tokens
that are not itself majority-digit (XX, a lone sign) or that trip the OCR-repair 'doubtful' path
(54y+, 56nDelta) meant for Thurloe's OCR'd print, not our by-hand manuscript notation.

Usage: python3 build_pairs.py RUNS_TSV PAIRS_OUT TOKEN_MAP_OUT
  RUNS_TSV: run_id <TAB> plain_gloss <TAB> cipher_tokens(space sep)
"""
import csv
import sys

def main(runs_path, pairs_out, map_out):
    rows = []
    with open(runs_path, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if not line or line.startswith('#'):
                continue
            run_id, plain, cipher = line.split('\t')
            rows.append((run_id, plain, cipher.split()))
    token_map = {}
    next_id = 100
    for _, _, toks in rows:
        for t in toks:
            if t not in token_map:
                token_map[t] = next_id
                next_id += 1
    with open(pairs_out, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['plain_line', 'plain_raw', 'cipher_line', 'cipher_raw'])
        for run_id, plain, toks in rows:
            surrogate = ' '.join(str(token_map[t]) for t in toks)
            w.writerow([run_id, plain, run_id, surrogate])
    with open(map_out, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['surrogate', 'raw_token'])
        for t, v in sorted(token_map.items(), key=lambda kv: kv[1]):
            w.writerow([v, t])
    print('%d runs, %d distinct tokens -> %s, %s' % (len(rows), len(token_map), pairs_out, map_out))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
