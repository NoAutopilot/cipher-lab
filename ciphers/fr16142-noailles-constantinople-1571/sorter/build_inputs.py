#!/usr/bin/env python3
"""N4-NXS (4 Oct 2026): build the sign-sorter inputs for fr.16142 c510-516 from RUN2's outputs.

  python3 build_inputs.py WORKDIR OUTDIR   (run from the repo root, after run2/nxatl/regen.sh WORKDIR)

1. topk.tsv: WORKDIR/atlf/classify_all.tsv rows for c510-516 (tile geometry from the regenerated segmentation), with
   code / cluster_code / k1-k3 / s1-s3 replaced by the COMMITTED run2/nxatl/sequences.tsv values, so pile and cluster
   ids are the committed atlas's (labels_clusterid.json, clusters.tsv). Tiles absent from either side are dropped and
   counted (Gallica re-encodes c511/c513 on refetch, so a few tile ids differ).
2. focus.tsv: sid<TAB>question, from run2/nxta/focus.tsv (example positions, c510), run2/nxtb/focus.tsv (c516) and
   run2/nxtb/c515/disagreements.tsv (c515: one row per label pair, its first column, the same rule NXTB used for c516).
   Kept: every NXTA example, NXTB pairs split on 2+ columns, c515 pairs split on 3+ (the box stays under ~100 tiles).
   A reader (line, column) is placed on an atlas tile by (a) the atlas line whose crop box y-centre on the same native
   canvas is nearest the reader crop's, then (b) the tile at the same fraction of the line (column / columns in the
   readers' alignment). This is approximate (about +-2 tiles); the page's focus note says so. Question text:
   '<candidates>? (<reader line>#<column>)', 'xN' = alignment columns the readers split on for that pair.
"""
import csv, json, os, sys
from collections import defaultdict
W, OUT = sys.argv[1], sys.argv[2]
R = 'ciphers/fr16142-noailles-constantinople-1571/run2'

def tsv(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))

seq = {r['tile']: r for r in tsv(f'{R}/nxatl/sequences.tsv') if r['leaf'] != 'c262'}
rows = tsv(f'{W}/atlf/classify_all.tsv')
hdr = list(rows[0].keys())
kept, drop_regen = [], 0
for r in rows:
    if not r['page'].startswith('c51'):
        continue
    s = seq.get(r['box'])
    if s is None:
        drop_regen += 1; continue
    r['code'] = r['cluster_code'] = s['cluster']
    for i in '123':
        r['k' + i], r['d' + i], r['s' + i] = s['k' + i], s['d' + i], s['s' + i]
    kept.append(r)
have = {r['box'] for r in kept}
drop_seq = sum(1 for t in seq if t not in have)
os.makedirs(OUT, exist_ok=True)
with open(f'{OUT}/topk.tsv', 'w', newline='') as f:
    w = csv.DictWriter(f, hdr, delimiter='\t'); w.writeheader(); w.writerows(kept)

# atlas lines: leaf -> [(ycentre, line, [tiles in reading order])]
amani = json.load(open(f'{W}/crops/manifest.json'))['iiif_lines']
ay = {}
for e in amani:
    if e['crop'].endswith('_s1.jpg'):
        b = e['box']; ay[e['crop'][:-7]] = (b[1] + b[3]) / 2
lines = defaultdict(list)
for t, s in seq.items():
    if t in have:
        lines[(s['leaf'], s['line'])].append((int(s['pos']), t))
atl = defaultdict(list)
for (leaf, line), ts in lines.items():
    atl[leaf].append((ay[f'{leaf}_{line}'], line, [t for _, t in sorted(ts)]))

def reader_y(manifest):
    m = json.load(open(manifest))['iiif_lines']
    return {e['crop'][:-7]: (e['box'][1] + e['box'][3]) / 2 for e in m if e['crop'].endswith('_s1.jpg')}

def ncols(p):
    return {r['line']: int(r['columns']) for r in tsv(p)}

ry = {**reader_y(f'{R}/nxta/crops_manifest.json'), **reader_y(f'{R}/nxtb/crops/manifest.json')}
cols = {**ncols(f'{R}/nxta/agreement.tsv'), **ncols(f'{R}/nxtb/agreement.tsv'), **ncols(f'{R}/nxtb/c515/agreement.tsv')}

def place(rline, col):
    leaf = rline[:4]
    y = ry[rline]
    _, aline, ts = min(atl[leaf], key=lambda a: abs(a[0] - y))
    i = min(len(ts) - 1, max(0, round((col - 0.5) / cols[rline] * len(ts) - 0.5)))
    return ts[i], aline

focus, seen = [], set()
def add(rline, col, q):
    if rline not in ry or rline not in cols:
        return
    sid, aline = place(rline, col)
    if sid in seen:
        return
    seen.add(sid)
    focus.append((sid, f'{q} ({rline}#{col})'))

for r in tsv(f'{R}/nxta/focus.tsv'):
    for p in r['example positions (line#col in disagreements.tsv)'].split():
        rl, c = p.split('#')
        add(rl, int(c), f"{r['family']}: {r['candidate labels'].replace(' ', '')}?")
for r in tsv(f'{R}/nxtb/focus.tsv'):
    if int(r['columns_split']) < 2:   # singletons left out: the box must stay under ~100 tiles (test_qa phone height)
        continue
    rl, c = r['example_line_col'].split(':')
    add(rl, int(c), f"{r['sign_a']} or {r['sign_b']}? x{r['columns_split']}")
pairs = {}
for r in tsv(f'{R}/nxtb/c515/disagreements.tsv'):
    k = tuple(sorted((r['A'] or '-', r['B'] or '-')))
    pairs.setdefault(k, [0, r['line'], int(r['col'])])[0] += 1
for (a, b), (n, rl, c) in sorted(pairs.items(), key=lambda kv: -kv[1][0]):
    if n >= 3:
        add(rl, c, f'{a} or {b}? x{n}')
with open(f'{OUT}/focus.tsv', 'w') as f:
    for sid, q in focus:
        f.write(f'{sid}\t{q}\n')
print(f'topk: {len(kept)} tiles (dropped {drop_regen} regen-only, {drop_seq} committed-only); focus: {len(focus)} tiles')
