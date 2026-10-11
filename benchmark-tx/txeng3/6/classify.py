#!/usr/bin/env python3
"""TXE3-6 UNIT steps 2b and 3 (PREREG-txeng3-6.md 'Classifier'): compose a glyph_atlas classify directory from the frozen
exemplars (seg/sign train boxes with a label) plus one condition's target boxes, run tools/glyph_atlas.py classify
--page all --knn 5 --topk 3 --pca-scale unit with every target page held out from voting, and write the outputs.

  python3 classify.py round1          # label the remaining TRAIN lines by alignment (round 1), appends to labels_train.tsv
  python3 classify.py test COND       # COND in pen, sign, rand1, rand2, rand3: classify the TEST lines' boxes ->
                                      # outputs/COND.top1.tsv (line, pos, sign) and outputs/COND.topk.tsv (line, pos, cand, score)
"""
import csv, difflib, json, os, subprocess, sys, collections
import numpy as np
ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(ROOT, '..', '..', '..'))
sys.path.insert(0, ROOT)
from seg import TRAIN, TEST, TRUTH
TOOL = os.path.join(REPO, 'tools/glyph_atlas.py')
SIGN_COLS = ['sid', 'page', 'line', 'pos', 'x', 'y', 'w', 'h', 'rh', 'rw', 'dy', 'marks']


def load_seg(name):
    d = os.path.join(ROOT, 'seg', name)
    rows = list(csv.DictReader(open(os.path.join(d, 'signs.tsv')), delimiter='\t'))
    bm = np.load(os.path.join(d, 'bitmaps.npz'))['signs']
    assert len(rows) == len(bm)
    boxes = {r['sid']: r for r in csv.DictReader(open(os.path.join(d, 'boxes.tsv')), delimiter='\t')}
    return rows, bm, boxes


def labels():
    p = os.path.join(ROOT, 'labels_train.tsv')
    return [r for r in csv.DictReader(open(p), delimiter='\t')]


def compose(out, ex_sids, cond, target_lines):
    """exemplars: seg/sign rows whose sid is in ex_sids; targets: seg/COND rows on target_lines (the boxes.tsv survivors)."""
    os.makedirs(out, exist_ok=True)
    srows, sbm, sboxes = load_seg('sign')
    trows, tbm, tboxes = load_seg(cond)
    keep_s = [i for i, r in enumerate(srows) if r['sid'] in ex_sids]
    tl = {f'f102r_{l}' for l in target_lines}
    keep_t = [i for i, r in enumerate(trows) if r['sid'] in tboxes and tboxes[r['sid']]['line'] in tl]
    rows = [srows[i] for i in keep_s] + [dict(trows[i], sid='T_' + trows[i]['sid'], page='T_' + trows[i]['page']) for i in keep_t]
    bm = np.concatenate([sbm[keep_s], tbm[keep_t]])
    with open(os.path.join(out, 'signs.tsv'), 'w') as f:
        f.write('\t'.join(SIGN_COLS) + '\n')
        for r in rows:
            f.write('\t'.join(str(r[c]) for c in SIGN_COLS) + '\n')
    np.savez_compressed(os.path.join(out, 'bitmaps.npz'), signs=bm, marks=np.zeros((0, 48, 48), np.uint8))
    open(os.path.join(out, 'marks.tsv'), 'w').write('mid\tpage\tline\tx\ty\tw\th\trh\trw\tsid\n')
    with open(os.path.join(out, 'clusters.tsv'), 'w') as f:
        f.write('kind\tid\tcluster\n')
        for r in rows:
            f.write(f"sign\t{r['sid']}\t_\n")
    json.dump({'signs': {}, 'marks': {}, 'override': {}, 'desc': {'_': 'unlabelled'}}, open(os.path.join(out, 'labels.json'), 'w'))
    pages = sorted({r['page'] for r in rows})
    json.dump({p: {} for p in pages}, open(os.path.join(out, 'pages.json'), 'w'))
    return rows, {('T_' + s): b for s, b in tboxes.items()}


def run_classify(out, tsv):
    cmd = [sys.executable, TOOL, 'classify', '--out', out, '--labels', os.path.join(out, 'labels.json'), '--page', 'all',
           '--tsv', tsv, '--knn', '5', '--topk', '3', '--pca-scale', 'unit', '--train-labels', os.path.join(ROOT, 'labels_train.tsv'),
           '--holdout', 'T_']
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stdout + r.stderr)
    open(tsv + '.log', 'w').write(' '.join(cmd[2:]) + '\n' + r.stdout)
    return [x for x in csv.DictReader(open(tsv), delimiter='\t') if x['box'].startswith('T_')]


def ordered(res, tboxes):
    by = collections.defaultdict(list)
    for x in res:
        b = tboxes[x['box']]
        by[b['line']].append((int(b['pos']), x))
    return {ln: [x for _, x in sorted(v)] for ln, v in by.items()}


def truth_lines():
    t = collections.defaultdict(list)
    for r in csv.DictReader((l for l in open(TRUTH) if not l.startswith('#')), delimiter='\t'):
        t[r['line']].append(r)
    return t


def round1():
    lab = labels()
    done_lines = {r['box'].split('_')[1] for r in lab}      # sid f102r_L25_s1_01_003 -> L25
    todo = [l for l in TRAIN if l not in done_lines]
    out = os.path.join(ROOT, 'cls', 'round1')
    rows, tboxes = compose(out, {r['box'] for r in lab}, 'sign', todo)
    res = ordered(run_classify(out, os.path.join(out, 'classify.tsv')), tboxes)
    T = truth_lines()
    key = {r['code'] for r in csv.DictReader(open(os.path.join(REPO, 'ciphers/fr16104-vivonne-spain-1572/key.tsv')), delimiter='\t')}
    new, rep = [], []
    for ln, xs in sorted(res.items()):
        pred = [x['code'] for x in xs]
        ref = [r['ref_sign'] for r in T[ln]]
        sm = difflib.SequenceMatcher(a=pred, b=ref, autojunk=False)
        n_eq = n_rep = 0
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == 'equal' or (tag == 'replace' and i2 - i1 == j2 - j1):
                for i, j in zip(range(i1, i2), range(j1, j2)):
                    tr = T[ln][j]
                    ts = tr['truth'].split('|') if tr['truth'] else []
                    if tr['status'] == 'scored':
                        code = tr['ref_sign'] if tr['ref_sign'] in ts else ts[0]
                    elif tr['ref_sign'] in key:
                        code = tr['ref_sign']
                    else:
                        continue
                    new.append((xs[i]['box'][2:], code))
                    n_eq += tag == 'equal'; n_rep += tag != 'equal'
        rep.append(f'{ln}: boxes {len(pred)} truth {len(ref)} -> labelled {n_eq} (equal) + {n_rep} (1:1 replace) of {len(pred)}')
    with open(os.path.join(ROOT, 'labels_train.tsv'), 'w') as f:
        f.write('box\tcode\tround\n')
        for r in lab:
            f.write(f"{r['box']}\t{r['code']}\t0\n")
        for s, c in new:
            f.write(f'{s}\t{c}\t1\n')
    cnt = collections.Counter([r['code'] for r in lab] + [c for _, c in new])
    rep.append(f'ROUND 1: +{len(new)} labels -> TOTAL {len(lab) + len(new)} exemplars, {len(cnt)} codes: ' + ', '.join(f'{c}:{n}' for c, n in cnt.most_common()))
    open(os.path.join(ROOT, 'labels_report.txt'), 'a').write('\n'.join(rep) + '\n')
    print('\n'.join(rep))


def test(cond):
    lab = labels()
    out = os.path.join(ROOT, 'cls', cond)
    rows, tboxes = compose(out, {r['box'] for r in lab}, cond, TEST)
    res = ordered(run_classify(out, os.path.join(out, 'classify.tsv')), tboxes)
    os.makedirs(os.path.join(ROOT, 'outputs'), exist_ok=True)
    n = 0
    with open(os.path.join(ROOT, 'outputs', f'{cond}.top1.tsv'), 'w') as f1, open(os.path.join(ROOT, 'outputs', f'{cond}.topk.tsv'), 'w') as fk:
        f1.write('line\tpos\tsign\n'); fk.write('line\tpos\tcand\tscore\n')
        for ln in sorted(res):
            for p, x in enumerate(res[ln], 1):
                f1.write(f"{ln}\t{p}\t{x['code']}\n"); n += 1
                for k in (1, 2, 3):
                    if x[f'k{k}']:
                        fk.write(f"{ln}\t{p}\t{x[f'k{k}']}\t{x[f's{k}']}\n")
    print(f'{cond}: {n} test boxes classified on {len(res)} lines; exemplars {len(lab)}')


if __name__ == '__main__':
    {'round1': round1, 'test': lambda: test(sys.argv[2])}[sys.argv[1]]()
