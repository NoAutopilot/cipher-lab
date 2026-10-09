#!/usr/bin/env python3
"""Contrast sweep before cutting: render each sign at five contrast levels, keep the strokes that persist, flag the signs
whose ink changes with contrast (TXE-I, LANE TX-ENGINEER round 2, 9 Oct 2026; owner's item 6, research/TX-IDEAS-2026-10-09.md
row O6; benchmark-tx/PREREG-txeng-2.md and its p < 0.01 amendment).

Lesson it answers (research/TX-TAXONOMY-2026-10-09.md classes 3 and 2b): on Birago no.87 half the mapped line-read errors sit
on thin strokes, and band-cut descenders hide the faint tail that separates d T18 from s T98. One rendering of a tile decides
for the reader which faint strokes exist. Here the same tile is shown at five contrasts; a script tracks which ink components
persist, which appear only at the hard end and which lose their identity there, and the sweep is logged as the cut's evidence.

Levels (the ladder is a set of grey thresholds; ink = grey < t_k). t_3 is the page's Otsu threshold; step = --step-frac x
(p95 - p5) of the page; t_k = Otsu + (k - 3) x step, so level 1 (soft) admits only dark ink and level 5 (hard) is the page
binarised at Otsu minus 2 steps on the ink-intensity scale (255 - grey), i.e. the most permissive cut. Rendering k (what a
reader sees) is a linear stretch whose window narrows from the page's p5-p95 (level 1) to a step at t_5 (level 5), centred
on t_k. Because the cuts are nested, ink only grows with level, so:
  STABLE     a component chain (IoU >= 0.5 to a component at the next level) present at >= 4 of the 5 levels;
  APPEARING  a chain present only at levels 4-5, OR new ink (>= --min-area px, outside a 1-px dilation of the level-3 ink)
             that attaches to a chain at the 3->4 or 4->5 step: the faint tail that exists only at high contrast;
  VANISHING  a chain present only at levels 1-2: a stroke seen apart at soft contrast that merges into another (a gap that
             closes, a speck that joins a stroke) at harder contrast -- the one a reader should not weigh.
A component belongs to the box it overlaps most among the page's atlas boxes; one that overlaps none belongs to the target
box when its centroid lies in the grown box and its x-centre inside the box's x-range (band-cut tails). uncertain =
n_appearing + n_vanishing >= 1. stable-ink box = bbox of the union of the box's stable components.

Subcommands
  sweep    --page P [--boxes SID,...|--lines f178v_L01,...] --levels 5: per box (grown --grow 0.5), the five renderings as
           one strip PNG (soft -> hard, left to right) under --strips (default: scratch, not committed) + manifest.json
           (page, otsu, step, p5, p95, the five thresholds and windows).
  stable   --page P: the per-box component table OUT/stable_<page>.tsv (sid, line, n_stable, n_appearing, n_vanishing,
           uncertain, atlas box, stable-ink box, dh, dw) and prints the share of boxes flagged and the share whose
           stable-ink box differs from the atlas box by > 10% in height or width.
  gate     --unit U: (opens truth through tools/tx_bench.position_errors; run only after the stable tables are committed)
           maps unit positions to boxes label-blind (tools/tx_compare.box_map: DP over box widths, no label), and prints
           precision/recall of `uncertain` against the line read's wrong positions and against pass A's; writes
           OUT/gate_<unit>.tsv and OUT/flags_<unit>.tsv (line, pos, sid, uncertain).
  sheet    --unit U: rows of the five-level strip for the flagged positions only (+ one neighbour each side at the middle
           level), <= 16 rows a sheet: OUT/<unit>/sheet_NN.png (to the reader) + sheet_NN.tsv (row -> line, pos; the key).
  resolve  --unit U: reads OUT/<unit>/reads_NN.tsv (row, sign_id, conf, strokes); a T## read replaces the line read at that
           position, X_NEW / ? keep it; writes --pass-out (line, pos, sign) for the unit lines.

Inputs, disk only: atlas signs.tsv and pages.json (the harvest src_*.jpg page images; box coordinates are in those images),
the line read benchmark-tx/outputs/birago1572-no87/labels.tsv. Never atlas/no87_box_token.tsv's truth column.
Offline test: tools/tests/test_tx_contrast_sweep.py (synthetic page, no network, no model).

Usage (repo root):
  python3 tools/tx_contrast_sweep.py sweep --page f178v
  python3 tools/tx_contrast_sweep.py stable --page f178v
  python3 tools/tx_contrast_sweep.py gate --unit dev_tune
"""
import argparse, csv, json, os, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import tx_compare as txc  # noqa: E402

T = 'ciphers/nevers-birago-fr3251-1572'
D = dict(atlas=f'{T}/atlas', line_read='benchmark-tx/outputs/birago1572-no87/labels.tsv',
         pass_a='benchmark-tx/txeng/units/passA_{unit}.tsv', units='benchmark-tx/txeng/units/README.md',
         out='benchmark-tx/txeng/sweep', bench='BENCHMARK-TX.tsv', item='birago1572-no87')


# ---------------------------------------------------------------- levels
def page_levels(g, levels=5, step_frac=0.06):
    import numpy as np
    from skimage.filters import threshold_otsu
    p5, p95 = (float(v) for v in np.percentile(g, [5, 95]))
    otsu = float(threshold_otsu(g))
    step = step_frac * (p95 - p5)
    mid = (levels - 1) / 2.0
    out = []
    for k in range(levels):
        t = otsu + (k - mid) * step
        half = (p95 - p5) / 2.0 * (1 - k / (levels - 1))     # window half-width: p5-p95 at level 1, a step at the last
        out.append(dict(level=k + 1, t=round(t, 2), lo=round(t - half, 2), hi=round(t + half, 2)))
    return dict(otsu=round(otsu, 2), step=round(step, 2), p5=p5, p95=p95, levels=out)


def render(tile, lv):
    import numpy as np
    lo, hi, t = lv['lo'], lv['hi'], lv['t']
    if hi - lo < 1:
        return np.where(tile < t, 0, 255).astype('uint8')
    return (np.clip((tile.astype(float) - lo) / (hi - lo), 0, 1) * 255).astype('uint8')


# ---------------------------------------------------------------- components
def grown(box, frac, W, H):
    x, y, w, h = box
    gx, gy = int(round(w * frac / 2)), int(round(h * frac / 2))
    return max(0, x - gx), max(0, y - gy), min(W, x + w + gx), min(H, y + h + gy)


def box_components(g, box, others, lv, grow=0.5, min_area=6):
    """Components (8-conn, >= min_area px) at one level that belong to `box` (x, y, w, h) on page `g`.
    -> list of (mask_in_region bool array, area); region = the grown box."""
    import numpy as np
    from scipy import ndimage
    H, W = g.shape
    x0, y0, x1, y1 = grown(box, grow, W, H)
    reg = g[y0:y1, x0:x1]
    ink = reg < lv['t']
    lab, n = ndimage.label(ink, structure=np.ones((3, 3)))
    bx, by, bw, bh = box
    out = []
    for i in range(1, n + 1):
        m = lab == i
        a = int(m.sum())
        if a < min_area:
            continue
        ys, xs = np.nonzero(m)
        def ov(b):
            ax0, ay0 = b[0] - x0, b[1] - y0
            return int(m[max(0, ay0):max(0, ay0 + b[3]), max(0, ax0):max(0, ax0 + b[2])].sum())
        own = ov(box)
        best_other = max((ov(o) for o in others), default=0)
        if own > 0:
            if own < best_other:
                continue
        else:
            if best_other > 0:
                continue
            cx = xs.mean() + x0
            if not (bx <= cx <= bx + bw):
                continue
        out.append((m, a))
    return out, (x0, y0, x1, y1)


def iou(a, b):
    inter = int((a & b).sum())
    return inter / float(int((a | b).sum()) or 1)


def analyse(comps, min_area=6, iou_min=0.5):
    """comps: per level, list of (mask, area). -> dict n_stable, n_appearing, n_vanishing, stable_mask (or None)."""
    import numpy as np
    from scipy import ndimage
    L = len(comps)
    chain_of = [[None] * len(c) for c in comps]
    chains = []
    for k in range(L):
        for i, (m, _) in enumerate(comps[k]):
            if chain_of[k][i] is None:
                chain_of[k][i] = len(chains); chains.append({k})
            if k + 1 < L:
                best, bj = 0.0, None
                for j, (m2, _) in enumerate(comps[k + 1]):
                    v = iou(m, m2)
                    if v > best:
                        best, bj = v, j
                if bj is not None and best >= iou_min and chain_of[k + 1][bj] is None:
                    chain_of[k + 1][bj] = chain_of[k][i]; chains[chain_of[k][i]].add(k + 1)
    hard = {L - 2, L - 1}; soft = {0, 1}
    n_st = sum(1 for c in chains if len(c) >= L - 1)
    n_ap = sum(1 for c in chains if c <= hard)
    n_va = sum(1 for c in chains if c <= soft)
    # new ink attached to a continuing chain at the two hard steps (tails that exist only at high contrast)
    for k in (L - 3, L - 2):
        if k < 0:
            continue
        base = np.zeros_like(comps[k][0][0]) if comps[k] else None
        if base is None:
            continue
        for m, _ in comps[k]:
            base |= m
        base = ndimage.binary_dilation(base, structure=np.ones((3, 3)))
        for j, (m2, _) in enumerate(comps[k + 1]):
            ch = chain_of[k + 1][j]
            if ch is None or min(chains[ch]) > k:      # a chain born here is already counted above
                continue
            new = m2 & ~base
            lab, n = ndimage.label(new, structure=np.ones((3, 3)))
            n_ap += sum(1 for i in range(1, n + 1) if int((lab == i).sum()) >= min_area)
    stable, mid = None, L // 2                     # stable ink = the stable chains' components at the middle level
    for i, (m, _) in enumerate(comps[mid]):
        if len(chains[chain_of[mid][i]]) >= L - 1:
            stable = m.copy() if stable is None else (stable | m)
    return dict(n_stable=n_st, n_appearing=n_ap, n_vanishing=n_va, stable_mask=stable)


def bbox(mask, origin):
    import numpy as np
    ys, xs = np.nonzero(mask)
    if not len(xs):
        return None
    return (int(xs.min()) + origin[0], int(ys.min()) + origin[1], int(xs.max() - xs.min() + 1), int(ys.max() - ys.min() + 1))


def box_row(g, s, others, lvls, grow, min_area):
    box = txc.xywh(s)
    comps, reg = [], None
    for lv in lvls['levels']:
        c, reg = box_components(g, box, others, lv, grow, min_area)
        comps.append(c)
    if not any(comps):
        return dict(n_stable=0, n_appearing=0, n_vanishing=0, uncertain=0, stable_box='', dh='', dw=''), reg
    r = analyse(comps, min_area)
    sb = bbox(r['stable_mask'], reg[:2]) if r['stable_mask'] is not None else None
    dh = round(sb[3] / box[3] - 1, 3) if sb else ''
    dw = round(sb[2] / box[2] - 1, 3) if sb else ''
    return dict(n_stable=r['n_stable'], n_appearing=r['n_appearing'], n_vanishing=r['n_vanishing'],
                uncertain=int(r['n_appearing'] + r['n_vanishing'] >= 1),
                stable_box=','.join(map(str, sb)) if sb else '', dh=dh, dw=dw), reg


# ---------------------------------------------------------------- io helpers
def load_page(a, page):
    import numpy as np
    im = txc.Pages(a.atlas).get(page)
    if im is None:
        sys.exit(f'no image for page {page}')
    return np.asarray(im)


def page_signs(a, page):
    return [s for s in txc.rd(os.path.join(txc.path(a.atlas), 'signs.tsv')) if s['page'] == page]


def neighbours(signs, s, pad=200):
    x, y, w, h = txc.xywh(s)
    return [txc.xywh(o) for o in signs if o['sid'] != s['sid'] and abs(int(o['x']) - x) < pad + w
            and abs(int(o['y']) - y) < pad + h]


def select(signs, a):
    if getattr(a, 'boxes', None):
        want = set(a.boxes.split(','))
        return [s for s in signs if s['sid'] in want]
    if getattr(a, 'lines', None):
        want = {int(txc.split_line(l)[1]) for l in a.lines.split(',')}
        return [s for s in signs if int(s['line']) in want]
    return signs


def strip_image(g, s, lvls, grow, scale=2):
    from PIL import Image
    H, W = g.shape
    x0, y0, x1, y1 = grown(txc.xywh(s), grow, W, H)
    tile = g[y0:y1, x0:x1]
    ims = [Image.fromarray(render(tile, lv)) for lv in lvls['levels']]
    tw, th = (x1 - x0) * scale, (y1 - y0) * scale
    out = Image.new('L', (len(ims) * (tw + 6) - 6, th), 255)
    for i, im in enumerate(ims):
        out.paste(im.resize((tw, th)), (i * (tw + 6), 0))
    return out


# ---------------------------------------------------------------- commands
def cmd_sweep(a):
    g = load_page(a, a.page)
    lv = page_levels(g, a.levels, a.step_frac)
    signs = select(page_signs(a, a.page), a)
    os.makedirs(a.strips, exist_ok=True)
    for s in signs:
        strip_image(g, s, lv, a.grow).save(os.path.join(a.strips, f"{s['sid']}.png"))
    man = dict(page=a.page, grow=a.grow, min_area=a.min_area, step_frac=a.step_frac, n_boxes=len(signs),
               strips=os.path.relpath(a.strips, ROOT) if a.strips.startswith(ROOT) else a.strips, **lv)
    os.makedirs(a.out, exist_ok=True)
    json.dump(man, open(os.path.join(a.out, f'manifest_{a.page}.json'), 'w'), indent=1)
    print(f'sweep {a.page}: {len(signs)} strips -> {a.strips}; otsu {lv["otsu"]} step {lv["step"]} thresholds '
          f'{[l["t"] for l in lv["levels"]]}')


def cmd_stable(a):
    g = load_page(a, a.page)
    lv = page_levels(g, a.levels, a.step_frac)
    allsigns = page_signs(a, a.page)
    signs = select(allsigns, a)
    rows = []
    for s in signs:
        r, _ = box_row(g, s, neighbours(allsigns, s), lv, a.grow, a.min_area)
        rows.append(dict(sid=s['sid'], line=s['line'], box=','.join(s[k] for k in 'xywh'), **r))
    cols = ['sid', 'line', 'n_stable', 'n_appearing', 'n_vanishing', 'uncertain', 'box', 'stable_box', 'dh', 'dw']
    txc.wr(os.path.join(a.out, f'stable_{a.page}.tsv'), cols, rows)
    n = len(rows) or 1
    fl = sum(r['uncertain'] for r in rows)
    ch = sum(1 for r in rows if r['dh'] != '' and (abs(r['dh']) > 0.1 or abs(r['dw']) > 0.1))
    print(f'stable {a.page}: {len(rows)} boxes; flagged uncertain {fl} ({fl / n:.1%}); stable-ink box differs > 10% in h or '
          f'w {ch} ({ch / n:.1%}); appearing>0 {sum(1 for r in rows if r["n_appearing"])}, vanishing>0 '
          f'{sum(1 for r in rows if r["n_vanishing"])}')
    return rows


def flags_for(a, unit):
    lines = txc.unit_lines(a.units, unit)
    signs = txc.rd(os.path.join(txc.path(a.atlas), 'signs.tsv'))
    L = txc.rd(txc.path(a.line_read))
    bp = txc.box_map(signs, L, lines)
    st = {}
    for page in {txc.split_line(l)[0] for l in lines}:
        p = os.path.join(a.out, f'stable_{page}.tsv')
        if not os.path.exists(p):
            sys.exit(f'run stable --page {page} first ({p} missing)')
        st.update({r['sid']: r for r in txc.rd(p)})
    rows = []
    for r in bp:
        sids = [x for x in r['sid'].split('+') if x]
        u = int(any(st.get(x, {}).get('uncertain') == '1' for x in sids))
        rows.append(dict(line=r['line'], pos=r['pos'], sid=r['sid'], op=r['op'], uncertain=u))
    return rows, lines, L


def cmd_gate(a):
    import tx_bench
    rows, lines, L = flags_for(a, a.unit)
    txc.wr(os.path.join(a.out, f'flags_{a.unit}.tsv'), ['line', 'pos', 'sid', 'op', 'uncertain'], rows)
    flag = {(r['line'], r['pos']): r['uncertain'] for r in rows}
    bench_base = os.path.dirname(os.path.abspath(txc.path(a.bench)))
    item = [r for r in tx_bench.read_tsv(txc.path(a.bench)) if r['item'] == a.item][0]
    truth = tx_bench.read_tsv(os.path.join(bench_base, item['truth']))
    truth = [r for r in truth if r['line'] in lines]
    out = []
    for name, p in (('L', a.line_read), ('passA', a.pass_a.format(unit=a.unit))):
        ol = tx_bench.load_output([txc.path(p)])
        ol = {k: v for k, v in ol.items() if k in lines}
        errs = tx_bench.position_errors(truth, ol)
        n = len(errs); wrong = [k for k, v in errs.items() if v]
        # the benchmark's (line, pos) keys are the line read's own (its ref_sign column is the line read): flag keys apply
        fl = [k for k in errs if flag.get(k, 0)]
        hit = [k for k in wrong if flag.get(k, 0)]
        rec = len(hit) / len(wrong) if wrong else float('nan')
        prec = len(hit) / len(fl) if fl else float('nan')
        out.append(dict(unit=a.unit, against=name, scored=n, wrong=len(wrong), flagged=len(fl),
                        flagged_share=round(len(fl) / n, 3) if n else '', wrong_flagged=len(hit),
                        recall=round(rec, 3), precision=round(prec, 3),
                        gate='MET' if wrong and rec >= 0.5 and len(fl) / n <= 0.2 else 'not met'))
    txc.wr(os.path.join(a.out, f'gate_{a.unit}.tsv'), list(out[0]), out)
    for r in out:
        print('gate %(unit)s vs %(against)s: scored %(scored)d, wrong %(wrong)d; flagged %(flagged)d (%(flagged_share)s); '
              'wrong flagged %(wrong_flagged)d -> recall %(recall)s precision %(precision)s; registered gate (recall >= 0.5 '
              'at <= 20%% flagged, vs L): %(gate)s' % r)
    return out


def cmd_sheet(a):
    from PIL import Image, ImageDraw
    rows = [r for r in txc.rd(os.path.join(a.out, f'flags_{a.unit}.tsv')) if r['uncertain'] == '1' and r['sid']]
    signs = {s['sid']: s for s in txc.rd(os.path.join(txc.path(a.atlas), 'signs.tsv'))}
    pages = {}
    od = os.path.join(a.out, a.unit); os.makedirs(od, exist_ok=True)
    built = []
    for si in range(0, len(rows), a.rows):
        chunk = rows[si:si + a.rows]
        tiles, key = [], []
        for ri, r in enumerate(chunk, 1):
            sids = r['sid'].split('+')
            s = dict(signs[sids[0]])
            if len(sids) > 1:
                bs = [txc.xywh(signs[x]) for x in sids]
                x0, y0 = min(b[0] for b in bs), min(b[1] for b in bs)
                s.update(x=x0, y=y0, w=max(b[0] + b[2] for b in bs) - x0, h=max(b[1] + b[3] for b in bs) - y0)
            page = s['page']
            if page not in pages:
                pages[page] = (load_page(a, page), page_levels(load_page(a, page), a.levels, a.step_frac))
            g, lv = pages[page]
            strip = strip_image(g, s, lv, a.grow)
            ctx = context_mid(g, signs, sids, lv, a.grow)
            tiles.append((ri, ctx, strip)); key.append(dict(row=ri, line=r['line'], pos=r['pos'], sid=r['sid']))
        th = 150
        ims = []
        for ri, ctx, strip in tiles:
            c = ctx.resize((max(1, int(ctx.width * th / ctx.height)), th))
            sw = strip.resize((max(1, int(strip.width * th / strip.height)), th))
            ims.append((ri, c, sw))
        W = 60 + max(c.width for _, c, _ in ims) + 30 + max(s.width for _, _, s in ims) + 10
        Hh = len(ims) * (th + 12) + 10
        sheet = Image.new('L', (W, Hh), 255); d = ImageDraw.Draw(sheet)
        cw = max(c.width for _, c, _ in ims)
        for i, (ri, c, sw) in enumerate(ims):
            y = 10 + i * (th + 12)
            d.text((8, y + th // 2 - 14), str(ri), fill=0, font=txc.font(28))
            sheet.paste(c, (60, y)); sheet.paste(sw, (60 + cw + 30, y))
            d.line([(0, y + th + 6), (W, y + th + 6)], fill=180)
        n = si // a.rows + 1
        sheet.save(os.path.join(od, f'sheet_{n:02d}.png'))
        txc.wr(os.path.join(od, f'sheet_{n:02d}.tsv'), ['row', 'line', 'pos', 'sid'], key)
        built.append(n)
    print(f'sheet {a.unit}: {len(rows)} flagged positions on {len(built)} sheets -> {od}')


def context_mid(g, signs, sids, lvls, grow):
    """The middle-level rendering of the sign with one neighbour each side (same line), target outlined."""
    from PIL import Image, ImageDraw
    s0 = signs[sids[0]]
    same = sorted([s for s in signs.values() if s['page'] == s0['page'] and s['line'] == s0['line']], key=lambda s: int(s['x']))
    idx = [i for i, s in enumerate(same) if s['sid'] in sids]
    grp = same[max(0, min(idx) - 1):max(idx) + 2]
    bs = [txc.xywh(s) for s in grp]
    x0, y0 = min(b[0] for b in bs), min(b[1] for b in bs)
    box = (x0, y0, max(b[0] + b[2] for b in bs) - x0, max(b[1] + b[3] for b in bs) - y0)
    H, W = g.shape
    gx0, gy0, gx1, gy1 = grown(box, grow * 0.5, W, H)
    im = Image.fromarray(render(g[gy0:gy1, gx0:gx1], lvls['levels'][len(lvls['levels']) // 2])).convert('L')
    d = ImageDraw.Draw(im)
    for s in grp:
        if s['sid'] in sids:
            x, y, w, h = txc.xywh(s)
            d.rectangle([x - gx0 - 2, y - gy0 - 2, x - gx0 + w + 2, y - gy0 + h + 2], outline=0, width=2)
    return im


def cmd_resolve(a):
    lines = txc.unit_lines(a.units, a.unit)
    L = [r for r in txc.rd(txc.path(a.line_read)) if r['line'] in lines]
    od = os.path.join(a.out, a.unit)
    new, stats = {}, Counter()
    for fn in sorted(os.listdir(od)):
        if not (fn.startswith('reads_') and fn.endswith('.tsv')):
            continue
        key = {r['row']: r for r in txc.rd(os.path.join(od, 'sheet_' + fn[6:]))}
        for r in txc.rd(os.path.join(od, fn)):
            k = key.get(str(r['row']).strip())
            sid = (r.get('sign_id') or '').strip()
            if not k:
                continue
            if sid.startswith('T') and sid[1:].isdigit():
                new[(k['line'], k['pos'])] = sid; stats['read'] += 1
            else:
                stats['kept'] += 1
    out = []
    for r in L:
        s = new.get((r['line'], r['pos']), r['sign'])
        stats['changed'] += int(s != r['sign'])
        out.append(dict(line=r['line'], pos=r['pos'], sign=s))
    txc.wr(a.pass_out, ['line', 'pos', 'sign'], out)
    print(f'resolve {a.unit}: {dict(stats)} -> {a.pass_out}')


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0], epilog=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)

    def common(p):
        p.add_argument('--atlas', default=D['atlas'])
        p.add_argument('--line-read', default=D['line_read'])
        p.add_argument('--units', default=D['units'])
        p.add_argument('--out', default=os.path.join(ROOT, D['out']))
        p.add_argument('--levels', type=int, default=5)
        p.add_argument('--step-frac', type=float, default=0.03)
        p.add_argument('--grow', type=float, default=0.5)
        p.add_argument('--min-area', type=int, default=20)
        return p
    for name in ('sweep', 'stable'):
        p = common(sub.add_parser(name))
        p.add_argument('--page', required=True)
        p.add_argument('--boxes'); p.add_argument('--lines')
        if name == 'sweep':
            p.add_argument('--strips', default='/tmp/tx_contrast_sweep_strips')
    p = common(sub.add_parser('gate')); p.add_argument('--unit', required=True)
    p.add_argument('--pass-a', default=D['pass_a']); p.add_argument('--bench', default=D['bench'])
    p.add_argument('--item', default=D['item'])
    p = common(sub.add_parser('sheet')); p.add_argument('--unit', required=True); p.add_argument('--rows', type=int, default=16)
    p = common(sub.add_parser('resolve')); p.add_argument('--unit', required=True); p.add_argument('--pass-out', required=True)
    a = ap.parse_args(argv)
    return {'sweep': cmd_sweep, 'stable': cmd_stable, 'gate': cmd_gate, 'sheet': cmd_sheet,
            'resolve': cmd_resolve}[a.cmd](a) and 0


if __name__ == '__main__':
    sys.exit(main())
