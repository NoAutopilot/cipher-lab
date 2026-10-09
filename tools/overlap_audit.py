#!/usr/bin/env python3
"""Overlap-zone audit of a transcription pass's deletions and insertions (TXE2-OVERLAP, PREREG-txeng2-7 O1, 9 Oct 2026).

Read-free: it never shows a sign value. For every line of an item cut into neighbouring segment crops (s1, s2, ...)
it measures the true overlap of each neighbouring pair two ways -- from the crop manifest's boxes (native px) and by
pixel-matching the shared strip of the two crop images (normalised cross-correlation of s2's left strip against s1,
a small vertical search for sheared bands) -- and then locates every deletion and insertion of each pass against the
truth (tools/tx_bench.py's own align(), so the indels are exactly the ones tx_bench counts) relative to the overlap
zones: inside, at the seam (within one sign width of a zone edge, or of a cut when segments do not overlap), outside.

Position model (stated, approximate): the crops' core-row column-ink densities are stitched into one profile per line
(native px, max over overlapping segments); truth position p of n sits at the (p - 0.5) / n quantile of the line's ink
mass (uniform over the boxes when a crop is missing); the sign width w is the 0.5-99.5% ink extent over n. An insertion
sits between its neighbouring truth positions. The share of the line inside or at the seam of
the zones is printed as the chance expectation for a uniformly placed indel.

  python3 tools/overlap_audit.py --manifest M.json --crop-dir DIR --truth T.truth.tsv --pass A=passA.tsv \\
      [--pass B=passB.tsv] [--lines f178v_L01,f178v_L02] [--label-map MAP.tsv] [--json OUT.json] [--no-match]

Manifest: an iiif_lines manifest ({"iiif_lines": [...]}) or a bare list; entries need "crop" (<line>_s<k>.<ext>, an
optional leading directory is dropped) and "box" (x0, y0, x1, y1 in native px; only x0, x1 are used). The crop's scale is
its image width over the box width.

Must catch (offline test tools/tests/test_overlap_audit.py): a deletion placed in a known overlap is 'inside'; a measured
overlap from the boxes equals the pixel-matched one on synthetic crops. Must NOT do: report sign values (output carries
line, position, kind and zone only), or call a zero-overlap cut an overlap (it is reported as a seam only).
"""
import argparse
import json
import os
import re
import sys
from collections import defaultdict

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tx_bench import align, load_label_map, load_output, map_truth, read_tsv  # noqa: E402


def load_manifest(path, crop_dir):
    d = json.load(open(path))
    entries = d['iiif_lines'] if isinstance(d, dict) else d
    segs = defaultdict(list)
    for e in entries:
        name = os.path.basename(e['crop'])
        m = re.match(r'(.+)_s(\d+)\.\w+$', name)
        if not m:
            continue
        segs[m.group(1)].append({'k': int(m.group(2)), 'x0': float(e['box'][0]), 'x1': float(e['box'][2]),
                                 'path': os.path.join(crop_dir, name)})
    return {ln: sorted(v, key=lambda s: s['k']) for ln, v in segs.items()}


def gray(path):
    return np.asarray(Image.open(path).convert('L'), dtype=np.float32)


def ink_cols(g, core=0.55):
    h = g.shape[0]
    c0, c1 = int(h * (1 - core) / 2), h - int(h * (1 - core) / 2)
    band = g[c0:c1]
    thr = min(128.0, float(np.percentile(band, 50)) - 40)
    dens = (band < thr).sum(axis=0).astype(float)
    dens = np.convolve(dens, np.ones(5) / 5, mode='same')
    return np.where(dens >= 1.0)[0]


def ink_profile(segs):
    """Stitched column-ink density of the line in native px (x from segs[0].x0), max over overlapping segments; or None."""
    X0, X1 = int(segs[0]['x0']), int(np.ceil(segs[-1]['x1']))
    prof = np.zeros(X1 - X0 + 1)
    try:
        for s in segs:
            g = gray(s['path']); sc = g.shape[1] / (s['x1'] - s['x0'])
            h = g.shape[0]; c0, c1 = int(h * 0.225), h - int(h * 0.225)
            band = g[c0:c1]
            thr = min(128.0, float(np.percentile(band, 50)) - 40)
            dens = (band < thr).sum(axis=0).astype(float) / max(1, band.shape[0])
            # drop the outer 1% of each crop's width (edge artefacts of shear/upscale)
            m = max(1, int(0.01 * len(dens))); dens[:m] = 0; dens[-m:] = 0
            xs = (s['x0'] + np.arange(len(dens)) / sc - X0).astype(int)
            ok = (xs >= 0) & (xs < len(prof))
            np.maximum.at(prof, xs[ok], dens[ok])
    except (FileNotFoundError, OSError):
        return None
    return prof


def sign_x(segs, n, model='ink'):
    """Native x of truth positions 1..n (and fractional): ink-mass quantiles of the line, else uniform over the boxes."""
    X0 = segs[0]['x0']
    prof = ink_profile(segs)
    if model == 'uniform' or prof is None or prof.sum() <= 0:
        x0, x1 = X0, segs[-1]['x1']
        if prof is not None and prof.sum() > 0:
            cum = np.cumsum(prof) / prof.sum()
            x0, x1 = X0 + float(np.searchsorted(cum, 0.005)), X0 + float(np.searchsorted(cum, 0.995))
        return lambda p: x0 + (p - 0.5) * (x1 - x0) / n, (x0, x1), 'uniform over ink extent' if model == 'uniform' else 'uniform over boxes'
    cum = np.cumsum(prof) / prof.sum()

    def f(p):
        q = min(max((p - 0.5) / n, 0.0), 1.0)
        return X0 + float(np.searchsorted(cum, q))
    return f, (X0 + float(np.searchsorted(cum, 0.005)), X0 + float(np.searchsorted(cum, 0.995))), 'ink-mass quantile'


def ncc(a, b):
    a = a - a.mean(); b = b - b.mean()
    d = np.sqrt((a * a).sum() * (b * b).sum())
    return float((a * b).sum() / d) if d > 1e-6 else -1.0


def pixel_overlap(p1, p2, ds=4, dy_max=0.15, strip=0.05):
    """Overlap of crop p2 over p1 in p1's image px by matching p2's left strip inside p1; (overlap_px, ncc)."""
    g1, g2 = gray(p1), gray(p2)
    h = min(g1.shape[0], g2.shape[0])
    g1, g2 = g1[:h], g2[:h]
    s1, s2 = g1[::ds, ::ds], g2[::ds, ::ds]
    W1 = s1.shape[1]
    sw = max(8, int(s2.shape[1] * strip))
    dym = max(1, int(s1.shape[0] * dy_max))
    tmpl = s2[dym:s2.shape[0] - dym, :sw]
    best = (-2.0, 0, 0)
    for o in range(sw, min(W1, s2.shape[1]) - 1):
        x = W1 - o
        for dy in range(-dym, dym + 1):
            win = s1[dym + dy:dym + dy + tmpl.shape[0], x:x + sw]
            if win.shape != tmpl.shape:
                continue
            v = ncc(win, tmpl)
            if v > best[0]:
                best = (v, o, dy)
    v, o, dy = best
    # refine at full resolution around the coarse hit
    t = g2[dym * ds:h - dym * ds, :sw * ds]
    fine = (v, o * ds)
    for of in range(o * ds - ds, o * ds + ds + 1):
        x = g1.shape[1] - of
        for fy in range(dy * ds - ds, dy * ds + ds + 1):
            y = dym * ds + fy
            win = g1[y:y + t.shape[0], x:x + t.shape[1]]
            if x < 0 or y < 0 or win.shape != t.shape:
                continue
            fv = ncc(win, t)
            if fv > fine[0]:
                fine = (fv, of)
    return fine[1], round(fine[0], 3)


def zones_of(segs):
    """[(a, b)] native-px overlap zones of neighbouring segments; a == b is a plain cut (no overlap)."""
    z = []
    for s, t in zip(segs, segs[1:]):
        a, b = t['x0'], s['x1']
        z.append((a, b) if b > a else ((a + b) / 2, (a + b) / 2))
    return z


def classify(x, zones, w):
    for a, b in zones:
        if b > a and a <= x <= b:
            return 'inside'
    for a, b in zones:
        if min(abs(x - a), abs(x - b)) <= w:
            return 'seam'
    return 'outside'


def indels(truth_rows, out_lines, lines):
    """[(line, ref_pos_float, kind)] -- ref_pos is a 1-based fractional truth index (insertions sit between)."""
    by_line = defaultdict(list)
    for r in truth_rows:
        by_line[r['line']].append(r)
    res = []
    for ln in lines:
        rows = sorted(by_line.get(ln, []), key=lambda r: float(r['pos']))
        if not rows or ln not in out_lines:
            continue
        ref = [r['ref_sign'] for r in rows]
        ts = [set(filter(None, r['truth'].split('|'))) for r in rows]
        last = 0.0
        for ri, osg in align(ref, ts, out_lines[ln]):
            if ri is None:
                res.append((ln, last + 0.5, 'inserted'))
                continue
            last = ri + 1.0
            if osg is None and rows[ri]['status'] == 'scored':
                res.append((ln, last, 'deleted'))
    return res, {ln: len(by_line.get(ln, [])) for ln in lines}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--manifest', action='append', required=True)
    ap.add_argument('--crop-dir', action='append', required=True, help='one per --manifest, same order')
    ap.add_argument('--truth', required=True)
    ap.add_argument('--pass', dest='passes', action='append', default=[], help='NAME=path.tsv')
    ap.add_argument('--lines', help='comma list; default every truth line with crops')
    ap.add_argument('--label-map', help="TSV from/to, applied to truth and passes exactly as tx_bench.py's --label-map")
    ap.add_argument('--model', choices=('ink', 'uniform'), default='ink',
                    help='sign positions at ink-mass quantiles (default) or evenly over the 0.5-99.5%% ink extent (sensitivity)')
    ap.add_argument('--no-positions', action='store_true',
                    help='JSON carries counts only, no per-indel line/position rows (for eval items: positions are opened, not kept)')
    ap.add_argument('--no-match', action='store_true', help='skip the pixel match (boxes only)')
    ap.add_argument('--json')
    a = ap.parse_args(argv)
    segs = {}
    for m, d in zip(a.manifest, a.crop_dir):
        segs.update(load_manifest(m, d))
    truth = read_tsv(a.truth)
    lm = load_label_map(a.label_map) if a.label_map else None
    if lm:
        truth = map_truth(truth, lm)
    tlines = sorted({r['line'] for r in truth})
    lines = a.lines.split(',') if a.lines else [ln for ln in tlines if ln in segs]
    out = {'lines': {}, 'passes': {}}
    fxs = {}
    for ln in lines:
        s = segs[ln]
        zs = zones_of(s)
        ov_box = [round(b - a_, 1) if (b - a_) > 0 else 0 for a_, b in ((t['x0'], u['x1']) for u, t in zip(s, s[1:]))]
        ov_pix = []
        if not a.no_match:
            for u, t in zip(s, s[1:]):
                try:
                    sc = gray(u['path']).shape[1] / (u['x1'] - u['x0'])
                    o, v = pixel_overlap(u['path'], t['path'])
                    ov_pix.append({'native_px': round(o / sc, 1), 'ncc': v})
                except (FileNotFoundError, OSError):
                    ov_pix.append(None)
        n_line = sum(1 for r in truth if r['line'] == ln)
        fx, (x0, x1), model = sign_x(s, max(1, n_line), a.model)
        fxs[ln] = fx
        out['lines'][ln] = {'position_model': model, 'segments': len(s), 'zones': zs, 'overlap_box_native': ov_box, 'overlap_pixel': ov_pix,
                            'ink_extent': [round(float(x0), 1), round(float(x1), 1)]}
    for spec in a.passes:
        name, path = spec.split('=', 1)
        ol = load_output([path])
        if lm:
            ol = {k: [lm.get(x, x) for x in v] for k, v in ol.items()}
        found, n_by = indels(truth, ol, lines)
        rows, cnt = [], {'inside': 0, 'seam': 0, 'outside': 0}
        for ln, rp, kind in found:
            L = out['lines'][ln]; n = max(1, n_by[ln])
            x0, x1 = L['ink_extent']; w = (x1 - x0) / n
            x = fxs[ln](rp)
            z = classify(x, L['zones'], w)
            cnt[z] += 1
            rows.append({'line': ln, 'pos': rp, 'kind': kind, 'x_native': round(x, 1), 'zone': z})
        tot = sum(cnt.values())
        out['passes'][name] = {'indels': [] if a.no_positions else rows, 'counts': cnt, 'total': tot,
                               'share_in_or_seam': round((cnt['inside'] + cnt['seam']) / tot, 3) if tot else None}
    # chance: share of the line's ink extent inside or within one sign width of a zone, sign-weighted
    num = den = 0.0
    n_by = defaultdict(int)
    for r in truth:
        n_by[r['line']] += 1
    for ln in lines:
        L = out['lines'][ln]; n = max(1, n_by[ln]); x0, x1 = L['ink_extent']; w = (x1 - x0) / n
        for p in range(1, n + 1):
            num += classify(fxs[ln](p), L['zones'], w) != 'outside'; den += 1
    out['chance_in_or_seam'] = round(num / den, 3) if den else None
    for ln, L in out['lines'].items():
        pix = ', '.join('%s (ncc %s)' % (p['native_px'], p['ncc']) if p else 'n/a' for p in L['overlap_pixel'])
        print('%s: %d segs; overlap boxes %s native px; pixel match %s; ink %s'
              % (ln, L['segments'], L['overlap_box_native'], pix or '-', L['ink_extent']))
    for name, P in out['passes'].items():
        print('%s: indels %d -- inside %d, seam %d, outside %d; in-or-seam share %s'
              % (name, P['total'], P['counts']['inside'], P['counts']['seam'], P['counts']['outside'],
                 P['share_in_or_seam']))
    print('chance in-or-seam share (uniform indel): %s' % out['chance_in_or_seam'])
    if a.json:
        with open(a.json, 'w') as f:
            json.dump(out, f, indent=1)
    return 0


if __name__ == '__main__':
    sys.exit(main())
