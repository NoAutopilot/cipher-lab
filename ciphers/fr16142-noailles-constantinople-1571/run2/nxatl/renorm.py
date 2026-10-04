"""Re-express rh, rw, dy in units of the LEAF's median sign height (median of per-strip estimates), not each strip's
own estimate, which collapses to 6-34 px on strips with blots, flourishes or little ink. Rewrites atl/signs.tsv in place
(original kept as signs_strip.tsv)."""
import csv, json, statistics, shutil, os
p = json.load(open('atl/pages.json'))
leafmh = {}
for k, v in p.items(): leafmh.setdefault(k.rsplit('_', 2)[0], []).append(v['median_h'])
leafmh = {k: statistics.median(v) for k, v in leafmh.items()}
print({k: round(v, 1) for k, v in leafmh.items()})
if not os.path.exists('atl/signs_strip.tsv'): shutil.copy('atl/signs.tsv', 'atl/signs_strip.tsv')
rows = list(csv.DictReader(open('atl/signs_strip.tsv'), delimiter='\t'))
cols = list(rows[0].keys())
for r in rows:
    mh_s = p[r['page']]['median_h']; MH = leafmh[r['page'].rsplit('_', 2)[0]]
    r['rh'] = f"{int(r['h'])/MH:.3f}"; r['rw'] = f"{int(r['w'])/MH:.3f}"; r['dy'] = f"{float(r['dy'])*mh_s/MH:.3f}"
with open('atl/signs.tsv', 'w') as f:
    f.write('\t'.join(cols) + '\n')
    for r in rows: f.write('\t'.join(r[c] for c in cols) + '\n')
