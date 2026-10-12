#!/usr/bin/env python3
"""Settle two readers' split rows with the page's own agreed tiles instead of a third reader (TXE4-6 TIEBREAK, 12 Oct 2026,
account 3; PREREG benchmark-tx/PREREG-txeng4-6.md). Read-free: no model call, no reader, no network, no truth file.

Why a new tool and not a reconcile_passes.py option: reconcile_passes.py aligns passes and has no image or atlas input, and
this step needs glyph_atlas classify's feature space (HOG + PCA + log size over the atlas bitmaps, scikit). It reads
reconcile_passes.py's own outputs (ciphertext_draft.tsv, disagreements.tsv) and a box-to-token map that has passed
tools/join_check.py (require(): a map with no PASS sidecar is refused, as every scored join since TXE4-0 REPAIR).

  python3 tools/tx_tiebreak.py --atlas DIR --map MAP.tsv --tiles TILES.tsv --rec REC_DIR --base BASE.tsv --out OUT.tsv
         [--k 5] [--margin 0.0] [--line-sub PATTERN REPL ...] [--permute-seed S] [--coin-seed S --coin-from DEC.tsv]
         [--allow-unchecked-join REASON] [--pca-scale unit|shared]

  --atlas   a glyph_atlas segment dir (signs.tsv, bitmaps.npz); features = glyph_atlas.feats over ALL its rows (unsupervised)
  --map     box_token_align.py output with a join_check PASS sidecar (require())
  --tiles   sid, line, pos: the boxes trusted on one token (e.g. 1:1 in two rounds); the map's own 1:1 rows if absent
  --rec     reconcile_passes.py --out-dir: ciphertext_draft.tsv (line, position, sign, confidence, why) and
            disagreements.tsv (line, col, A, B)
  --base    the committed output (line, pos, sign) the overrides are written into (the adjudicated pass)
  --line-sub PATTERN REPL  regex applied to rec and base line ids to reach the map's line ids (repeatable)

Rule at each A != B row with both candidates non-blank: the row's box (by the map) is compared with the k nearest agreed
tiles (draft why 'agree', lower confidence not L, on OTHER lines of the same page) of class A and of class B: d(c) = mean
distance to the min(k, available) nearest tiles of class c; margin m = (d_far - d_near) / d_near; the nearer class is
written when m > --margin. No box, no tile of one class elsewhere on the page, or a base gap at that column: the base
is kept (reason in the decisions file). The draft column is carried to the base position by tx_bench.align on sign
identity.
Controls: --permute-seed S permutes the agreed tiles' labels within each page before the comparison (the shuffled-label
chance null); --coin-seed S --coin-from DEC.tsv flips a seeded coin between A and B at exactly the rows that file applied.
Writes OUT.tsv (line, pos, sign; base line ids) and OUT.decisions.tsv (line, col, A, B, box, nA, nB, dA, dB, near, margin,
pick, base_pos, base_sign, applied, reason).

Offline test: tools/tests/test_tx_tiebreak.py (synthetic two-class atlas with planted splits; must catch: a split whose box
matches the agreed ink of one candidate is settled for it, a permuted-label control changes picks, a base gap and an
absent class keep the base; must not block: a margin above every row's writes nothing, output = base).
"""
import argparse, csv, os, random, re, sys
from collections import defaultdict
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import join_check as JC
import tx_bench as TB


def rd(p):
    with open(p, encoding='utf-8') as f:
        return list(csv.DictReader((ln for ln in f if not ln.startswith('#')), delimiter='\t'))


def wr(p, cols, rows):
    with open(p, 'w', encoding='utf-8') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(str(r.get(c, '')) for c in cols) + '\n')


def features(atlas, pca_scale='unit'):
    import glyph_atlas as GA
    rows = GA.read(atlas, 'signs.tsv')
    bm = np.load(os.path.join(atlas, 'bitmaps.npz'))['signs']
    X = GA.feats(bm, rows, pca_scale=pca_scale)
    return {r['sid']: X[i] for i, r in enumerate(rows)}, {r['sid']: r['page'] for r in rows}


def col_to_base(base_signs, draft_signs):
    """{draft column index (0-based): base index or None} by tx_bench.align on sign identity."""
    out, j = {}, 0
    for bi, ds in TB.align(base_signs, [{s} for s in base_signs], draft_signs, G=0.75):
        if ds is None:
            continue
        out[j] = bi
        j += 1
    return out


def decide(X, page_of, tiles, agreed, splits, k=5, margin=0.0, rnd=None):
    """agreed: [(sid, line, sign)]; splits: [(line, col, A, B)]; tiles: {(line, col): sid}. -> decision rows."""
    if rnd is not None:                        # shuffled-label null: labels permuted among the agreed tiles of one page
        by_page = defaultdict(list)
        for i, (sid, _, _) in enumerate(agreed):
            by_page[page_of.get(sid, '')].append(i)
        agreed = list(agreed)
        for idx in by_page.values():
            labs = [agreed[i][2] for i in idx]
            rnd.shuffle(labs)
            for i, l in zip(idx, labs):
                agreed[i] = (agreed[i][0], agreed[i][1], l)
    out = []
    for line, col, A, B in splits:
        d = dict(line=line, col=col, A=A, B=B, box='', nA=0, nB=0, dA='', dB='', near='', margin='', pick='', reason='')
        sid = tiles.get((line, col))
        if not sid or sid not in X:
            d['reason'] = 'nobox'; out.append(d); continue
        d['box'] = sid
        x = X[sid]
        dist = {}
        for c in (A, B):
            cand = [agreed_sid for agreed_sid, l, s in agreed if s == c and l != line and agreed_sid in X]
            if not cand:
                dist[c] = None; continue
            ds = np.sort(np.linalg.norm(np.stack([X[s] for s in cand]) - x, axis=1))
            dist[c] = float(ds[:max(1, min(k, len(ds)))].mean())
        d['nA'] = sum(1 for _, l, s in agreed if s == A and l != line)
        d['nB'] = sum(1 for _, l, s in agreed if s == B and l != line)
        if dist[A] is None or dist[B] is None or A == B:
            d['reason'] = 'undecidable'; out.append(d); continue
        d['dA'], d['dB'] = f'{dist[A]:.4f}', f'{dist[B]:.4f}'
        near, far = (A, B) if dist[A] <= dist[B] else (B, A)
        m = (dist[far] - dist[near]) / dist[near] if dist[near] > 0 else float('inf')
        d['near'], d['margin'] = near, f'{m:.4f}'
        if m > margin:
            d['pick'] = near
        else:
            d['reason'] = 'under-margin'
        out.append(d)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--atlas', required=True); ap.add_argument('--map', required=True); ap.add_argument('--tiles')
    ap.add_argument('--rec', required=True); ap.add_argument('--base', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--k', type=int, default=5); ap.add_argument('--margin', type=float, default=0.0)
    ap.add_argument('--line-sub', nargs=2, action='append', default=[], metavar=('PATTERN', 'REPL'))
    ap.add_argument('--permute-seed', type=int); ap.add_argument('--coin-seed', type=int); ap.add_argument('--coin-from')
    ap.add_argument('--allow-unchecked-join')
    ap.add_argument('--pca-scale', choices=['unit', 'shared'], default='unit',
                    help="glyph_atlas feats scaling: 'unit' (classify's default) or 'shared' (small atlases, where 'unit' makes every tile equidistant)")
    a = ap.parse_args(argv)
    JC.require(a.map, a.allow_unchecked_join)
    sub = lambda l: next((re.sub(p, r, l) for p, r in a.line_sub if re.match(p, l)), l)
    X, page_of = features(a.atlas, a.pca_scale)
    if a.tiles:
        tiles = {(r['line'], str(r['pos'])): r['sid'] for r in rd(a.tiles)}
    else:
        tiles = {(r['line'], str(r['pos'])): r['sid'] for r in rd(a.map) if r['op'] == '1:1' and r['sid']}
    draft = rd(os.path.join(a.rec, 'ciphertext_draft.tsv'))
    agreed = [(tiles[(sub(r['line']), r['position'])], sub(r['line']), r['sign'].strip()) for r in draft
              if r['why'] == 'agree' and r['confidence'] != 'L' and (sub(r['line']), r['position']) in tiles]
    splits = [(sub(r['line']), r['col'], r['A'].strip(), r['B'].strip()) for r in rd(os.path.join(a.rec, 'disagreements.tsv'))
              if r['A'].strip() not in ('', '-') and r['B'].strip() not in ('', '-')]
    rnd = random.Random(a.permute_seed) if a.permute_seed is not None else None
    dec = decide(X, page_of, tiles, agreed, splits, a.k, a.margin, rnd)
    if a.coin_seed is not None:
        if not a.coin_from:
            ap.error('--coin-seed needs --coin-from')
        applied = {(r['line'], r['col']) for r in rd(a.coin_from) if r['applied'] == 'yes'}
        crnd = random.Random(a.coin_seed)
        for d in dec:
            if (d['line'], d['col']) in applied:
                d['pick'], d['reason'] = crnd.choice([d['A'], d['B']]), 'coin'
            else:
                d['pick'], d['reason'] = '', d['reason'] or 'not-in-coin-set'
    base = rd(a.base)
    by_line = defaultdict(list)
    for r in base:
        by_line[r['line']].append(r)
    for rows in by_line.values():
        rows.sort(key=lambda r: int(r['pos']))
    draft_by = defaultdict(list)
    for r in draft:
        draft_by[sub(r['line'])].append(r['sign'].strip())
    base_line_of = {sub(l): l for l in by_line}
    for d in dec:
        d['base_pos'] = d['base_sign'] = ''; d['applied'] = 'no'
        bl = base_line_of.get(d['line'])
        if not d['pick'] or bl is None:
            continue
        c2b = col_to_base([r['sign'] for r in by_line[bl]], draft_by[d['line']])
        bi = c2b.get(int(d['col']) - 1)
        if bi is None:
            d['reason'] = 'basegap'; continue
        row = by_line[bl][bi]
        d['base_pos'], d['base_sign'] = row['pos'], row['sign']
        if row['sign'] != d['pick']:
            row['sign'] = d['pick']; d['applied'] = 'yes'
        else:
            d['applied'] = 'same'
    out = []
    seen = set()
    for r in base:
        if r['line'] in seen:
            continue
        seen.add(r['line']); out += by_line[r['line']]
    wr(a.out, ['line', 'pos', 'sign'], out)
    wr(a.out[:-4] + '.decisions.tsv' if a.out.endswith('.tsv') else a.out + '.decisions.tsv',
       ['line', 'col', 'A', 'B', 'box', 'nA', 'nB', 'dA', 'dB', 'near', 'margin', 'pick', 'base_pos', 'base_sign', 'applied', 'reason'], dec)
    n_app = sum(d['applied'] == 'yes' for d in dec)
    print(f'tiebreak: {len(splits)} reachable split rows, {sum(bool(d["box"]) for d in dec)} boxed, '
          f'{sum(bool(d["pick"]) for d in dec)} picked, {n_app} overrides written (margin > {a.margin}, k {a.k}'
          f'{", permuted labels seed " + str(a.permute_seed) if a.permute_seed is not None else ""}'
          f'{", coin seed " + str(a.coin_seed) if a.coin_seed is not None else ""}) -> {a.out}')
    return dec


if __name__ == '__main__':
    main()
