#!/usr/bin/env python3
"""VIV-HUMAN: sorter inputs for f.201r (PREREG-VIVHUMAN.md "The page"). Needs the crops on disk (images/manifest.json "vivcls"
regenerate commands; one openapi.bnf.fr request). Writes tx/sorter_human/{signs.tsv,labels.tsv,focus.tsv,cipher_lines.tsv} and
the untracked page image tx/sorter_human/pages/f201r.jpg (the region 680,1500,2970,3700 of the c206 native fetch; never committed).

Tiles: every VIV-CLS round-2 map tile with op 1:1 and one tile per passA token (tx/vivcls/real/map_r2_f201r.tsv); x and w from
tx/vivcls/map_signs.tsv (line x = source x); y and h from the ink rows of that column span in the sheared line crop, mapped back to the
region with the crop's own slope fit (region y = a + b*x - half + crop row). Pile label = the committed reconciliation's sign at the
truth row passA's token aligns to (truth ref_sign); question tiles (tx/vivhuman/questions.tsv) go to the neutral pile 'unsorted'.

--attempt 2 (PREREG-VIVHUMAN.md Addendum B, VIV-HUMAN2): question tiles = ATTEMPT2 only (shuffled, seed 20261014); the other attempt-1
question tiles go back to their committed piles; a tile labelled in FILTERED is kept only if its truth row is scored, unflagged and its
label lies in the row's truth set (others left out, counted); output tx/sorter_human2/ (focus.tsv in the shuffled order, filter.tsv).
"""
import csv, json, os, random, sys, collections
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
FOLD = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import sets  # noqa: E402
CUT = os.path.join(FOLD, 'images', 'p67', 'cut')
SRC = os.path.join(FOLD, 'images', 'p67', 'fetch', 'src_image_v3_ark_12148_btv1b9009663p_f206_4100_350_3650_5350.jpg')
RX, RY, RW, RH = 680, 1500, 2970, 3700
OUT = os.path.join(FOLD, 'tx', 'sorter_human')
QPILE = 'unsorted'
ATTEMPT2 = ['Q04', 'Q14', 'Q15', 'Q19', 'Q12', 'Q23', 'Q24', 'Q25']
FILTERED = {'3', 'z', 'L', 'l', 's', 'S', 'h', 'k'}
QUESTION = 'Which pile holds signs that look like this one? If none does, "None of these: new sign".'


def ink_rows(crop, x0, x1, thr=150):
    a = np.asarray(crop.convert('L'))[:, max(0, x0):max(x0 + 1, x1)]
    rows = (a < thr).sum(axis=1) > 0
    H, c = len(rows), len(rows) // 2
    if not rows.any():
        return c - 20, 40
    # the run of ink rows (gaps <= 4) nearest the strip centre
    idx = np.where(rows)[0]
    runs, s, p = [], idx[0], idx[0]
    for i in idx[1:]:
        if i - p > 4:
            runs.append((s, p)); s = i
        p = i
    runs.append((s, p))
    best = min(runs, key=lambda r: 0 if r[0] <= c <= r[1] else min(abs(r[0] - c), abs(r[1] - c)))
    y0, y1 = max(0, best[0] - 4), min(H - 1, best[1] + 4)
    return int(y0), int(y1 - y0 + 1)


def main(attempt=1):
    out = OUT if attempt == 1 else OUT + '2'
    man = {e['crop']: e for e in json.load(open(os.path.join(CUT, 'manifest.json')))['iiif_lines']}
    ms = {r['sid']: r for r in sets.rd(os.path.join(FOLD, 'tx', 'vivcls', 'map_signs.tsv'))}
    truth = sets.rd(sets.TRUTH)
    tl = collections.defaultdict(list)
    for r in truth:
        tl[r['line']].append(r)
    for ln in tl:
        tl[ln].sort(key=lambda r: float(r['pos']))
    pa = sets.rd(os.path.join(sets.OUTS, 'passA.tsv'))
    A = sets.aligned(tl, pa)                       # (line, tpos) -> (sign, apos)
    a2t = {(ln, ap): tp for (ln, tp), (sg, ap) in A.items()}
    ref = {(r['line'], r['pos']): r['ref_sign'] for r in truth}
    per = collections.defaultdict(list)
    for m in sets.rd(sets.MAP):
        if m['op'] == '1:1':
            per[(m['line'], m['pos'])].append(m['sid'])
    allq = sets.rd(os.path.join(HERE, 'questions.tsv'))
    q = {r['sid']: r for r in allq if not r['excluded'] and (attempt == 1 or r['qid'] in ATTEMPT2)}
    trow = {(r['line'], r['pos']): r for r in truth}
    filt = collections.defaultdict(collections.Counter)   # label -> before/after/out reason
    drop = {r['sid'] for r in allq if r['excluded']}
    os.makedirs(os.path.join(out, 'pages'), exist_ok=True)
    Image.open(SRC).crop((RX, RY, RX + RW, RY + RH)).save(os.path.join(out, 'pages', 'f201r.jpg'), quality=85)
    crops = {}
    signs, labels, skipped = [], [], collections.Counter()
    for (ln, ap), sids in sorted(per.items(), key=lambda kv: (kv[0][0], int(kv[0][1]))):
        if len(sids) != 1:
            skipped['two tiles on one token'] += 1; continue
        sid = sids[0]
        if sid in drop:
            skipped['excluded question tile (Addendum A)'] += 1; continue
        tp = a2t.get((ln, ap))
        if tp is None and sid not in q:
            skipped['passA token with no truth row'] += 1; continue
        m = ms[sid]
        cname = 'c206_' + m['crop_page'] + '.jpg'
        e = man[cname]
        if cname not in crops:
            crops[cname] = Image.open(os.path.join(CUT, cname))
        X, w = int(m['x']), int(m['w'])
        cy, h = ink_rows(crops[cname], X - e['box'][0], X - e['box'][0] + w)
        f = e['slope_fit']
        xr = X - RX
        yr = f['a'] + f['b'] * xr - f['half_height'] + cy
        signs.append(dict(sid=sid, page='f201r', x=xr, y=int(round(yr)), w=w, h=h))
        if sid in q:
            labels.append(dict(sid=sid, sign=QPILE, family='to place'))
        else:
            lab = ref[(ln, tp)]
            if attempt == 2 and lab in FILTERED:
                r = trow[(ln, tp)]
                filt[lab]['before'] += 1
                if r['status'] != 'scored' or r['flag']:
                    filt[lab]['out: row flagged or not scored'] += 1; signs.pop(); continue
                if lab not in set(filter(None, r['truth'].split('|'))):
                    filt[lab]['out: label not in truth set'] += 1; signs.pop(); continue
                filt[lab]['after'] += 1
            labels.append(dict(sid=sid, sign=lab, family='f201r'))
    missing = set(q) - {s['sid'] for s in signs}
    assert not missing, missing
    def w(name, cols, rows):
        with open(os.path.join(out, name), 'w') as fh:
            fh.write('\t'.join(cols) + '\n')
            for r in rows:
                fh.write('\t'.join(str(r[c]) for c in cols) + '\n')
    w('signs.tsv', ['sid', 'page', 'x', 'y', 'w', 'h'], signs)
    w('labels.tsv', ['sid', 'sign', 'family'], labels)
    with open(os.path.join(out, 'focus.tsv'), 'w') as fh:
        order = sorted(q.values(), key=lambda r: r['qid'])
        if attempt == 2:
            random.Random(sets.SEED).shuffle(order)
        for r in order:
            fh.write(f"{r['sid']}\t{r['qid']}: {QUESTION}\n")
    with open(os.path.join(out, 'cipher_lines.tsv'), 'w') as fh:
        fh.write('# f.201r cipher region (lines L01-L25 of the VIV-67 cut); the whole page image is cipher\nf201r\n')
    if attempt == 2:
        with open(os.path.join(out, 'filter.tsv'), 'w') as fh:
            fh.write('# PREREG-VIVHUMAN.md Addendum B pile filter (build_inputs.py --attempt 2)\nlabel\tbefore\tafter\tout_flagged_or_unscored\tout_not_in_truth\n')
            for lab in sorted(FILTERED):
                c = filt[lab]
                fh.write(f"{lab}\t{c['before']}\t{c['after']}\t{c['out: row flagged or not scored']}\t{c['out: label not in truth set']}\n")
        print({k: dict(v) for k, v in sorted(filt.items())})
    print('tiles', len(signs), 'question tiles', len(q), 'piles', len({l['sign'] for l in labels}), 'skipped', dict(skipped))


if __name__ == '__main__':
    main(attempt=int(sys.argv[sys.argv.index('--attempt') + 1]) if '--attempt' in sys.argv else 1)
