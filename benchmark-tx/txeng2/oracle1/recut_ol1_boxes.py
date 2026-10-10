#!/usr/bin/env python3
"""OL1-PAGE amended (PREREG-txeng2-21 "OL1-PAGE amended", TXE2-OL1PAGE, 10 Oct 2026): re-cut the committed OL1-BOXES proposals
by the declared, read-free, per-hand geometric rules, and write the sorter inputs for the box-verify page.

READ-FREE: the only inputs are boxes/boxes_all.tsv (the committed proposals) and the crop images. No reader, truth, key,
decode, pass output or label. The piles are the machine's cut kind only (`sign box`, and `mark box` for a mark left alone).

Rules, in the PREREG's order; all medians per hand over the hand's kind=sign boxes (the committed proposals):
 ink     ink ratio of a box = share of its pixels darker than the crop's Otsu threshold, measured on the crop autocontrasted
         (cutoff 1%) as tools/sign_sorter.py embeds it -- the same measure tools/sorter_preflight.py check 3 uses.
 (1) over-wide: a sign box wider than 2.5 x the hand median width is split into k = round(w / median) boxes at the k-1
         deepest valleys of its column ink profile (profile smoothed over 3 columns; valleys taken deepest first, each at
         least 0.5 x median from the box edges and from each other); each piece keeps the box's y and h.
 (2) strip-height: a box touching both the top (y <= 1) and bottom (y + h >= H - 1) edge of its crop is trimmed to the rows
         of its own ink inside the crop's core band (5th to 95th percentile rows of the crop's ink row profile); still
         touching both edges, or no ink in the band -> dropped as a neighbour-line intrusion and listed.
 (3) ink outliers: a sign box under 3% ink is dropped (blank or speck); a sign box over 60% ink is padded 2 px a side and
         re-measured (kept either way; a residual is reported by the plain preflight).
 marks   a kind=mark box is not a tile: it is attached (marks.tsv, the sorter's --marks) to the sign box on the same crop it
         overlaps most in x, else the sign whose centre is nearest in x within one hand median width; a mark with no sign in
         reach stays its own box in the `mark box` pile and is listed.
Every change is a row of boxes/boxes_recut.tsv (box_id, rule, from, to; boxes as x,y,w,h in crop pixels). Focus = every box
a rule changed (split piece, trimmed, padded, mark-attached union) with a geometric note only.

  python3 benchmark-tx/txeng2/oracle1/recut_ol1_boxes.py
Writes boxes/boxes_recut.tsv, boxes/boxes_recut_all.tsv, sorter/{signs,labels,marks,focus}.tsv (pages.json and
cipher_lines.tsv are OL1-BOXES's, unchanged)."""
import csv, os, statistics
from collections import defaultdict
import numpy as np
from PIL import Image, ImageOps

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
O = os.path.join(ROOT, 'benchmark-tx/txeng2/oracle1')
WIDE, INK_LO, INK_HI = 2.5, 0.03, 0.60


def otsu(a):
    hist = np.bincount(a.ravel(), minlength=256).astype(float)
    tot, sm = hist.sum(), (np.arange(256) * hist).sum()
    wb = sb = 0.0; best, t = -1, 128
    for i in range(256):
        wb += hist[i]
        if wb == 0: continue
        wf = tot - wb
        if wf == 0: break
        sb += i * hist[i]
        v = wb * wf * (sb / wb - (sm - sb) / wf) ** 2
        if v > best: best, t = v, i
    return t + 1


class Crop:
    def __init__(self, path):
        g = np.asarray(ImageOps.autocontrast(Image.open(os.path.join(ROOT, path)).convert('L'), cutoff=1))
        self.H, self.W = g.shape
        self.ink = g < otsu(g)
        rows = self.ink.sum(1).astype(float); c = np.cumsum(rows) / max(1.0, rows.sum())
        self.band = (int(np.searchsorted(c, 0.05)), int(np.searchsorted(c, 0.95)))

    def ratio(self, x, y, w, h):
        p = self.ink[max(0, y):max(0, y) + max(1, h), max(0, x):max(0, x) + max(1, w)]
        return float(p.mean()) if p.size else 0.0


def split(cr, b, med):
    x, y, w, h = b
    k = max(2, round(w / med))
    prof = cr.ink[y:y + h, x:x + w].sum(0).astype(float)
    prof = np.convolve(prof, np.ones(3) / 3, mode='same')
    margin = int(0.5 * med)
    cuts = []
    for c in np.argsort(prof, kind='stable'):
        if len(cuts) == k - 1: break
        if c < margin or c > w - margin or any(abs(c - d) < margin for d in cuts): continue
        cuts.append(int(c))
    edges = [0] + sorted(cuts) + [w]
    return [(x + a, y, b2 - a, h) for a, b2 in zip(edges, edges[1:]) if b2 > a]


def fmt(b):
    return ','.join(map(str, b))


def main():
    rows = list(csv.DictReader(open(os.path.join(O, 'boxes/boxes_all.tsv')), delimiter='\t'))
    crops = {}
    def C(p):
        if p not in crops: crops[p] = Crop(p)
        return crops[p]
    med = {h: statistics.median(int(r['w']) for r in rows if r['hand'] == h and r['kind'] == 'sign') for h in {r['hand'] for r in rows}}
    log, notes, out, marks_in = [], defaultdict(list), [], []
    for r in rows:
        b = tuple(int(r[k]) for k in ('x', 'y', 'w', 'h'))
        if r['kind'] == 'mark':
            marks_in.append((r, b)); continue
        cr, m = C(r['crop']), med[r['hand']]
        pieces = [(r['box_id'], b)]
        if b[2] > WIDE * m:   # (1)
            ps = split(cr, b, m)
            pieces = [(f"{r['box_id']}{chr(97 + i)}", p) for i, p in enumerate(ps)]
            for pid, p in pieces:
                log.append((pid, 'split-over-wide', fmt(b), fmt(p))); notes[pid].append(f'split from a box {b[2] / m:.1f}x the median width of its hand')
        for pid, p in pieces:
            x, y, w, h = p
            if y <= 1 and y + h >= cr.H - 1:   # (2)
                lo, hi = cr.band
                sub = cr.ink[lo:hi + 1, x:x + w].any(1)
                if not sub.any():
                    log.append((pid, 'strip-height-dropped', fmt(p), '-')); continue
                ys = np.nonzero(sub)[0]; q = (x, lo + int(ys[0]), w, int(ys[-1] - ys[0]) + 1)
                if q[1] <= 1 and q[1] + q[3] >= cr.H - 1:
                    log.append((pid, 'strip-height-dropped', fmt(p), '-')); continue
                log.append((pid, 'strip-height-trimmed', fmt(p), fmt(q))); notes[pid].append('trimmed: it touched both strip edges'); p = q
            ir = cr.ratio(*p)   # (3)
            if ir < INK_LO:
                log.append((pid, 'ink-under-3-dropped', fmt(p), '-')); continue
            if ir > INK_HI:
                x, y, w, h = p; q = (max(0, x - 2), max(0, y - 2), w + 4, h + 4)
                log.append((pid, 'ink-over-60-padded', fmt(p), fmt(q))); notes[pid].append('padded: ink over 60% of the box'); p = q
            out.append({'box_id': pid, 'hand': r['hand'], 'line': r['line'], 'crop': r['crop'], 'b': p, 'kind': 'sign'})
    by_crop = defaultdict(list)
    for o in out: by_crop[o['crop']].append(o)
    attached, alone = [], []
    for r, b in marks_in:
        x, y, w, h = b; m = med[r['hand']]; best = None
        ov = [(min(x + w, o['b'][0] + o['b'][2]) - max(x, o['b'][0]), o) for o in by_crop[r['crop']]]
        ov = [t for t in ov if t[0] > 0]
        if ov: best = max(ov, key=lambda t: t[0])[1]
        else:
            cx = x + w / 2; near = [(abs(o['b'][0] + o['b'][2] / 2 - cx), o) for o in by_crop[r['crop']]]
            near = [t for t in near if t[0] <= m]
            if near: best = min(near, key=lambda t: t[0])[1]
        if best:
            attached.append((r['box_id'], best['box_id'], b)); log.append((r['box_id'], 'mark-attached', fmt(b), best['box_id']))
            if 'mark attached: the tile is cut around the sign and its detached mark' not in notes[best['box_id']]:
                notes[best['box_id']].append('mark attached: the tile is cut around the sign and its detached mark')
        else:
            alone.append(r['box_id']); log.append((r['box_id'], 'mark-alone', fmt(b), fmt(b)))
            out.append({'box_id': r['box_id'], 'hand': r['hand'], 'line': r['line'], 'crop': r['crop'], 'b': b, 'kind': 'mark'})
    page = lambda c: os.path.basename(c)[:-4]
    order = {r['box_id']: i for i, r in enumerate(rows)}
    out.sort(key=lambda o: (order.get(o['box_id'], order.get(o['box_id'][:-1], 0)), o['box_id']))
    W = lambda p, rs, cols: (open(p, 'w').write('\t'.join(cols) + '\n' + ''.join('\t'.join(map(str, q)) + '\n' for q in rs)))
    W(os.path.join(O, 'boxes/boxes_recut.tsv'), log, ['box_id', 'rule', 'from', 'to'])
    W(os.path.join(O, 'boxes/boxes_recut_all.tsv'), [(o['box_id'], o['hand'], o['line'], o['crop'], *o['b'], o['kind']) for o in out],
      ['box_id', 'hand', 'line', 'crop', 'x', 'y', 'w', 'h', 'kind'])
    sd = os.path.join(O, 'sorter')
    W(os.path.join(sd, 'signs.tsv'), [(o['box_id'], page(o['crop']), *o['b']) for o in out], ['sid', 'page', 'x', 'y', 'w', 'h'])
    W(os.path.join(sd, 'labels.tsv'), [(o['box_id'], f"{o['kind']} box", f"{o['kind']} box") for o in out], ['sid', 'sign', 'family'])
    W(os.path.join(sd, 'marks.tsv'), [(*b, sid, 'mark', mid) for mid, sid, b in attached], ['x', 'y', 'w', 'h', 'sid', 'kind', 'mark_id'])
    W(os.path.join(sd, 'focus.tsv'), [(o['box_id'], '; '.join(notes[o['box_id']]) + '. Accept the cut, or fix it.') for o in out if notes[o['box_id']]],
      ['sid', 'question'])
    cnt = defaultdict(lambda: defaultdict(int))
    hand_of = {r['box_id']: r['hand'] for r in rows}
    for q in log:
        bid = q[0] if q[0] in hand_of else q[0][:-1]
        cnt[q[1]][hand_of.get(bid, '?')] += 1
    print('hand medians (sign width px):', {h: med[h] for h in sorted(med)})
    for rule in sorted(cnt): print(rule, dict(cnt[rule]))
    print('tiles', len(out), 'signs', sum(o['kind'] == 'sign' for o in out), 'marks alone', len(alone), 'focus', sum(1 for o in out if notes[o['box_id']]))


if __name__ == '__main__':
    main()
