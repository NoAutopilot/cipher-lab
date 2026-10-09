#!/usr/bin/env python3
"""Feature-first reading protocol (TXE-M, LANE TX-ENGINEER, idea M24; 9 Oct 2026; benchmark-tx/PREREG-txeng-2.md,
benchmark-tx/txeng/feature/PREREG.md).

Lesson it answers (research/TX-IDEAS-2026-10-09.md Results log): eleven instruments changed WHAT the blind reader sees
beside the glyph (exemplars, hints, upscaling) and none moved the reader; its errors sit in the glyph. None changed HOW it
decides. A palaeographer names the deciding features first (descender? one bar or two? loop closed? dot?) and only then
the letter. This tool derives a fixed feature vocabulary from the printed sign sheet's own cells (never from the hand,
never from truth), appends the cell-feature table and one output rule to the unchanged blind brief, and afterwards
checks whether the reader's written features contradict the cell it chose (a read-free self-consistency flag).

Vocabulary (7 features, every value computed from the cell's ink by the functions below):
  desc   none/short/long  ink below the glyph's body band, as a fraction of body height (<0.25 none, <0.75 short)
  asc    none/short/long  ink above the body band, same cut points
  bars   0/1/2            groups of rows whose longest horizontal ink run exceeds 0.6 x glyph width (capped at 2)
  loops  0/1/2            enclosed background holes, area >= 1% of the glyph box (capped at 2)
  dots   0/1/2+           separate small ink components (area < 12% of the largest component)
  lean   left/upright/right  principal-axis shear dx/dy of the ink (|shear| < 0.15 upright)
  tail   none/left/right  mean x of the lowest 20% of ink rows vs the glyph's mean x (|offset| < 0.15 width none)
The body band joins the runs of rows whose horizontal ink extent is >= 0.45 x the glyph's width (the longest run and
every run at least half as long).

Subcommands (disk only, no network, no model):
  cells    --sheet sign_sheet_blind_1572.png --ids-from sign_id_map_1572.json --out cell_features.tsv
           Cuts the 9-column 110 px grid of the printed sheet; reads ONLY the ids (sorted, the sheet's order) from the
           map, never a value. Writes id + the seven features + raw measures.
  assemble --base harvest/blind_pass_brief_1572.md --cells cell_features.tsv --signsheet PNG --crops ... --raw OUT --out TASK
           The unchanged brief + the feature rule + the cell table + the task lines.
  norm     --raw RAW.tsv --leaf f178v --out passX.tsv   (passage,pos,sign_id) -> (line,pos,sign), as build_birago87.py.
  consist  --raw RAW.tsv --cells cell_features.tsv [--wrong wrong.tsv] --out consist.tsv
           Per sign: how many of the seven written features contradict the chosen cell's; with --wrong (line,pos of
           wrong signs, from tx_bench after the read is committed) the share of wrong vs right signs flagged.

Two-call protocol (TXE-M2, 9 Oct 2026; benchmark-tx/txeng/feature/PREREG-M2.md). Lesson: in TXE-M one call saw the sheet
and the table together, so a reader named the cell first and filled the features backwards (167/167 rows = the table).
Here the features are written in a call that never sees the sheet, the table or a sign name, and a read-free compliance
gate runs before any cell is named:
  tiles    --sheet PNG --ids-from MAP.json --seed N --out TILES.png --map MAP.tsv
           The 51 printed cells without their labels, renumbered 1..51 in a seeded order, as one montage (the control of
           gate c); the tile -> cell map goes to a file the reader never gets.
  task1    --crops ... --raw OUT --out TASK  (or --tiles TILES.png for the control)
           Features-only task: crops, overlap rule, vocabulary; no sheet, no table, no sign names.
  comply   --raw1 c1.tsv c2.tsv --base passA.tsv --control CTRL.tsv --map MAP.tsv --cells cell_features.tsv
           (a) signs per line within 10% of the base pass on every line; (b) every feature column that varies in the
           cell table itself (two values on >= 10% of cells) has two values on >= 10% of rows; (c) control tiles whose
           written features differ from the cell table in at most one feature >= 70%. Exit 0 = compliant, 4 = not.
  task2    --crops ... --signsheet PNG --cells cell_features.tsv --feats c1.tsv --raw OUT --out TASK
           Cell naming from the reader's own call-1 features (pasted), nearest cell plus `mismatch` beyond one feature.
"""
import argparse, csv, json, os, sys

FEATS = ('desc', 'asc', 'bars', 'loops', 'dots', 'lean', 'tail')
VOCAB = {'desc': ('none', 'short', 'long'), 'asc': ('none', 'short', 'long'), 'bars': ('0', '1', '2'),
         'loops': ('0', '1', '2'), 'dots': ('0', '1', '2+'), 'lean': ('left', 'upright', 'right'),
         'tail': ('none', 'left', 'right')}
SECTION = 'Features first, then the cell'


def rd(p):
    with open(p, newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


# ---------- measures (pure; tested offline) ----------
def crop_ink(ink):
    import numpy as np
    ys, xs = np.nonzero(ink)
    if len(ys) == 0:
        return ink[:0, :0]
    return ink[ys.min():ys.max() + 1, xs.min():xs.max() + 1]


def body_band(ink, frac=0.45, keep=0.5):
    """(top, bottom) rows of the body: runs of rows whose ink extent >= frac x width; the longest run and every run at
    least keep x as long are joined (so a C or a # with two wide strokes is one body, not a top bar and a descender)."""
    W = ink.shape[1]
    ok = []
    for row in ink:
        idx = [i for i, v in enumerate(row) if v]
        ok.append(bool(idx) and (idx[-1] - idx[0] + 1) >= frac * W)
    runs, start = [], None
    for i, v in enumerate(ok + [False]):
        if v and start is None:
            start = i
        elif not v and start is not None:
            runs.append((start, i - 1)); start = None
    if not runs:
        return (0, ink.shape[0] - 1)
    best = max(e - s + 1 for s, e in runs)
    big = [(s, e) for s, e in runs if e - s + 1 >= keep * best]
    return (min(s for s, _ in big), max(e for _, e in big))


def level(v):
    return 'none' if v < 0.25 else ('short' if v < 0.75 else 'long')


def count_loops(ink, min_frac=0.01):
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
    W = ink.shape[1]
    hit = []
    for row in ink:
        best = cur = 0
        for v in row:
            cur = cur + 1 if v else 0
            best = max(best, cur)
        hit.append(best > frac * W)
    return int(sum(1 for i, h in enumerate(hit) if h and (i == 0 or not hit[i - 1])))


def count_dots(ink, frac=0.12):
    from scipy import ndimage
    lab, n = ndimage.label(ink, structure=[[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    if n < 2:
        return 0
    sizes = list(ndimage.sum(ink, lab, range(1, n + 1)))
    big = max(sizes)
    return sum(1 for s in sizes if s < frac * big and s >= 3)


def shear(ink):
    """dx/dy of the ink's principal direction; positive = top leans right."""
    import numpy as np
    ys, xs = np.nonzero(ink)
    if len(ys) < 3:
        return 0.0
    y = ys - ys.mean(); x = xs - xs.mean()
    vy = (y * y).mean()
    return float(-(x * y).mean() / vy) if vy else 0.0


def tail_offset(ink, frac=0.2):
    import numpy as np
    ys, xs = np.nonzero(ink)
    if len(ys) == 0:
        return 0.0
    H, W = ink.shape
    low = ys >= ys.max() - max(1, int(round(frac * H)))
    return float((xs[low].mean() - xs.mean()) / W)


def features(ink):
    """ink: boolean mask of one glyph (any margin). -> (feature dict, raw measure dict)."""
    g = crop_ink(ink)
    H = g.shape[0]
    t, b = body_band(g)
    bh = max(1, b - t + 1)
    d, a = (H - 1 - b) / bh, t / bh
    nb, nl, nd = min(2, count_bars(g)), min(2, count_loops(g)), count_dots(g)
    sh, to = shear(g), tail_offset(g)
    f = {'desc': level(d), 'asc': level(a), 'bars': str(nb), 'loops': str(nl), 'dots': '2+' if nd >= 2 else str(nd),
         'lean': 'upright' if abs(sh) < 0.15 else ('right' if sh > 0 else 'left'),
         'tail': 'none' if abs(to) < 0.15 else ('right' if to > 0 else 'left')}
    raw = {'desc_r': round(d, 2), 'asc_r': round(a, 2), 'shear': round(sh, 2), 'tail_off': round(to, 2)}
    return f, raw


def parse_written(s):
    """'desc=long asc=none bars=0 ...' (any order, ; , or space separated) -> dict of recognised features."""
    out = {}
    for tok in s.replace(';', ' ').replace(',', ' ').split():
        if '=' in tok:
            k, v = tok.split('=', 1)
            k, v = k.strip().lower(), v.strip().lower()
            if v == '2' and k == 'dots':
                v = '2+'
            if k in VOCAB and v in VOCAB[k]:
                out[k] = v
    return out


def contradictions(written, cell):
    return [k for k in FEATS if k in written and k in cell and written[k] != cell[k]]


# ---------- cells ----------
def cmd_cells(a):
    import numpy as np
    from PIL import Image
    im = np.asarray(Image.open(a.sheet).convert('L'))
    ids = sorted(c['id'] for c in json.load(open(a.ids_from)))  # ids only; never a value
    CW = CH = 110; NC = 9
    with open(a.out, 'w') as f:
        f.write('# tools/tx_features.py cells: features of each printed sheet cell (sign_sheet_blind_1572.png), '
                'derived by script from the cell ink; no hand, no truth\n')
        f.write('cell\t' + '\t'.join(FEATS) + '\tdesc_r\tasc_r\tshear\ttail_off\n')
        for n, cid in enumerate(ids):
            gx, gy = (n % NC) * CW, (n // NC) * CH
            ink = im[gy + 25:gy + CH - 2, gx + 2:gx + CW - 2] < 110
            ft, raw = features(ink)
            f.write(cid + '\t' + '\t'.join(ft[k] for k in FEATS) + '\t' +
                    '\t'.join(str(raw[k]) for k in ('desc_r', 'asc_r', 'shear', 'tail_off')) + '\n')
    print(f'{len(ids)} cells -> {a.out}')
    return 0


def rule_text(cells):
    lines = [f'## {SECTION}', '',
             'For every sign, look at the ink FIRST and write its features in a `features` column, BEFORE you choose the '
             'cell. Then choose the cell whose features (table below, measured by script on the printed sheet) match '
             'what you wrote; where two cells share the features, decide by the rest of the shape. If the ink '
             'clearly disagrees with every cell\'s features, say so in the note. The output header becomes:', '',
             '    passage\tpos\tfeatures\tsign_id\talt\tconf\tnote', '',
             'Write `features` exactly as seven key=value pairs separated by spaces, in this order and vocabulary:', '',
             '    desc=none|short|long asc=none|short|long bars=0|1|2 loops=0|1|2 dots=0|1|2+ '
             'lean=left|upright|right tail=none|left|right', '',
             '- desc / asc: ink below / above the main body of the sign, compared with the body\'s height '
             '(none: under a quarter; short: under three quarters; long: more).',
             '- bars: long horizontal strokes running across most of the sign\'s width (a flat loop top counts).',
             '- loops: closed loops (enclosed holes).',
             '- dots: separate small marks (dot, tick, accent) apart from the main stroke.',
             '- lean: the sign\'s main axis tilts left, stands upright, or tilts right.',
             '- tail: the lowest part of the ink ends to the left or right of the sign\'s centre, or is centred (none).',
             '', 'Cell features (from the printed sheet):', '',
             '| cell | ' + ' | '.join(FEATS) + ' |', '|' + '---|' * (len(FEATS) + 1)]
    for c in cells:
        lines.append(f"| {c['cell']} | " + ' | '.join(c[k] for k in FEATS) + ' |')
    return '\n'.join(lines)


def cmd_assemble(a):
    base = open(a.base).read().rstrip() + '\n\n'
    task = ['## Your task', '', f'The sheet: {os.path.abspath(a.signsheet)}', '',
            f'The crops ({len(a.crops)} images, 2x, s1 s2 s3 of each line in order; the passage id is the L number in the '
            'file name):'] + [os.path.abspath(c) for c in a.crops] + ['', f'Write your TSV to: {os.path.abspath(a.raw)}']
    with open(a.out, 'w') as f:
        f.write(base + rule_text(rd(a.cells)) + '\n\n' + '\n'.join(task) + '\n')
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


def cmd_consist(a):
    cells = {c['cell']: c for c in rd(a.cells)}
    wrong = None
    if a.wrong:
        wrong = {(r['line'], r['pos']) for r in rd(a.wrong)}
    n = {'right': [0, 0], 'wrong': [0, 0], 'all': [0, 0]}
    parsed = 0
    with open(a.out, 'w') as f:
        f.write('line\tpos\tsign\tn_written\tcontra\tfeatures_contradicted' + ('\twrong' if wrong is not None else '') + '\n')
        for r in rd(a.raw):
            line = f"{a.leaf}_{r['passage']}"
            w = parse_written(r.get('features', ''))
            parsed += len(w) == len(FEATS)
            c = cells.get(r['sign_id'])
            con = contradictions(w, c) if c else []
            flag = len(con) >= a.min_contra
            n['all'][0] += 1; n['all'][1] += flag
            row = f"{line}\t{r['pos']}\t{r['sign_id']}\t{len(w)}\t{len(con)}\t{','.join(con)}"
            if wrong is not None:
                k = 'wrong' if (line, r['pos']) in wrong else 'right'
                n[k][0] += 1; n[k][1] += flag
                row += f"\t{int(k == 'wrong')}"
            f.write(row + '\n')
    print(f"rows {n['all'][0]}; fully parsed features {parsed}; flagged (>= {a.min_contra} contradictions) {n['all'][1]}")
    if wrong is not None:
        for k in ('wrong', 'right'):
            t, fl = n[k]
            print(f"  {k}: {fl}/{t} flagged ({fl / t:.3f})" if t else f"  {k}: 0")
    return 0


# ---------- two-call protocol (TXE-M2) ----------
VOCAB_TEXT = [
    '- desc: ink below the main body of the sign, compared with the body\'s height (none: under a quarter; short: under '
    'three quarters; long: more).',
    '- asc: ink above the main body, same scale.',
    '- bars: long horizontal strokes running across most of the sign\'s width, 0, 1 or 2 (a flat loop top counts).',
    '- loops: closed loops (enclosed holes), 0, 1 or 2.',
    '- dots: separate small marks (dot, tick, accent) apart from the main stroke, 0, 1 or 2+.',
    '- lean: the sign\'s main axis tilts left, stands upright, or tilts right.',
    '- tail: the lowest part of the ink ends to the left or right of the sign\'s centre, or is centred (none).',
    '- conf: H (features clear), M (one feature uncertain), L (hard to see).']
FEAT_HEADER = 'passage\tpos\t' + '\t'.join(FEATS) + '\tconf\tnote'


def task1_text(crops=None, tiles=None, raw=''):
    L = ['# Feature read of hand-drawn signs (TXE-M2 call 1)', '',
         'You describe the SHAPE of every mark on the images named below, one row per mark. You are not asked what the '
         'marks are or mean, and you get no list of sign names. Read ONLY the images named below; do not open any other '
         'file in this repository. Write only the TSV named below.', '']
    if tiles:
        L += [f'The image: {os.path.abspath(tiles)}', '',
              'It shows numbered tiles, each holding one printed sign (the number is written above the tile). Write one '
              'row per tile: `passage` = TILES, `pos` = the tile number.', '']
    else:
        L += ['The images are horizontal segments of manuscript lines (a 16th-century cipher page; every mark is a cipher '
              'sign, upscaled 2x). Segments s1, s2, s3 of a line run left to right and overlap by about 100 px at the 2x '
              'scale (50 px native), so a sign that appears at the right edge of s1 and again at the left edge of s2 is ONE '
              'sign -- count it once, and continue the count across the segments. Small marks that look like punctuation '
              '("=", "+", a slash between two dots, "3", "2", a crossed or barred stroke, a lone "o") are signs too; take '
              'every mark as a sign unless it is clearly a pen slip. A sign\'s own dots or ticks belong to it.', '',
              '`passage` = the line id (L01, L02 ... from the file name), `pos` = 1-based position in the line, left to right.', '']
    L += ['Output: one TSV with this header and one row per sign:', '', '    ' + FEAT_HEADER, '',
          'Each feature column holds exactly one value from its vocabulary:', '',
          '    desc=none|short|long  asc=none|short|long  bars=0|1|2  loops=0|1|2  dots=0|1|2+  '
          'lean=left|upright|right  tail=none|left|right', ''] + VOCAB_TEXT + [
          '- note: a few words on the shape (optional).', '',
          'Look at the ink of each mark and write what you see. Do not name, classify or compare the marks with any sign '
          'list. When done, report in one short paragraph: rows per passage and how sure you were.', '']
    if crops:
        L += [f'The images ({len(crops)}, s1 s2 s3 of each line in order):'] + [os.path.abspath(c) for c in crops] + ['']
    L += [f'Write your TSV to: {os.path.abspath(raw)}']
    return '\n'.join(L) + '\n'


def cmd_task1(a):
    with open(a.out, 'w') as f:
        f.write(task1_text(a.crops, a.tiles, a.raw))
    print(a.out)
    return 0


def cmd_tiles(a):
    import random
    import numpy as np
    from PIL import Image, ImageDraw
    im = Image.open(a.sheet).convert('L')
    ids = sorted(c['id'] for c in json.load(open(a.ids_from)))
    order = list(range(len(ids)))
    random.Random(a.seed).shuffle(order)
    CW = CH = 110; NC = 9; S = 2; TW, TH = (CW - 4) * S, (CH - 27) * S + 30
    rows = (len(ids) + NC - 1) // NC
    out = Image.new('L', (NC * TW, rows * TH), 255)
    d = ImageDraw.Draw(out)
    with open(a.map, 'w') as m:
        m.write('tile\tcell\n')
        for t, n in enumerate(order, 1):
            gx, gy = (n % NC) * CW, (n // NC) * CH
            tile = im.crop((gx + 2, gy + 25, gx + CW - 2, gy + CH - 2)).resize(((CW - 4) * S, (CH - 27) * S))
            ox, oy = ((t - 1) % NC) * TW, ((t - 1) // NC) * TH
            out.paste(tile, (ox, oy + 30))
            d.text((ox + 6, oy + 6), str(t), fill=0)
            d.rectangle((ox, oy, ox + TW - 1, oy + TH - 1), outline=160)
            m.write(f'{t}\t{ids[n]}\n')
    out.save(a.out)
    print(f'{len(ids)} tiles -> {a.out}; map -> {a.map}')
    return 0


def varied(values, share=0.1):
    from collections import Counter
    c = Counter(values)
    return sum(1 for v in c.values() if v >= share * len(values)) >= 2


def cmd_comply(a):
    from collections import Counter
    rows = [r for p in a.raw1 for r in rd(p)]
    base = Counter(r['line'] for r in rd(a.base))
    got = Counter(f"{a.leaf}_{r['passage']}" for r in rows)
    ok_a = True
    print('(a) signs per line vs base (within 10%):')
    for ln in sorted(base):
        dev = abs(got.get(ln, 0) - base[ln]) / base[ln]
        ok_a &= dev <= 0.10
        print(f'    {ln} base {base[ln]} read {got.get(ln, 0)} dev {dev:.3f} {"ok" if dev <= 0.10 else "FAIL"}')
    cells = {c['cell']: c for c in rd(a.cells)}
    ok_b = True
    print('(b) feature variety (two values on >= 10% of rows; columns constant in the cell table exempt):')
    for k in FEATS:
        ref = varied([c[k] for c in cells.values()])
        vals = [norm_val(k, r.get(k, '')) for r in rows]
        v = varied(vals)
        if ref:
            ok_b &= v
        print(f'    {k}: {dict(Counter(vals))} {"ok" if v else ("FAIL" if ref else "exempt (constant in the cell table)")}')
    ok_c = True
    if a.control:
        mp = {r['tile']: r['cell'] for r in rd(a.map)}
        n = m1 = m0 = 0
        per = Counter()
        for r in rd(a.control):
            cell = cells.get(mp.get(r['pos'], ''))
            if not cell:
                continue
            w = {k: norm_val(k, r.get(k, '')) for k in FEATS}
            con = [k for k in FEATS if w[k] != cell[k]]
            n += 1; m1 += len(con) <= 1; m0 += not con
            for k in FEATS:
                per[k] += k not in con
        share = m1 / len(mp) if mp else 0
        ok_c = share >= 0.70
        print(f'(c) control: {n} of {len(mp)} tiles read; within one feature {m1} ({share:.3f}, gate 0.70) '
              f'{"ok" if ok_c else "FAIL"}; all seven {m0}')
        print('    per feature agreement: ' + ' '.join(f'{k} {per[k]}/{n}' for k in FEATS))
    ok = ok_a and ok_b and ok_c
    print(f'COMPLIANCE a {"ok" if ok_a else "FAIL"} b {"ok" if ok_b else "FAIL"} c {"ok" if ok_c else "FAIL"} -> '
          f'{"compliant" if ok else "non-test: no compliant feature read"}')
    return 0 if ok else 4


def norm_val(k, v):
    v = (v or '').strip().lower()
    if '=' in v:
        v = v.split('=', 1)[1]
    if k == 'dots' and v in ('2', '3', '2+'):
        return '2+'
    return v


def cmd_task2(a):
    feats = [r for p in a.feats for r in rd(p)]
    L = ['# Cell naming from your own feature read (TXE-M2 call 2)', '',
         'A first reader (who saw these crops but no sign sheet) wrote the features of every sign, one row per sign, '
         'below. Your job: for each row, name the cell of the sign sheet whose table features match the written '
         'features, checking the ink on the crop. Where no cell matches within one feature, write the nearest cell '
         '(fewest differing features, then the closest shape on the sheet) and put `mismatch` in the flag column. '
         'Keep the rows exactly as given: same passage, same pos, one output row per input row, none added or dropped.',
         '', 'Read ONLY the sheet, the crops named below and this file; do not open any other file in this repository. '
         'The pass is value-blind: you match shapes only; do not decode or guess at meanings.', '',
         'Output: one TSV with this header:', '', '    passage\tpos\tsign_id\talt\tconf\tflag\tnote', '',
         '- sign_id: a sheet cell (T##); `alt`: a second candidate or blank; conf H/M/L; flag: `mismatch` or blank.', '',
         'Cell features (measured by script on the printed sheet):', '',
         '| cell | ' + ' | '.join(FEATS) + ' |', '|' + '---|' * (len(FEATS) + 1)]
    for c in rd(a.cells):
        L.append(f"| {c['cell']} | " + ' | '.join(c[k] for k in FEATS) + ' |')
    L += ['', 'The written features (TSV):', '', '```', 'passage\tpos\t' + '\t'.join(FEATS)]
    for r in feats:
        L.append(f"{r['passage']}\t{r['pos']}\t" + '\t'.join(norm_val(k, r.get(k, '')) for k in FEATS))
    L += ['```', '', f'The sheet: {os.path.abspath(a.signsheet)}', '',
          f'The crops ({len(a.crops)}, s1 s2 s3 of each line in order):'] + [os.path.abspath(c) for c in a.crops]
    L += ['', f'Write your TSV to: {os.path.abspath(a.raw)}']
    with open(a.out, 'w') as f:
        f.write('\n'.join(L) + '\n')
    print(a.out)
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest='cmd', required=True)
    c = sp.add_parser('cells')
    c.add_argument('--sheet', required=True); c.add_argument('--ids-from', required=True); c.add_argument('--out', required=True)
    s = sp.add_parser('assemble')
    s.add_argument('--base', required=True); s.add_argument('--cells', required=True)
    s.add_argument('--signsheet', required=True); s.add_argument('--crops', nargs='+', required=True)
    s.add_argument('--raw', required=True); s.add_argument('--out', required=True)
    n = sp.add_parser('norm')
    n.add_argument('--raw', required=True); n.add_argument('--leaf', required=True); n.add_argument('--out', required=True)
    k = sp.add_parser('consist')
    k.add_argument('--raw', required=True); k.add_argument('--cells', required=True); k.add_argument('--leaf', default='f178v')
    k.add_argument('--wrong', default=''); k.add_argument('--min-contra', type=int, default=2)
    k.add_argument('--out', required=True)
    t = sp.add_parser('tiles')
    t.add_argument('--sheet', required=True); t.add_argument('--ids-from', required=True)
    t.add_argument('--seed', type=int, default=20261009); t.add_argument('--out', required=True); t.add_argument('--map', required=True)
    t1 = sp.add_parser('task1')
    t1.add_argument('--crops', nargs='*', default=None); t1.add_argument('--tiles', default=None)
    t1.add_argument('--raw', required=True); t1.add_argument('--out', required=True)
    co = sp.add_parser('comply')
    co.add_argument('--raw1', nargs='+', required=True); co.add_argument('--base', required=True)
    co.add_argument('--control', default=''); co.add_argument('--map', default='')
    co.add_argument('--cells', required=True); co.add_argument('--leaf', default='f178v')
    t2 = sp.add_parser('task2')
    t2.add_argument('--crops', nargs='+', required=True); t2.add_argument('--signsheet', required=True)
    t2.add_argument('--cells', required=True); t2.add_argument('--feats', nargs='+', required=True)
    t2.add_argument('--raw', required=True); t2.add_argument('--out', required=True)
    a = p.parse_args(argv)
    return {'cells': cmd_cells, 'assemble': cmd_assemble, 'norm': cmd_norm, 'consist': cmd_consist, 'tiles': cmd_tiles,
            'task1': cmd_task1, 'comply': cmd_comply, 'task2': cmd_task2}[a.cmd](a)


if __name__ == '__main__':
    sys.exit(main())
