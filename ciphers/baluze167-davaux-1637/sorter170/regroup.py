#!/usr/bin/env python3
"""R12A-BALS (6 Oct 2026): second pass over build_inputs.py's tiles (tools/sorter_recut.py over-splits on purpose).
1. Marks: a tile shorter than MARK_H px whose bottom sits above row MARK_BOT of its 221-row strip (strip centre row 110; digits
   sit on rows ~85-140) is an accent/diaeresis/bar, not a sign: it goes to marks.tsv attached to the tile below it with the most
   x-overlap (nearest centre within 40 px if none), so tools/sign_sorter.py --marks cuts that sign's tile around both and the
   mark/no-mark question is visible on the tile.
2. Groups: per line, a monotone DP matches the remaining tiles to the reader columns (build_inputs.glyph_cols); a digit column
   takes one tile, a letter-sign column takes 1-3 adjacent tiles (gap < GAP px: u4 = u + 4, y+ = y + cross, the hook's tail),
   specks (under 30 px tall and 700 px^2: dots, dashes, stray ink below the marks' rows) are dropped first; columns are laid out
   over each span's ink as digit 1 unit, letter sign 2, 0.1 inside a number, 0.8 between tokens;
   cost 0.6 x |group centre - column centre| + 2 per extra piece + 25 for a letter sign under 55 px wide, 15 or a digit over 75; skip tile 45, skip column 70. A multi-tile group becomes one
   tile (union box), except that a group wider than W_CAP px (2.5 x the ~41 px digit, the preflight's merged-sign line)
   stays in pieces: the first takes the pile, each further piece sits in the same pile with a focus question. Unmatched tiles keep sorter_recut's shape-cluster pile and are focus questions.
3. Focus: the classes the D1-BAL170B reconciliation could not settle: u4/4u, q, ff, the hook/wave/v, y+, h, ll, m4, gam, g+;
   every numeral ending in 6 (marked or not: does the stroke over it belong to it?); every column the reconciled sheet marked ?;
   and the unmatched tiles.
Writes signs.tsv, labels.tsv, marks.tsv, focus.tsv (overwriting build_inputs.py's) and regroup_fit.tsv.
"""
import csv, sys
from collections import defaultdict
from pathlib import Path
import numpy as np
S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
import build_inputs as bi  # noqa: E402
MARK_H, MARK_BOT, GAP, W_CAP = 52, 92, 26, 100
LETTER_Q = {'u4': 'u4 or 4u (the crossed minim before or after the 4)? Move to the 4u pile if the 4 comes first; Fix the cut if two signs.',
            'q': 'q-shaped letter sign or the digit 9 (straight descender = q, curved tail = 9)?',
            'ff': 'the crossed double long s: one sign (ff pile) or two s signs? Fix the cut if two.',
            'hook': 'hook, wave or v: which of the three wave-shaped signs is this?', 'wave': 'hook, wave or v: which wave-shaped sign is this?',
            'v': 'hook, wave or v: which wave-shaped sign is this?', 'y+': 'y with a cross stroke (y+): right pile, or another sign?',
            'h': 'h-shaped sign: right pile, or another sign?', 'll': 'll or u4? (the readers split on this shape)',
            'm4': 'm4 or u4? (the minims before the 4)', 'gam': 'gamma-shaped sign: right pile, or another sign?',
            'g+': 'g with a cross (g+, written gt-like): right pile, or another sign?'}


def rd(n): return list(csv.DictReader(open(S / n), delimiter='\t'))


def main():
    sig = rd('signs.tsv'); lab = {r['sid']: r for r in rd('labels.tsv')}
    for r in sig:
        for k in 'xywh': r[k] = int(r[k])
    unc = {(r['line'], int(r['col'])) for r in rd('uncertain_cols.tsv')}
    # reader columns again (same code path as build_inputs)
    rec = {}
    for f in ('passes/reconciled_b170f228r.tsv', 'passes/reconciled_b170f228v.tsv'):
        for ln in open(bi.T / f):
            if ln.startswith('#') or ln.startswith('line\t'): continue
            k, v = ln.rstrip('\n').split('\t', 1); rec[k] = v
    from PIL import Image
    byline = defaultdict(list)
    for r in sig: byline[r['page']].append(r)
    out, marks, focus, fit = [], [], [], []
    for ln in bi.LINES:
        ts = sorted(byline[ln], key=lambda r: r['x'])
        mk = [t for t in ts if t['h'] < MARK_H and t['y'] + t['h'] < MARK_BOT]
        speck = [t for t in ts if t not in mk and t['h'] < 30 and t['w'] * t['h'] < 700]   # dots, dashes, stray ink on the line
        base = [t for t in ts if t not in mk and t not in speck]
        # columns with centres re-spread over each cipher span's base-tile extent
        cols = []
        for run, (x0, x1) in zip(bi.spans_tokens(rec[ln]), bi.CIPHER[ln]):
            inside = [t for t in base if x0 <= t['x'] + t['w'] / 2 <= x1]
            e0 = min(t['x'] for t in inside); e1 = max(t['x'] + t['w'] for t in inside)
            # expected layout: a digit 1 unit wide, a letter sign 2, 0.1 between the digits of one number, 0.8 between tokens
            lay, pos = [], 0.0
            for ti, t in enumerate(run):
                for gi, (p, f) in enumerate(bi.glyph_cols(t)):
                    if ti or gi: pos += 0.1 if gi else 0.8
                    wd = 1.0 if f.isdigit() else 2.0; lay.append((p, f, pos + wd / 2)); pos += wd
            for p, f, c in lay: cols.append((p, f, e0 + c / pos * (e1 - e0)))
        n, m = len(base), len(cols); INF = 1e18
        D = np.full((n + 1, m + 1), INF); B = {}; D[0, 0] = 0
        for i in range(n + 1):
            for j in range(m + 1):
                if D[i, j] >= INF: continue
                if i < n and D[i, j] + 45 < D[i + 1, j]: D[i + 1, j] = D[i, j] + 45; B[i + 1, j] = (i, j, 0)
                if j < m and D[i, j] + 70 < D[i, j + 1]: D[i, j + 1] = D[i, j] + 70; B[i, j + 1] = (i, j, -1)
                if j < m:
                    letter = not cols[j][1].isdigit()
                    for k in (1, 2, 3) if letter else (1,):
                        if i + k > n: break
                        g = base[i:i + k]
                        if k > 1 and g[-1]['x'] - (g[-2]['x'] + g[-2]['w']) > GAP: break
                        cx = (g[0]['x'] + g[-1]['x'] + g[-1]['w']) / 2
                        gw = g[-1]['x'] + g[-1]['w'] - g[0]['x']
                        c = (D[i, j] + .6 * abs(cx - cols[j][2]) + 2 * (k - 1)
                             + (25 if letter and gw < 55 else 0) + (15 if not letter and gw > 75 else 0))
                        if c < D[i + k, j + 1]: D[i + k, j + 1] = c; B[i + k, j + 1] = (i, j, k)
        i, j, grp = n, m, []
        while (i, j) != (0, 0):
            pi, pj, k = B[i, j]
            if k > 0: grp.append((base[pi:i], j - 1))
            elif k == 0: grp.append(([base[pi]], None))
            i, j = pi, pj
        grp.reverse(); kk = 0; matched = 0
        sub = []
        for g, j in grp:          # a group wider than W_CAP (2.5 x the ~41 px digit, the preflight's merged-sign line) stays in pieces
            cur = [g[0]]
            for t in g[1:]:
                if t['x'] + t['w'] - cur[0]['x'] > W_CAP: sub.append((cur, j, len(sub) and sub[-1][1] == j and j is not None)); cur = [t]
                else: cur.append(t)
            sub.append((cur, j, bool(sub) and sub[-1][1] == j and j is not None))
        for g, j, piece in sub:
            kk += 1; sid = f'{ln}_{kk:02d}'
            x0 = min(t['x'] for t in g); y0 = min(t['y'] for t in g); x1 = max(t['x'] + t['w'] for t in g); y1 = max(t['y'] + t['h'] for t in g)
            if j is not None:
                pile, fam = cols[j][0], cols[j][1]; matched += 0 if piece else 1
            else:
                l0 = lab[g[0]['sid']]; pile, fam = l0['sign'], l0['family']
            out.append(dict(sid=sid, page=ln, x=x0, y=y0, w=x1 - x0, h=y1 - y0, sign=pile, family=fam, j=j, n=len(g)))
            short = sid.split('_', 1)[1]
            if piece:
                focus.append((sid, f'{short}: the right-hand piece of the {pile} before it (cut apart because the whole is wider than 2.5 digits). One sign with its left neighbour (Fix the cut to join), or a sign of its own?'))
            elif j is None:
                focus.append((sid, f'{short}: cut from the ink, no reader column lined up with it; started in the {pile} pile by shape. Right pile, another sign, or a bad cut / not a sign?'))
            elif not fam.isdigit() and fam in LETTER_Q:
                focus.append((sid, f'{short}: {LETTER_Q[fam]}'))
            elif fam == '6':
                focus.append((sid, f'{short}: a 6 {"with" if pile != "6" else "without"} a mark on the reconciled sheet. Is there an accent over it (6\' pile) or not (6 pile)? The curled top of this hand\'s 6 and descenders from the line above can look like an accent.'))
            elif (ln, j + 1) in unc:
                focus.append((sid, f'{short}: the reconciled sheet marks this sign uncertain (started in {pile}). Right pile, another sign, or a bad cut?'))
        rows = [t for t in out if t['page'] == ln]
        for t in mk:
            cx = t['x'] + t['w'] / 2; best, bo = None, 0
            for r in rows:
                ov = min(r['x'] + r['w'], t['x'] + t['w']) - max(r['x'], t['x'])
                if ov > bo: best, bo = r, ov
            if best is None:
                near = min(rows, key=lambda r: abs(r['x'] + r['w'] / 2 - cx))
                if abs(near['x'] + near['w'] / 2 - cx) <= 40: best = near
            if best is not None: marks.append((t['x'], t['y'], t['w'], t['h'], best['sid']))
        fit.append((ln, len(ts), len(mk), len(speck), len(sub), matched, m))
    seen = set(); focus = [f for f in focus if not (f[0] in seen or seen.add(f[0]))]
    with open(S / 'signs.tsv', 'w') as o:
        o.write('sid\tpage\tx\ty\tw\th\n'); o.writelines(f"{t['sid']}\t{t['page']}\t{t['x']}\t{t['y']}\t{t['w']}\t{t['h']}\n" for t in out)
    with open(S / 'labels.tsv', 'w') as o:
        o.write('sid\tsign\tfamily\n'); o.writelines(f"{t['sid']}\t{t['sign']}\t{t['family']}\n" for t in out)
    with open(S / 'marks.tsv', 'w') as o:
        o.write('x\ty\tw\th\tsid\n'); o.writelines('\t'.join(map(str, m)) + '\n' for m in marks)
    with open(S / 'focus.tsv', 'w') as o: o.writelines(f'{s}\t{q}\n' for s, q in focus)
    with open(S / 'regroup_fit.tsv', 'w') as o:
        o.write('line\traw_tiles\tmarks\tspecks_dropped\ttiles\tmatched\tcolumns\n'); o.writelines('\t'.join(map(str, f)) + '\n' for f in fit)
    print(len(out), 'tiles;', len(marks), 'marks;', sum(f[3] for f in fit), 'specks dropped;', sum(f[5] for f in fit), 'of', sum(f[6] for f in fit), 'columns matched;', len(focus), 'focus')
    for f in fit: print(*f, sep='\t')


if __name__ == '__main__':
    main()
