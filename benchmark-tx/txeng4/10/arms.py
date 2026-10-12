#!/usr/bin/env python3
"""TXE4-10 RECOG-CUT unit 3 (PREREG-txeng4-10.md 'Arms'): the recognition-split arms and the frozen-kNN classification
of every arm. Tools: glyph_atlas.py with benchmark-tx/txeng4/10/glyph_atlas.patch applied (R7: TXE4-3 landed on the shared
file within the hour, so the option runs from a patched scratch copy named by $TXE4_10_TOOLS; default tools/).
  python3 arms.py lambda     # TRAIN lines: --split-by-recognition at each grid L; |boxes - consensus count| -> lambda.tsv
  python3 arms.py build      # TEST lines: (d) rec at the chosen L; (e) rec_perm1..3 (--rec-permute-labels); can-vary counts
  python3 arms.py classify   # every arm's test boxes through the frozen RecKNN -> outputs/<arm>.top1.tsv, .topk.tsv
No truth file is opened here (counts come from the machine consensus; scores come later from tools/tx_bench.py)."""
import csv, collections, hashlib, json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
import numpy as np
ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(ROOT, '..', '..', '..'))
TOOLS = os.environ.get('TXE4_10_TOOLS', os.path.join(REPO, 'tools'))
sys.path.insert(0, TOOLS)
sys.path.insert(0, os.path.join(REPO, 'benchmark-tx/txeng3/6'))
from seg import TRAIN, TEST, crops
import glyph_atlas as GA
TEST = [l for l in TEST if l != 'L14']          # L14 has no truth rows (TXE3-6 amendment 1)
T36 = os.path.join(REPO, 'benchmark-tx/txeng3/6/seg')
ATLAS = os.path.join(T36, 'sign')                  # the exemplar atlas: TXE3-6's seg/sign (train boxes carry labels.tsv)
LABELS = os.path.join(ROOT, 'labels/labels.tsv')
GRID = [0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.5, 3.0]
ARMS36 = ['pen', 'sign', 'rand1', 'rand2', 'rand3']


def rd(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))


def log(msg):
    open(os.path.join(ROOT, 'arms.log'), 'a').write(msg + '\n')


def segment(name, extra, lines):
    """glyph_atlas segment over the line crops of `lines` -> seg/<name>/ (signs.tsv, bitmaps.npz, rec_split.tsv) and
    boxes.tsv in TXE3-6's layout (OL1-BOXES dedupe at the s1/s2 midpoint, order by centre x)."""
    cr = crops()
    out = os.path.join(ROOT, 'seg', name)
    os.makedirs(out, exist_ok=True)
    pages = []
    for (ln, sg), e in sorted(cr.items()):
        if ln in lines:
            pages += ['--page', f"{e['page']}={e['path']}"]
    cmd = [sys.executable, os.path.join(TOOLS, 'glyph_atlas.py'), 'segment', '--out', out] + pages + extra
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stdout + r.stderr)
    open(os.path.join(out, 'segment.log'), 'w').write(' '.join(cmd[2:5]) + ' ...' + ' '.join(extra) + '\n' + r.stdout)
    rows = rd(os.path.join(out, 'signs.tsv'))
    byline = collections.defaultdict(list)
    for s in rows:
        ln, sg = s['page'].split('_')[1], int(s['page'][-1])
        e = cr[(ln, sg)]
        byline[ln].append(dict(s, seg=sg, xl=e['x0'] + int(s['x']), xc=e['x0'] + int(s['x']) + int(s['w']) / 2))
    n = collections.Counter()
    with open(os.path.join(out, 'boxes.tsv'), 'w') as f:
        f.write('line\tpos\tsid\tpage\tx_line\tx\ty\tw\th\n')
        for ln in sorted(byline):
            segs = sorted({s for (l2, s) in cr if l2 == ln})
            keep = []
            for b in byline[ln]:
                lo = -1e9 if b['seg'] == segs[0] else (cr[(ln, b['seg'])]['x0'] + cr[(ln, b['seg'] - 1)]['x1']) / 2
                hi = 1e9 if b['seg'] == segs[-1] else (cr[(ln, b['seg'] + 1)]['x0'] + cr[(ln, b['seg'])]['x1']) / 2
                if lo <= b['xc'] < hi:
                    keep.append(b)
            keep.sort(key=lambda b: b['xc'])
            for i, b in enumerate(keep):
                f.write(f"f102r_{ln}\t{i + 1}\t{b['sid']}\t{b['page']}\t{b['xl']}\t{b['x']}\t{b['y']}\t{b['w']}\t{b['h']}\n")
            n[ln] = len(keep)
    return n


def rec_args(L, seed=None):
    a = ['--split-by-recognition', LABELS, '--rec-atlas', ATLAS, '--rec-lambda', str(L)]
    return a + (['--rec-permute-labels', str(seed)] if seed is not None else [])


def consensus_counts():
    c = collections.Counter()
    for r in rd(os.path.join(ROOT, 'labels/consensus_read.tsv')):
        c[r['line'].split('_')[1]] += 1
    return c


def cmd_lambda():
    cc = consensus_counts()
    with ThreadPoolExecutor(4) as ex:
        res = dict(zip(GRID, ex.map(lambda L: segment(f'lam_{L}', rec_args(L), TRAIN), GRID)))
    rows = []
    for L in GRID:
        n = res[L]
        d = sum(abs(n[l] - cc[l]) for l in TRAIN)
        rows.append((d, -L, L, sum(n[l] for l in TRAIN)))
        print(f'L {L}: train boxes {sum(n[l] for l in TRAIN)} vs consensus {sum(cc[l] for l in TRAIN)}, sum|diff| {d}')
    rows.sort()
    best = rows[0][2]
    with open(os.path.join(ROOT, 'lambda.tsv'), 'w') as f:
        f.write('L\ttrain_boxes\tconsensus_count\tsum_absdiff\tchosen\n')
        for d, _, L, nb in sorted(rows, key=lambda r: r[2]):
            f.write(f'{L}\t{nb}\t{sum(cc[l] for l in TRAIN)}\t{d}\t{int(L == best)}\n')
    print(f'CHOSEN L {best} (sum|diff| {rows[0][0]}, train boxes {rows[0][3]} vs consensus {sum(cc[l] for l in TRAIN)}; '
          f'pen units {sum(1 for b in rd(os.path.join(T36, "pen/boxes.tsv")) if b["line"].split("_")[1] in TRAIN)})')
    log(f'lambda: chosen {best}; ' + '; '.join(f'L {L} d {d}' for d, _, L, _ in sorted(rows, key=lambda r: r[2])))


def chosen_lambda():
    return [float(r['L']) for r in rd(os.path.join(ROOT, 'lambda.tsv')) if r['chosen'] == '1'][0]


def cmd_build():
    L = chosen_lambda()
    jobs = [('rec', rec_args(L))] + [(f'rec_perm{s}', rec_args(L, s)) for s in (1, 2, 3)]
    with ThreadPoolExecutor(4) as ex:
        res = dict(zip([j[0] for j in jobs], ex.map(lambda j: segment(j[0], j[1], TEST), jobs)))
    geo = lambda name: {(b['line'], b['x_line'], b['w'], b['y'], b['h']) for b in rd(os.path.join(ROOT, 'seg', name, 'boxes.tsv'))}
    d = geo('rec')
    rep = [f"(d) rec at L {L}: test boxes {sum(res['rec'].values())}"]
    for s in (1, 2, 3):
        e = geo(f'rec_perm{s}')
        rep.append(f"(e) rec_perm{s}: test boxes {sum(res[f'rec_perm{s}'].values())}; boxes differing in geometry from (d): "
                   f"{len(e - d)} of {len(e)} (can-vary count)")
    rep.append('per line (d): ' + ', '.join(f"{l} {res['rec'][l]}" for l in TEST))
    open(os.path.join(ROOT, 'build_report.txt'), 'w').write('\n'.join(rep) + '\n')
    print('\n'.join(rep))


def cmd_classify():
    knn = GA.RecKNN.from_atlas(ATLAS, LABELS, k=5)
    assert knn.pca_scale == 'unit', knn.pca_scale
    os.makedirs(os.path.join(ROOT, 'outputs'), exist_ok=True)
    tl = {f'f102r_{l}' for l in TEST}
    rep = [f'frozen RecKNN: {len(knn.y)} exemplars, {len(knn.codes)} codes, k 5, alpha 0.5, pca_scale {knn.pca_scale}']
    for arm in ARMS36 + ['rec', 'rec_perm1', 'rec_perm2', 'rec_perm3']:
        d = os.path.join(T36, arm) if arm in ARMS36 else os.path.join(ROOT, 'seg', arm)
        rows = rd(os.path.join(d, 'signs.tsv'))
        bm = np.load(os.path.join(d, 'bitmaps.npz'))['signs']
        idx = {r['sid']: i for i, r in enumerate(rows)}
        boxes = [b for b in rd(os.path.join(d, 'boxes.tsv')) if b['line'] in tl]
        ii = [idx[b['sid']] for b in boxes]
        assert not (set(b['sid'] for b in boxes) & set(knn.sids)), 'a test box is an exemplar'
        tk = knn.topk(bm[ii], [float(rows[i]['rh']) for i in ii], [float(rows[i]['rw']) for i in ii], k=3)
        with open(os.path.join(ROOT, 'outputs', f'{arm}.top1.tsv'), 'w') as f1, \
                open(os.path.join(ROOT, 'outputs', f'{arm}.topk.tsv'), 'w') as fk:
            f1.write('line\tpos\tsign\n'); fk.write('box\tline\tpos\tk1\ts1\tk2\ts2\tk3\ts3\n')
            for b, t in zip(boxes, tk):
                f1.write(f"{b['line']}\t{b['pos']}\t{t[0][0]}\n")
                fk.write(f"{b['sid']}\t{b['line']}\t{b['pos']}\t" + '\t'.join(f'{c}\t{p:.3f}' for c, p in t) + '\n')
        rep.append(f'{arm}: {len(boxes)} test boxes classified ({d.replace(REPO + "/", "")})')
    open(os.path.join(ROOT, 'classify_report.txt'), 'w').write('\n'.join(rep) + '\n')
    print('\n'.join(rep))


if __name__ == '__main__':
    log(f'{sys.argv[1]}: tools {TOOLS}')
    {'lambda': cmd_lambda, 'build': cmd_build, 'classify': cmd_classify}[sys.argv[1]]()
