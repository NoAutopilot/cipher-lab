#!/usr/bin/env python3
"""BOXCLIP scorer (account 3, 12 Oct 2026). Runs the FROZEN tools/box_clip_check.py once over every machine box of the two
labelled sorter pages and scores it against the owner's behaviour. Script only: no model, no network, no vision.
Pre-registration: benchmark-tx/boxclip/PREREG-BOXCLIP.md (committed before this was run).

  python3 benchmark-tx/boxclip/run_boxclip.py            writes scores.tsv and RESULTS.md (the test, once)
  python3 benchmark-tx/boxclip/run_boxclip.py --sensitivity   appends the "sensitivity (not the test)" section to RESULTS.md
  python3 benchmark-tx/boxclip/run_boxclip.py --check    recomputes and exits 1 if scores.tsv is stale (rule 7)

Labels (counts printed in RESULTS.md):
  positive = a box the owner re-cut (Modena recuts.tsv, 21; Matignon owner_db_2026-10-12_partial/recuts/*.json, 22);
  negative = a box the owner looked at and did not re-cut (Modena: the other tiles of the 31-tile page; Matignon: tiles with
             a doc in owner_db_2026-10-12_partial/checked/ and no recut doc).
  Boxes with no label are never scored; they are given to the tool only because its neighbour rule needs every box of a page.
The owner's boxes are read here, for IoU only, never by the method.
"""
import argparse
import base64
import csv
import glob
import hashlib
import io
import json
import os
import re
import sys
import time

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import box_clip_check as BC  # noqa: E402

MOD = os.path.join(ROOT, 'ciphers/decode-1162-modena-ambung-1492/sorter')
MAT = os.path.join(ROOT, 'ciphers/matignon-mayenne-1586/sorter')
GATE = dict(recall=0.70, fa=0.30, ba_margin=0.10, p=0.05, iou_gain=0.15)
N_PERM, SEED = 10000, 20261012


def rd(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def modena_pages():
    s = open(os.path.join(MOD, 'modena-gq-sorter.html')).read()
    i = s.find('"pages": {'); start = s.find('{', i); depth = 0
    for p in range(start, len(s)):
        depth += (s[p] == '{') - (s[p] == '}')
        if depth == 0:
            end = p + 1; break
    pages = json.loads(s[start:end])
    return {k: np.asarray(Image.open(io.BytesIO(base64.b64decode(v))).convert('L')) for k, v in pages.items()}


def load():
    """-> sorters: {name: dict(rows=all machine boxes, images, scale, labels=[...])}"""
    out = {}
    rows = rd(os.path.join(MOD, 'signs.tsv'))
    rec = {r['tile']: r for r in rd(os.path.join(MOD, 'recuts.tsv'))}
    lab = []
    for r in rows:
        k = r['sid']
        if k in rec:
            o = rec[k]
            lab.append(dict(sid=k, label=1, owner=tuple(int(o['new_' + c]) for c in 'xywh')))
        else:
            lab.append(dict(sid=k, label=0, owner=None))
    out['modena'] = dict(rows=rows, images=modena_pages(), scale=0.5, labels=lab)
    rows = rd(os.path.join(MAT, 'signs.tsv'))
    d = os.path.join(MAT, 'owner_db_2026-10-12_partial')
    rec = {}
    for f in sorted(glob.glob(os.path.join(d, 'recuts/*.json'))):
        j = json.load(open(f)); rec[j['sid']] = j
    chk = {json.load(open(f))['sid'] for f in sorted(glob.glob(os.path.join(d, 'checked/*.json')))}
    known = {r['sid'] for r in rows}
    assert set(rec) <= known and chk <= known
    lab = [dict(sid=k, label=1, owner=tuple(int(rec[k][c]) for c in 'xywh')) for k in sorted(rec)]
    lab += [dict(sid=k, label=0, owner=None) for k in sorted(chk - set(rec))]
    imgs = {p: np.asarray(Image.open(os.path.join(MAT, 'pages', p + '.jpg')).convert('L'))
            for p in sorted({r['page'] for r in rows})}
    out['matignon'] = dict(rows=rows, images=imgs, scale=1.0, labels=lab)
    return out


def iou(a, b):
    ix = max(0, min(a[0] + a[2], b[0] + b[2]) - max(a[0], b[0])); iy = max(0, min(a[1] + a[3], b[1] + b[3]) - max(a[1], b[1]))
    u = a[2] * a[3] + b[2] * b[3] - ix * iy
    return ix * iy / u if u else 0.0


def union_box(a, b):
    x0, y0 = min(a[0], b[0]), min(a[1], b[1]); x1, y1 = max(a[0] + a[2], b[0] + b[2]), max(a[1] + a[3], b[1] + b[3])
    return (x0, y0, x1 - x0, y1 - y0)


def run_tool(S, **kw):
    scales = {r['page']: S['scale'] for r in S['rows']}
    res = BC.run(S['rows'], S['images'], scales, **kw)
    return {r['sid']: g for r, g in zip(S['rows'], res)}


def build(sorters, **kw):
    """One record per labelled box, all sorters."""
    recs = []
    for name, S in sorters.items():
        flags = run_tool(S, **kw)
        by = {r['sid']: r for r in S['rows']}
        med = {}
        for p in {r['page'] for r in S['rows']}:
            med[p] = float(np.median([float(r['w']) * float(r['h']) for r in S['rows'] if r['page'] == p]))
        for L in S['labels']:
            r = by[L['sid']]; g = flags[L['sid']]
            m = tuple(int(float(r[c])) for c in 'xywh'); area = m[2] * m[3]
            rec = dict(sorter=name, sid=L['sid'], page=r['page'], label=L['label'], machine=m, owner=L['owner'],
                       flagged=int(g['flagged']), outside_frac=g['outside_frac'], n_comp=g['n_comp'], grown=tuple(g['grown']),
                       area=area, page_median=med[r['page']], small=int(area < med[r['page']]))
            if L['owner']:
                rec['iou_machine'] = iou(m, L['owner']); rec['iou_grown'] = iou(rec['grown'], L['owner'])
                rec['iou_union'] = iou(union_box(m, rec['grown']), L['owner'])
            recs.append(rec)
    return recs


def confusion(recs, key):
    tp = sum(1 for r in recs if r['label'] and r[key]); fn = sum(1 for r in recs if r['label'] and not r[key])
    fp = sum(1 for r in recs if not r['label'] and r[key]); tn = sum(1 for r in recs if not r['label'] and not r[key])
    rec = tp / (tp + fn) if tp + fn else float('nan'); fa = fp / (fp + tn) if fp + tn else float('nan')
    return dict(tp=tp, fn=fn, fp=fp, tn=tn, recall=rec, fa=fa, ba=(rec + (1 - fa)) / 2)


def ba_vec(y, f):
    pos = y == 1
    return ((f[pos].mean()) + (1 - f[~pos].mean())) / 2


def perm_p(recs, groups):
    """p of the observed balanced accuracy under 10,000 shuffles of the flags; groups = list of index arrays that are shuffled
    separately (one group = pooled shuffle)."""
    y = np.array([r['label'] for r in recs]); f = np.array([r['flagged'] for r in recs])
    obs = ba_vec(y, f); rng = np.random.RandomState(SEED); k = 0
    for _ in range(N_PERM):
        g = f.copy()
        for idx in groups:
            g[idx] = f[idx][rng.permutation(len(idx))]
        k += ba_vec(y, g) >= obs - 1e-12
    return (k + 1) / (N_PERM + 1), float(obs)


def med(v):
    return float(np.median(v)) if len(v) else float('nan')


def evaluate(recs, per_sorter_groups=None):
    """All the numbers for one set of labelled boxes."""
    c = confusion(recs, 'flagged'); b = confusion(recs, 'small')
    pos = [r for r in recs if r['label']]
    ig = [r['iou_grown'] for r in pos]; im = [r['iou_machine'] for r in pos]
    fl = [r for r in pos if r['flagged']]
    n = len(recs)
    pooled_p, _ = perm_p(recs, [np.arange(n)])
    sorter_ix = [np.array([i for i, r in enumerate(recs) if r['sorter'] == s]) for s in sorted({r['sorter'] for r in recs})]
    strat_p, _ = perm_p(recs, sorter_ix)
    return dict(n=n, npos=len(pos), nneg=n - len(pos), conf=c, small=b, p_pooled=pooled_p, p_strat=strat_p,
                iou_machine=med(im), iou_grown=med(ig), iou_gain=med(ig) - med(im),
                iou_machine_flagged=med([r['iou_machine'] for r in fl]), iou_grown_flagged=med([r['iou_grown'] for r in fl]),
                n_flagged_pos=len(fl), iou_union_gain=med([r['iou_union'] for r in pos]) - med(im))


def gate_lines(E):
    c, b = E['conf'], E['small']
    return [
        ('recall on positives', '%.3f' % c['recall'], '>= %.2f' % GATE['recall'], c['recall'] >= GATE['recall'] - 1e-12),
        ('false-alarm rate on negatives', '%.3f' % c['fa'], '<= %.2f' % GATE['fa'], c['fa'] <= GATE['fa'] + 1e-12),
        ('balanced accuracy vs small-box baseline', '%.3f vs %.3f (margin %+.3f)' % (c['ba'], b['ba'], c['ba'] - b['ba']),
         'margin >= +%.2f' % GATE['ba_margin'], c['ba'] - b['ba'] >= GATE['ba_margin'] - 1e-12),
        ('permutation p, flags shuffled over all labelled boxes', '%.4f' % E['p_pooled'], '< %.2f' % GATE['p'], bool(E['p_pooled'] < GATE['p'])),
        ('permutation p, flags shuffled within each sorter', '%.4f' % E['p_strat'], '< %.2f' % GATE['p'], bool(E['p_strat'] < GATE['p'])),
        ('median IoU gain, grown vs machine box, on positives',
         '%.3f vs %.3f (gain %+.3f)' % (E['iou_grown'], E['iou_machine'], E['iou_gain']), 'gain >= +%.2f' % GATE['iou_gain'],
         E['iou_gain'] >= GATE['iou_gain'] - 1e-12),
    ]


def scores_tsv(recs):
    cols = ['sorter', 'sid', 'page', 'label', 'mx', 'my', 'mw', 'mh', 'ox', 'oy', 'ow', 'oh', 'flagged', 'outside_frac', 'n_comp',
            'gx', 'gy', 'gw', 'gh', 'iou_machine', 'iou_grown', 'area', 'page_median_area', 'small_box_flag']
    lines = ['\t'.join(cols)]
    for r in recs:
        o = r['owner'] or ('', '', '', '')
        lines.append('\t'.join(str(v) for v in [
            r['sorter'], r['sid'], r['page'], r['label'], *r['machine'], *o, r['flagged'], '%.3f' % r['outside_frac'], r['n_comp'],
            *r['grown'], ('%.3f' % r['iou_machine']) if 'iou_machine' in r else '', ('%.3f' % r['iou_grown']) if 'iou_grown' in r else '',
            r['area'], '%.1f' % r['page_median'], r['small']]))
    return '\n'.join(lines) + '\n'


def sha(path):
    return hashlib.sha256(open(os.path.join(ROOT, path), 'rb').read()).hexdigest()


def frozen_check():
    t = open(os.path.join(HERE, 'PREREG-BOXCLIP.md')).read()
    out = []
    for path in ('tools/box_clip_check.py', 'benchmark-tx/boxclip/run_boxclip.py'):
        m = re.search(r'FROZEN\s+%s\s+sha256\s+([0-9a-f]{64})' % re.escape(path), t)
        out.append((path, sha(path), m.group(1) if m else None))
    return out


def fmt_conf(c):
    return '| | flagged | not flagged |\n|---|---|---|\n| positive (owner re-cut) | %d | %d |\n| negative (looked at, not re-cut) | %d | %d |' % (
        c['tp'], c['fn'], c['fp'], c['tn'])


def results_md(sorters, recs, stamp):
    allE = evaluate(recs)
    parts = []
    L = lambda s='': parts.append(s)
    L('# BOXCLIP results (12 Oct 2026)')
    L()
    L('Scored once with the frozen method of `PREREG-BOXCLIP.md`; run at %s (machine clock). Script: `run_boxclip.py`; flags and IoU per box: `scores.tsv`.' % stamp)
    L()
    for path, have, want in frozen_check():
        L('- frozen file `%s` sha256 %s: **%s**' % (path, have[:16], 'matches PREREG' if have == want else 'DOES NOT MATCH PREREG (%s)' % (want[:16] if want else 'no FROZEN line')))
    L()
    gl = gate_lines(allE)
    verdict = 'PASS' if all(g[3] for g in gl) else 'FAIL'
    L('## Verdict: **%s** (pooled gate, every line must hold)' % verdict)
    L()
    L('| gate line | number | threshold | result |')
    L('|---|---|---|---|')
    for name, num, thr, ok in gl:
        L('| %s | %s | %s | **%s** |' % (name, num, thr, 'PASS' if ok else 'FAIL'))
    L()
    L('## Labels')
    L()
    L('| sorter | positives (owner re-cut) | negatives (looked at, not re-cut) | boxes on the page(s), all given to the tool |')
    L('|---|---|---|---|')
    for name, S in sorters.items():
        y = [l['label'] for l in S['labels']]
        L('| %s | %d | %d | %d |' % (name, sum(y), len(y) - sum(y), len(S['rows'])))
    L('| **pooled** | **%d** | **%d** | |' % (allE['npos'], allE['nneg']))
    L()
    L('## Pooled confusion table (the method, 25% rule)')
    L()
    L(fmt_conf(allE['conf']))
    L()
    L('recall %.3f, false-alarm rate %.3f, balanced accuracy %.3f.' % (allE['conf']['recall'], allE['conf']['fa'], allE['conf']['ba']))
    L()
    L('## Controls')
    L()
    L('**(b) Small-box baseline** (flag every box whose area is below the median machine-box area of its page; all boxes of the page set the median):')
    L()
    L(fmt_conf(allE['small']))
    L()
    L('recall %.3f, false-alarm rate %.3f, balanced accuracy %.3f.' % (allE['small']['recall'], allE['small']['fa'], allE['small']['ba']))
    L()
    L('**(a) Random-flag null** (the flags shuffled over the labelled boxes, %d shuffles, seed %d): observed balanced accuracy %.3f; '
      'p = %.4f with the flags shuffled over all %d labelled boxes (the registered shuffle), p = %.4f with the flags shuffled only within each sorter '
      '(added to the gate in the pre-registration because the share of positives differs by sorter).' % (
          N_PERM, SEED, allE['conf']['ba'], allE['p_pooled'], allE['n'], allE['p_strat']))
    L()
    L('## IoU on positives')
    L()
    L('| | median IoU with the owner box |')
    L('|---|---|')
    L('| machine box, all %d positives | %.3f |' % (allE['npos'], allE['iou_machine']))
    L('| grown box (machine box where unflagged), all %d positives | %.3f |' % (allE['npos'], allE['iou_grown']))
    L('| machine box, the %d flagged positives only | %.3f |' % (allE['n_flagged_pos'], allE['iou_machine_flagged']))
    L('| grown box, the %d flagged positives only | %.3f |' % (allE['n_flagged_pos'], allE['iou_grown_flagged']))
    L()
    L('## Per sorter (same lines, controls recomputed inside the sorter)')
    L()
    for name in sorters:
        sub = [r for r in recs if r['sorter'] == name]
        E = evaluate(sub)
        # inside one sorter the pooled and the within-sorter shuffle are the same shuffle
        gl2 = gate_lines(E)
        L('### %s: %d positives, %d negatives' % (name, E['npos'], E['nneg']))
        L()
        L(fmt_conf(E['conf']))
        L()
        L('small-box baseline: recall %.3f, false-alarm %.3f, balanced accuracy %.3f.' % (E['small']['recall'], E['small']['fa'], E['small']['ba']))
        L()
        L('| gate line | number | threshold | result |')
        L('|---|---|---|---|')
        for gname, num, thr, ok in gl2[:4] + gl2[5:]:
            L('| %s | %s | %s | %s |' % (gname, num, thr, 'PASS' if ok else 'FAIL'))
        L()
        L('IoU on the %d flagged positives: machine %.3f, grown %.3f.' % (E['n_flagged_pos'], E['iou_machine_flagged'], E['iou_grown_flagged']))
        L()
    return '\n'.join(parts) + '\n', allE, gl


def sensitivity_md(sorters):
    parts = ['', '## Sensitivity (not the test)', '',
             'Nothing below changes the verdict above: the registered threshold is 25%. The table only shows how the pooled numbers move if the '
             'outside-ink threshold were 15% or 35% (all else frozen), plus one exploratory IoU variant (the grown box united with the machine box). '
             'The gate lines are shown for information.', '',
             '| outside-ink threshold | recall | false-alarm | balanced acc | small-box BA | IoU gain (grown vs machine) | IoU gain (grown united with machine) | p (pooled shuffle) |',
             '|---|---|---|---|---|---|---|---|']
    for thr in (0.15, 0.25, 0.35):
        recs = build(sorters, thr=thr)
        E = evaluate(recs); c = E['conf']
        parts.append('| %.2f%s | %.3f | %.3f | %.3f | %.3f | %+.3f | %+.3f | %.4f |' % (
            thr, ' (registered)' if thr == 0.25 else '', c['recall'], c['fa'], c['ba'], E['small']['ba'], E['iou_gain'], E['iou_union_gain'], E['p_pooled']))
    return '\n'.join(parts) + '\n'


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0], epilog=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--sensitivity', action='store_true')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args(argv)
    sorters = load()
    recs = build(sorters)
    sc = scores_tsv(recs)
    sp, rp = os.path.join(HERE, 'scores.tsv'), os.path.join(HERE, 'RESULTS.md')
    if a.check:
        cur = open(sp).read() if os.path.exists(sp) else ''
        if cur != sc:
            print('STALE: scores.tsv differs from a fresh run'); return 1
        print('scores.tsv is current (%d rows)' % (sc.count('\n') - 1)); return 0
    if a.sensitivity:
        cur = open(rp).read()
        cur = cur.split('\n## Sensitivity (not the test)')[0].rstrip('\n') + '\n'
        open(rp, 'w').write(cur + sensitivity_md(sorters)); print('sensitivity section written'); return 0
    stamp = time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())
    md, E, gl = results_md(sorters, recs, stamp)
    open(sp, 'w').write(sc); open(rp, 'w').write(md)
    print(md)
    return 0


if __name__ == '__main__':
    sys.exit(main())
