#!/usr/bin/env python3
"""RUN2-NXATL: align the c262 tile sequence (glyph_atlas cluster ids, reading order) to NX-RECUT's reconciled labels
(witness/c262rc_recon.tsv) line by line, by hard-EM Needleman-Wunsch: match score = log P(label | cluster) / P(label)
from the previous alignment, gap -GAP; starts from a proportional (diagonal) alignment. Writes the per-tile alignment
and a cluster -> provisional label table (majority label, support, purity). Provisional, grade M: the labels are one
reconciler's rulings and the alignment is not checked by eye.
usage: c262_align.py SEQUENCES.tsv RECON.tsv OUTDIR"""
import sys, csv, math, collections
seq_f, rec_f, outd = sys.argv[1:4]
SHUF = int(sys.argv[sys.argv.index('--shuffle')+1]) if '--shuffle' in sys.argv else None
GAP, ITERS = 2.0, 15
tiles = collections.defaultdict(list)
for r in csv.DictReader((l for l in open(seq_f) if not l.startswith('#')), delimiter='\t'):
    if r['leaf'] == 'c262': tiles[r['line']].append(r)
rec = {}
for ln in open(rec_f):
    if ln.startswith('#') or not ln.strip(): continue
    L, toks = ln.rstrip('\n').split('\t', 1); rec[L] = toks.split()
lines = sorted(rec)
if SHUF is not None:  # null: cluster ids permuted among the c262 tiles (counts kept), same EM
    import random; allc = [t['cluster'] for L in lines for t in tiles[L]]; random.Random(SHUF).shuffle(allc); k = 0
    for L in lines:
        for t in tiles[L]: t.update(cluster=allc[k]); k += 1
def nw(cs, ts, sc):
    n, m = len(cs), len(ts); D = [[0.0]*(m+1) for _ in range(n+1)]; B = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1): D[i][0] = -GAP*i; B[i][0] = 1
    for j in range(1, m+1): D[0][j] = -GAP*j; B[0][j] = 2
    for i in range(1, n+1):
        for j in range(1, m+1):
            opts = (D[i-1][j-1] + sc(cs[i-1], ts[j-1]), D[i-1][j] - GAP, D[i][j-1] - GAP)
            k = max(range(3), key=lambda q: opts[q]); D[i][j] = opts[k]; B[i][j] = k
    i, j, pairs = n, m, []
    while i or j:
        k = B[i][j] if i and j else (1 if i else 2)
        if k == 0: pairs.append((i-1, j-1)); i, j = i-1, j-1
        elif k == 1: pairs.append((i-1, None)); i -= 1
        else: pairs.append((None, j-1)); j -= 1
    return pairs[::-1]
# init: proportional
align = {}
for L in lines:
    cs = [t['cluster'] for t in tiles[L]]; ts = rec[L]
    align[L] = [(i, min(len(ts)-1, round(i*len(ts)/len(cs)))) for i in range(len(cs))]
for it in range(ITERS):
    cnt = collections.Counter(); cc = collections.Counter(); tc = collections.Counter()
    for L in lines:
        cs = [t['cluster'] for t in tiles[L]]
        for i, j in align[L]:
            if i is not None and j is not None: cnt[(cs[i], rec[L][j])] += 1; cc[cs[i]] += 1; tc[rec[L][j]] += 1
    V = len(tc) or 1; N = sum(tc.values())
    sc = lambda c, t: math.log((cnt[(c, t)] + 0.2) / (cc[c] + 0.2*V)) - math.log((tc[t] + 0.2) / (N + 0.2*V))
    new = {L: nw([t['cluster'] for t in tiles[L]], rec[L], sc) for L in lines}
    if new == align: break
    align = new
by0 = collections.defaultdict(collections.Counter)
for L in lines:
    for i, j in align[L]:
        if i is not None and j is not None: by0[tiles[L][i]['cluster']][rec[L][j]] += 1
pur = sum(c.most_common(1)[0][1] for c in by0.values()) / max(1, sum(sum(c.values()) for c in by0.values()))
print(f'weighted purity {pur:.3f}')
if SHUF is not None: sys.exit(0)
with open(f'{outd}/c262_tile_alignment.tsv', 'w') as f:
    f.write('line\ttile\tcluster\trecon_pos\trecon_label\n')
    for L in lines:
        for i, j in align[L]:
            f.write(f"{L}\t{tiles[L][i]['tile'] if i is not None else '-'}\t{tiles[L][i]['cluster'] if i is not None else '-'}\t"
                    f"{j+1 if j is not None else '-'}\t{rec[L][j] if j is not None else '-'}\n")
by = collections.defaultdict(collections.Counter)
for L in lines:
    for i, j in align[L]:
        if i is not None and j is not None: by[tiles[L][i]['cluster']][rec[L][j]] += 1
with open(f'{outd}/cluster_provisional_names.tsv', 'w') as f:
    f.write('# cluster -> provisional label from c262 tile position (RUN2-NXATL, grade M). support = c262 tiles aligned; purity = share of the majority label\n')
    f.write('cluster\tlabel\tsupport\tpurity\tother_labels\n')
    for c in sorted(by, key=lambda c: -sum(by[c].values())):
        (lab, n), tot = by[c].most_common(1)[0], sum(by[c].values())
        f.write(f"{c}\t{lab}\t{tot}\t{n/tot:.2f}\t{' '.join(f'{a}:{b}' for a, b in by[c].most_common()[1:])}\n")
m = sum(1 for L in lines for i, j in align[L] if i is not None and j is not None)
gi = sum(1 for L in lines for i, j in align[L] if j is None); gj = sum(1 for L in lines for i, j in align[L] if i is None)
print(f'iterations {it+1}; matched {m}, extra tiles {gi}, unmatched labels {gj}; clusters named {len(by)}')
