#!/usr/bin/env python3
"""TXE4-2 step 2d inputs (read-free): from the f.130 passes aligned per line by tools/reconcile_passes.py --method nw --keep-dots
--keep-dots (tiles/reads/wideA.tsv, wideB.tsv -> ciphertext_draft.tsv, disagreements.tsv), write for box_token_align:
  tiles/read.tsv      line, pos, sign   -- pass A's tokens (labels mapped through dint128_label_map.tsv) at pass-A positions
  tiles/read_alt.tsv  line, pos, sign   -- pass B's token at each aligned pass-A position where the two differ
  tiles/keep.tsv      line, pos         -- the pass-A positions where A and B carry the same label (agreed positions)
    python3 line_reads.py [TILE_DIR]"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(HERE, sys.argv[1] if len(sys.argv) > 1 else 'tiles')
draft = list(csv.DictReader(open(os.path.join(T, 'reads', 'ciphertext_draft.tsv')), delimiter='\t'))
dis = {(r['line'], int(r['col'])): r for r in csv.DictReader(open(os.path.join(T, 'reads', 'disagreements.tsv')), delimiter='\t')}
wideA = {l.split('\t')[0]: l.rstrip('\n').split('\t')[1].split() for l in open(os.path.join(T, 'reads', 'wideA.tsv'))}
read, alt, keep = [], [], []
posA = {}
for r in draft:
    ln, col = r['line'], int(r['position'])
    d = dis.get((ln, col))
    a = d['A'] if d else r['sign']
    b = d['B'] if d else r['sign']
    if a == '-':
        continue                              # a column where only B has a token: no pass-A position
    posA[ln] = posA.get(ln, 0) + 1; p = posA[ln]
    assert wideA[ln][p - 1] == a, (ln, p, wideA[ln][p - 1], a)
    read.append((ln, p, a))
    if b == '-':
        continue
    if a == b:
        keep.append((ln, p))
    else:
        alt.append((ln, p, b))
for ln in wideA:
    assert posA[ln] == len(wideA[ln]), ln
for fn, rows, cols in (('read.tsv', read, 'line\tpos\tsign'), ('read_alt.tsv', alt, 'line\tpos\tsign'), ('keep.tsv', keep, 'line\tpos')):
    with open(os.path.join(T, fn), 'w') as f:
        f.write(cols + '\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in rows))
print(f'read {len(read)} tokens; alt {len(alt)}; keep (agreed) {len(keep)}; per line ' +
      ', '.join(f'{ln[5:]} {sum(1 for l, _ in keep if l == ln)}/{len(wideA[ln])}' for ln in wideA))
