#!/usr/bin/env python3
"""Compare, don't recall: a reader picks a sign among SHOWN atlas candidates instead of naming it from memory
(TXE-A, LANE TX-ENGINEER round 2, 9 Oct 2026; benchmark-tx/PREREG-txeng-2.md "Instrument A").

Lesson it answers (research/TX-TAXONOMY-2026-10-09.md class 1): on Birago no.87 half the line-read error is the reader
naming a sign from memory against a printed sheet cell when the hand's form sits between two cells (d T18 / s T98,
p T90 / t T53, n T76 / e, h T64 / l), and the same wrong sign recurs in every pass. Here the reader never recalls: each
doubtful position is shown as the sign in context beside exemplar tiles of a few numbered candidates (the line read's
own sign plus the atlas's held-out top-3), code names hidden, order shuffled per row, and the question is only "which
numbered candidate matches, or none".

Subcommands
  map      Label-blind box <-> line-position map (the atlas/no87_map.py method: a per-line DP over box widths only,
           1:1 / 2:1 / 1:2 / skip box / skip token; no sign label on either side steers it). Writes box_pos.tsv
           (sid, line, pos, op). `build` runs it itself when --box-pos is absent.
  build    --unit U: per unit position, candidates = {line-read sign} + atlas top-3 codes ('_' dropped, deduplicated).
           A position is SHOWN when atlas top-1 != the line-read sign, or the top-1 share < --share (0.6), or the merged
           line-read confidence is M/L; an unmapped position (no single box) is shown only if its confidence is M/L and
           it has a box. A shown position with fewer than 2 candidates is not decidable and is counted, not shown.
           Row = the sign in context (target box drawn, one neighbour each side, region grown 50%) | 2 exemplar tiles
           per candidate, numbered 1..k in a seeded random order. Sheets of at most --rows (16) rows:
           OUT/<unit>/sheet_NN.png (given to the reader) + sheet_NN.tsv (row, line, pos, cands in shown order; the key,
           NEVER given to the reader).
  resolve  --unit U: reads OUT/<unit>/reads_NN.tsv (row, pick, conf, note; pick a number, or none/?), writes
           --pass-out (line, pos, sign: the pick's code, else the line read's sign) for every unit position, and
           OUT/<unit>/topk_weighted.tsv (line, pos, cand, score: the pick H 1.0 / M 0.6 / L 0.3, the other candidates
           sharing the rest; 'none' gives the line-read sign 0.6; an unshown position is its line-read sign at 1.0) for
           tools/key_decode_lattice.py decode.
  lattice-out  P.decode.tsv from key_decode_lattice.py -> line, pos, sign (its `chosen` column) for tools/tx_bench.py.

Inputs (defaults are the Birago no.87 files; every one is a flag): the atlas folder (signs.tsv, clusters.tsv,
labels.json -- its "signs" cluster->code map only, never its "override" per-tile known answers --, pages.json or
crops/<page>.png), a held-out classify TSV (glyph_atlas.py classify --topk 3 with every target page held out), the line
read (line, pos, sign), merged-confidence agreement TSVs (passage, merged, merged_conf; aligned to the line read by
difflib per line), exemplar lists (atlas/sheet_truth/sheet.tsv: code, exemplars), the unit list (units README).
Pages named by --exclude-page never give an exemplar (the target letter itself).

Usage (repo root):
  python3 tools/tx_compare.py build --unit dev_tune
  python3 tools/tx_compare.py resolve --unit dev_tune
Offline test: tools/tests/test_tx_compare.py (synthetic page, no network, no model).
"""
import argparse, csv, difflib, json, math, os, random, re, sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = 'ciphers/nevers-birago-fr3251-1572'
D = dict(atlas=f'{T}/atlas', topk='benchmark-tx/txeng/compare/topk_no87_allheld.tsv',
         line_read='benchmark-tx/outputs/birago1572-no87/labels.tsv',
         conf=[f'{T}/harvest/f178v/passC_agreement.tsv:f178v', f'{T}/harvest/f178v/passC_L11-23_agreement.tsv:f178v',
               f'{T}/harvest/f179r/passC_agreement.tsv:f179r'],
         exemplars=f'{T}/atlas/sheet_truth/sheet.tsv', units='benchmark-tx/txeng/units/README.md',
         out='benchmark-tx/txeng/compare', exclude=['f178r', 'f178v', 'f179r'])
CONF_W = {'H': 1.0, 'M': 0.6, 'L': 0.3}
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'


def rd(p):
    with open(p, encoding='utf-8') as f:
        return list(csv.DictReader((ln for ln in f if not ln.startswith('#')), delimiter='\t'))


def wr(p, cols, rows):
    os.makedirs(os.path.dirname(os.path.abspath(p)), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(str(r.get(c, '')) for c in cols) + '\n')


def path(p):
    return p if os.path.isabs(p) or os.path.exists(p) else os.path.join(ROOT, p)


def unit_lines(readme, unit):
    for ln in open(path(readme), encoding='utf-8'):
        m = re.match(r'\s*-\s*(\S+):\s*(.+)$', ln)
        if m and m.group(1) == unit:
            return m.group(2).split()
    sys.exit(f'unit {unit} not in {readme}')


def split_line(line):                                  # f178v_L03 -> ('f178v', 3)
    m = re.match(r'(.+)_L(\d+)$', line)
    return m.group(1), int(m.group(2))


# ---------------------------------------------------------------- label-blind map (atlas/no87_map.py's DP)
def dp(bw, n, W):
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
    out, i, j = [], m, n
    while (i, j) != (0, 0):
        pi, pj, op = B[i][j]; out.append((pi, pj, op)); i, j = pi, pj
    return out[::-1]


def box_map(signs, L, lines):
    """-> rows sid, line, pos, op for every position of `lines` (sid '' when no box; 'a+b' for 2:1)."""
    out = []
    for line in lines:
        page, li = split_line(line)
        pg = [s for s in signs if s['page'] == page]
        if not pg:
            continue
        W = sorted(int(s['w']) for s in pg)[len(pg) // 2]
        bx = sorted([s for s in pg if int(s['line']) == li], key=lambda s: int(s['x']))
        tk = [r for r in L if r['line'] == line]
        if not bx:
            out += [dict(sid='', line=line, pos=t['pos'], op='skiptok') for t in tk]
            continue
        for i, j, op in dp([int(s['w']) for s in bx], len(tk), W):
            if op == '1:1':
                out.append(dict(sid=bx[i]['sid'], line=line, pos=tk[j]['pos'], op=op))
            elif op == '2:1':
                out.append(dict(sid=bx[i]['sid'] + '+' + bx[i + 1]['sid'], line=line, pos=tk[j]['pos'], op=op))
            elif op == '1:2':
                for jj in (j, j + 1):
                    out.append(dict(sid=bx[i]['sid'], line=line, pos=tk[jj]['pos'], op=op))
            elif op == 'skiptok':
                out.append(dict(sid='', line=line, pos=tk[j]['pos'], op=op))
    return out


# ---------------------------------------------------------------- confidence
def merged_conf(conf_specs, L):
    """{(line, pos): conf} from passage-format agreement files (FILE:page), aligned to the line read per line."""
    out = {}
    for spec in conf_specs:
        p, page = spec.rsplit(':', 1)
        by = defaultdict(list)
        for r in rd(path(p)):
            if r.get('merged', '') not in ('', '-'):
                by[f"{page}_{r['passage']}"].append(r)
        for line, rows in by.items():
            lab = [r for r in L if r['line'] == line]
            a, b = [r['merged'] for r in rows], [r['sign'] for r in lab]
            for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
                if op in ('equal', 'replace') and i2 - i1 == j2 - j1:
                    for k in range(i2 - i1):
                        out[(line, lab[j1 + k]['pos'])] = rows[i1 + k].get('merged_conf', '')
    return out


# ---------------------------------------------------------------- images
_FONTS = {}


def font(sz):
    from PIL import ImageFont
    if sz not in _FONTS:
        try:
            _FONTS[sz] = ImageFont.truetype(FONT, sz)
        except OSError:
            _FONTS[sz] = ImageFont.load_default()
    return _FONTS[sz]


class Pages:
    def __init__(self, atlas):
        self.atlas, self.cache = path(atlas), {}
        pj = os.path.join(self.atlas, 'pages.json')
        self.info = json.load(open(pj)) if os.path.exists(pj) else {}

    def get(self, page):
        from PIL import Image
        if page not in self.cache:
            im = None
            for cand in (os.path.join(self.atlas, 'crops', page + '.png'), path(self.info.get(page, {}).get('image') or '/nonexistent'),
                         os.path.join(self.atlas, 'pages', page + '.jpg')):
                if os.path.exists(cand):
                    im = Image.open(cand).convert('L')
                    box = self.info.get(page, {}).get('box')
                    if box and 'crops' not in cand:
                        im = im.crop(tuple(box))
                    break
            self.cache[page] = im
        return self.cache[page]


def xywh(r):
    return tuple(int(r[k]) for k in 'xywh')


def union(rs):
    x0 = min(r[0] for r in rs); y0 = min(r[1] for r in rs)
    x1 = max(r[0] + r[2] for r in rs); y1 = max(r[1] + r[3] for r in rs)
    return x0, y0, x1 - x0, y1 - y0


def exemplar_tile(pages, s, cell):
    """One sign at `cell` px, marks above kept (glyph_atlas._tile's margins)."""
    from PIL import Image
    t = Image.new('L', (cell, cell), 255)
    g = pages.get(s['page'])
    if g is None:
        return t
    x, y, w, h = xywh(s)
    m = int(0.2 * max(w, h)); top = int(0.6 * max(w, h))
    sub = g.crop((max(0, x - m), max(0, y - top), min(g.width, x + w + m), min(g.height, y + h + m)))
    sc = min((cell - 6) / sub.width, (cell - 6) / sub.height, 3.0)
    sub = sub.resize((max(1, int(sub.width * sc)), max(1, int(sub.height * sc))), Image.BICUBIC)
    t.paste(sub, ((cell - sub.width) // 2, (cell - sub.height) // 2))
    return t


def context_tile(pages, page_rows, sids, target_h, max_scale, max_w):
    """The target box(es) with one neighbour each side, region grown 50% of the target size, target framed."""
    from PIL import Image, ImageDraw
    tg = [page_rows[s] for s in sids]
    page = tg[0]['page']
    g = pages.get(page)
    tb = union([xywh(r) for r in tg])
    line = sorted((r for r in page_rows.values() if r['page'] == page and r['line'] == tg[0]['line']),
                  key=lambda r: int(r['x']))
    ids = [r['sid'] for r in line]
    i0, i1 = ids.index(sids[0]), ids.index(sids[-1])
    nb = [xywh(line[i]) for i in (i0 - 1, i1 + 1) if 0 <= i < len(line)]
    x, y, w, h = union([tb] + nb)
    gx, gy = int(0.5 * tb[2]), int(0.5 * tb[3])
    top = int(0.6 * tb[3])
    X0, Y0 = max(0, x - gx), max(0, tb[1] - top)              # vertical: the target's own band, marks above kept
    X1, Y1 = min(g.width, x + w + gx), min(g.height, tb[1] + tb[3] + int(0.35 * tb[3]))
    sub = g.crop((X0, Y0, X1, Y1))
    sc = min(max_scale, target_h / max(1, tb[3]), max_w / max(1, sub.width))
    sub = sub.resize((max(1, int(sub.width * sc)), max(1, int(sub.height * sc))), Image.BICUBIC).convert('RGB')
    d = ImageDraw.Draw(sub)
    bx0, by0 = (tb[0] - X0) * sc - 4, (tb[1] - Y0) * sc - 4
    d.rectangle((bx0, by0, bx0 + tb[2] * sc + 8, by0 + tb[3] * sc + 8), outline=(0, 0, 0), width=3)
    return sub


# ---------------------------------------------------------------- build
def exemplars_for(code, ex_lists, signs_by_sid, by_code, exclude, n=2):
    got = [s for s in ex_lists.get(code, []) if s in signs_by_sid and signs_by_sid[s]['page'] not in exclude]
    for s in by_code.get(code, []):
        if len(got) >= n:
            break
        if s not in got:
            got.append(s)
    return got[:n]


def load(a):
    signs = rd(os.path.join(path(a.atlas), 'signs.tsv'))
    L = rd(path(a.line_read))
    return signs, L


def cmd_map(a, signs=None, L=None, lines=None):
    if signs is None:
        signs, L = load(a)
    if lines is None:
        lines = sorted({r['line'] for r in L})
    rows = box_map(signs, L, lines)
    wr(a.box_pos_out, ['sid', 'line', 'pos', 'op'], rows)
    print(f'map: {len(rows)} positions, ops {dict(Counter(r["op"] for r in rows))} -> {a.box_pos_out}')
    return rows


def cmd_build(a):
    from PIL import Image, ImageDraw
    signs, L = load(a)
    lines = unit_lines(a.units, a.unit)
    sb = {s['sid']: s for s in signs}
    if a.box_pos and os.path.exists(path(a.box_pos)):
        bp = rd(path(a.box_pos))
    else:
        a.box_pos_out = a.box_pos or os.path.join(a.out, 'box_pos.tsv')
        bp = cmd_map(a, signs, L, sorted({r['line'] for r in L}))
    pos2box = {(r['line'], r['pos']): r for r in bp}
    tk = {r['box']: r for r in rd(path(a.topk))}
    conf = merged_conf(a.conf, L)
    lab = json.load(open(os.path.join(path(a.atlas), 'labels.json')))['signs']          # never 'override'
    cl = {r['id']: r for r in rd(os.path.join(path(a.atlas), 'clusters.tsv')) if r['kind'] == 'sign'}
    excl = set(a.exclude_page)
    by_code = defaultdict(list)
    for sid, r in sorted(cl.items(), key=lambda kv: float(kv[1].get('dist') or 0)):
        if sid in sb and sb[sid]['page'] not in excl:
            by_code[lab.get(r['cluster'], '_')].append(sid)
    ex_lists = {}
    if a.exemplars and os.path.exists(path(a.exemplars)):
        ex_lists = {r['code']: [s for s in (r.get('exemplars') or '').split(',') if s] for r in rd(path(a.exemplars))}
    pages = Pages(a.atlas)
    shown, stats = [], Counter()
    for r in L:
        if r['line'] not in lines:
            continue
        stats['positions'] += 1
        key = (r['line'], r['pos'])
        b = pos2box.get(key)
        c = conf.get(key, '')
        cf = c if c in ('H', 'M', 'L') else 'M'                     # no merged confidence on file -> doubtful
        sids = b['sid'].split('+') if b and b['sid'] else []
        mapped = b is not None and b['op'] in ('1:1', '2:1') and sids
        cands, why = [r['sign']], []
        if mapped:
            t = max((tk[s] for s in sids if s in tk), key=lambda t: int(t['w']), default=None)
            if t is None:
                mapped = False
            else:
                top = [t.get(f'k{k}', '') for k in (1, 2, 3)]
                cands += [x for x in top if x and x != '_']
                if top[0] != r['sign']: why.append('top1')
                if float(t.get('s1') or 0) < a.share: why.append('share')
        if cf in ('M', 'L'): why.append('conf')
        if not mapped:
            stats['unmapped'] += 1
            if cf not in ('M', 'L') or not sids:
                continue
        if not why:
            continue
        cands = list(dict.fromkeys(cands))
        if len(cands) < 2:
            stats['undecidable'] += 1
            continue
        random.Random(f'{a.seed}|{r["line"]}|{r["pos"]}').shuffle(cands)
        shown.append(dict(line=r['line'], pos=r['pos'], sids=sids, cands=cands, why='+'.join(why)))
    od = os.path.join(a.out, a.unit)
    os.makedirs(od, exist_ok=True)
    nsheet = 0
    for k0 in range(0, len(shown), a.rows):
        nsheet += 1
        rows = shown[k0:k0 + a.rows]
        cell, gap = a.cell, 8
        tiles = [context_tile(pages, sb, s['sids'], a.ctx_h, a.ctx_scale, a.ctx_w) for s in rows]
        kmax = max(len(s['cands']) for s in rows)
        ctxw = max(t.width for t in tiles)
        rowh = max(cell, max(t.height for t in tiles)) + 2 * gap
        W = 60 + ctxw + 24 + kmax * (2 * cell + 50) + gap
        H = 40 + rowh * len(rows)
        sheet = Image.new('RGB', (W, H), (255, 255, 255))  # saved greyscale (size)
        d = ImageDraw.Draw(sheet)
        d.text((10, 8), f'{a.unit} sheet {nsheet:02d}: which numbered candidate matches the boxed sign? (or none)',
               fill=(0, 0, 0), font=font(18))
        for n, (s, t) in enumerate(zip(rows, tiles), 1):
            y = 40 + (n - 1) * rowh
            d.line((0, y, W, y), fill=(120, 120, 120), width=2)
            d.text((10, y + rowh // 2 - 14), f'{n}', fill=(0, 0, 0), font=font(26))
            sheet.paste(t, (60, y + (rowh - t.height) // 2))
            x = 60 + ctxw + 24
            d.line((x - 12, y, x - 12, y + rowh), fill=(0, 0, 0), width=3)
            for ci, code in enumerate(s['cands'], 1):
                d.text((x, y + rowh // 2 - 14), f'{ci}', fill=(0, 0, 0), font=font(24))
                ex = exemplars_for(code, ex_lists, sb, by_code, excl)
                for e in range(2):
                    tt = exemplar_tile(pages, sb[ex[e]], cell) if e < len(ex) else Image.new('L', (cell, cell), 235)
                    sheet.paste(tt.convert('RGB'), (x + 30 + e * (cell + 4), y + (rowh - cell) // 2))
                x += 2 * cell + 50
        d.line((0, H - 1, W, H - 1), fill=(120, 120, 120), width=2)
        base = os.path.join(od, f'sheet_{nsheet:02d}')
        sheet.convert('L').save(base + '.png', optimize=True)
        wr(base + '.tsv', ['row', 'line', 'pos', 'cands', 'why'],
           [dict(row=n, line=s['line'], pos=s['pos'], cands=','.join(s['cands']), why=s['why']) for n, s in enumerate(rows, 1)])
    print(f'{a.unit}: positions {stats["positions"]}, shown {len(shown)}, sheets {nsheet} '
          f'(unmapped {stats["unmapped"]}, undecidable {stats["undecidable"]})')
    return shown


# ---------------------------------------------------------------- resolve
def parse_pick(p, k):
    p = (p or '').strip().lower()
    return int(p) if p.isdigit() and 1 <= int(p) <= k else None


def cmd_resolve(a):
    L = rd(path(a.line_read))
    lines = unit_lines(a.units, a.unit)
    od = os.path.join(a.out, a.unit)
    picks, n_sheets = {}, 0
    for fn in sorted(os.listdir(od)):
        m = re.match(r'sheet_(\d+)\.tsv$', fn)
        if not m:
            continue
        keyrows = {r['row']: r for r in rd(os.path.join(od, fn))}
        rp = os.path.join(od, f'reads_{m.group(1)}.tsv')
        if not os.path.exists(rp):
            sys.exit(f'resolve: {rp} missing (read every sheet first)')
        n_sheets += 1
        for r in rd(rp):
            kr = keyrows.get(str(r.get('row', '')).strip())
            if kr:
                cands = kr['cands'].split(',')
                picks[(kr['line'], kr['pos'])] = (cands, parse_pick(r.get('pick'), len(cands)),
                                                  (r.get('conf') or '').strip().upper())
    out, wt, ch = [], [], Counter()
    for r in L:
        if r['line'] not in lines:
            continue
        key, sign = (r['line'], r['pos']), r['sign']
        if key in picks:
            cands, pk, cf = picks[key]
            if pk is None:
                ch['none'] += 1
                sc = {c: (0.6 if c == sign else 0.4 / max(1, len(cands) - 1)) for c in cands}
            else:
                new = cands[pk - 1]
                ch['kept' if new == sign else 'changed'] += 1
                sign, w = new, CONF_W.get(cf, 0.6)
                sc = {c: (w if c == new else (1 - w) / max(1, len(cands) - 1)) for c in cands}
            wt += [dict(line=r['line'], pos=r['pos'], cand=c, score=f'{s:.3f}') for c, s in sc.items() if s > 0]
        else:
            wt.append(dict(line=r['line'], pos=r['pos'], cand=sign, score='1.000'))
        out.append(dict(line=r['line'], pos=r['pos'], sign=sign))
    po = a.pass_out or f'benchmark-tx/outputs/birago1572-no87/passG_compare_{a.unit}.tsv'
    wr(path(po) if not os.path.isabs(po) else po, ['line', 'pos', 'sign'], out)
    wr(os.path.join(od, 'topk_weighted.tsv'), ['line', 'pos', 'cand', 'score'], wt)
    print(f'{a.unit}: {len(out)} positions from {n_sheets} sheets; picks {dict(ch)} -> {po}')
    return out


def cmd_lattice_out(a):
    rows = rd(a.decode)
    wr(a.pass_out, ['line', 'pos', 'sign'], [dict(line=r['line'], pos=r['pos'], sign=r['chosen']) for r in rows])
    print(f'{len(rows)} positions -> {a.pass_out}')


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest='cmd', required=True)

    def common(p):
        p.add_argument('--atlas', default=D['atlas']); p.add_argument('--line-read', default=D['line_read'])
        p.add_argument('--units', default=D['units']); p.add_argument('--out', default=D['out'])
    m = sp.add_parser('map'); common(m)
    m.add_argument('--box-pos-out', default=os.path.join(D['out'], 'box_pos.tsv'))
    b = sp.add_parser('build'); common(b)
    b.add_argument('--unit', required=True); b.add_argument('--topk', default=D['topk'])
    b.add_argument('--conf', action='append', help='agreement TSV:page (repeatable; default the no.87 passC files)')
    b.add_argument('--exemplars', default=D['exemplars']); b.add_argument('--box-pos', default=None,
                   help='box_pos.tsv from `map` (default: OUT/box_pos.tsv, made if absent)')
    b.add_argument('--exclude-page', action='append', help='page never used for exemplars (default f178r f178v f179r)')
    b.add_argument('--share', type=float, default=0.6); b.add_argument('--rows', type=int, default=16)
    b.add_argument('--seed', default='txe-a'); b.add_argument('--cell', type=int, default=100)
    b.add_argument('--ctx-h', type=int, default=90, help='target sign height in the context tile, px (90)')
    b.add_argument('--ctx-scale', type=float, default=4.0, help='upscale cap for the context tile (4)')
    b.add_argument('--ctx-w', type=int, default=420, help='context tile width cap, px (420)')
    r = sp.add_parser('resolve'); common(r)
    r.add_argument('--unit', required=True); r.add_argument('--pass-out')
    lo = sp.add_parser('lattice-out'); lo.add_argument('decode'); lo.add_argument('--pass-out', required=True)
    a = ap.parse_args(argv)
    if a.cmd == 'build':
        a.conf = a.conf or D['conf']; a.exclude_page = a.exclude_page or D['exclude']
        if a.box_pos is None and os.path.exists(path(os.path.join(a.out, 'box_pos.tsv'))):
            a.box_pos = os.path.join(a.out, 'box_pos.tsv')
    return {'map': cmd_map, 'build': cmd_build, 'resolve': cmd_resolve, 'lattice-out': cmd_lattice_out}[a.cmd](a)


if __name__ == '__main__':
    main()
