#!/usr/bin/env python3
"""TXE2-CELLS harness (PREREG-txeng2-3 X13; LANE TX-ENGINEER-2, 9 Oct 2026). Disk only, no network, no model.

  build   rows = the X9 combo feed's dev_tune positions (latt OR vote OR selfcons in txeng2/doubt/dev_tune_signals3.tsv)
          with a 1:1 atlas box (txeng/pair/dev_tune/box_pos.tsv, TXE-C's label-blind width DP). Per row: the boxed tile at
          4x with +-1 neighbour (tx_pair_reread.context_tile), and the NAMES of two cells: L's sign and lattice d's best
          candidate != L (txeng2/latt/topk_d.tsv). A/B order seeded random per row ('txe2-cells:<line>:<pos>').
          Arm 'real' -> rows/real/row_NN.jpg + key_real.tsv; arm 'control' (registered): the alternative replaced by a
          random sheet cell (T10..T98 sheet names, not L, not the lattice alternative; random.Random(1) in row order)
          -> rows/control/row_NN.jpg + key_control.tsv. The names are printed on the row image; the key (which name is L)
          is never shown. A row whose lattice has no candidate other than L is not shown (keeps L), counted.
          Off-sheet L names (X_CE, X_NEW ...) are printed as 'off-sheet form (no cell)'.
  resolve --arm real|control: reads_<arm>_*.tsv (row, pick A/B/neither/?, conf, feature) + key -> outputs/birago1572-no87/
          passX13_<arm>_dev_tune.tsv over every dev_tune L position: A/B -> that name's sign, neither/? -> L.
Never opens a truth file.
"""
import argparse, csv, os, random, re, sys
from collections import Counter
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import tx_pair_reread as P

HERE = os.path.dirname(os.path.abspath(__file__))
FOLDER = os.path.join(ROOT, 'ciphers', 'nevers-birago-fr3251-1572')
SIG = os.path.join(ROOT, 'benchmark-tx', 'txeng2', 'doubt', 'dev_tune_signals3.tsv')
BOX = os.path.join(ROOT, 'benchmark-tx', 'txeng', 'pair', 'dev_tune', 'box_pos.tsv')
TOPK = os.path.join(ROOT, 'benchmark-tx', 'txeng2', 'latt', 'topk_d.tsv')
L_DEV = os.path.join(ROOT, 'benchmark-tx', 'txeng', 'units', 'labels_dev_tune.tsv')
OUTD = os.path.join(ROOT, 'benchmark-tx', 'outputs', 'birago1572-no87')


def sheet_names():
    """The 51 cell names on sign_sheet_blind_1572.png, read from the sheet's own cut script output (sign_id_map keys)."""
    import json
    m = json.load(open(os.path.join(FOLDER, 'harvest', 'sign_id_map_1572.json')))
    return sorted(r['id'] for r in m if re.fullmatch(r'T\d\d', r['id']))   # ids only; values never read


def disp(name):
    return name if re.fullmatch(r'T\d\d', name) else 'off-sheet form (no cell)'


def rows_build():
    sig = P.rd(SIG)
    combo = [(r['line'], r['pos'], r['sign']) for r in sig if '1' in (r['latt'], r['vote'], r['selfcons'])]
    bp = {(r['line'], r['pos']): r for r in P.rd(BOX)}
    tk = {}
    for r in P.rd(TOPK):
        tk.setdefault((r['line'], r['pos']), []).append((float(r['score']), r['cand']))
    out, nobox, noalt = [], [], []
    for ln, pos, L in combo:
        b = bp.get((ln, pos))
        alts = [c for s, c in sorted(tk.get((ln, pos), []), key=lambda x: -x[0]) if c != L]
        if not b:
            nobox.append((ln, pos)); continue
        if not alts:
            noalt.append((ln, pos)); continue
        out.append(dict(line=ln, pos=pos, sid=b['sid'], L=L, alt=alts[0]))
    return out, nobox, noalt


def cmd_build(a):
    from PIL import Image, ImageDraw, ImageFont
    rows, nobox, noalt = rows_build()
    names = sheet_names()
    rng_c = random.Random(1)
    for r in rows:
        pool = [n for n in names if n not in (r['L'], r['alt'])]
        r['rand'] = rng_c.choice(pool)
    signs = {s['sid']: s for s in P.rd(os.path.join(FOLDER, 'atlas', 'signs.tsv'))}
    pages = P.load_pages(FOLDER, sorted({signs[r['sid']]['page'] for r in rows}))
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 34)
    for arm, other in (('real', 'alt'), ('control', 'rand')):
        d = os.path.join(HERE, 'rows', arm); os.makedirs(d, exist_ok=True)
        for f in os.listdir(d):
            os.remove(os.path.join(d, f))
        key = []
        for i, r in enumerate(rows, 1):
            s = signs[r['sid']]; leaf = s['page']
            same = sorted([b for b in signs.values() if b['page'] == leaf and b['line'] == s['line']],
                          key=lambda b: int(b['x']))
            ctx = P.context_tile(pages[leaf], s, same, a.zoom)
            codes = [r['L'], r[other]]
            if random.Random(f'txe2-cells:{r["line"]}:{r["pos"]}').random() < 0.5:
                codes = codes[::-1]
            W = max(ctx.width + 40, 1100)
            im = Image.new('RGB', (W, ctx.height + 130), 'white')
            dr = ImageDraw.Draw(im)
            dr.text((20, 15), f'Row {i}:   A = {disp(codes[0])}     B = {disp(codes[1])}', fill='black', font=font)
            im.paste(ctx, (20, 110))
            im.save(os.path.join(d, f'row_{i:02d}.jpg'), quality=88)
            key.append(dict(row=i, line=r['line'], pos=r['pos'], sid=r['sid'], L=r['L'], A=codes[0], B=codes[1]))
        P.wr(os.path.join(HERE, f'key_{arm}.tsv'), ['row', 'line', 'pos', 'sid', 'L', 'A', 'B'], key)
    print(f'combo positions {len(rows) + len(nobox) + len(noalt)}; rows {len(rows)}; no 1:1 box {len(nobox)} {nobox}; '
          f'no lattice alternative {len(noalt)} {noalt}')
    return 0


def cmd_resolve(a):
    key = P.rd(os.path.join(HERE, f'key_{a.arm}.tsv'))
    picks = {}
    for f in sorted(os.listdir(HERE)):
        if re.fullmatch(rf'reads_{a.arm}_\d+\.tsv', f):
            for r in P.rd(os.path.join(HERE, f)):
                picks[str(r['row']).strip()] = (r.get('pick') or '?').strip()
    change, tally = {}, Counter()
    for k in key:
        p = picks.get(k['row'], 'missing')
        p = p.upper() if p.upper() in ('A', 'B') else p.lower()
        new = k[p] if p in ('A', 'B') else k['L']
        tally['keepL' if p in ('A', 'B') and new == k['L'] else ('other' if p in ('A', 'B') else p)] += 1
        change[(k['line'], k['pos'])] = new
    L = P.rd(L_DEV)
    rows = [dict(line=r['line'], pos=r['pos'], sign=change.get((r['line'], r['pos']), r['sign'])) for r in L]
    dst = os.path.join(OUTD, f'passX13_{a.arm}_dev_tune.tsv')
    P.wr(dst, ['line', 'pos', 'sign'], rows)
    print(f'{dst}: {len(rows)} positions; picks ' + ', '.join(f'{k} {v}' for k, v in sorted(tally.items())))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest='cmd', required=True)
    b = sp.add_parser('build'); b.add_argument('--zoom', type=float, default=4.0)
    r = sp.add_parser('resolve'); r.add_argument('--arm', choices=['real', 'control'], required=True)
    a = ap.parse_args()
    return cmd_build(a) if a.cmd == 'build' else cmd_resolve(a)


if __name__ == '__main__':
    sys.exit(main())
