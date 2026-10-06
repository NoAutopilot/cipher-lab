#!/usr/bin/env python3
"""R7-OLDFIX (6 Oct 2026): re-cut the blocks A/C2 sorter so that one tile = one sign, from the sign's own ink, on the
cipher text only.

Why: the R7-OLDSORT cut (build_inputs.py, kept for the record as signs_v1.tsv / labels_v1.tsv / focus_v1.tsv / fit_v1.tsv)
laid each line's words out by sign count and cut tiles at proportional positions, with boxes from the whole strip height,
so many tiles reached into the line above or below; and line A1 was tiled from its clear Spanish opening ("labreuedad que
desseo y espero,"), which is not cipher. The line map itself was right (R7-OLDFIX, NOTES.md section 15): R7-OLDA's
--centres sit on the 11 block-A and 8 block-C2 cipher lines.

Method: tools/sorter_recut.py (the shared Pisany/Longlee re-cut). The two leaf regions (leaf 001 x 900-2690, leaf 006
x 700-2630, R7-OLDA's own regions) are stacked into one composite image (written as region.jpg, the sorter's page view);
each line's trace is the straight line through the centres of R7-OLDA's three deskewed crops of that line
(images/crops_AC2/manifest_*.json boxes), re-centred by sorter_recut on the strip's own ink. Reader columns are the
reconciled draft's signs (transcription/reconciled_AC2_R7OLDA.tsv, sign units as build_inputs.units), positioned at the
v1 tile centres. Tiles on line A1 left of the cipher start (x < A1_CIPHER_X, the "8l" before s8cr8t4r37) are dropped.
Focus: a tile aligned to a column whose v1 tile was in the v1 focus box (a blind-pass split) carries that question,
then the shape-cluster focus from sorter_recut.

  python3 ciphers/na-oldenbarnevelt-2442-1605/sorter/recut.py [--debug DIR]
"""
import argparse, csv, json, re, shutil, sys
from collections import defaultdict
from pathlib import Path
import numpy as np
from PIL import Image

S = Path(__file__).resolve().parent; T = S.parent; P = S / 'pages'
sys.path.insert(0, str(S.parents[2] / 'tools'))
import sorter_recut as sr  # noqa: E402

BLOCKS = [  # block, leaf image, region x0, x1, y0, y1 (leaf px), manifest
    ('A', '001_3f72fc28-348d-42ae-974f-3a94f3c76007.jpg', 900, 2690, 1250, 2700, 'manifest_A.json'),
    ('C2', '006_d027ee45-9cd0-44db-82cd-45ed3575eecb.jpg', 700, 2630, 2600, 3730, 'manifest_C2.json'),
]
A1_CIPHER_X = 1015   # composite x (= leaf x - 900) where line A1's cipher starts ("8l"); measured on the R7-OLDFIX grid overlay
TRACE_FIX = {'A_L11': (-0.07, 1350, 2520)}   # slope, leaf x, leaf y: R7-OLDA's own deskew fit for this short line (-0.020) runs
                                            # under the text at the right; slope from the block's other lines, anchor by eye
XMAX = {'A_L11': 1100}  # composite x: line A11's cipher ends ("8n8"); right of it the trace meets the clear line below
NCARRY, NFOCUS = 18, 24   # focus box: v1 split questions in v1 order (named pairs, R7-OLDA's pairs, others), then shape
CFG = sr.Cfg(pitch=100, half=78, xmin=10, rel=0.76, nclu=40, per_clu=2, nfocus=40)


def units(tok):
    """raw token -> sign units (build_inputs.units, copied: build_inputs.py runs its build on import)."""
    import re
    t = re.sub(r"[,.;:\-|'? ]", '', tok.replace('~', '').replace('+', '')); out = []; i = 0
    while i < len(t):
        if t[i] == '^' and i + 1 < len(t) and out: out[-1] += '^' + t[i + 1]; i += 2
        else: out.append(t[i]); i += 1
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--debug'); a = ap.parse_args()
    for f in ('signs', 'labels', 'focus', 'fit'):                    # the v1 cut, kept for the record (once)
        src, dst = S / f'{f}.tsv', S / f'{f}_v1.tsv'
        if src.exists() and not dst.exists(): shutil.copy(src, dst)
    v1c = defaultdict(list)
    for r in csv.DictReader(open(S / 'signs_v1.tsv'), delimiter='\t'):
        v1c[r['page']].append(int(r['x']) + int(r['w']) / 2)
    v1q = dict(l.rstrip('\n').split('\t', 1) for l in open(S / 'focus_v1.tsv') if l.strip())
    rec = defaultdict(list)
    for r in csv.DictReader(open(T / 'transcription' / 'reconciled_AC2_R7OLDA.tsv'), delimiter='\t'):
        if r['token'].startswith('+'): continue                       # interlinear addition, not on the line
        rec[(r['block'], int(r['line']))].extend(units(r['token']))
    W = max(x1 - x0 for _, _, x0, x1, _, _, _ in BLOCKS)
    parts, traces, pages, cols, cents, yoff = [], [], [], [], [], 0
    for block, leaf, x0, x1, y0, y1, man in BLOCKS:
        g = np.array(Image.open(T / 'images' / leaf).convert('L'))[y0:y1, x0:x1]
        pad = np.full((y1 - y0, W), 255, np.uint8); pad[:, :x1 - x0] = g; parts.append(pad)
        segs = defaultdict(list)
        for e in json.load(open(T / 'images' / 'crops_AC2' / man))['iiif_lines']:
            if e['crop'].startswith(f'{block}_L') and e.get('segment'):
                bx = e['box']; segs[int(e['crop'].split('_L')[1][:2])].append(((bx[0] + bx[2]) / 2 - x0, (bx[1] + bx[3]) / 2 - y0 + yoff))
        for ln in sorted(segs):
            if (block, ln) not in rec: continue
            xs, ys = zip(*sorted(segs[ln])); k, c = np.polyfit(xs, ys, 1) if len(xs) > 1 else (0.0, ys[0])
            page = f'{block}_L{ln:02d}'
            if page in TRACE_FIX:
                k, fx, fy = TRACE_FIX[page]; c = fy - y0 + yoff - k * (fx - x0)
            traces.append(k * np.arange(W) + c); pages.append(page)
            cols.append([(u, u) for u in rec[(block, ln)]]); cents.append(v1c[page])
        yoff += y1 - y0
    grey = np.vstack(parts); Image.fromarray(grey).save(S / 'region.jpg', quality=70)
    sr.run(grey, traces, pages, cols, cents, S, P, CFG, debug=a.debug,
           region_image=str((S / 'region.jpg').relative_to(S.parents[2])))
    # drop the clear opening of line A1; carry the v1 split questions onto aligned tiles
    rows = {n: list(csv.DictReader(open(S / f'{n}.tsv'), delimiter='\t')) for n in ('signs', 'labels', 'clusters')}
    cx = lambda r: int(r['x']) + int(r['w']) / 2
    drop = {r['sid'] for r in rows['signs'] if (r['page'] == 'A_L01' and cx(r) < A1_CIPHER_X)
            or (r['page'] in XMAX and cx(r) > XMAX[r['page']])}
    for n, keys in (('signs', ['sid', 'page', 'x', 'y', 'w', 'h']), ('labels', ['sid', 'sign', 'family']),
                    ('clusters', ['sid', 'cluster', 'col', 'dx'])):
        with open(S / f'{n}.tsv', 'w') as o:
            o.write('\t'.join(keys) + '\n'); o.writelines('\t'.join(r[k] for k in keys) + '\n' for r in rows[n] if r['sid'] not in drop)
    page_of = {r['sid']: r['page'] for r in rows['signs']}
    carried = []
    for r in rows['clusters']:
        if r['sid'] in drop or not r['col'] or float(r['dx'] or 1e9) > CFG.clear: continue
        old = f"{page_of[r['sid']]}_{int(r['col']):03d}"
        if old in v1q and old not in {c[2] for c in carried}:
            q = re.sub(r'^(\w+) line (\d+), word \d+ ("[^"]*"), sign (\d+): draft (\S+), blind pass A (\S+), pass B (\S+) \((\w+).*$',
                       lambda m: f'{m[1]}{m[2]} {m[3]} sign {m[4]}: draft {m[5]}, readers {m[6]} / {m[7]}'
                                 f'{" (uncertain word)" if m[8] == "uncertain" else ""}. Which sign?', v1q[old])
            carried.append((r['sid'], q, old))
    shape = [l.rstrip('\n').split('\t', 1) for l in open(S / 'focus.tsv') if l.strip()]
    seen = {s for s, _, _ in carried}
    order = {k: i for i, k in enumerate(v1q)}; carried.sort(key=lambda c: order[c[2]]); carried = [(a, b) for a, b, _ in carried]
    shape = [(s, re.sub(r'^.*started in (\S+) by shape.*$', r'No draft sign lines up here; started in \1 by shape. Right pile, other sign, or bad cut?', q))
             for s, q in shape if s not in drop and s not in seen]
    carried, shape = carried[:NCARRY], shape[:NFOCUS - min(NCARRY, len(carried))]   # the phone's focus box stays short
    with open(S / 'focus.tsv', 'w') as o:
        o.writelines(f'{s}\t{q}\n' for s, q in carried + shape)
    print(len(drop), 'clear-text tiles dropped (A_L01 opening, A_L11 past the cipher);', len(carried), 'split questions carried;',
          len(shape), 'shape-focus tiles;',
          len(rows['signs']) - len(drop), 'tiles kept')


if __name__ == '__main__':
    main()
