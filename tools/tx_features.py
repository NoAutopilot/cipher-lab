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
    a = p.parse_args(argv)
    return {'cells': cmd_cells, 'assemble': cmd_assemble, 'norm': cmd_norm, 'consist': cmd_consist}[a.cmd](a)


if __name__ == '__main__':
    sys.exit(main())
