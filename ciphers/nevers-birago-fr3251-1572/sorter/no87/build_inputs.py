#!/usr/bin/env python3
"""BIR87-SORTER (4 Oct 2026): inputs for a small no.87 sign sorter (f.178r, f.178v, f.179r) whose piles are the owner's
own piles from the 4 Oct sort (../owner-sort-2026-10-04/settled_labels.tsv), so settled no.87 labels can feed
tools/interlinear_align.py against the clerk sheet (harvest/keyfit/RESULTS.md "Next").

1. Owner tiles -> atlas boxes. The owner sorted line-strip tiles (f117_L01_01, f144r_L03_02, f168_R03_06; boxes on the
   strips in ../../harvest/tx_decode/eye/open/sorter/owner-2026-10-03/signs.tsv). Each strip is a crop of the same
   Gallica region image the family atlas segmented (../../atlas/pages.json), so a tile's centre is shifted back to
   that image and matched to the atlas box (same page) that contains it, else the nearest box centre within 0.6 x the
   tile's height. Unmatched tiles (box empty in owner_map.tsv) and atlas boxes matched by two owner tiles (one atlas
   box over two strip tiles: ambiguous, dup=1) are not used.
2. Scope. A family is SPLIT when the owner made a new pile carrying its name (T45 -> T45-b); moving a tile into an
   existing pile alone does not count (nearly every family had one such move). No.87 boxes (atlas/topk/no87.tsv,
   k1 != '_') whose k1 is a split family are candidates; families are taken in descending no.87 count, skipping any
   that would take the total over CAP (250). The rest keep their atlas label and stay off the page (scope.tsv lists every family).
3. Piles = every owner pile (new_sign of a 'kept'/'moved' tile) that a tile of a kept family ended in, named exactly as
   in settled_labels.tsv. Reference tiles = the owner's tiles in that pile (any family), up to 6 shown (nearest the
   pile mean); they are marked "sorted by you" on the page (sign_sorter.py --refs) and are never in apply_labels.tsv.
4. Seed. Features are tools/glyph_atlas.py feats() (HOG + PCA + size ratios, unit scale) on the whole atlas bitmap set,
   the same space glyph_atlas classify uses. Pile distance = mean of the 3 nearest owner tiles in the pile (all of the
   owner's tiles in it, not only the 6 shown). Candidate piles for a no.87 tile = the owner piles reached from its
   k1/k2/k3 families among the kept families. Margin = (d2 - d1) / d1; tiles with margin < MARGIN go to focus.tsv,
   smallest first, at most 30.
No sign values anywhere. No network.

  python3 ciphers/nevers-birago-fr3251-1572/sorter/no87/build_inputs.py
writes signs.tsv, labels.tsv (no.87 + reference tiles, for sign_sorter.py), refs.tsv, apply_labels.tsv (no.87 only,
for sign_sorter_apply.py), focus.tsv, seed.tsv, scope.tsv, owner_map.tsv.
"""
import csv, json, os, sys
from collections import Counter, defaultdict
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent; T = HERE.parents[1]; ROOT = T.parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import glyph_atlas as ga   # noqa: E402

CAP, MARGIN, NFOCUS, NREF, KNN = 250, 0.06, 30, 6, 3
OWN = T / 'sorter' / 'owner-sort-2026-10-04'
OSIGNS = T / 'harvest/tx_decode/eye/open/sorter/owner-2026-10-03/signs.tsv'
A = T / 'atlas'


def rd(p):
    return list(csv.DictReader(open(p), delimiter='\t'))


def wr(p, cols, rows):
    with open(HERE / p, 'w') as f:
        f.write('\t'.join(cols) + '\n' + ''.join('\t'.join(str(r[c]) for c in cols) + '\n' for r in rows))


def strip_origin(page):
    """(atlas page, x0, y0): where a sorter strip sits in the atlas page's source image."""
    if page.startswith('f117_L'):        # ../../../birago-fr3252-1571-72/sorter/build_inputs.py strip(): manifest band, y-40
        band = int(page[6:]); im = ROOT / 'ciphers/birago-fr3252-1571-72/images/f117'
        es = [e for e in json.load(open(im / 'manifest.json'))['iiif_lines'] if e['band'] == band]
        return 'f117r', min(e['box'][0] for e in es), max(0, min(e['box'][1] for e in es) - 40)
    leaf, band = page.split('_L'); band = int(band)   # ../build_inputs.py strip(): Gallica coords minus region offset
    es = [e for e in json.load(open(T / 'harvest' / leaf / 'manifest.json'))['iiif_lines'] if e['band'] == band]
    ox, oy = (int(v) for v in es[0]['source_url'].split('/full/')[0].split('/')[-1].split(',')[:2])
    return leaf, min(e['box'][0] for e in es) - ox, min(e['box'][1] for e in es) - oy


def main():
    asg = rd(A / 'signs.tsv'); idx = {r['sid']: i for i, r in enumerate(asg)}
    bypage = defaultdict(list)
    for r in asg:
        bypage[r['page']].append(r)
    # 1. owner tile -> atlas box
    omap, origin = [], {}
    for s in rd(OSIGNS):
        if s['page'] not in origin:
            origin[s['page']] = strip_origin(s['page'])
        pg, ox, oy = origin[s['page']]
        x, y, w, h = (int(s[k]) for k in 'xywh'); cx, cy = ox + x + w / 2, oy + y + h / 2
        best, bd = '', 1e9
        for b in bypage[pg]:
            bx, by, bw, bh = (int(b[k]) for k in 'xywh')
            inside = bx <= cx <= bx + bw and by <= cy <= by + bh
            d = 0 if inside else ((bx + bw / 2 - cx) ** 2 + (by + bh / 2 - cy) ** 2) ** .5
            if d < bd:
                best, bd = b['sid'], d
        ok = bd <= 0.6 * h
        omap.append({'sid': s['sid'], 'atlas_page': pg, 'box': best if ok else '', 'dist_px': round(bd, 1)})
    nb = Counter(r['box'] for r in omap if r['box'])
    for r in omap:
        r['dup'] = int(nb.get(r['box'], 0) > 1)
    wr('owner_map.tsv', ['sid', 'atlas_page', 'box', 'dist_px', 'dup'], omap)
    o2a = {r['sid']: r['box'] for r in omap if r['box'] and not r['dup']}
    # 2. scope
    pub = {r['sid']: r for r in rd(OWN / 'labels_as_published.tsv')}
    st = [r for r in rd(OWN / 'settled_labels.tsv') if r['status'] in ('kept', 'moved') and r['new_sign']]
    orig = {r['sign'] for r in pub.values()}
    fam_piles = defaultdict(set)
    for r in st:
        fam_piles[pub[r['sid']]['family']].add(r['new_sign'])
    split = {f for f, ps in fam_piles.items() if any(p not in orig and p.rsplit('-', 1)[0] == f for p in ps)}
    n87 = [r for r in rd(A / 'topk/no87.tsv') if r['k1'] and r['k1'] != '_']
    cnt = Counter(r['k1'] for r in n87)
    keep, tot, scope = [], 0, []
    for f, n in cnt.most_common():
        why = 'not split'
        if f in split:
            if tot + n <= CAP and (not keep or tot + n <= CAP):
                keep.append(f); tot += n; why = 'on page'
            else:
                why = 'split, over cap'
        scope.append({'family': f, 'no87_tiles': n, 'owner_piles': '|'.join(sorted(fam_piles.get(f, ()))), 'scope': why})
    wr('scope.tsv', ['family', 'no87_tiles', 'owner_piles', 'scope'], scope)
    piles = sorted(set().union(*(fam_piles[f] for f in keep)))
    members = defaultdict(list)      # pile -> atlas boxes of the owner's tiles in it
    for r in st:
        if r['new_sign'] in piles and r['sid'] in o2a:
            members[r['new_sign']].append((r['sid'], o2a[r['sid']]))
    # 4. features in glyph_atlas's classify space
    X = ga.feats(np.load(A / 'bitmaps.npz')['signs'], asg)
    def pd(i, pile):
        d = sorted(float(np.linalg.norm(X[i] - X[idx[b]])) for _, b in members[pile])
        return float(np.mean(d[:KNN])) if d else 1e9
    tiles = [r for r in n87 if r['k1'] in keep]
    seed, labels, signs = [], [], []
    for r in tiles:
        fams = [r[k] for k in ('k1', 'k2', 'k3') if r.get(k) in keep]
        cands = sorted(set().union(*(fam_piles[f] for f in fams)) & set(members))
        ds = sorted((pd(idx[r['box']], p), p) for p in cands)
        d1, p1 = ds[0]; d2, p2 = ds[1] if len(ds) > 1 else (1e9, '')
        m = (d2 - d1) / d1 if d1 else 0
        seed.append({'sid': r['box'], 'atlas': r['k1'], 'seed': p1, 'd1': round(d1, 3), 'second': p2,
                     'd2': round(d2, 3) if p2 else '', 'margin': round(m, 3)})
        labels.append({'sid': r['box'], 'sign': p1, 'family': r['k1']})
    wr('seed.tsv', ['sid', 'atlas', 'seed', 'd1', 'second', 'd2', 'margin'], seed)
    wr('apply_labels.tsv', ['sid', 'sign', 'family'], labels)
    near = sorted((s for s in seed if s['second'] and s['margin'] < MARGIN), key=lambda s: s['margin'])[:NFOCUS]
    with open(HERE / 'focus.tsv', 'w') as f:
        f.write(''.join(f"{s['sid']}\tAbout as close to two of your piles; {s['seed']} or {s['second']}?\n" for s in near))
    refs = []
    for p in piles:
        ms = members[p]
        if not ms:
            continue
        c = np.mean([X[idx[b]] for _, b in ms], axis=0)
        for sid, b in sorted(ms, key=lambda m: float(np.linalg.norm(X[idx[m[1]]] - c)))[:NREF]:
            refs.append({'sid': b, 'sign': p, 'family': pub[sid]['family'], 'owner_sid': sid})
    wr('refs.tsv', ['sid', 'sign', 'family', 'owner_sid'], refs)
    wr('labels.tsv', ['sid', 'sign', 'family'], labels + refs)
    used = {r['sid'] for r in labels + refs}
    signs = [{'sid': r['sid'], 'page': r['page'], 'x': r['x'], 'y': r['y'], 'w': r['w'], 'h': r['h']} for r in asg if r['sid'] in used]
    wr('signs.tsv', ['sid', 'page', 'x', 'y', 'w', 'h'], signs)
    empty = [p for p in piles if not members[p]]
    print(f'owner tiles mapped {len(o2a)}/{len(omap)}; split families {len(split)}; on page {keep} = {len(tiles)} no.87 tiles; '
          f'{len(piles)} owner piles ({len(empty)} with no mapped tile: {empty}); {len(refs)} reference tiles; focus {len(near)}')


if __name__ == '__main__':
    main()
