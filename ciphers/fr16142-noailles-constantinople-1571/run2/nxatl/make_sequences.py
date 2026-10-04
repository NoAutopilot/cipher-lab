#!/usr/bin/env python3
"""RUN2-NXATL: write sequences.tsv (reading order) and sign_counts.tsv from a glyph_atlas run.
usage: make_sequences.py ATLAS_DIR OUTDIR [--check]
ATLAS_DIR holds classify_all.tsv (glyph_atlas classify --page all --topk 3 with labels = cluster ids) and order.json
(tile -> leaf, line, position, x along the line), both written by regen.sh. --check: exit 1 if the committed files differ; --check --tolerant (regen.sh adds it when a
re-fetched canvas's sha1 differs from source_manifest.json): per-leaf tile counts within 1%."""
import sys, csv, json, collections, io
d, outd = sys.argv[1], sys.argv[2]
order = json.load(open(f'{d}/order.json'))
rows = list(csv.DictReader(open(f'{d}/classify_all.tsv'), delimiter='\t'))
for r in rows: r['leaf'], r['L'], r['lpos'], r['gx'] = order[r['box']]
rows.sort(key=lambda r: (int(r['leaf'][1:]), r['L'], r['lpos']))
cols = ['leaf', 'line', 'pos', 'tile', 'x_line', 'cluster', 'marks', 'k1', 'd1', 's1', 'k2', 'd2', 's2', 'k3', 'd3', 's3']
seq = io.StringIO()
seq.write('# RUN2-NXATL 4 Oct 2026: fr.16142 c510-516 cipher lines (+ c262 NX-RECUT block) as glyph_atlas tiles. cluster = k-means id\n'
          '# (deliberate over-split, k=120); k1-k3 = kNN top-3 cluster ids with distance and vote share; marks = mark clusters above.\n'
          '# Tiles, not signs: on c262 tiles/reconciled signs = 403/384 (1.05). No sign is named here; see cluster_provisional_names.tsv.\n')
seq.write('\t'.join(cols) + '\n')
for r in rows:
    v = dict(leaf=r['leaf'], line=r['L'], pos=r['lpos'], tile=r['box'], x_line=r['gx'], cluster=r['cluster_code'], marks=r['marks'],
             **{k: r[k] for k in ('k1', 'd1', 's1', 'k2', 'd2', 's2', 'k3', 'd3', 's3')})
    seq.write('\t'.join(str(v[c]) for c in cols) + '\n')
cnt = collections.Counter(r['leaf'] for r in rows); ln = collections.defaultdict(set)
for r in rows: ln[r['leaf']].add(r['L'])
sc = io.StringIO(); sc.write('leaf\tcipher_lines\ttiles\test_signs_at_c262_ratio_1.05\n')
for lf in sorted(cnt, key=lambda x: int(x[1:])):
    sc.write(f"{lf}\t{len(ln[lf])}\t{cnt[lf]}\t{round(cnt[lf]/1.0495)}\n")
tot = sum(v for k, v in cnt.items() if k != 'c262'); sc.write(f"c510-516\t{sum(len(ln[k]) for k in ln if k!='c262')}\t{tot}\t{round(tot/1.0495)}\n")
outs = {'sequences.tsv': seq.getvalue(), 'sign_counts.tsv': sc.getvalue()}
if '--check' in sys.argv and '--tolerant' in sys.argv:
    # Gallica re-encodes some canvases between fetches (c513, c514 on 4 Oct 2026; source_manifest.json), so a refetch is not
    # byte-stable: then each leaf's tile count must be within 1% of the committed count.
    old = {l.split('\t')[0]: int(l.split('\t')[2]) for l in open(f'{outd}/sign_counts.tsv').read().splitlines()[1:]}
    new = {l.split('\t')[0]: int(l.split('\t')[2]) for l in sc.getvalue().splitlines()[1:]}
    bad = [f'{k} {old[k]}->{new.get(k)}' for k in old if abs(new.get(k, 0) - old[k]) > 0.01 * old[k]]
    print('tolerant check: ' + ('FAIL ' + '; '.join(bad) if bad else 'OK ' + ' '.join(f'{k} {old[k]}->{new[k]}' for k in old)))
    sys.exit(1 if bad else 0)
if '--check' in sys.argv:
    bad = [f for f, t in outs.items() if open(f'{outd}/{f}').read() != t]
    print('stale: ' + ' '.join(bad) if bad else 'check OK'); sys.exit(1 if bad else 0)
for f, t in outs.items(): open(f'{outd}/{f}', 'w').write(t)
print(sc.getvalue())
