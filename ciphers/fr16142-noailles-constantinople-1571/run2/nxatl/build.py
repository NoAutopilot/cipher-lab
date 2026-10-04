"""Filtered cipher-only atlas dir atlf/ from atl/: keep.json tiles minus clear lines; reading order; global x."""
import csv, json, os, shutil, collections, numpy as np
src, dst = 'atl', 'atlf'
os.makedirs(dst, exist_ok=True)
if not os.path.exists(f'{dst}/crops'): os.symlink(os.path.abspath(f'{src}/crops'), f'{dst}/crops')
shutil.copy(f'{src}/pages.json', dst)
keep = set(json.load(open(f'{src}/keep.json')))
CLEAR = {('c510', L) for L in ('L01', 'L02', 'L03', 'L04')} | {('c516', L) for L in ('L04', 'L05', 'L20', 'L21', 'L22', 'L23')}
MIXED_CUT = {('c510', 'L05'): 22}   # tiles before index 22 (last wide cursive tile at 21) are the clear lead-in
SEGSTEP = {'c262': 1800 - 100}      # NX-RECUT crops --max-width 1800 --overlap 100
rows = list(csv.DictReader(open(f'{src}/signs.tsv'), delimiter='\t'))
bm = np.load(f'{src}/bitmaps.npz')
idx = {r['sid']: i for i, r in enumerate(rows)}
per = collections.defaultdict(list)
for r in rows:
    if r['sid'] not in keep: continue
    leaf, L, seg = r['page'].rsplit('_', 2)
    r['gx'] = int(r['x']) + (int(seg[1:]) - 1) * SEGSTEP.get(leaf, 2300)
    per[(leaf, L)].append(r)
out, clear_log = [], []
for (leaf, L) in sorted(per):
    v = sorted(per[(leaf, L)], key=lambda r: r['gx'])
    if (leaf, L) in CLEAR: clear_log.append((leaf, L, len(v), 'clear')); continue
    cut = MIXED_CUT.get((leaf, L), 0)
    if cut: clear_log.append((leaf, L, cut, 'clear lead-in tiles dropped'))
    for p, r in enumerate(v[cut:], 1):
        r['leaf'], r['L'], r['lpos'] = leaf, L, p
        out.append(r)
cols = list(rows[0].keys())[:12]
with open(f'{dst}/signs.tsv', 'w') as f:
    f.write('\t'.join(cols) + '\n')
    for r in out: f.write('\t'.join(r[c] for c in cols) + '\n')
mk = list(csv.DictReader(open(f'{src}/marks.tsv'), delimiter='\t'))
kept_sids = {r['sid'] for r in out}
mk2 = [m for m in mk if m['sid'] in kept_sids]
with open(f'{dst}/marks.tsv', 'w') as f:
    mc = list(mk[0].keys()); f.write('\t'.join(mc) + '\n')
    for m in mk2: f.write('\t'.join(m[c] for c in mc) + '\n')
midx = {m['mid']: i for i, m in enumerate(mk)}
np.savez_compressed(f'{dst}/bitmaps.npz', signs=bm['signs'][[idx[r['sid']] for r in out]],
                    marks=bm['marks'][[midx[m['mid']] for m in mk2]] if mk2 else np.zeros((0, 48, 48), np.uint8))
json.dump({r['sid']: [r['leaf'], r['L'], r['lpos'], r['gx']] for r in out}, open(f'{dst}/order.json', 'w'))
json.dump(clear_log, open(f'{dst}/clear_log.json', 'w'))
c = collections.Counter(r['leaf'] for r in out); print(dict(c), 'total', len(out), 'marks', len(mk2))
for x in clear_log: print(x)
