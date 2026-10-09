#!/usr/bin/env python3
"""UNA-NEVBIR (9 Oct 2026): two-pass 0.8 + atlas 0.2 lattices for f.144r, f.168 and fr.3252 f.117r (PREREG-UNA-NEVBIR.md).
Box -> position map is label-blind: each line-read position's line-strip sorter tile is placed in source-image
coordinates by its strip origin and takes the atlas box with the largest IoU on the same page (IoU < 0.2: none).
Atlas mass per box and the 0.8/0.2 mix are the rule of tx_decode/atlas_mix.py. Run from harvest/:
  python3 tx_decode/mix/mix_build.py   -> tx_decode/mix/<L>_mix_topk.tsv, <L>_mixmap.tsv, mix_build.json"""
import csv, json, os
R = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
T = '..'; B = '../../birago-fr3252-1571-72'; O = 'tx_decode/mix/'
pos = {r['sid']: (r['leaf'], r['line'], int(r['pos'])) for r in R('tx_decode/eye/open/sorter/owner_positions.tsv') if r['line']}
tiles = R(T + '/sorter/signs.tsv') + R(B + '/sorter/signs.tsv')


def origin(page):
    """source-image origin of a sorter strip page (each sorter's build_inputs.py strip rule)"""
    leaf, band = page.rsplit('_L', 1); band = int(band)
    if leaf == 'f117':
        es = [e for e in json.load(open(B + '/images/f117/manifest.json'))['iiif_lines'] if e['band'] == band]
        return 'f117r', min(e['box'][0] for e in es), max(0, min(e['box'][1] for e in es) - 40)
    es = [e for e in json.load(open(leaf + '/manifest.json'))['iiif_lines'] if e['band'] == band]
    ox, oy = (int(v) for v in es[0]['source_url'].split('/full/')[0].split('/')[-1].split(',')[:2])
    return leaf, min(e['box'][0] for e in es) - ox, min(e['box'][1] for e in es) - oy


def iou(a, b):
    ix = max(0, min(a[0] + a[2], b[0] + b[2]) - max(a[0], b[0])); iy = max(0, min(a[1] + a[3], b[1] + b[3]) - max(a[1], b[1]))
    i = ix * iy; u = a[2] * a[3] + b[2] * b[3] - i
    return i / u if u else 0.0


def atlas_mass(r):
    m = {}
    for i in (1, 2, 3):
        k = r.get(f'k{i}') or ''
        if k and k != '_':
            m[k] = m.get(k, 0) + max(float(r.get(f's{i}') or 0), 0.05)
    t = sum(m.values())
    return {k: v / t for k, v in m.items()} if t else None


LET = [('f144r', 'no73', 'f144r'), ('f168', 'no85', 'f168'), ('f117', 'fr3252-no77', 'f117')]
summary = {}
for L, at, leaf in LET:
    boxes = [r for r in R(f'{T}/atlas/topk/{at}.tsv')]
    tmap = {}
    for t in tiles:
        if t['sid'] not in pos or pos[t['sid']][0] != leaf: continue
        pg, dx, dy = origin(t['page'])
        tb = (int(t['x']) + dx, int(t['y']) + dy, int(t['w']), int(t['h']))
        best = max(((iou(tb, (int(b['x']), int(b['y']), int(b['w']), int(b['h']))), b) for b in boxes if b['page'] == pg),
                   key=lambda z: z[0], default=(0, None))
        tmap[pos[t['sid']][1:]] = (t['sid'], best[0], best[1])
    lat = [(r['line'], int(r['pos']), r['cand'], float(r['score'])) for r in R(f'tx_decode/{L}_topk.tsv')]
    order, two = [], {}
    for ln, p, c, s in lat:
        if (ln, p) not in two: order.append((ln, p)); two[(ln, p)] = {}
        two[(ln, p)][c] = s
    nmap = nmass = 0
    with open(O + f'{L}_mix_topk.tsv', 'w') as f, open(O + f'{L}_mixmap.tsv', 'w') as g:
        f.write('line\tpos\tcand\tscore\n'); g.write('line\tpos\ttile\tbox\tiou\tatlas\n')
        for k in order:
            c = two[k]; sid, v, b = tmap.get(k, ('', 0, None))
            a = atlas_mass(b) if (b is not None and v >= 0.2) else None
            g.write(f"{k[0]}\t{k[1]}\t{sid}\t{b['box'] if b is not None and v >= 0.2 else ''}\t{v:.3f}\t"
                    f"{','.join(f'{x}:{y:.2f}' for x, y in sorted((a or {}).items(), key=lambda z: -z[1]))}\n")
            if b is not None and v >= 0.2: nmap += 1
            if a:
                nmass += 1; c = {x: 0.8 * c.get(x, 0) + 0.2 * a.get(x, 0) for x in set(c) | set(a)}
            for x, s in sorted(c.items(), key=lambda z: -z[1]):
                if s > 0: f.write(f'{k[0]}\t{k[1]}\t{x}\t{s:.4f}\n')
    summary[L] = {'positions': len(order), 'tile_mapped': len([k for k in order if k in tmap]), 'box_iou>=0.2': nmap,
                  'atlas_mass_added': nmass}
    print(L, summary[L])
json.dump(summary, open(O + 'mix_build.json', 'w'), indent=1)
