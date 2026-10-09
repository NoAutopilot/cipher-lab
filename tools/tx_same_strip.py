#!/usr/bin/env python3
"""Same-sign retrieval strips (TXE2-SAME, LANE TX-ENGINEER-2, PREREG benchmark-tx/PREREG-txeng2-3.md X7, 9 Oct 2026).

At named doubt positions of a line read L, each sheet row shows the sign in context (target framed, +-1 neighbour, up to
4x) and, for each candidate sign (L's own sign; the lattice runner-up; the taxonomy pair partner if any), a STRIP of up to
--per-strip (6) other occurrences of that sign ON THE SAME PAGE as L reads it (atlas boxes mapped label-blind to L's
positions by tools/tx_compare.py map, op 1:1 only; never another leaf, never a printed cell). The tile's own position and
its two neighbours are never in a strip. Strips are lettered A, B, C in a seeded random order per row; sign names are never
drawn; the row -> sign map is written to a separate key TSV that is NEVER given to the reader. The reader's question per
row: "which strip does the tile belong to, or neither".

The difference from the retired compare family (tx_compare.py, TXE-A/TXE-S): every exemplar is the hand's own page as the
line read reads it, not foreign-page or printed exemplars.

Subcommands
  build    --line-read L.tsv --positions P.tsv (line, pos[, sign]) --box-pos BOX.tsv (tx_compare map output)
           --topk TOPK.tsv (line, pos, cand, score; runner-up = best cand != L's sign) --page PAGE --out DIR
           [--key KEY.tsv] [--confusion C.tsv] [--swap-seed S]. A row is shown only when its position maps to one box
           and at least two candidates have a strip; others are counted ('unmapped', 'one_strip') and keep L.
           --swap-seed S (the registered control): every shown row's strips are cyclically shifted by a seeded nonzero
           amount between its candidates, while the key keeps the unshifted letter -> sign map, so the reader's true
           match resolves to a different sign.
           Writes DIR/row_NNN.png (one per shown row; the reader's material), KEY (row, line, pos, L, A, B, C, n_A..,
           why) and prints counts.
  resolve  --line-read L.tsv --key KEY.tsv --reads READS.tsv (row, pick, conf[, note]; pick A/B/C, neither or ?)
           --pass-out OUT.tsv [--positions-only]: pick -> that strip's sign (per the key), neither/? -> L's sign.
           Writes every L position (line, pos, sign).

Test: tools/tests/test_tx_same_strip.py (offline).
"""
import argparse
import csv
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAIRS = ['T18/T98', 'T90/T53', 'T76/T66', 'T76/T86', 'T76/T45', 'T64/T95', 'T64/T51', 'T50/T36', 'T92/T95', 'T92/T98',
         'T83/T24', 'T60/T86', 'T13/T64']                          # = tools/tx_pair_reread.py PAIRS (taxonomy class 1)
LETTERS = 'ABC'
SKIP = {'_', '?', '', 'UNK'}


def rd(p):
    with open(p) as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def wr(p, cols, rows):
    os.makedirs(os.path.dirname(os.path.abspath(p)), exist_ok=True)
    with open(p, 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(str(r.get(c, '')) for c in cols) + '\n')


def path(p):
    return p if os.path.isabs(p) else os.path.join(ROOT, p)


def partner(code, confusion_counts):
    """Taxonomy pair partner: of the PAIRS naming `code`, the one with the highest confusion count (ties: list order)."""
    best = None
    for k, p in enumerate(PAIRS):
        a, b = p.split('/')
        if code not in (a, b):
            continue
        sc = (confusion_counts.get(frozenset((a, b)), 0), -k)
        if best is None or sc > best[0]:
            best = (sc, b if code == a else a)
    return best[1] if best else None


def runner_up(cands, lsign):
    """cands: [(cand, score)] -> highest-scoring cand that is not L's sign (or a skip code)."""
    for c, _ in sorted(cands, key=lambda t: -t[1]):
        if c != lsign and c not in SKIP:
            return c
    return None


def occurrences(L, box1, page):
    """sign -> [(line, pos, sid)] for L's 1:1-mapped positions on `page`."""
    occ = {}
    for r in L:
        if not r['line'].startswith(page + '_'):
            continue
        sid = box1.get((r['line'], r['pos']))
        if sid:
            occ.setdefault(r['sign'], []).append((r['line'], int(r['pos']), sid))
    return occ


def pick_strip(occ_list, line, pos, n, rng):
    pool = [o for o in occ_list if not (o[0] == line and abs(o[1] - pos) <= 1)]
    rng.shuffle(pool)
    return pool[:n]


def plan(L, positions, box_rows, topk, page, confusion_counts, per_strip=6, seed=0, swap_seed=None):
    """Pure planning step (no images): -> (rows, counts). rows carry line, pos, L, cands [(letter, sign, [sids])],
    why, sid; with swap_seed the strips are shifted between letters while each letter keeps its own sign in the key."""
    box1, nbox = {}, {}
    for b in box_rows:
        k = (b['line'], b['pos'])
        nbox[k] = nbox.get(k, 0) + 1
        if b.get('op', '1:1') == '1:1':
            box1[k] = b['sid']
    Ls = {(r['line'], r['pos']): r['sign'] for r in L}
    occ = occurrences(L, box1, page)
    tk = {}
    for r in topk:
        tk.setdefault((r['line'], r['pos']), []).append((r['cand'], float(r['score'])))
    rows, counts = [], {'positions': 0, 'shown': 0, 'unmapped': 0, 'one_strip': 0}
    for i, p in enumerate(positions):
        counts['positions'] += 1
        key = (p['line'], str(p['pos']))
        ls = Ls.get(key)
        sid = box1.get(key)
        if ls is None or sid is None:
            counts['unmapped'] += 1
            continue
        cands, why = [ls], ['L']
        ru = runner_up(tk.get(key, []), ls)
        if ru and ru not in cands:
            cands.append(ru); why.append('latt')
        pt = partner(ls, confusion_counts)
        if pt and pt not in cands:
            cands.append(pt); why.append('pair')
        rng = random.Random(f'{seed}:{key[0]}:{key[1]}')
        strips = []
        for c, w in zip(cands, why):
            s = pick_strip(occ.get(c, []), key[0], int(key[1]), per_strip, rng)
            if s:
                strips.append((c, w, [o[2] for o in s]))
        if len(strips) < 2:
            counts['one_strip'] += 1
            continue
        rng.shuffle(strips)
        shown = [s[2] for s in strips]
        if swap_seed is not None:
            srng = random.Random(f'swap{swap_seed}:{key[0]}:{key[1]}')
            k = srng.randrange(1, len(strips))
            shown = shown[k:] + shown[:k]
        rows.append({'line': key[0], 'pos': key[1], 'L': ls, 'sid': sid,
                     'cands': [(LETTERS[j], strips[j][0], strips[j][1], shown[j]) for j in range(len(strips))]})
        counts['shown'] += 1
    return rows, counts


def render_row(pages, page_rows, row, n, out, per_strip, scale=4.0, cell=120):
    from PIL import Image, ImageDraw
    import tx_compare as tc
    ctx = tc.context_tile(pages, page_rows, [row['sid']], target_h=68 * scale, max_scale=scale, max_w=1100)
    strips = []
    for letter, _, _, sids in row['cands']:
        im = Image.new('RGB', (60 + per_strip * (cell + 6), cell + 8), 'white')
        d = ImageDraw.Draw(im)
        d.text((12, cell // 2 - 18), letter, fill=(0, 0, 0), font=tc.font(36))
        for j, s in enumerate(sids):
            im.paste(tc.exemplar_tile(pages, page_rows[s], cell).convert('RGB'), (60 + j * (cell + 6), 4))
        strips.append(im)
    W = max(ctx.width, max(s.width for s in strips)) + 20
    H = 50 + ctx.height + 20 + sum(s.height + 14 for s in strips)
    sheet = Image.new('RGB', (W, H), 'white')
    d = ImageDraw.Draw(sheet)
    d.text((10, 8), f'Row {n}: tile (framed sign)', fill=(0, 0, 0), font=tc.font(28))
    sheet.paste(ctx, (10, 50))
    y = 50 + ctx.height + 20
    for s in strips:
        d.line((10, y - 6, W - 10, y - 6), fill=(120, 120, 120), width=1)
        sheet.paste(s, (10, y)); y += s.height + 14
    sheet.convert('L').save(out)


def cmd_build(a):
    L = rd(path(a.line_read))
    positions = rd(path(a.positions))
    box_rows = rd(path(a.box_pos))
    topk = rd(path(a.topk)) if a.topk else []
    cc = {}
    if a.confusion and os.path.exists(path(a.confusion)):
        for r in rd(path(a.confusion)):
            cc[frozenset((r['label_a'], r['label_b']))] = int(r['n'])
    rows, counts = plan(L, positions, box_rows, topk, a.page, cc, a.per_strip, a.seed, a.swap_seed)
    out = path(a.out)
    os.makedirs(out, exist_ok=True)
    if not a.dry:
        import tx_compare as tc
        signs = rd(os.path.join(path(a.atlas), 'signs.tsv'))
        page_rows = {s['sid']: s for s in signs if s['page'] == a.page}
        pages = tc.Pages(a.atlas)
    krows = []
    for n, r in enumerate(rows, 1):
        if not a.dry:
            render_row(pages, page_rows, r, n, os.path.join(out, f'row_{n:03d}.png'), a.per_strip)
        kr = {'row': n, 'line': r['line'], 'pos': r['pos'], 'L': r['L'], 'sid': r['sid']}
        for letter, sign, why, sids in r['cands']:
            kr[letter] = sign; kr['why_' + letter] = why; kr['n_' + letter] = len(sids)
            kr['strip_' + letter] = ','.join(sids)
        krows.append(kr)
    cols = ['row', 'line', 'pos', 'L', 'sid'] + [f'{x}{l}' for l in LETTERS for x in ('', 'why_', 'n_', 'strip_')]
    wr(path(a.key), cols, krows)
    print(f'build: {counts} -> {out} ({len(rows)} rows), key {a.key}')
    return counts


def cmd_resolve(a):
    L = rd(path(a.line_read))
    key = {r['row']: r for r in rd(path(a.key))}
    change, stats = {}, {'pick': 0, 'neither': 0, 'changed': 0, 'kept_L': 0, 'missing': 0}
    reads = {r['row'].strip(): r for r in rd(path(a.reads))}
    for n, k in key.items():
        r = reads.get(n)
        if r is None:
            stats['missing'] += 1; continue
        pk = r['pick'].strip().upper()
        if pk in LETTERS and k.get(pk):
            stats['pick'] += 1
            if k[pk] != k['L']:
                change[(k['line'], k['pos'])] = k[pk]; stats['changed'] += 1
            else:
                stats['kept_L'] += 1
        else:
            stats['neither'] += 1
    out = [{'line': r['line'], 'pos': r['pos'], 'sign': change.get((r['line'], r['pos']), r['sign'])} for r in L]
    wr(path(a.pass_out), ['line', 'pos', 'sign'], out)
    print(f'resolve: {stats} -> {a.pass_out}')
    return stats


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest='cmd', required=True)
    b = sp.add_parser('build')
    b.add_argument('--line-read', required=True)
    b.add_argument('--positions', required=True)
    b.add_argument('--box-pos', required=True)
    b.add_argument('--topk')
    b.add_argument('--page', required=True)
    b.add_argument('--atlas', default='ciphers/nevers-birago-fr3251-1572/atlas')
    b.add_argument('--confusion', default='ciphers/nevers-birago-fr3251-1572/harvest/confusion_1572.tsv')
    b.add_argument('--out', required=True)
    b.add_argument('--key', required=True)
    b.add_argument('--per-strip', type=int, default=6)
    b.add_argument('--seed', type=int, default=0)
    b.add_argument('--swap-seed', type=int)
    b.add_argument('--dry', action='store_true', help='plan and write the key only, no images')
    r = sp.add_parser('resolve')
    r.add_argument('--line-read', required=True)
    r.add_argument('--key', required=True)
    r.add_argument('--reads', required=True)
    r.add_argument('--pass-out', required=True)
    a = ap.parse_args(argv)
    return {'build': cmd_build, 'resolve': cmd_resolve}[a.cmd](a)


if __name__ == '__main__':
    main()
