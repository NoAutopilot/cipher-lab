#!/usr/bin/env python3
"""R8-MATCUT (6 Oct 2026): re-cut the f.110 sorter so that one tile = one sign, on deskewed strips that follow the five
written lines, with tools/sorter_recut.py (the shared Pisany/Longlee/Oldenbarnevelt re-cut).

Why: the R7-MATSORT cut (build_inputs.py, kept for the record as signs_v1.tsv / labels_v1.tsv / focus_v1.tsv / fit_v1.tsv)
cut flat ~52 px bands across five lines that slope upward to the right, so each band carried pieces of two lines and
6 of 6 random tiles were off their label (R7-MATQA, README.md).

Region: BnF fr.15572 f.110, Gallica btv1b9061879d canvas 116, x 4780-8110, y 300-860 (native; D2B-MATF110's own source
region, fetched once 6 Oct 2026 as region.jpg). Traces (TRACES below): each written line followed from the left margin
by the row-ink peak per 200 px window (step 100, within +-14 px of the previous window), median-smoothed; checked by eye
against the region. The lines rise ~25 px over the left two-thirds and another ~50-90 px over the last third.

Reader columns: Bourdeau's ciphertext.txt f110-1..5, in SEGMENTS (an inference from the image, grade I, layout only):
at the right edge each written line's rising tail carries the tail of the PREVIOUS transcribed line -- written line 2's
right end (after the blots and the struck-through stretch) is f110-1's "t m o h e BOX z q BOX 7 s n 1 e"; written
line 3's right end after "o z o B m" is f110-2's "n 7 BOX q o ff z M o z ff"; written line 4's right end after "A B m"
is f110-3's "e h z o d e U ff 7 6 z ff". Written line 1's right end ("... I x S T I ... w q 8 o t A v o ...", rising
toward the folio number) and written line 5's right end match no transcribed line and get no columns; f110-5's tail
"m Ze t 6 w- 7 z m f o" sits on written line 6, which is not tiled. Within a segment the columns are spread over its
tiles by index (pass 1 cuts, pass 2 aligns), so a starting pile can be a position off where a sign is in pieces.

  python3 ciphers/matignon-mayenne-1586/sorter/recut.py [--debug DIR]
"""
import argparse, json, shutil, sys
from pathlib import Path
import numpy as np
from PIL import Image

S = Path(__file__).resolve().parent; T = S.parent; P = S / 'pages'
sys.path.insert(0, str(S.parents[2] / 'tools'))
import sorter_recut as sr  # noqa: E402

W = 3330
TX = [100 + 100 * k for k in range(32)]     # trace sample x (window centres)
TRACES = [  # written lines 1-5, region y at TX (track.py, R8-MATCUT)
    [174, 173, 168, 168, 168, 168, 168, 169, 169, 168, 165, 159, 158, 158, 157, 157, 156, 153, 145, 140, 134, 134, 131, 121, 107, 99, 99, 82, 80, 79, 79, 78],
    [228, 232, 233, 233, 231, 228, 228, 231, 231, 222, 222, 223, 223, 222, 221, 218, 218, 211, 211, 210, 201, 186, 186, 185, 183, 172, 165, 159, 157, 148, 141, 140],
    [298, 297, 296, 296, 296, 297, 297, 297, 296, 294, 294, 294, 294, 294, 291, 290, 282, 281, 277, 277, 275, 273, 269, 262, 262, 245, 235, 230, 223, 221, 220, 218],
    [363, 362, 360, 360, 352, 352, 359, 360, 364, 364, 364, 364, 360, 360, 360, 353, 352, 351, 351, 346, 344, 335, 335, 335, 329, 321, 315, 313, 302, 293, 289, 288],
    [429, 429, 427, 423, 423, 424, 424, 426, 429, 429, 429, 429, 429, 431, 431, 423, 422, 421, 421, 420, 410, 409, 395, 395, 394, 385, 384, 374, 370, 366, 364, 363],
]
PAGES = [f'f110_W{i}' for i in range(1, 6)]
# per written line: (x0, x1, f110 line, first token index, last token index + 1) -- region x of each segment, by eye on the
# region (R8-MATCUT); token indexes into ciphertext.txt's line
SEGMENTS = {
    1: [(0, 2450, 1, 0, 48)],                       # f110-1 up to "... w- t e 8 m"; right end untranscribed
    2: [(0, 2140, 2, 0, 46), (2530, W, 1, 48, 62)],  # f110-2 up to "z h f"; f110-1 tail "t m o h e ..."
    3: [(0, 2550, 3, 0, 50), (2550, W, 2, 46, 57)],  # f110-3 up to "B m"; f110-2 tail "n 7 BOX q o ff z M o z ff"
    4: [(0, 2540, 4, 0, 45), (2540, W, 3, 50, 62)],  # f110-4 whole; f110-3 tail "e h z o d e U ff 7 6 z ff"
    5: [(0, 2510, 5, 0, 48)],                       # f110-5 up to "z A BOX 7 z"; right end untranscribed
}
FOCUS = ['BOX', 'z', 'T', 'U', 'w', '4']       # the labels D2B-MATF110's blind passes split on (README.md)
NCARRY, NFOCUS = 20, 36
CFG = sr.Cfg(pitch=66, half=46, xmin=25, xmax=3240, rel=0.88, recentre=12, minpix=100, merge=0.25, nclu=36, per_clu=2, nfocus=40, skip=40, clear=30)


def tokens():
    out = {}
    for line in open(T / 'ciphertext.txt'):
        f = line.rstrip('\n').split('\t')
        if f[0].startswith('f110-') and f[0][5:].isdigit():
            out[int(f[0][5:])] = f[1].split()
    return out


def em_align(tiles, tok, pdir, rounds=6, skip_tile=0.55, skip_tok=0.9):
    """Place each segment's transcription columns on pass-1 tiles by shape (value-blind as to meaning, shape labels only):
    start from an even spread by tile index, then alternate (a) a prototype bitmap per label from the tiles it holds and
    (b) a monotone DP per segment matching tokens to tiles at cost = mean squared bitmap distance to the label's prototype,
    a tile left over costs SKIP_TILE (signs in pieces, untranscribed ink), a token left unplaced SKIP_TOK. Returns per page
    the columns and an x for each (the matched tile's centre; an unplaced token the midpoint of its neighbours)."""
    from collections import defaultdict
    bm = {}
    for page in PAGES:
        im = np.array(Image.open(pdir / f'{page}.jpg').convert('L'))
        for t in tiles:
            if t['page'] != page: continue
            g = im[t['y']:t['y'] + t['h'], t['x']:t['x'] + t['w']].astype(float)
            bm[t['sid']] = sr.bitmap(g < CFG.rel * max(g.max(), 1) * .9).ravel()
    segs = []                                       # (page index, tile list, token labels)
    for i, page in enumerate(PAGES, 1):
        tl = sorted((t for t in tiles if t['page'] == page), key=lambda t: t['x'])
        for x0, x1, ln, t0, t1 in SEGMENTS[i]:
            segs.append((i - 1, [t for t in tl if x0 <= t['x'] + t['w'] / 2 < x1], tok[ln][t0:t1]))
    match = [{k: s[round(k * (len(s) - 1) / max(1, len(lb) - 1))]['sid'] for k in range(len(lb))} if s else {} for _, s, lb in segs]
    for _ in range(rounds):
        acc = defaultdict(list)
        for (_, s, lb), m in zip(segs, match):
            for k, sid in m.items(): acc[lb[k]].append(bm[sid])
        proto = {u: np.mean(v, 0) for u, v in acc.items()}
        new = []
        for _, s, lb in segs:
            n, mm = len(lb), len(s); D = np.full((n + 1, mm + 1), 1e9); B = np.zeros((n + 1, mm + 1), int)
            D[0, :] = np.arange(mm + 1) * skip_tile; D[:, 0] = np.arange(n + 1) * skip_tok
            for a in range(1, n + 1):
                pr = proto.get(lb[a - 1])
                for b in range(1, mm + 1):
                    c = np.mean((bm[s[b - 1]['sid']] - pr) ** 2) * 10 if pr is not None else skip_tile
                    o = (D[a - 1, b - 1] + c, D[a, b - 1] + skip_tile, D[a - 1, b] + skip_tok)
                    k = int(np.argmin(o)); D[a, b] = o[k]; B[a, b] = k
            a, b, m = n, mm, {}
            while a > 0 and b > 0:
                k = B[a, b]
                if k == 0: m[a - 1] = s[b - 1]['sid']; a -= 1; b -= 1
                elif k == 1: b -= 1
                else: a -= 1
            new.append(m)
        match = new
    xs = {t['sid']: t['x'] + t['w'] / 2 for t in tiles}
    cols, cents = [[] for _ in PAGES], [[] for _ in PAGES]
    for (pi, s, lb), m in zip(segs, match):
        known = [(k, xs[m[k]]) for k in sorted(m)]
        for k, u in enumerate(lb):
            x = xs[m[k]] if k in m else (np.interp(k, *zip(*known)) if known else 0) + 0.5   # off any tile centre: no clear match
            cols[pi].append((u, u)); cents[pi].append(x)
    print('em_align:', sum(len(m) for m in match), 'of', sum(len(lb) for _, _, lb in segs), 'tokens placed on a tile')
    return cols, cents


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--debug'); a = ap.parse_args()
    for f in ('signs', 'labels', 'focus', 'fit'):                    # the v1 cut, kept for the record (once)
        src, dst = S / f'{f}.tsv', S / f'{f}_v1.tsv'
        if src.exists() and not dst.exists(): shutil.copy(src, dst)
    tok = tokens()
    for i, segs in SEGMENTS.items():                                 # the segment token ranges must be what they say
        for _, _, ln, t0, t1 in segs: assert t1 <= len(tok[ln]), (i, ln, t1, len(tok[ln]))
    grey = np.array(Image.open(S / 'region.jpg').convert('L'))
    assert grey.shape[1] == W, grey.shape
    traces = [np.interp(np.arange(W), TX, t) for t in TRACES]
    # pass 1: cut only, to place each segment's columns on its own tiles
    tiles, _ = sr.run(grey, traces, PAGES, [[] for _ in PAGES], [[] for _ in PAGES], S / '_pass1', S / '_pass1', CFG)
    cols, cents = em_align(tiles, tok, S / '_pass1')
    shutil.rmtree(S / '_pass1')
    if P.exists(): shutil.rmtree(P)
    sr.run(grey, traces, PAGES, cols, cents, S, P, CFG, debug=a.debug,
           region_image=str((S / 'region.jpg').relative_to(S.parents[2])))
    # focus: aligned tiles on the split labels first (one question per label in turn), then the tool's shape focus
    import csv
    lab = {r['sid']: r for r in csv.DictReader(open(S / 'labels.tsv'), delimiter='\t')}
    clu = {r['sid']: r for r in csv.DictReader(open(S / 'clusters.tsv'), delimiter='\t')}
    split = {f: [] for f in FOCUS}
    for sid, r in clu.items():
        if r['col'] and r['dx'] != '' and float(r['dx']) <= CFG.clear and lab[sid]['sign'] in split:
            split[lab[sid]['sign']].append(sid)
    carried = []
    while len(carried) < NCARRY and any(split.values()):
        for f in FOCUS:
            if split[f] and len(carried) < NCARRY:
                sid = split[f].pop(0)
                carried.append((sid, f"{sid.split('_', 1)[1]}: started in {f} from the transcription; the two blind machine "
                                     f"readers split on this sign. Is it {f}, a variant of another pile's sign, or a bad cut?"))
    seen = {s for s, _ in carried}
    shape = [l.rstrip('\n').split('\t', 1) for l in open(S / 'focus.tsv') if l.strip()]
    shape = [(s, q) for s, q in shape if s not in seen][:NFOCUS - len(carried)]
    with open(S / 'focus.tsv', 'w') as o:
        o.writelines(f'{s}\t{q}\n' for s, q in carried + shape)
    with open(S / 'cipher_lines.tsv', 'w') as o:                     # for tools/sorter_preflight.py check 3
        o.writelines(f'{p}\t0\t{W}\n' for p in PAGES)
    print(len(carried), 'split questions;', len(shape), 'shape-focus tiles')


if __name__ == '__main__':
    main()
