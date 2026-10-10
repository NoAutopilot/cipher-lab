#!/usr/bin/env python3
"""OL1-BOXES (PREREG-txeng2-21, TXE2-OL1BOXES, 10 Oct 2026): machine-proposed sign boxes and a left-to-right reading order
on the 35 ORACLE-LOCATION-1 manifest lines, blind overlays, and the inputs of the owner's blind box-verify sorter page.

READ-FREE and value-blind: no reader, no truth, no key, no decode, no pass output and no label is read. The only inputs are
the manifest (benchmark-tx/txeng2/oracle1/manifest.tsv, sha256 checked first), the crop images and their crop manifests
(for the s1/s2/s3 overlap geometry), and one `tools/glyph_atlas.py segment` run per hand (default mode, the no.87 atlas
recipe). Box counts are compared to nothing.

Recipe (TXE2-BOXES's spin_join.py rule, generalised to three crops): a box's centre is put in line coordinates
(crop box x0 + x * crop-box width / image width); with crops s1..sn and overlap midpoints m_i = (x0 of s_(i+1) + x1 of
s_i) / 2, a box is kept from s_i when its centre lies in [m_(i-1), m_i), so a sign in an overlap is counted once. Small
detached marks (glyph_atlas's marks.tsv) are KEPT as their own boxes (kind=mark), joined by the same rule. Dropped: only
verso bleed-through by spin_join.py's --ghost rule made crop-relative: a box is dropped when its darkest-10% grey / the crop
median grey exceeds max(0.45, 1.25 x the median of that ratio over the crop's own segment boxes). Why: the Spinelli absolute
0.45 dropped 461 of 468 luzerne p1 boxes (a small pale hand: box ratios 0.49-0.77, median 0.67, against 0.27 vivonne and
0.38 birago); the relative floor was set on those ratio numbers alone, before any overlay existed, and no image was looked at;
spin_join.py's --min-frac fragment rule is NOT applied (PREREG: a component rule is a proposal, never truth). Reading order
= ascending line-coordinate centre x, signs and marks together.

  python3 tools/glyph_atlas.py segment --page NAME=CROP ... --out SEG/<hand>     (one run per hand, default mode)
  python3 benchmark-tx/txeng2/oracle1/build_ol1_boxes.py SEG
Writes boxes/<hand>/<line>.tsv, boxes/boxes_all.tsv, boxes/<hand>/<line>_overlay.jpg + <line>_plain.jpg, and the sorter
inputs sorter/{signs.tsv,labels.tsv,pages.json,cipher_lines.tsv} (one neutral pile `unsorted`, nothing else)."""
import argparse, csv, hashlib, json, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageOps

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
O = os.path.join(ROOT, 'benchmark-tx/txeng2/oracle1')
MANIFEST_SHA = '978322f62c04d59097f521d73690db00d61a44e794af40546db3d9dfb34b45de'
BLUE, ORANGE = (0, 114, 178), (179, 89, 0)   # Okabe-Ito blue #0072B2 (signs, solid) / Okabe-Ito orange darkened to #B35900 for 3:1 on the page grey (marks, dashed); RGB colour
GHOST = 0.45


def crop_geometry(path):
    """(x0, x1, scale) of a crop in its page's pixels, from the folder's manifest.json; a one-crop line gets (0, w, 1)."""
    d, f = os.path.split(path)
    w = Image.open(os.path.join(ROOT, path)).size[0]
    mp = os.path.join(ROOT, d, 'manifest.json')
    if os.path.exists(mp):
        for c in json.load(open(mp)).get('iiif_lines', []):
            if c['crop'] == f:
                x0, x1 = c['box'][0], c['box'][2]
                return x0, x1, (x1 - x0) / w
    return 0, w, 1.0


def dashed_rect(dr, x0, y0, x1, y1, fill, width=2, dash=6):
    for a, b, horiz, c in ((x0, x1, True, y0), (x0, x1, True, y1), (y0, y1, False, x0), (y0, y1, False, x1)):
        t = a
        while t < b:
            e = min(t + dash, b)
            dr.line([(t, c), (e, c)] if horiz else [(c, t), (c, e)], fill=fill, width=width)
            t += 2 * dash


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('segdir', help='folder holding one glyph_atlas segment output folder per hand (named by the hand)')
    a = ap.parse_args()
    mpath = os.path.join(O, 'manifest.tsv')
    if hashlib.sha256(open(mpath, 'rb').read()).hexdigest() != MANIFEST_SHA:
        sys.exit('manifest.tsv sha256 does not match the registered value -- STOP')
    man = list(csv.DictReader(open(mpath), delimiter='\t'))
    allrows, sorter_signs, pages, summary = [], [], {}, []
    for r in man:
        hand, line, crops = r['hand'], r['line'], r['crops'].split(';')
        seg = os.path.join(a.segdir, hand)
        names = [os.path.basename(c)[:-4] for c in crops]
        geo = {n: crop_geometry(c) for n, c in zip(names, crops)}
        grey = {n: np.asarray(Image.open(os.path.join(ROOT, c)).convert('L'), dtype=float) for n, c in zip(names, crops)}
        mids = [(geo[names[i + 1]][0] + geo[names[i]][1]) / 2.0 for i in range(len(names) - 1)]
        lo = {n: (mids[i - 1] if i > 0 else -1e9) for i, n in enumerate(names)}
        hi = {n: (mids[i] if i < len(mids) else 1e9) for i, n in enumerate(names)}
        cand = [(s, 'sign') for s in csv.DictReader(open(os.path.join(seg, 'signs.tsv')), delimiter='\t')]
        cand += [(m, 'mark') for m in csv.DictReader(open(os.path.join(seg, 'marks.tsv')), delimiter='\t')]
        ratio = {}
        for s, kind in cand:
            n = s['page']
            if n in geo:
                x, y, w, h = (int(s[k]) for k in ('x', 'y', 'w', 'h')); patch = grey[n][y:y + h, x:x + w]
                ratio[id(s)] = np.quantile(patch, 0.1) / np.median(grey[n]) if patch.size else 9.0
        floor = {n: max(GHOST, 1.25 * float(np.median([ratio[id(s)] for s, kd in cand if s['page'] == n and kd == 'sign'] or [GHOST])))
                 for n in names}
        kept, ghosts = [], 0
        for s, kind in cand:
            n = s['page']
            if n not in geo:
                continue
            x, y, w, h = (int(s[k]) for k in ('x', 'y', 'w', 'h'))
            G = grey[n]; patch = G[y:y + h, x:x + w]
            gx = geo[n][0] + (x + w / 2.0) * geo[n][2]
            if not (lo[n] <= gx < hi[n]):
                continue
            if patch.size == 0 or ratio[id(s)] > floor[n]:
                ghosts += 1; continue
            kept.append((gx, kind, n, x, y, w, h))
        kept.sort(key=lambda t: (t[0], t[4]))
        rows = []
        for k, (gx, kind, n, x, y, w, h) in enumerate(kept, 1):
            rows.append({'box_id': f'{line}_b{k:03d}', 'hand': hand, 'line': line, 'crop': crops[names.index(n)],
                         'x': x, 'y': y, 'w': w, 'h': h, 'order': k, 'kind': kind})
        hd = os.path.join(O, 'boxes', hand); os.makedirs(hd, exist_ok=True)
        cols = ['box_id', 'crop', 'x', 'y', 'w', 'h', 'order', 'kind']
        with open(os.path.join(hd, line + '.tsv'), 'w') as f:
            f.write('\t'.join(cols) + '\n')
            f.writelines('\t'.join(str(q[c]) for c in cols) + '\n' for q in rows)
        allrows += rows
        # overlays: the line's crops stacked top to bottom, greyscale page, numbered boxes; the plain stack beside
        ims = [ImageOps.grayscale(Image.open(os.path.join(ROOT, c))) for c in crops]
        W, gap = max(i.width for i in ims), 26
        H = sum(i.height + gap for i in ims)
        plain = Image.new('L', (W, H), 255); ov = Image.new('RGB', (W, H), (255, 255, 255))
        yo = {}
        y0 = 0
        for n, im in zip(names, ims):
            yo[n] = y0; plain.paste(im, (0, y0)); ov.paste(im.convert('RGB'), (0, y0)); y0 += im.height + gap
        dr = ImageDraw.Draw(ov)
        for q in rows:
            n = os.path.basename(q['crop'])[:-4]
            bx0, by0 = q['x'], q['y'] + yo[n]; bx1, by1 = bx0 + q['w'], by0 + q['h']
            if q['kind'] == 'sign':
                dr.rectangle([bx0, by0, bx1, by1], outline=BLUE, width=2)
            else:
                dashed_rect(dr, bx0, by0, bx1, by1, ORANGE, width=2, dash=3)
            ty = min(by1 + 2, yo[n] + ims[names.index(n)].height + 12)
            tw = 7 * len(str(q['order'])) + 2
            dr.rectangle([bx0, ty, bx0 + tw, ty + 11], fill=(255, 255, 255))
            dr.text((bx0 + 1, ty), str(q['order']), fill=(0, 0, 0))
        ov.save(os.path.join(hd, line + '_overlay.jpg'), quality=72)
        plain.save(os.path.join(hd, line + '_plain.jpg'), quality=72)
        for q in rows:
            n = os.path.basename(q['crop'])[:-4]
            sorter_signs.append((q['box_id'], n, q['x'], q['y'], q['w'], q['h']))
            pages[n] = {'image': q['crop']}
        for n, c in zip(names, crops):
            pages.setdefault(n, {'image': c})
        summary.append((hand, line, len(rows), sum(q['kind'] == 'sign' for q in rows), sum(q['kind'] == 'mark' for q in rows), ghosts))
    cols = ['box_id', 'hand', 'line', 'crop', 'x', 'y', 'w', 'h', 'order', 'kind']
    with open(os.path.join(O, 'boxes', 'boxes_all.tsv'), 'w') as f:
        f.write('\t'.join(cols) + '\n')
        f.writelines('\t'.join(str(q[c]) for c in cols) + '\n' for q in allrows)
    sd = os.path.join(O, 'sorter'); os.makedirs(sd, exist_ok=True)
    with open(os.path.join(sd, 'signs.tsv'), 'w') as f, open(os.path.join(sd, 'labels.tsv'), 'w') as g:
        f.write('sid\tpage\tx\ty\tw\th\n'); g.write('sid\tsign\tfamily\n')
        for s in sorter_signs:
            f.write('\t'.join(map(str, s)) + '\n'); g.write(f'{s[0]}\tunsorted\tunsorted\n')
    json.dump(pages, open(os.path.join(sd, 'pages.json'), 'w'), indent=1, sort_keys=True)
    with open(os.path.join(sd, 'cipher_lines.tsv'), 'w') as f:
        f.write('# every crop of the 35 OL1 manifest lines is a cipher line (manifest.tsv); no x-range given\n')
        f.writelines(n + '\n' for n in sorted(pages))
    with open(os.path.join(O, 'boxes', 'counts.tsv'), 'w') as f:
        f.write('hand\tline\tboxes\tsigns\tmarks\tghost_dropped\n')
        f.writelines('\t'.join(map(str, s)) + '\n' for s in summary)
    for s in summary:
        print(*s, sep='\t')
    print('total boxes', len(allrows))


if __name__ == '__main__':
    main()
