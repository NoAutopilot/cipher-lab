#!/usr/bin/env python3
"""VIV-LOOKALIKE (PREREG-VIVLOOKALIKE.md, rule DEDUP): drop the second copy of an s1/s2 crop-overlap block a reader wrote twice.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv_lookalike/dedup.py PAGE [PAGE ...]

Reads tx/<page>_pass{A,B}_c.tsv (the output of tx/viv63_clean.py, or the leaf's own clean step), writes
tx/viv_lookalike/<page>_pass{A,B}_c.tsv and tx/viv_lookalike/dedup_log.tsv (page, pass, line, k, junction index, block).
Scratch only: never writes tx/<page>_pass?_c.tsv, a rec file or a reading. Rule, fixed before any scan: exact X X with 4 <= k <= 12,
junction (first index of the second copy / row length) in [0.20, 0.80], longest k first (ties leftmost), repeat until none.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TX = os.path.dirname(HERE)
KMIN, KMAX, LO, HI = 4, 12, 0.20, 0.80


def find(toks):
    n, best = len(toks), None
    for k in range(min(KMAX, n // 2), KMIN - 1, -1):
        for i in range(0, n - 2 * k + 1):
            if toks[i:i + k] == toks[i + k:i + 2 * k] and LO <= (i + k) / n <= HI:
                return k, i
    return best


def dedup(toks):
    removed = []
    while True:
        f = find(toks)
        if not f:
            return toks, removed
        k, i = f
        removed.append((k, i + k, ' '.join(toks[i:i + k])))
        toks = toks[:i + k] + toks[i + 2 * k:]


def main(pages):
    log = []
    for page in pages:
        for p in 'AB':
            out = []
            for ln in open(os.path.join(TX, f'{page}_pass{p}_c.tsv'), encoding='utf-8'):
                if ln.startswith('row\t') or not ln.strip():
                    continue
                row, codes = (ln.rstrip('\n').split('\t', 1) + [''])[:2]
                toks, rem = dedup(codes.split())
                for k, j, blk in rem:
                    log.append(f'{page}\t{p}\t{row}\t{k}\t{j}\t{blk}')
                out.append(f'{row}\t{" ".join(toks)}')
            with open(os.path.join(HERE, f'{page}_pass{p}_c.tsv'), 'w', encoding='utf-8') as f:
                f.write('row\tcodes\n' + '\n'.join(out) + '\n')
    mode = 'a' if os.environ.get('DEDUP_APPEND') else 'w'
    with open(os.path.join(HERE, 'dedup_log.tsv'), mode, encoding='utf-8') as f:
        if mode == 'w':
            f.write('page\tpass\tline\tk\tjunction\tblock\n')
        f.write(''.join(l + '\n' for l in log))
    for l in log:
        print(l)
    print(len(log), 'blocks removed')


if __name__ == '__main__':
    main(sys.argv[1:])
