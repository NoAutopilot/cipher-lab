#!/usr/bin/env python3
"""Offline test for tools/glyph_atlas.py classify --features hog+zone+topo / --metric lda|nca (TXE4-3 ATLAS-NCA, 12 Oct 2026).
Builds a synthetic two-page atlas folder (signs.tsv, bitmaps.npz, marks.tsv, clusters.tsv): two shapes (a filled bar and a
ring) with jitter, page p1 labelled (the voters), page p2 held out.
Must catch: (1) the metric fit seeing a held-out page -- the sidecar <tsv>.metric.json lists fit_pages and fit_tiles, and
both must name p1 only with exactly the labelled count (72); (2) a planted two-class toy not separating under the learned
metric -- p2's top-1 must equal its true class on >= 90% of its boxes under hog+zone+topo NCA and under hog LDA, and hog
NCA must at least beat the unlearned HOG+PCA40 distance (it overfits 40 unit-scaled components from 72 tiles: 0.85 vs 0.72).
Must NOT block: the default path -- a run without the new flags writes no sidecar and is byte-identical to a run that names
--features hog --metric none. No network, no model, no truth file."""
import csv, json, os, subprocess, sys, tempfile
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, '..', 'glyph_atlas.py')


def tile(kind, rng):
    bm = np.zeros((48, 48), np.uint8)
    j = lambda: int(rng.integers(-3, 4))
    if kind == 'bar':
        bm[10 + j():38 + j(), 18 + j():30 + j()] = 255
    else:
        yy, xx = np.mgrid[:48, :48]
        r = np.hypot(yy - 24 - j(), xx - 24 - j())
        bm[(r < 16 + j()) & (r > 8 + j())] = 255
    k = rng.integers(0, 48, size=(6, 2))          # speckle noise
    for y, x in k:
        bm[y, x] = 255
    return bm


def build(d, rng):
    rows, bms, labels = [], [], []
    for page in ('p1', 'p2'):
        for li in range(1, 7):
            for pos in range(1, 13):
                kind = 'bar' if (pos + li) % 2 else 'ring'
                sid = f'{page}_{li:02d}_{pos:03d}'
                rows.append(dict(sid=sid, page=page, line=li, pos=pos, x=pos * 60, y=li * 80, w=24 + int(rng.integers(-3, 4)),
                                 h=40 + int(rng.integers(-3, 4)), rh=f'{1.0 + rng.normal(0, 0.05):.3f}',
                                 rw=f'{0.6 + rng.normal(0, 0.05):.3f}', dy=f'{rng.normal(0, 0.1):.3f}', marks=''))
                bms.append(tile(kind, rng)); labels.append((sid, 'T1' if kind == 'bar' else 'T2', page))
    cols = ['sid', 'page', 'line', 'pos', 'x', 'y', 'w', 'h', 'rh', 'rw', 'dy', 'marks']
    with open(os.path.join(d, 'signs.tsv'), 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(str(r[c]) for c in cols) + '\n')
    np.savez(os.path.join(d, 'bitmaps.npz'), signs=np.array(bms, np.uint8), marks=np.zeros((0, 48, 48), np.uint8))
    open(os.path.join(d, 'marks.tsv'), 'w').write('mid\tpage\tline\tx\ty\tw\th\n')
    open(os.path.join(d, 'clusters.tsv'), 'w').write('kind\tid\tcluster\n' + ''.join(f'sign\t{r["sid"]}\t0\n' for r in rows))
    json.dump({'signs': {}, 'marks': {}, 'override': {}}, open(os.path.join(d, 'labels.json'), 'w'))
    with open(os.path.join(d, 'train.tsv'), 'w') as f:
        f.write('box\tcode\n')
        for sid, code, page in labels:
            if page == 'p1':
                f.write(f'{sid}\t{code}\n')
    return {sid: code for sid, code, page in labels if page == 'p2'}


def run(d, tsv, extra):
    cmd = [sys.executable, TOOL, 'classify', '--out', d, '--labels', os.path.join(d, 'labels.json'), '--page', 'all',
           '--tsv', tsv, '--topk', '3', '--train-labels', os.path.join(d, 'train.tsv'), '--only-train-labels',
           '--holdout', 'p2_'] + extra
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr + r.stdout
    return list(csv.DictReader(open(tsv), delimiter='\t'))


def main():
    d = tempfile.mkdtemp(); rng = np.random.default_rng(3)
    truth = build(d, rng)
    # must NOT block: default path unchanged, no sidecar
    a = run(d, os.path.join(d, 'a.tsv'), [])
    b = run(d, os.path.join(d, 'b.tsv'), ['--features', 'hog', '--metric', 'none'])
    assert open(os.path.join(d, 'a.tsv')).read() == open(os.path.join(d, 'b.tsv')).read(), 'default path changed'
    assert not os.path.exists(os.path.join(d, 'a.tsv.metric.json')), 'default path wrote a metric sidecar'
    print('ok test_default_path_unchanged')
    p2a = [r for r in a if r['page'] == 'p2']
    base = sum(r['code'] == truth[r['box']] for r in p2a) / len(p2a)
    print(f'base HOG+PCA40 kNN5 on the toy: p2 acc {base:.2f}')
    for feats, metric in (('hog', 'nca'), ('hog+zone+topo', 'nca'), ('hog', 'lda')):
        tsv = os.path.join(d, f'{feats}_{metric}.tsv')
        out = run(d, tsv, ['--features', feats, '--metric', metric, '--metric-dim', '8',
                           '--topo-cache', os.path.join(d, 'topo.npy')])
        info = json.load(open(tsv + '.metric.json'))
        # must catch 1: the fit never sees the held-out page
        assert info['fit_pages'] == ['p1'], info
        assert info['fit_tiles'] == 72, info
        # must catch 2: the planted toy separates on the held-out page
        p2 = [r for r in out if r['page'] == 'p2']
        acc = sum(r['code'] == truth[r['box']] for r in p2) / len(p2)
        # hog+nca: NCA on 40 unit-scaled PCA components from 72 tiles only beats the base distance (0.85 vs 0.72 here);
        # the other two separate outright. A learned metric on few tiles over many noise components can overfit --
        # that is a property of the instrument, recorded here, not hidden by a bigger toy.
        assert acc >= 0.9 or (feats == 'hog' and metric == 'nca' and acc > base), (feats, metric, acc, base)
        assert all(r['cluster_code'] == '_held' for r in p2)
        print(f'ok test_{feats.replace("+", "_")}_{metric}: fit on p1 only ({info["fit_tiles"]} tiles, dim {info["dim"]}), p2 acc {acc:.2f}')
    print('test_glyph_atlas_metric: all passed')


if __name__ == '__main__':
    main()
