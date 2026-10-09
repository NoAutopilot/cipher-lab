#!/usr/bin/env python3
"""Thin-stroke targeted pair re-read (TXE-C, LANE TX-ENGINEER round 2, 9 Oct 2026; benchmark-tx/PREREG-txeng-2.md "Instrument C").

Lesson it answers (research/TX-TAXONOMY-2026-10-09.md class 3): on Birago no.87 the thin third of the hand's strokes
carries half of every reader's errors; the tick or tail that separates a look-alike pair fades first. A whole re-pass
repeats the first reader's errors (TX-VIEWS, phi 0.71-0.76), so this tool asks a second look ONLY at thin signs whose
line-read sign (L) is in a named look-alike pair, shown beside two exemplar rows, as "A, B or neither".

Subcommands (all disk-only, no network, no model):
  select  --unit U   map the unit's atlas boxes to L's line positions label-blind (a per-line DP over box widths, the
                     costs of atlas/no87_map.py; neither side's labels steer it) -> box_pos.tsv; stroke measure per box =
                     tools/tx_taxonomy.erosion_share on the page image; thin = the page's lowest tercile over ALL its
                     boxes; selected = thin AND L sign in a listed pair -> selected.tsv; prints counts.
  build   --unit U   one row per selected box: the sign at 4x, autocontrast, +-1 neighbour (box grown 50%), boxed |
                     exemplar row A | exemplar row B (3 tiles each; A/B order seeded random per row); sheets of at most
                     --rows rows -> sheet_NN.png + sheet_NN.tsv (the row -> A/B code key, never given to the reader).
  resolve --unit U   reads_NN.tsv (row, pick A/B/neither/?, conf, feature) + keys -> passJ_pair_<unit>.tsv
                     (line, pos, sign): A/B -> that code, neither/? -> L's sign; every unit position written.

Partner rule (fixed, stated once): a listed pair is usable only when both codes have exemplar tiles; an L sign in several
usable pairs gets the partner with the highest pair count in harvest/confusion_1572.tsv (ties: pair-list order).
Exemplar tiles: the secure tiles of atlas/sheet_truth/sheet.tsv (non-no.87 leaves) only. --cluster-fallback adds, for a
code without secure tiles, the non-no.87 boxes whose atlas cluster is named that code (labels.json "signs" only -- never
its "override"), nearest the cluster centre first; it is off by default because on the dev build (9 Oct 2026, before any
read) it produced dot marks for T24 and a mixed cluster (1/3 votes) for T64.
Never opens a truth file (benchmark-tx/*.truth.tsv, atlas/no87_box_token.tsv, labels.json override, harvest/align87).
"""
import argparse, csv, json, os, random, re, sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
PAIRS = ['T18/T98', 'T90/T53', 'T76/T66', 'T76/T86', 'T76/T45', 'T64/T95', 'T64/T51', 'T50/T36', 'T92/T95', 'T92/T98',
         'T83/T24', 'T60/T86', 'T13/T64']
NO87 = ('f178r', 'f178v', 'f179r')
D_FOLDER = os.path.join(ROOT, 'ciphers', 'nevers-birago-fr3251-1572')
D_L = os.path.join(ROOT, 'benchmark-tx', 'outputs', 'birago1572-no87', 'labels.tsv')
D_UNITS = os.path.join(ROOT, 'benchmark-tx', 'txeng', 'units')
D_OUT = os.path.join(ROOT, 'benchmark-tx', 'txeng', 'pair')


def rd(p):
    with open(p) as f:
        return list(csv.DictReader(f, delimiter='\t'))


def wr(p, cols, rows):
    os.makedirs(os.path.dirname(os.path.abspath(p)), exist_ok=True)
    with open(p, 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(str(r.get(c, '')) for c in cols) + '\n')


def dp(bw, n, W):
    """Label-blind box<->token alignment over widths (costs as atlas/no87_map.py). Returns [(box_i, tok_j, op)]."""
    import math
    m = len(bw); INF = 1e9
    C = [[INF] * (n + 1) for _ in range(m + 1)]; B = [[None] * (n + 1) for _ in range(m + 1)]; C[0][0] = 0
    for i in range(m + 1):
        for j in range(n + 1):
            c = C[i][j]
            if c >= INF:
                continue
            opts = []
            if i < m and j < n: opts.append((i + 1, j + 1, abs(math.log(bw[i] / W)), '1:1'))
            if i + 1 < m and j < n: opts.append((i + 2, j + 1, 1.0 + abs(math.log((bw[i] + bw[i + 1]) / W)), '2:1'))
            if i < m and j + 1 < n: opts.append((i + 1, j + 2, 1.0 + abs(math.log(bw[i] / (2 * W))), '1:2'))
            if i < m: opts.append((i + 1, j, 1.2 if bw[i] < 0.5 * W else 2.5, 'skipbox'))
            if j < n: opts.append((i, j + 1, 2.5, 'skiptok'))
            for a, b, k, op in opts:
                if c + k < C[a][b]:
                    C[a][b] = c + k; B[a][b] = (i, j, op)
    path, i, j = [], m, n
    while (i, j) != (0, 0):
        pi, pj, op = B[i][j]; path.append((pi, pj, op)); i, j = pi, pj
    return path[::-1]


def load_pages(folder, leaves):
    """Page images: harvest/<leaf>/src_*.jpg (the frame signs.tsv boxes are in), else atlas/pages/<leaf>.jpg."""
    import numpy as np
    from PIL import Image
    out = {}
    for leaf in leaves:
        d = os.path.join(folder, 'harvest', leaf)
        src = sorted(f for f in os.listdir(d) if f.startswith('src_') and f.endswith('.jpg')) if os.path.isdir(d) else []
        p = os.path.join(d, src[0]) if src else os.path.join(folder, 'atlas', 'pages', f'{leaf}.jpg')
        if not os.path.exists(p):
            for name, path in page_args(folder):
                if name == leaf:
                    p = os.path.join(ROOT, path)
        if os.path.exists(p):
            out[leaf] = np.asarray(Image.open(p).convert('L'))
    return out


def page_args(folder):
    """(name, path) from atlas/pages.py (used only for pages not under harvest/<leaf>/)."""
    pp = os.path.join(folder, 'atlas', 'pages.py')
    if not os.path.exists(pp):
        return []
    import subprocess
    o = subprocess.run([sys.executable, pp], capture_output=True, text=True, cwd=ROOT).stdout
    return re.findall(r'--page (\S+?)=(\S+)', o)


def unit_lines(units_dir, unit):
    return sorted({r['line'] for r in rd(os.path.join(units_dir, f'labels_{unit}.tsv'))})


def pair_partners(exemplar_codes, confusion):
    """L code -> chosen partner under the stated rule, plus the per-code list of unusable pairs."""
    cnt = {}
    if confusion and os.path.exists(confusion):
        for r in rd(confusion):
            cnt[frozenset((r['label_a'], r['label_b']))] = int(r['n'])
    part, unusable = {}, []
    for code in sorted({c for p in PAIRS for c in p.split('/')}):
        best = None
        for k, p in enumerate(PAIRS):
            a, b = p.split('/')
            if code not in (a, b):
                continue
            other = b if code == a else a
            if code not in exemplar_codes or other not in exemplar_codes:
                unusable.append(p); continue
            score = (cnt.get(frozenset((a, b)), 0), -k)
            if best is None or score > best[0]:
                best = (score, other)
        if best:
            part[code] = best[1]
    return part, sorted(set(unusable), key=PAIRS.index)


def exemplars(folder, n=3, fallback=False):
    """code -> [sid...] from sheet_truth secure tiles, else nearest-centre non-no.87 boxes of clusters named that code."""
    at = os.path.join(folder, 'atlas')
    ex = {}
    st = os.path.join(at, 'sheet_truth', 'sheet.tsv')
    if os.path.exists(st):
        for r in rd(st):
            sids = [s for s in r.get('exemplars', '').split(',') if s and not s.startswith(NO87)]
            if sids:
                ex[r['code']] = sids[:n]
    if not fallback:
        return ex
    lab = json.load(open(os.path.join(at, 'labels.json'))).get('signs', {})
    byc = defaultdict(list)
    for r in rd(os.path.join(at, 'clusters.tsv')):
        if r['kind'] != 'sign' or r['id'].startswith(NO87):
            continue
        c = lab.get(r['cluster'], '_')
        if c != '_':
            byc[c].append((float(r['dist']), r['id']))
    for c, v in byc.items():
        if c not in ex:
            ex[c] = [s for _, s in sorted(v)[:n]]
    return ex


def cmd_select(a):
    from tx_taxonomy import erosion_share
    signs = rd(os.path.join(a.folder, 'atlas', 'signs.tsv'))
    L = defaultdict(list)
    for r in rd(a.line_read):
        L[r['line']].append(r)
    lines = unit_lines(a.units, a.unit)
    leaves = sorted({ln.split('_')[0] for ln in lines})
    pages = load_pages(a.folder, leaves)
    ex = exemplars(a.folder, fallback=a.cluster_fallback)
    part, unusable = pair_partners(set(ex), a.confusion)
    rows = []
    for leaf in leaves:
        pb = [s for s in signs if s['page'] == leaf]
        es = {s['sid']: erosion_share(pages[leaf], int(s['x']), int(s['y']), int(s['w']), int(s['h'])) for s in pb}
        vals = sorted(v for v in es.values() if v is not None)
        cut = vals[len(vals) // 3] if vals else 0.0          # lowest tercile: es < cut
        W = sorted(int(s['w']) for s in pb)[len(pb) // 2]
        for ln in [x for x in lines if x.startswith(leaf + '_')]:
            li = int(ln.split('_L')[1])
            bx = sorted([s for s in pb if int(s['line']) == li], key=lambda s: int(s['x']))
            tk = sorted(L.get(ln, []), key=lambda r: int(r['pos']))
            if not bx or not tk:
                continue
            for i, j, op in dp([int(s['w']) for s in bx], len(tk), W):
                if op != '1:1':
                    continue
                s, t = bx[i], tk[j]
                e = es[s['sid']]
                thin = e is not None and e < cut
                sel = thin and t['sign'] in part
                rows.append(dict(sid=s['sid'], line=ln, pos=t['pos'], L=t['sign'], es='' if e is None else f'{e:.3f}',
                                 cut=f'{cut:.3f}', thin=int(thin), selected=int(sel),
                                 partner=part.get(t['sign'], '') if sel else ''))
    out = os.path.join(a.out, a.unit)
    wr(os.path.join(out, 'box_pos.tsv'), ['sid', 'line', 'pos', 'L', 'es', 'cut', 'thin', 'selected', 'partner'], rows)
    sel = [r for r in rows if r['selected']]
    wr(os.path.join(out, 'selected.tsv'), ['sid', 'line', 'pos', 'L', 'partner', 'es'], sel)
    per = Counter('/'.join(sorted((r['L'], r['partner']))) for r in sel)
    nL = sum(len(L.get(ln, [])) for ln in lines)
    print(f'unit {a.unit}: L positions {nL}; boxes mapped 1:1 {len(rows)}; thin {sum(r["thin"] for r in rows)}; '
          f'selected {len(sel)}')
    print('partners used: ' + ', '.join(f'{k}->{v}' for k, v in sorted(part.items())))
    print('unusable pairs (a code without exemplar tiles): ' + (', '.join(unusable) or 'none'))
    print('per pair: ' + (', '.join(f'{k} {v}' for k, v in sorted(per.items())) or 'none'))
    return 0


def tile(img, x, y, w, h, f, grow=0.25):
    """The box grown by `grow`, autocontrast, scaled by `f` (one factor for every tile, so sizes stay comparable)."""
    from PIL import Image, ImageOps
    H, Wd = img.shape
    gx, gy = int(w * grow), int(h * grow)
    x0, y0, x1, y1 = max(0, x - gx), max(0, y - gy), min(Wd, x + w + gx), min(H, y + h + gy)
    t = ImageOps.autocontrast(Image.fromarray(img[y0:y1, x0:x1]), cutoff=1)
    return t.resize((max(1, int(t.width * f)), max(1, int(t.height * f))), Image.LANCZOS)


def context_tile(img, s, same, f):
    """The sign with one neighbour each side (x range of the three boxes, the sign's own box grown 50%), boxed in blue."""
    from PIL import Image, ImageDraw, ImageOps
    x, y, w, h = (int(s[k]) for k in ('x', 'y', 'w', 'h'))
    k = [b['sid'] for b in same].index(s['sid'])
    nb = same[max(0, k - 1):k + 2]
    gx, gy = int(w * 0.5), int(h * 0.5)
    X0 = max(0, min(int(b['x']) for b in nb) - gx // 2)
    X1 = min(img.shape[1], max(int(b['x']) + int(b['w']) for b in nb) + gx // 2)
    X0, X1 = min(X0, x - gx), max(X1, x + w + gx)
    X0, X1 = max(0, X0), min(img.shape[1], X1)
    Y0, Y1 = max(0, y - gy), min(img.shape[0], y + h + gy)
    ctx = ImageOps.autocontrast(Image.fromarray(img[Y0:Y1, X0:X1]), cutoff=1).convert('RGB')
    ctx = ctx.resize((max(1, int(ctx.width * f)), max(1, int(ctx.height * f))), Image.LANCZOS)
    d = ImageDraw.Draw(ctx)
    d.rectangle([(x - X0) * f - 5, (y - Y0) * f - 5, (x - X0 + w) * f + 5, (y - Y0 + h) * f + 5],
                outline=(0, 60, 200), width=4)
    return ctx


def cmd_build(a):
    from PIL import Image, ImageDraw, ImageFont
    out = os.path.join(a.out, a.unit)
    sel = rd(os.path.join(out, 'selected.tsv'))
    signs = {s['sid']: s for s in rd(os.path.join(a.folder, 'atlas', 'signs.tsv'))}
    ex = exemplars(a.folder, fallback=a.cluster_fallback)
    leaves = sorted({signs[r['sid']]['page'] for r in sel} | {signs[s]['page'] for c in ex for s in ex[c] if s in signs})
    pages = load_pages(a.folder, leaves)
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 30)
    except OSError:
        font = ImageFont.load_default()
    for f in os.listdir(out):
        if re.match(r'sheet_\d+\.(png|tsv)$', f):
            os.remove(os.path.join(out, f))
    rows = []
    for r in sel:
        s = signs[r['sid']]; leaf = s['page']
        same = sorted([b for b in signs.values() if b['page'] == leaf and b['line'] == s['line']], key=lambda b: int(b['x']))
        ctx = context_tile(pages[leaf], s, same, a.zoom)
        rng = random.Random(f'{a.seed}:{r["line"]}:{r["pos"]}')
        codes = [r['L'], r['partner']]
        if rng.random() < 0.5:
            codes = codes[::-1]
        exrows = []
        for c in codes:
            exrows.append([tile(pages[signs[sid]['page']], *(int(signs[sid][k]) for k in ('x', 'y', 'w', 'h')),
                                a.zoom).convert('RGB') for sid in ex.get(c, [])[:3]])
        rows.append(dict(r=r, ctx=ctx, A=exrows[0], B=exrows[1], A_code=codes[0], B_code=codes[1]))
    n_sheets = 0
    per = max(1, -(-len(rows) // max(1, -(-len(rows) // a.rows)))) if rows else a.rows   # balanced sheets
    for si in range(0, len(rows), per):
        chunk = rows[si:si + per]; n_sheets += 1; nn = f'{n_sheets:02d}'
        cw = max(c['ctx'].width for c in chunk)
        gw = max(sum(t.width + 12 for t in c[g]) for c in chunk for g in ('A', 'B'))
        rh = [max([c['ctx'].height] + [t.height for t in c['A'] + c['B']]) + 24 for c in chunk]
        xA = 70 + cw + 30; xB = xA + 50 + gw + 30
        W = xB + 50 + gw + 10
        sheet = Image.new('RGB', (W, 60 + sum(rh)), 'white')
        d = ImageDraw.Draw(sheet)
        d.text((15, 12), 'Pick the exemplar row (A or B) that matches the boxed sign, or neither.', fill='black', font=font)
        yy = 60; key = []
        for i, c in enumerate(chunk, 1):
            d.line([(0, yy), (W, yy)], fill=(120, 120, 120), width=2)
            d.text((12, yy + rh[i - 1] // 2 - 18), str(i), fill='black', font=font)
            sheet.paste(c['ctx'], (70, yy + 12))
            for lab, ts, x0 in (('A', c['A'], xA), ('B', c['B'], xB)):
                d.line([(x0 - 15, yy), (x0 - 15, yy + rh[i - 1])], fill=(120, 120, 120), width=2)
                d.text((x0, yy + rh[i - 1] // 2 - 18), lab, fill='black', font=font)
                xx = x0 + 45
                for t in ts:
                    sheet.paste(t, (xx, yy + 12)); xx += t.width + 12
            key.append(dict(row=i, line=c['r']['line'], pos=c['r']['pos'], sid=c['r']['sid'], L=c['r']['L'],
                            A=c['A_code'], B=c['B_code']))
            yy += rh[i - 1]
        sheet.save(os.path.join(out, f'sheet_{nn}.png'))
        wr(os.path.join(out, f'sheet_{nn}.tsv'), ['row', 'line', 'pos', 'sid', 'L', 'A', 'B'], key)
        print(f'sheet_{nn}.png: {len(chunk)} rows, {sheet.width}x{sheet.height}')
    print(f'{len(rows)} rows on {n_sheets} sheet(s)')
    return 0


def cmd_resolve(a):
    out = os.path.join(a.out, a.unit)
    lines = set(unit_lines(a.units, a.unit))
    L = [r for r in rd(a.line_read) if r['line'] in lines]
    change = {}; tally = Counter(); per = defaultdict(Counter)
    for kp in sorted(f for f in os.listdir(out) if re.match(r'sheet_\d+\.tsv$', f)):
        nn = kp[6:8]
        rp = os.path.join(out, f'reads_{nn}.tsv')
        if not os.path.exists(rp):
            print(f'missing {rp}', file=sys.stderr); return 2
        picks = {}
        for r in rd(rp):
            picks[str(r['row']).strip()] = (r.get('pick') or '?').strip()
        for k in rd(os.path.join(out, kp)):
            p = picks.get(k['row'], '?')
            p = p.upper() if p.upper() in ('A', 'B') else ('neither' if p.lower() == 'neither' else '?')
            new = k[p] if p in ('A', 'B') else k['L']
            pair = '/'.join(sorted((k['A'], k['B'])))
            lab = 'keepL' if new == k['L'] and p in ('A', 'B') else ('partner' if p in ('A', 'B') else p)
            per[pair][lab] += 1; tally[lab] += 1
            change[(k['line'], k['pos'])] = new
    rows = [dict(line=r['line'], pos=r['pos'], sign=change.get((r['line'], r['pos']), r['sign'])) for r in L]
    dst = a.dest or os.path.join(ROOT, 'benchmark-tx', 'outputs', 'birago1572-no87', f'passJ_pair_{a.unit}.tsv')
    wr(dst, ['line', 'pos', 'sign'], rows)
    print(f'{dst}: {len(rows)} positions; picks: ' + ', '.join(f'{k} {v}' for k, v in sorted(tally.items())))
    for pair, c in sorted(per.items()):
        print(f'  {pair}: L kept by pick {c["keepL"]}, partner picked (changed L) {c["partner"]}, '
              f'neither {c["neither"]}, ? {c["?"]}')
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    for name in ('select', 'build', 'resolve'):
        p = sub.add_parser(name)
        p.add_argument('--unit', required=True, help='dev_tune | eval_heldout | geo (labels_<unit>.tsv in --units)')
        p.add_argument('--folder', default=D_FOLDER, help='target folder (atlas/, harvest/)')
        p.add_argument('--line-read', default=D_L, help='the line read L (line, pos, sign)')
        p.add_argument('--units', default=D_UNITS)
        p.add_argument('--out', default=D_OUT, help='writes <out>/<unit>/')
        p.add_argument('--cluster-fallback', action='store_true',
                       help='also take exemplars from clusters named a code (off: on the dev build, 9 Oct 2026, before any '
                            'read, it gave dot marks for T24 and a mixed 1/3-vote cluster for T64)')
        p.add_argument('--confusion', default=os.path.join(D_FOLDER, 'harvest', 'confusion_1572.tsv'))
        if name == 'build':
            p.add_argument('--rows', type=int, default=16, help='rows per sheet (max 16)')
            p.add_argument('--zoom', type=float, default=1.6,
                           help='one scale for every tile (no.87 boxes run 40-110 native px, so 1.6 renders a tall sign '
                                'at about the 160 px the brief\'s "4x of a 40 px sign" means, and keeps a 12-row sheet '
                                'under about 1500 x 2500 px for one vision read)')
            p.add_argument('--seed', default='txe-c')
        if name == 'resolve':
            p.add_argument('--dest', help='output tsv (default benchmark-tx/outputs/birago1572-no87/passJ_pair_<unit>.tsv)')
    a = ap.parse_args(argv)
    if a.cmd == 'build' and a.rows > 16:
        ap.error('--rows at most 16')
    return {'select': cmd_select, 'build': cmd_build, 'resolve': cmd_resolve}[a.cmd](a)


if __name__ == '__main__':
    sys.exit(main())
