#!/usr/bin/env python3
"""Error taxonomy of transcription passes against BENCHMARK-TX.tsv (LANE TX-ENGINEER round 1, 9 Oct 2026).

    python3 tools/tx_taxonomy.py --item birago1572-no87 --pass A=benchmark-tx/outputs/birago1572-no87/passA.tsv \
        [--pass B=...] [--boxes atlas/signs.tsv --box-token atlas/no87_box_token.tsv --harvest ciphers/<t>/harvest] \
        --out-tsv OUT.tsv [--md OUT.md] [--ref A]

For every scored truth position of the item (tools/tx_bench.py's alignment, so the figures match tx_bench) it writes one row
with the sign each pass read there (`<deleted>` when the pass dropped it), whether that read is wrong, and the features the
taxonomy sorts errors by:

  pos_class    first / last / inner: the sign's place in its truth line (first and last scored-or-not position of the line)
  line_len     signs in the truth line
  line_in_call index of the line within its reader call group (--call-lines "f178v_L01-10,f178v_L11-23,...": lines not
               named get their line index within the leaf); the brief's "fatigue by call position" axis
  seg_edge     geometry, only when --boxes/--box-token/--harvest map the position to a segmented box: `edge` when the
               box lies within --edge-frac (default 0.05) of a left/right border of every segment crop that holds it,
               `overlap` when it lies inside two segment crops (the s1/s2/s3 overlap zone), `inner` otherwise
  band_edge    `cut` when the box's top or bottom lies outside the crop band, `near` within --edge-frac of the band
               height, else `in`
  glued        the box<->token op from --box-token: `2:1` one box = two tokens (a joined pair), `1:2` one token = two
               boxes (a split sign), `1:1`, or `-` when unmapped
  stroke       thin / mid / heavy: terciles over the item's mapped signs of the share of the box's ink that survives a
               3x3 erosion on the page image (thin strokes lose it all); `-` when unmapped
  n_wrong      how many of the passes are wrong at this position; same_wrong = all wrong passes read the same sign

Reader agreement on errors (TXP-AGREE, 9 Oct 2026; appended as the last columns, every earlier column and every earlier
--md section unchanged). The first --pass is the baseline:
  n_pass_wrong how many covering passes are wrong here (equals n_wrong; kept under its own name for the agreement table)
  n_same_wrong how many covering passes, baseline included, read the baseline's own wrong sign (`<deleted>` is a sign of its
               own); 0 when the baseline is right, empty when the baseline does not cover the position
  agree_class  right | all-same-wrong (every covering pass wrong with the baseline's sign) | all-wrong-split (every
               covering pass wrong, signs differ) | majority-wrong (more than half wrong, not all) | baseline-only (no
               other pass wrong) | minority-wrong (some other pass wrong, at most half in all) | no-other-pass (only the
               baseline covers it); empty when the baseline does not cover the position
  err_class    the baseline error's class for the cross table, first match wins: crop (band_edge cut, seg_edge
               outside, or the baseline deleted the sign) | look-alike (the baseline's (truth plain <- read) pair recurs
               at least twice among its errors on this item) | thin (stroke tercile thin) | other; empty when right
The --md output gains a last section: the baseline's errors by agree_class, crossed with err_class and with the top
(truth <- read) pairs. A class that is all-same-wrong is "every reader, every presentation"; a reader-split class is
where a second look can help. Passes that cover only some lines (dev-only passes) count only where they cover.

The markdown summary (--md) gives, per pass, the error mass by each feature class and the top (truth value <- read) pairs
with their feature profile, and a correlation table (share of pass X's errors repeated by pass Y, same wrong sign). It
sorts, it does not explain: the mechanism per class is the analyst's sentence in the research note, not this tool's.

Geometry is optional and item-specific: BENCHMARK-TX items without a box<->token map get pos_class, line_in_call and the
correlation columns only. Nothing here reads a crop with a model; no truth file is edited. Exit 0; exit 2 on bad input.
Offline test: tools/tests/test_tx_taxonomy.py.
"""
import argparse, csv, json, os, re, sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tx_bench  # noqa: E402


def read_tsv(path):
    return tx_bench.read_tsv(path)


def aligned_reads(truth_rows, out_lines):
    """{(line, pos): read sign or '<deleted>'} over scored positions of covered lines, plus inserted count per line."""
    by_line = defaultdict(list)
    for r in truth_rows:
        by_line[r['line']].append(r)
    reads, inserted = {}, Counter()
    for ln, rows in by_line.items():
        if ln not in out_lines:
            continue
        rows.sort(key=lambda r: float(r['pos']))
        ref = [r['ref_sign'] for r in rows]
        ts = [set(filter(None, r['truth'].split('|'))) for r in rows]
        for ri, osg in tx_bench.align(ref, ts, out_lines[ln]):
            if ri is None:
                inserted[ln] += 1
                continue
            if rows[ri]['status'] != 'scored':
                continue
            reads[(ln, rows[ri]['pos'])] = osg if osg is not None else '<deleted>'
    return reads, inserted


def parse_call_lines(spec):
    """'f178v_L01-10,f178v_L11-23' -> {line_id: index within its group (1-based)}."""
    out = {}
    if not spec:
        return out
    for grp in spec.split(','):
        m = re.match(r'^(.+)_L(\d+)-(\d+)$', grp.strip())
        if not m:
            sys.exit('tx_taxonomy: bad --call-lines group %r (want leaf_Lnn-mm)' % grp)
        leaf, a, b = m.group(1), int(m.group(2)), int(m.group(3))
        for i, n in enumerate(range(a, b + 1), 1):
            out['%s_L%02d' % (leaf, n)] = i
    return out


def page_origin(source_file):
    """src_ark_..._f182_1703_848_2900_3452.jpg -> (1703, 848)."""
    m = re.search(r'_f\d+_(\d+)_(\d+)_(\d+)_(\d+)\.jpg$', source_file)
    return (int(m.group(1)), int(m.group(2))) if m else (0, 0)


def load_geometry(boxes, box_token, harvest):
    """Returns pos_geo {(line,pos): dict(seg_edge, band_edge, glued, erosion_share)} using the atlas boxes, the box<->token
    map and each leaf's manifest.json under harvest/<leaf>/."""
    sids = {r['sid']: r for r in read_tsv(boxes)}
    tok = defaultdict(list)
    for r in read_tsv(box_token):
        if r['sid'] in sids:
            tok[(r['line'], r['pos'])].append(r)
    leaves = {r['fol'] for r in read_tsv(box_token)}
    crops = {}
    for leaf in leaves:
        mp = os.path.join(harvest, leaf, 'manifest.json')
        if not os.path.exists(mp):
            continue
        ox, oy = None, None
        for e in json.load(open(mp))['iiif_lines']:
            if ox is None:
                ox, oy = page_origin(e.get('source_file', ''))
            m = re.match(r'^(.+_L\d+)_s(\d+)\.jpg$', e['crop'])
            if not m:
                continue
            x0, y0, x1, y1 = e['box']
            crops.setdefault(m.group(1), []).append((x0 - ox, y0 - oy, x1 - ox, y1 - oy))
    pages = {}
    try:
        from PIL import Image
        import numpy as np
        for leaf in leaves:
            d = os.path.join(harvest, leaf)
            if not os.path.isdir(d):
                continue
            src = [f for f in os.listdir(d) if f.startswith('src_') and f.endswith('.jpg')]
            if src:
                pages[leaf] = np.asarray(Image.open(os.path.join(d, src[0])).convert('L'))
    except ImportError:
        pass
    return sids, tok, crops, pages


def erosion_share(page, x, y, w, h):
    """Share of ink pixels in the box that survive a 3x3 erosion (0 = hairline strokes, 1 = solid blobs)."""
    import numpy as np
    tile = page[max(0, y):y + h, max(0, x):x + w]
    if tile.size == 0:
        return None
    thr = (int(tile.min()) + int(tile.max())) / 2.0
    ink = tile < thr
    if ink.sum() == 0:
        return None
    p = np.pad(ink, 1)
    er = p[1:-1, 1:-1].copy()
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            er &= p[1 + dy:p.shape[0] - 1 + dy, 1 + dx:p.shape[1] - 1 + dx]
    return float(er.sum()) / float(ink.sum())


def geo_features(key, sids, tok, crops, pages, edge_frac):
    rows = tok.get(key)
    if not rows:
        return None
    r = rows[0]
    b = sids[r['sid']]
    x, y, w, h = int(b['x']), int(b['y']), int(b['w']), int(b['h'])
    line = r['line']
    segs = crops.get(line, [])
    cx = x + w / 2.0
    holding = [s for s in segs if s[0] <= cx <= s[2]]
    seg_edge = '-'
    band_edge = '-'
    if segs:
        if len(holding) >= 2:
            seg_edge = 'overlap'
        elif holding:
            s = holding[0]
            cw = s[2] - s[0]
            near = min(x - s[0], s[2] - (x + w)) < edge_frac * cw
            seg_edge = 'edge' if near else 'inner'
        else:
            seg_edge = 'outside'
        s = holding[0] if holding else segs[0]
        bh = s[3] - s[1]
        if y < s[1] or y + h > s[3]:
            band_edge = 'cut'
        elif min(y - s[1], s[3] - (y + h)) < edge_frac * bh:
            band_edge = 'near'
        else:
            band_edge = 'in'
    es = None
    leaf = r['fol']
    if leaf in pages:
        es = erosion_share(pages[leaf], x, y, w, h)
    return dict(seg_edge=seg_edge, band_edge=band_edge, glued=r.get('op', '-') or '-', erosion=es,
                box_w=w, box_h=h)


def tercile_classes(values):
    vals = sorted(v for v in values if v is not None)
    if len(vals) < 3:
        return lambda v: '-'
    t1, t2 = vals[len(vals) // 3], vals[2 * len(vals) // 3]

    def cls(v):
        if v is None:
            return '-'
        return 'thin' if v < t1 else ('mid' if v < t2 else 'heavy')
    return cls


def build_rows(truth_rows, passes, call_lines, geo, edge_frac):
    by_line = defaultdict(list)
    for r in truth_rows:
        by_line[r['line']].append(r)
    reads = {}
    for name, lines in passes.items():
        reads[name], _ = aligned_reads(truth_rows, lines)
    names = list(passes)
    rows = []
    geo_cache = {}
    for ln, trs in by_line.items():
        trs.sort(key=lambda r: float(r['pos']))
        first, last = trs[0]['pos'], trs[-1]['pos']
        li = call_lines.get(ln) or int(re.search(r'L(\d+)', ln).group(1)) if re.search(r'L(\d+)', ln) else 0
        for r in trs:
            if r['status'] != 'scored':
                continue
            key = (ln, r['pos'])
            covered = [n for n in names if key in reads[n]]
            if not covered:
                continue
            ts = set(filter(None, r['truth'].split('|')))
            row = dict(line=ln, pos=r['pos'], plain=r['plain'], truth=r['truth'], ref_sign=r['ref_sign'],
                       pos_class='first' if r['pos'] == first else ('last' if r['pos'] == last else 'inner'),
                       line_len=len(trs), line_in_call=li)
            wrong_signs = []
            for n in names:
                rd = reads[n].get(key)
                row['read_' + n] = rd if rd is not None else ''
                if rd is None:
                    row['err_' + n] = ''
                else:
                    e = rd == '<deleted>' or rd not in ts
                    row['err_' + n] = '1' if e else '0'
                    if e:
                        wrong_signs.append(rd)
            row['n_cov'] = len(covered)
            row['n_wrong'] = len(wrong_signs)
            row['same_wrong'] = '1' if len(wrong_signs) >= 2 and len(set(wrong_signs)) == 1 else ('0' if len(wrong_signs) >= 2 else '')
            g = None
            if geo:
                sids, tok, crops, pages = geo
                g = geo_features(key, sids, tok, crops, pages, edge_frac)
            if g:
                row.update(seg_edge=g['seg_edge'], band_edge=g['band_edge'], glued=g['glued'], box_w=g['box_w'],
                           box_h=g['box_h'])
                geo_cache[key] = g['erosion']
            else:
                row.update(seg_edge='-', band_edge='-', glued='-', box_w='', box_h='')
            rows.append(row)
    cls = tercile_classes(geo_cache.values())
    for row in rows:
        row['stroke'] = cls(geo_cache.get((row['line'], row['pos'])))
        e = geo_cache.get((row['line'], row['pos']))
        row['erosion'] = '' if e is None else '%.3f' % e
    rows.sort(key=lambda r: (r['line'], float(r['pos'])))
    add_agreement(rows, names)
    return rows, names


AGREE_CLASSES = ['all-same-wrong', 'all-wrong-split', 'majority-wrong', 'minority-wrong', 'baseline-only', 'no-other-pass']
ERR_CLASSES = ['crop', 'look-alike', 'thin', 'other']


def add_agreement(rows, names):
    """n_pass_wrong, n_same_wrong, agree_class and err_class per row, with names[0] as the baseline."""
    b = names[0]
    pairs = Counter((r['plain'], r['read_' + b]) for r in rows if r['err_' + b] == '1' and r['read_' + b] != '<deleted>')
    for r in rows:
        cov = [n for n in names if r['err_' + n] != '']
        wrong = [n for n in cov if r['err_' + n] == '1']
        r['n_pass_wrong'] = len(wrong)
        if r['err_' + b] == '':
            r['n_same_wrong'] = r['agree_class'] = r['err_class'] = ''
            continue
        if r['err_' + b] == '0':
            r['n_same_wrong'], r['agree_class'], r['err_class'] = 0, 'right', ''
            continue
        rb = r['read_' + b]
        same = [n for n in wrong if r['read_' + n] == rb]
        r['n_same_wrong'] = len(same)
        if len(cov) == 1:
            ac = 'no-other-pass'
        elif len(wrong) == len(cov):
            ac = 'all-same-wrong' if len(same) == len(cov) else 'all-wrong-split'
        elif 2 * len(wrong) > len(cov):
            ac = 'majority-wrong'
        elif len(wrong) == 1:
            ac = 'baseline-only'
        else:
            ac = 'minority-wrong'
        r['agree_class'] = ac
        if r.get('band_edge') == 'cut' or r.get('seg_edge') == 'outside' or rb == '<deleted>':
            r['err_class'] = 'crop'
        elif pairs[(r['plain'], rb)] >= 2:
            r['err_class'] = 'look-alike'
        elif r.get('stroke') == 'thin':
            r['err_class'] = 'thin'
        else:
            r['err_class'] = 'other'


def fmt_agree(rows, names, top):
    """The baseline's errors by agree_class, crossed with err_class and with the top (truth <- read) pairs."""
    b = names[0]
    err = [r for r in rows if r['err_' + b] == '1']
    acs = [c for c in AGREE_CLASSES if any(r['agree_class'] == c for r in err)]
    ne = len(err)
    lines = ['', '### Reader agreement on the baseline\'s errors (baseline %s; %d errors; passes %s)' % (b, ne, ', '.join(names)),
             '']
    ac = Counter(r['agree_class'] for r in err)
    lines.append('| agree_class | errors | share |')
    lines.append('|---|---|---|')
    for c in acs:
        lines.append('| %s | %d | %.1f%% |' % (c, ac[c], 100.0 * ac[c] / ne if ne else 0))
    lines += ['', '| err_class | errors | ' + ' | '.join(acs) + ' |', '|---|---|' + '---|' * len(acs)]
    for ec in ERR_CLASSES:
        rs = [r for r in err if r['err_class'] == ec]
        if not rs:
            continue
        c = Counter(r['agree_class'] for r in rs)
        lines.append('| %s | %d | %s |' % (ec, len(rs), ' | '.join('%d (%.0f%%)' % (c[a], 100.0 * c[a] / len(rs)) for a in acs)))
    pc = Counter((r['plain'], r['read_' + b]) for r in err)
    lines += ['', '| truth <- read | n | err_class | ' + ' | '.join(acs) + ' | lines |', '|---|---|---|' + '---|' * len(acs) + '---|']
    for k, v in pc.most_common(top):
        rs = [r for r in err if (r['plain'], r['read_' + b]) == k]
        c = Counter(r['agree_class'] for r in rs)
        ecs = Counter(r['err_class'] for r in rs)
        lines.append('| %s <- %s | %d | %s | %s | %s |' % (
            k[0], k[1], v, ', '.join('%s %d' % kv for kv in ecs.most_common()), ' | '.join(str(c[a]) for a in acs),
            ' '.join(sorted({'%s.%s' % (r['line'].split('_')[-1], r['pos']) for r in rs}))[:120]))
    return lines


def mass_table(rows, names, feature):
    """Per pass: errors by class / errors total, and the class's share of covered positions (the base rate)."""
    out = {}
    for n in names:
        cov = [r for r in rows if r['err_' + n] != '']
        err = [r for r in cov if r['err_' + n] == '1']
        base = Counter(r[feature] for r in cov)
        em = Counter(r[feature] for r in err)
        out[n] = (len(err), len(cov), base, em)
    return out


def fmt_mass(rows, names, feature, title):
    classes = sorted({r[feature] for r in rows}, key=str)
    lines = ['', '### %s' % title, '', '| pass | errors | ' + ' | '.join('%s (base %%)' % c for c in classes) + ' |',
             '|---|---|' + '---|' * len(classes)]
    mt = mass_table(rows, names, feature)
    for n in names:
        ne, nc, base, em = mt[n]
        cells = []
        for c in classes:
            b = 100.0 * base[c] / nc if nc else 0
            e = em[c]
            rate = 100.0 * e / base[c] if base[c] else 0
            cells.append('%d (%.0f%% of errs; rate %.1f%%; base %.0f%%)' % (e, 100.0 * e / ne if ne else 0, rate, b))
        lines.append('| %s | %d/%d | %s |' % (n, ne, nc, ' | '.join(cells)))
    return lines


def fmt_pairs(rows, names, top):
    lines = ['', '### Top (truth value <- read) pairs per pass, with feature profile', '']
    for n in names:
        c = Counter()
        prof = defaultdict(list)
        for r in rows:
            if r['err_' + n] == '1':
                k = (r['plain'], r['read_' + n])
                c[k] += 1
                prof[k].append(r)
        lines.append('**%s** (%d errors):' % (n, sum(c.values())))
        lines.append('')
        lines.append('| truth <- read | n | first/last/inner | seg edge/overlap/inner | band cut/near/in | glued 2:1/1:2 | stroke thin/mid/heavy | also wrong in (same sign) | lines |')
        lines.append('|---|---|---|---|---|---|---|---|---|')
        for k, v in c.most_common(top):
            rs = prof[k]
            pc = Counter(r['pos_class'] for r in rs)
            se = Counter(r['seg_edge'] for r in rs)
            be = Counter(r['band_edge'] for r in rs)
            gl = Counter(r['glued'] for r in rs)
            st = Counter(r['stroke'] for r in rs)
            others = Counter()
            for r in rs:
                for m in names:
                    if m != n and r['err_' + m] == '1':
                        others[m + ('=' if r['read_' + m] == r['read_' + n] else '~')] += 1
            lines.append('| %s <- %s | %d | %d/%d/%d | %d/%d/%d | %d/%d/%d | %d/%d | %d/%d/%d | %s | %s |' % (
                k[0], k[1], v, pc['first'], pc['last'], pc['inner'], se['edge'], se['overlap'], se['inner'],
                be['cut'], be['near'], be['in'], gl['2:1'], gl['1:2'], st['thin'], st['mid'], st['heavy'],
                ', '.join('%s %d' % kv for kv in others.most_common()),
                ' '.join(sorted({'%s.%s' % (r['line'].split('_')[-1], r['pos']) for r in rs}))[:120]))
        lines.append('')
    return lines


def fmt_corr(rows, names):
    lines = ['', '### Error correlation: share of the row pass\'s errors repeated by the column pass (same wrong sign in brackets)', '',
             '| pass | errors | ' + ' | '.join(names) + ' |', '|---|---|' + '---|' * len(names)]
    for a in names:
        ea = [r for r in rows if r['err_' + a] == '1']
        cells = []
        for b in names:
            if a == b:
                cells.append('-')
                continue
            both = [r for r in ea if r['err_' + b] == '1']
            same = [r for r in both if r['read_' + a] == r['read_' + b]]
            cov = [r for r in ea if r['err_' + b] != '']
            cells.append('%d/%d (%d)' % (len(both), len(cov), len(same)))
        lines.append('| %s | %d | %s |' % (a, len(ea), ' | '.join(cells)))
    lines.append('')
    lines.append('Positions wrong in every covering pass (n_wrong == n_cov, n_cov >= 2): %d; wrong in exactly one: %d' % (
        sum(1 for r in rows if r['n_cov'] >= 2 and r['n_wrong'] == r['n_cov']),
        sum(1 for r in rows if r['n_wrong'] == 1)))
    return lines


def fmt_callpos(rows, names):
    lines = ['', '### Error rate by line index within the reader call (fatigue axis)', '']
    idx = sorted({r['line_in_call'] for r in rows})
    lines.append('| pass | ' + ' | '.join('L+%d' % i for i in idx) + ' |')
    lines.append('|---|' + '---|' * len(idx))
    for n in names:
        cells = []
        for i in idx:
            cov = [r for r in rows if r['line_in_call'] == i and r['err_' + n] != '']
            err = sum(1 for r in cov if r['err_' + n] == '1')
            cells.append('%d/%d' % (err, len(cov)) if cov else '')
        lines.append('| %s | %s |' % (n, ' | '.join(cells)))
    return lines


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--bench', default='BENCHMARK-TX.tsv')
    ap.add_argument('--item', required=True)
    ap.add_argument('--pass', dest='passes', action='append', required=True, metavar='NAME=PATH',
                    help='a pass to score (repeatable); the first is the baseline for the agreement columns')
    ap.add_argument('--line-prefix')
    ap.add_argument('--call-lines', help='comma-separated leaf_Lnn-mm groups read in one reader call')
    ap.add_argument('--boxes', help='atlas signs.tsv')
    ap.add_argument('--box-token', help='atlas box<->token map (sid, fol, line, pos, op)')
    ap.add_argument('--harvest', help='harvest folder holding <leaf>/manifest.json and the src_ page image')
    ap.add_argument('--edge-frac', type=float, default=0.05)
    ap.add_argument('--out-tsv', required=True)
    ap.add_argument('--md')
    ap.add_argument('--top', type=int, default=10)
    ap.add_argument('--label-map', help='TSV from/to applied to outputs, reference and truth before scoring (as tx_bench)')
    a = ap.parse_args(argv)
    bench = {r['item']: r for r in read_tsv(a.bench)}
    if a.item not in bench:
        sys.exit('tx_taxonomy: item %s not in %s' % (a.item, a.bench))
    tpath = bench[a.item]['truth']
    if not os.path.isabs(tpath) and not os.path.exists(tpath):
        tpath = os.path.join(os.path.dirname(os.path.abspath(a.bench)), tpath)
    truth = read_tsv(tpath)
    lm = tx_bench.load_label_map(a.label_map) if a.label_map else {}
    if lm:
        truth = tx_bench.map_truth(truth, lm)
    passes = {}
    for spec in a.passes:
        if '=' not in spec:
            sys.exit('tx_taxonomy: --pass wants NAME=PATH')
        n, p = spec.split('=', 1)
        lines = tx_bench.load_output([p], a.line_prefix)
        passes[n] = {k: [lm.get(s, s) for s in v] for k, v in lines.items()} if lm else lines
    geo = None
    if a.boxes and a.box_token and a.harvest:
        geo = load_geometry(a.boxes, a.box_token, a.harvest)
    rows, names = build_rows(truth, passes, parse_call_lines(a.call_lines), geo, a.edge_frac)
    cols = ['line', 'pos', 'plain', 'truth', 'ref_sign', 'pos_class', 'line_len', 'line_in_call', 'seg_edge', 'band_edge',
            'glued', 'stroke', 'erosion', 'box_w', 'box_h', 'n_cov', 'n_wrong', 'same_wrong'] + \
           ['read_' + n for n in names] + ['err_' + n for n in names] + \
           ['n_pass_wrong', 'n_same_wrong', 'agree_class', 'err_class']
    with open(a.out_tsv, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter='\t')
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, '') for k in cols})
    md = ['## %s: %d scored positions, passes %s' % (a.item, len(rows), ', '.join(names))]
    for n in names:
        cov = [r for r in rows if r['err_' + n] != '']
        err = sum(1 for r in cov if r['err_' + n] == '1')
        md.append('- %s: %d wrong-or-deleted of %d covered positions (insertions not counted here; tx_bench adds them)' % (n, err, len(cov)))
    md += fmt_mass(rows, names, 'pos_class', 'Error mass by position in line')
    if geo:
        md += fmt_mass(rows, names, 'seg_edge', 'Error mass by segment-crop edge (left/right)')
        md += fmt_mass(rows, names, 'band_edge', 'Error mass by line-band edge (top/bottom)')
        md += fmt_mass(rows, names, 'glued', 'Error mass by box<->token op (glued 2:1, split 1:2)')
        md += fmt_mass(rows, names, 'stroke', 'Error mass by stroke weight (erosion-survival terciles)')
    md += fmt_callpos(rows, names)
    md += fmt_corr(rows, names)
    md += fmt_pairs(rows, names, a.top)
    md += fmt_agree(rows, names, a.top)
    text = '\n'.join(md) + '\n'
    if a.md:
        with open(a.md, 'w') as f:
            f.write(text)
    print(text)
    return 0


if __name__ == '__main__':
    sys.exit(main())
