#!/usr/bin/env python3
"""SORT-A2o (10 Oct 2026): sign sorter inputs for the OLD-O2 line crops of leaves 4 and 7 (images/crops_O2: rot_L4a, rot_L4b,
rot_L7a, rot_L7b, the four levelled regions; 75 cipher lines). One tile = one ink group (tools/sorter_recut.py), cut from the
levelled region with a flat trace through each line's OLD-O2 centre (manifest.json params.centres_given), neighbouring lines
excluded by the cutter's own row test. Starting piles are value-blind shape clusters (no reader column is given: no machine label
reaches the page). Focus = tiles near the places where OLD-O2's two blind passes (passL_OLDO2_{L4,L7}_{A,B}) disagree, found by an
edit alignment of each line's normalised string and a proportional map onto the line's tiles; the page text names no value.
  python3 ciphers/na-oldenbarnevelt-2442-1605/sorter/a2o/cut.py [--debug DIR]
"""
import argparse, csv, json, sys
from collections import defaultdict
from pathlib import Path
import numpy as np
from PIL import Image
S = Path(__file__).resolve().parent; T = S.parents[1]
sys.path.insert(0, str(T.parents[1] / 'tools')); sys.path.insert(0, str(T / 'scripts'))
import sorter_recut as sr
from decode_L457 import sn, pass_file
NFOCUS = 80
NEIGH = 2
PERLINE = 3
CFG = sr.Cfg(pitch=110, half=75, xmin=10, rel=0.76, nclu=30, per_clu=2, nfocus=0)
REGIONS = ['rot_L4a', 'rot_L4b', 'rot_L7a', 'rot_L7b']

def edit_positions(a, b):
    """indices into a where an edit op against b falls (substitution, deletion; insertions map to the next a index)."""
    n, m = len(a), len(b); D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): D[i][0] = i
    for j in range(m + 1): D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + (a[i-1] != b[j-1]))
    i, j, out = n, m, []
    while i or j:
        if i and j and D[i][j] == D[i-1][j-1] + (a[i-1] != b[j-1]):
            if a[i-1] != b[j-1]: out.append(i - 1)
            i, j = i - 1, j - 1
        elif i and D[i][j] == D[i-1][j] + 1: out.append(i - 1); i -= 1
        else: out.append(min(i, n - 1)); j -= 1
    return sorted(set(out))

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--debug'); a = ap.parse_args()
    man = json.load(open(T / 'images/crops_O2/manifest.json'))['iiif_lines']
    ims = {r: np.array(Image.open(T / 'images/crops_O2' / f'{r}.jpg').convert('L')) for r in REGIONS}
    W = max(i.shape[1] for i in ims.values()); parts, off = [], {}; y = 0
    for r in REGIONS:
        g = ims[r]; pad = np.full((g.shape[0], W), 255, np.uint8); pad[:, :g.shape[1]] = g; parts.append(pad); off[r] = y; y += g.shape[0]
    grey = np.vstack(parts); Image.fromarray(grey).save(S / 'region.jpg', quality=70)
    pages, traces = [], []
    for e in man:
        r = e['source_file'][:-4]; c = e['params']['centres_given'][e['band'] - 1]
        pages.append(e['crop'][:-4]); traces.append(np.full(W, off[r] + c, float))
    tiles, _ = sr.run(grey, traces, pages, [[] for _ in pages], [[] for _ in pages], S, S / 'pages', CFG,
                      fallback=['unsorted'] * len(pages), debug=a.debug, region_image=str((S / 'region.jpg').relative_to(T.parents[1])))
    # focus: tiles near the OLD-O2 pass A/B edit positions
    lines = {}
    for lf in ('L4', 'L7'):
        for side in 'AB':
            for r in csv.DictReader(open(pass_file(lf, side, 'O2')), delimiter='\t'):
                if r['token'] != 'EMPTY': lines.setdefault(r['line'], {}).setdefault(side, []).append(sn(r['token'], 'o4'))
    bypage = defaultdict(list)
    for t in tiles: bypage[t['page']].append(t)
    cand = []
    for ln, d in lines.items():
        A, B = ''.join(d.get('A', [])), ''.join(d.get('B', []))
        ts = sorted(bypage.get(ln, []), key=lambda t: t['x'])
        if not A or not B or not ts: continue
        pos = edit_positions(A, B); sel = set()
        for p in pos: sel.add(min(len(ts) - 1, int((p + .5) * len(ts) / len(A))))
        cand.append((len(pos), ln, [ts[i]['sid'] for i in sorted(sel)]))
    cand.sort(key=lambda c: (-c[0], c[1])); focus = []
    for n, ln, sids in cand:      # at most PERLINE tiles per line (evenly spread over its split places), most-split lines first
        step = max(1, len(sids) // PERLINE) if len(sids) > PERLINE else 1
        for s in sids[::step][:PERLINE]:
            if len(focus) < NFOCUS: focus.append((s, ln))
    focus.sort()
    # keep the page phone-sized: the focus tiles and their two neighbours each side on the line (2537 tiles = 8 MB); the rest of the
    # cut stays reproducible by raising NEIGH. Piles are the value-blind shape clusters.
    keep = set()
    for s, ln in focus:
        ts = sorted(bypage[ln], key=lambda t: t['x']); i = [t['sid'] for t in ts].index(s)
        keep.update(t['sid'] for t in ts[max(0, i - NEIGH):i + NEIGH + 1])
    tiles = [t for t in tiles if t['sid'] in keep]
    for t in tiles: t['sign'] = t['family'] = 'shape-%02d' % t['cluster']
    for name, keys in (('signs', ['sid', 'page', 'x', 'y', 'w', 'h']), ('labels', ['sid', 'sign', 'family']), ('clusters', ['sid', 'cluster', 'col', 'dx'])):
        with open(S / f'{name}.tsv', 'w') as o:
            o.write('\t'.join(keys) + '\n'); o.writelines('\t'.join(str(t[k]) for k in keys) + '\n' for t in tiles)
    used = {t['page'] for t in tiles}
    for p in (S / 'pages').glob('*.jpg'):
        if p.stem not in used: p.unlink()
    with open(S / 'focus.tsv', 'w') as o:
        for s, ln in focus:
            o.write(f"{s}\tLine {ln}: the two blind readers split near here. Which sign is this tile? (If the box is off, Fix the cut; if it is two signs or part of one, BAD-CUT.)\n")
    print(len(tiles), 'tiles on', len(pages), 'lines;', len(focus), 'focus tiles from', len(cand), 'lines with two passes')

if __name__ == '__main__': main()
