#!/usr/bin/env python3
"""Pair hints for a blind reader's brief (TXE-H, LANE TX-ENGINEER, idea M17; 9 Oct 2026; benchmark-tx/PREREG-txeng-2.md).

Lesson it answers (research/TX-TAXONOMY-2026-10-09.md class 1; TXE-A): showing look-alike exemplars beside a sign made
the reader swap right reads for the look-alike (fixed 4 / broken 16). This tool tests the cheapest form of the same
knowledge: the reader keeps the ordinary blind line read, and the brief names, for each look-alike pair, the ONE shape
feature that separates the two codes in the hand's own secure tiles -- one plain sentence per pair.

Subcommands (disk only, no network, no model):
  derive   --pairs T18/T98,... --exemplars atlas/sheet_truth/sheet.tsv --atlas DIR --out hints.md --sheet hints_sheet.png
           For each pair, the secure tiles of each code (atlas/secure_tokens.tsv rows on non-no.87 leaves; never a no.87
           tile, never labels.json) on the page image; three statistics per tile:
             descender = (box bottom - the line's median box bottom) / box height, floored at 0;
             loops     = holes in the ink (background components not touching the tile edge, area >= 1% of the box);
             bars      = horizontal ink runs wider than 0.6 x width (groups of consecutive such rows);
           d' = |mean_a - mean_b| / sqrt((var_a + var_b) / 2) per statistic; the largest is written as one sentence.
           A pair is DROPPED (printed, never in hints.md) when a code has fewer than --min-tiles secure tiles or the best
           d' < --min-d. Writes hints.md (the reader section), hints_dprime.tsv and a sheet (3 tiles of each code per row,
           the tiles named in sheet.tsv's exemplars column first).
  assemble --base harvest/blind_pass_brief_1572.md --hints hints.md --sheet hints_sheet.png --crops ... --out task.md
           The unchanged base brief + the hints section + the task lines (sheet, hints sheet, crops, output path).
  norm     --raw RAW.tsv --leaf f178v --out passX.tsv   (passage,pos,sign_id) -> (line,pos,sign), as build_birago87.py.
"""
import argparse, csv, math, os, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
NO87 = ('f178r', 'f178v', 'f179r')
PAIRS = 'T18/T98,T90/T53,T76/T66,T76/T86,T76/T45,T64/T95,T64/T51,T50/T36,T92/T95,T92/T98,T83/T24,T60/T86'
STATS = ('descender', 'loops', 'bars')
SECTION = 'Pairs that are easy to confuse: what decides them'


def rd(p):
    with open(p, newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


# ---------- statistics (pure; tested offline) ----------
def ink_mask(tile):
    """Boolean ink mask of a greyscale tile (Otsu threshold; ink is dark)."""
    import numpy as np
    t = np.asarray(tile, dtype=float)
    if t.max() == t.min():
        return np.zeros(t.shape, bool)
    hist, edges = np.histogram(t, bins=64)
    mids = (edges[:-1] + edges[1:]) / 2
    best, thr, tot, sm = -1, mids[0], hist.sum(), (hist * mids).sum()
    w0 = s0 = 0.0
    for h, m in zip(hist, mids):
        w0 += h; s0 += h * m
        if w0 == 0 or w0 == tot:
            continue
        m0, m1 = s0 / w0, (sm - s0) / (tot - w0)
        v = w0 * (tot - w0) * (m0 - m1) ** 2
        if v > best:
            best, thr = v, m
    return t < thr


def count_loops(ink, min_frac=0.01):
    """Enclosed background regions (holes) of the ink, 4-connected background, area >= min_frac of the tile."""
    from scipy import ndimage
    bg = ~ink
    lab, n = ndimage.label(bg)
    if n == 0:
        return 0
    edge = set(lab[0, :]) | set(lab[-1, :]) | set(lab[:, 0]) | set(lab[:, -1])
    sizes = ndimage.sum(bg, lab, range(1, n + 1))
    minarea = max(2, min_frac * ink.size)
    return sum(1 for i, s in enumerate(sizes, 1) if i not in edge and s >= minarea)


def count_bars(ink, frac=0.6):
    """Groups of consecutive rows whose longest horizontal ink run exceeds frac x tile width."""
    import numpy as np
    W = ink.shape[1]
    hit = []
    for row in ink:
        best = cur = 0
        for v in row:
            cur = cur + 1 if v else 0
            best = max(best, cur)
        hit.append(best > frac * W)
    return int(sum(1 for i, h in enumerate(hit) if h and (i == 0 or not hit[i - 1])))


def descender(bottom, baseline, h):
    return max(0.0, (bottom - baseline) / float(h)) if h else 0.0


def tile_stats(ink, bottom, baseline, h):
    return {'descender': descender(bottom, baseline, h), 'loops': count_loops(ink), 'bars': count_bars(ink)}


def dprime(a, b):
    n1, n2 = len(a), len(b)
    if n1 < 2 or n2 < 2:
        return 0.0
    m1, m2 = sum(a) / n1, sum(b) / n2
    v1 = sum((x - m1) ** 2 for x in a) / (n1 - 1)
    v2 = sum((x - m2) ** 2 for x in b) / (n2 - 1)
    sd = math.sqrt((v1 + v2) / 2)
    if sd == 0:
        return 0.0 if m1 == m2 else 99.0
    return abs(m1 - m2) / sd


FRACS = [(0.1, 'a tenth'), (0.2, 'a fifth'), (0.25, 'a quarter'), (1 / 3, 'a third'), (0.5, 'half'), (2 / 3, 'two thirds'),
         (1.0, 'its full height')]


def frac_word(v):
    return min(FRACS, key=lambda f: abs(f[0] - v))[1]


def count_word(n, one, many):
    n = int(round(n))
    if n == 0:
        return 'no ' + many
    return {1: 'one ', 2: 'two ', 3: 'three '}.get(n, f'{n} ') + (one if n == 1 else many)


def sentence(a, b, stat, ma, mb):
    """One plain sentence naming the feature that decides a vs b (means ma, mb of `stat`)."""
    if stat == 'descender':
        hi, lo, mh, ml = (a, b, ma, mb) if ma >= mb else (b, a, mb, ma)
        low = (f"{lo}'s does not" if ml < 0.07 else f"{lo}'s only by about {frac_word(ml)}")
        return f"{a} vs {b}: {hi}'s tail goes below the line by about {frac_word(mh)} of its height; {low}."
    if stat == 'loops':
        if int(round(ma)) == int(round(mb)):
            hi, lo = (a, b) if ma > mb else (b, a)
            return f"{a} vs {b}: {hi} more often has a closed loop than {lo}."
        return (f"{a} vs {b}: {a} has {count_word(ma, 'closed loop', 'closed loops')}; "
                f"{b} has {count_word(mb, 'closed loop', 'closed loops')}.")
    if int(round(ma)) == int(round(mb)):
        hi, lo = (a, b) if ma > mb else (b, a)
        return f"{a} vs {b}: {hi} more often has a long horizontal bar across most of its width than {lo}."
    return (f"{a} vs {b}: {a} has {count_word(ma, 'long horizontal bar', 'long horizontal bars')} across most of its "
            f"width; {b} has {count_word(mb, 'long horizontal bar', 'long horizontal bars')}.")


def decide(a, b, sa, sb, min_tiles=3, min_d=1.0):
    """sa, sb: lists of stat dicts. -> (kept, best_stat, d, ma, mb, all_d, reason)."""
    if len(sa) < min_tiles or len(sb) < min_tiles:
        return False, '', 0.0, 0, 0, {}, f'too few secure tiles ({a} {len(sa)}, {b} {len(sb)}; need {min_tiles})'
    ds = {s: dprime([t[s] for t in sa], [t[s] for t in sb]) for s in STATS}
    best = max(STATS, key=lambda s: ds[s])
    ma = sum(t[best] for t in sa) / len(sa)
    mb = sum(t[best] for t in sb) / len(sb)
    if ds[best] < min_d:
        return False, best, ds[best], ma, mb, ds, f"best d' {ds[best]:.2f} < {min_d}"
    return True, best, ds[best], ma, mb, ds, ''


# ---------- derive ----------
def cmd_derive(a):
    from tx_pair_reread import load_pages, tile
    atlas = a.atlas
    folder = os.path.dirname(os.path.abspath(atlas))
    sheet = {r['code']: r for r in rd(a.exemplars)}
    signs = {r['sid']: r for r in rd(os.path.join(atlas, 'signs.tsv'))}
    by_line = defaultdict(list)
    for r in signs.values():
        by_line[(r['page'], r['line'])].append(int(r['y']) + int(r['h']))
    base = {k: sorted(v)[len(v) // 2] for k, v in by_line.items()}
    tiles = defaultdict(list)
    for r in rd(os.path.join(atlas, 'secure_tokens.tsv')):
        if r['page'] in NO87 or r['sid'].startswith(NO87) or r['sid'] not in signs:
            continue
        tiles[r['code']].append(r['sid'])
    pairs = [p.split('/') for p in a.pairs.split(',')]
    codes = sorted({c for p in pairs for c in p})
    leaves = sorted({signs[s]['page'] for c in codes for s in tiles[c]})
    pages = load_pages(folder, leaves)
    stats = {}
    for c in codes:
        for sid in tiles[c]:
            s = signs[sid]
            img = pages.get(s['page'])
            if img is None:
                continue
            x, y, w, h = (int(s[k]) for k in ('x', 'y', 'w', 'h'))
            ink = ink_mask(img[max(0, y):y + h, max(0, x):x + w])
            stats[sid] = tile_stats(ink, y + h, base[(s['page'], s['line'])], h)
    kept, rows = [], []
    for ca, cb in pairs:
        sa = [stats[s] for s in tiles[ca] if s in stats]
        sb = [stats[s] for s in tiles[cb] if s in stats]
        ok, best, d, ma, mb, ds, why = decide(ca, cb, sa, sb, a.min_tiles, a.min_d)
        sent = sentence(ca, cb, best, ma, mb) if ok else ''
        rows.append([f'{ca}/{cb}', len(sa), len(sb)] + [f'{ds.get(s, 0):.2f}' for s in STATS] +
                    [best, f'{d:.2f}', f'{ma:.3f}', f'{mb:.3f}', 'kept' if ok else 'dropped: ' + why, sent])
        print(f"{ca}/{cb}: n {len(sa)}/{len(sb)}  d' " + ' '.join(f'{s} {ds.get(s, 0):.2f}' for s in STATS) +
              f"  -> {'KEPT ' + best if ok else 'DROPPED (' + why + ')'}")
        if ok:
            kept.append((ca, cb, sent))
    out_dir = os.path.dirname(os.path.abspath(a.out))
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'hints_dprime.tsv'), 'w') as f:
        f.write('pair\tn_a\tn_b\t' + '\t'.join('d_' + s for s in STATS) + '\tbest\td\tmean_a\tmean_b\tstatus\tsentence\n')
        for r in rows:
            f.write('\t'.join(map(str, r)) + '\n')
    with open(a.out, 'w') as f:
        f.write(f'## {SECTION}\n\n')
        f.write('Some cells on the sheet look alike. For each pair below, the sentence names the one feature that '
                'tells them apart in this hand (measured on this writer\'s own signs on other pages). The picture '
                f'`{os.path.basename(a.sheet)}` shows three examples of each code, side by side. Use it only to decide '
                'between the two cells of a pair; read everything else exactly as the brief above says.\n\n')
        for _, _, s in kept:
            f.write(f'- {s}\n')
    if a.sheet and kept:
        make_sheet(kept, sheet, tiles, signs, pages, a.sheet, tile)
    print(f'kept {len(kept)} of {len(pairs)} pairs -> {a.out}')
    return 0


def make_sheet(kept, sheet, tiles, signs, pages, path, tile):
    from PIL import Image, ImageDraw, ImageFont
    H = 96
    try:
        font = ImageFont.truetype('DejaVuSans-Bold.ttf', 28)
    except Exception:
        font = ImageFont.load_default()

    def pick(code):
        ex = [s for s in (sheet.get(code, {}).get('exemplars') or '').split(',') if s in signs and not s.startswith(NO87)]
        rest = [s for s in tiles[code] if s not in ex]
        out = []
        for s in ex + rest:
            if signs[s]['page'] in pages:
                out.append(s)
            if len(out) == 3:
                break
        return out

    def ims(code):
        res = []
        for sid in pick(code):
            s = signs[sid]
            t = tile(pages[s['page']], int(s['x']), int(s['y']), int(s['w']), int(s['h']), 1.0)
            f = H / t.height
            res.append(t.resize((max(1, int(t.width * f)), H)))
        return res

    rows = []
    for ca, cb, _ in kept:
        A, B = ims(ca), ims(cb)
        w = 90 + sum(i.width + 10 for i in A) + 60 + 90 + sum(i.width + 10 for i in B)
        r = Image.new('RGB', (w, H + 20), 'white')
        d = ImageDraw.Draw(r)
        x = 10
        for code, group in ((ca, A), (cb, B)):
            d.text((x, H // 2 - 10), code, fill='black', font=font)
            x += 90
            for i in group:
                r.paste(i.convert('RGB'), (x, 10)); x += i.width + 10
            x += 60
        rows.append(r)
    W = max(r.width for r in rows)
    out = Image.new('RGB', (W, sum(r.height + 6 for r in rows)), 'white')
    y = 0
    for r in rows:
        out.paste(r, (0, y)); y += r.height
        ImageDraw.Draw(out).line([(0, y + 2), (W, y + 2)], fill=(160, 160, 160), width=2); y += 6
    out.save(path)


# ---------- assemble / norm ----------
def cmd_assemble(a):
    base = open(a.base).read().rstrip() + '\n\n'
    hints = open(a.hints).read().rstrip() + '\n\n'
    task = ['## Your task', '', f'The sheet: {os.path.abspath(a.signsheet)}', '',
            f'The pair examples: {os.path.abspath(a.sheet)}', '',
            f'The crops ({len(a.crops)} images, 2x, s1 s2 s3 of each line in order; the passage id is the L number in the '
            'file name):'] + [os.path.abspath(c) for c in a.crops] + ['', f'Write your TSV to: {os.path.abspath(a.raw)}']
    with open(a.out, 'w') as f:
        f.write(base + hints + '\n'.join(task) + '\n')
    print(a.out)
    return 0


def cmd_norm(a):
    rows = rd(a.raw)
    with open(a.out, 'w') as f:
        f.write('line\tpos\tsign\n')
        for r in rows:
            f.write(f"{a.leaf}_{r['passage']}\t{r['pos']}\t{r['sign_id']}\n")
    print(f'{len(rows)} rows -> {a.out}')
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest='cmd', required=True)
    d = sp.add_parser('derive')
    d.add_argument('--pairs', default=PAIRS)
    d.add_argument('--exemplars', required=True, help='atlas/sheet_truth/sheet.tsv')
    d.add_argument('--atlas', required=True, help='atlas folder (signs.tsv, secure_tokens.tsv)')
    d.add_argument('--out', required=True)
    d.add_argument('--sheet', default='')
    d.add_argument('--min-tiles', type=int, default=3)
    d.add_argument('--min-d', type=float, default=1.0)
    s = sp.add_parser('assemble')
    s.add_argument('--base', required=True); s.add_argument('--hints', required=True)
    s.add_argument('--signsheet', required=True); s.add_argument('--sheet', required=True)
    s.add_argument('--crops', nargs='+', required=True); s.add_argument('--raw', required=True)
    s.add_argument('--out', required=True)
    n = sp.add_parser('norm')
    n.add_argument('--raw', required=True); n.add_argument('--leaf', required=True); n.add_argument('--out', required=True)
    a = p.parse_args(argv)
    return {'derive': cmd_derive, 'assemble': cmd_assemble, 'norm': cmd_norm}[a.cmd](a)


if __name__ == '__main__':
    sys.exit(main())
