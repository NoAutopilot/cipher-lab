#!/usr/bin/env python3
"""VIV-ESPLIT step 2 (PREREG-VIVESPLIT.md Addendum B; post-hoc, a measurement only -- no key edit, no committed reading changes).

  python3 .../tx/vivesplit/step2.py seg      # glyph_atlas segment of ink 63 f193v / f193r / f192v (images/p63/esplit, untracked)
  python3 .../tx/vivesplit/step2.py label    # width-only box map vs viv63_decode's token sequence; refit the six-class y model
                                             # on all three truth leaves; per ink-63 y token: sub-label + posterior
  python3 .../tx/vivesplit/step2.py gates    # b2 + 200 wrong keys (vivanchor_gates.wrong) on the three pages, unsplit vs split
                                             # (y_l -> l where P(l) >= 0.6), plus 200 random splits of the same count
Writes tx/viv63_esplit/{tokens.tsv,gates.json}. Crops: images/p63/esplit/<prefix>/ from the tools/iiif_lines.py commands in
tx/viv63_esplit/README.md (3 openapi.bnf.fr requests; boxes equal images/p63/manifest.json's).
"""
import csv, json, os, subprocess, sys, collections, random
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
TX = os.path.dirname(HERE)
FOLD = os.path.dirname(TX)
REPO = os.path.abspath(os.path.join(FOLD, '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'tools'))
sys.path.insert(0, TX)
sys.path.insert(0, HERE)
import box_token_align as bta  # noqa: E402
import glyph_atlas as ga  # noqa: E402
import esplit as es  # noqa: E402
OUT = os.path.join(TX, 'viv63_esplit')
IMG = os.path.join(FOLD, 'images', 'p63', 'esplit')
ATL = os.path.join(IMG, 'atlas')
PAGES = {'f193v': 'c199_f193v', 'f193r': 'c198_f193r', 'f192v': 'c198_f192v'}
THR = 0.6
SEED = 20261014


def crops():
    out = {}
    for page, pre in PAGES.items():
        for e in json.load(open(os.path.join(IMG, pre, 'manifest.json')))['iiif_lines']:
            c = e['crop']; ln = c.split('_')[2]; seg = int(c.split('_s')[1].split('.')[0])
            out[(page, ln, seg)] = dict(path=os.path.join(IMG, pre, c), x0=e['box'][0], x1=e['box'][2], page=f'{page}_{ln}_s{seg}')
    return out


def cmd_seg():
    cr = crops(); pages = []
    for k, e in sorted(cr.items()):
        pages += ['--page', f"{e['page']}={e['path']}"]
    p = subprocess.run([sys.executable, os.path.join(REPO, 'tools/glyph_atlas.py'), 'segment', '--out', ATL, '--median-h', 'pool'] + pages,
                       capture_output=True, text=True)
    if p.returncode:
        sys.exit(p.stdout + p.stderr)
    rows = es.rd(os.path.join(ATL, 'signs.tsv'))
    by = collections.defaultdict(list)
    for r in rows:
        page, ln, s = r['page'].split('_'); seg = int(s[1:]); e = cr[(page, ln, seg)]
        by[(page, ln)].append(dict(r, seg=seg, xl=e['x0'] + int(r['x']), xc=e['x0'] + int(r['x']) + int(r['w']) / 2))
    keep = []
    for (page, ln), bs in sorted(by.items()):
        segs = sorted({s for (p0, l0, s) in cr if (p0, l0) == (page, ln)})
        for b in bs:
            sg = b['seg']
            lo = -1e9 if sg == segs[0] else (cr[(page, ln, sg)]['x0'] + cr[(page, ln, sg - 1)]['x1']) / 2
            hi = 1e9 if sg == segs[-1] else (cr[(page, ln, sg + 1)]['x0'] + cr[(page, ln, sg)]['x1']) / 2
            if lo <= b['xc'] < hi:
                keep.append(dict(sid=b['sid'], page=page, line=int(ln[1:]), x=b['xl'], w=b['w'], crop_page=b['page']))
    es.wr(os.path.join(ATL, 'map_signs.tsv'), ['sid', 'page', 'line', 'x', 'w', 'crop_page'], sorted(keep, key=lambda r: (r['page'], r['line'], r['x'])))
    print('ink 63 tiles kept', collections.Counter(r['page'] for r in keep))


def seqs():
    import viv63_decode as v63
    return [(p, l, seq) for p, l, seq in v63.lines(tuple(PAGES)) if p in PAGES]


def cmd_label():
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
    os.makedirs(OUT, exist_ok=True)
    sg = es.rd(os.path.join(ATL, 'map_signs.tsv'))
    read = [dict(line=f'{p}_{l}', pos=str(i + 1), sign=c) for p, l, seq in seqs() for i, (c, _) in enumerate(seq)]
    rows, _ = bta.build_map(sg, read, lam=0.0, loo=False)
    by = collections.defaultdict(list); share = collections.defaultdict(list)
    for r in rows:
        if r['sid']:
            by[(r['line'], str(r['pos']))].append(r); share[r['sid']].append(int(r['pos']))
    S = {r['sid']: r for r in es.rd(os.path.join(ATL, 'signs.tsv'))}
    med = {k: v['median_h'] for k, v in json.load(open(os.path.join(ATL, 'pages.json'))).items()}
    grey, items, bms = {}, [], []
    for t in read:
        if t['sign'] != 'y':
            continue
        it = dict(line=t['line'], pos=t['pos'])
        bx = by.get((t['line'], t['pos']), [])
        if not bx:
            items.append(dict(it, tier='none')); continue
        ops = {b['op'] for b in bx}
        tier = 'T1' if len(bx) == 1 and ops == {'1:1'} else ('T3' if '1:2' in ops else 'T2')
        boxes = [S[b['sid']] for b in bx]
        pg = collections.Counter(b['page'] for b in boxes).most_common(1)[0][0]
        boxes = [b for b in boxes if b['page'] == pg]
        x0 = min(int(b['x']) for b in boxes); x1 = max(int(b['x']) + int(b['w']) for b in boxes)
        y0 = min(int(b['y']) for b in boxes); y1 = max(int(b['y']) + int(b['h']) for b in boxes)
        if tier == 'T3':
            sid = [b['sid'] for b in bx if b['op'] == '1:2'][0]; ps = sorted(set(share[sid]))
            if len(ps) >= 2:
                k = ps.index(int(t['pos'])); w = (x1 - x0) / len(ps); x0, x1 = int(x0 + k * w), int(x0 + (k + 1) * w)
        if pg not in grey:
            from PIL import Image
            grey[pg] = ga.binarise(np.asarray(Image.open(os.path.join(ATL, 'crops', pg + '.png')).convert('L')))
        ink = grey[pg][y0:y1, x0:x1]
        if ink.size == 0 or ink.sum() == 0:
            items.append(dict(it, tier='empty')); continue
        ys, xs = np.nonzero(ink); ink = ink[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
        mh = float(med[pg])
        items.append(dict(it, tier=tier, crop=pg, x0=x0, x1=x1, rh=round(ink.shape[0] / mh, 3), rw=round(ink.shape[1] / mh, 3), idx=len(bms)))
        bms.append(ga.bitmap(ink))
    # training: the six-class y items of step 1, all three leaves
    g = json.load(open(os.path.join(HERE, 'gate.json')))
    classes = g['y_classes']
    tb = np.load(os.path.join(HERE, 'tiles.npz'))['bm']
    tr = [r for r in es.rd(os.path.join(HERE, 'items.tsv')) if r['set'] == 'y' and r['tier'] in ('T1', 'T2', 'T3') and r['cls'] in classes]
    Btr = tb[[int(r['idx']) for r in tr]]
    q = [r for r in items if 'idx' in r]
    Bq = np.array(bms, np.uint8)

    def raw(B, R):
        return ga._hog(B), np.array([ga.zone_topo_feats(b, (float(r['rh']), float(r['rw']), 0.0)) for b, r in zip(B, R)])
    Ht, Zt = raw(Btr, tr); Hq, Zq = raw(Bq, q)
    s1 = StandardScaler().fit(Ht); pca = PCA(n_components=20, random_state=SEED).fit(s1.transform(Ht)); s2 = StandardScaler().fit(Zt)
    X = lambda H, Z: np.hstack([pca.transform(s1.transform(H)), s2.transform(Z)])
    m = LDA(solver='lsqr', shrinkage='auto').fit(X(Ht, Zt), [r['cls'] for r in tr])
    P = m.predict_proba(X(Hq, Zq))
    for r, p in zip(q, P):
        j = int(np.argmax(p)); r['sub'] = m.classes_[j]; r['post'] = round(float(p[j]), 3)
        r['p_l'] = round(float(p[list(m.classes_).index('l')]), 3); r['p_h'] = round(float(p[list(m.classes_).index('h')]), 3)
        r['split'] = 'y_l' if r['p_l'] >= THR else 'y'
    es.wr(os.path.join(OUT, 'tokens.tsv'), ['line', 'pos', 'tier', 'crop', 'x0', 'x1', 'sub', 'post', 'p_l', 'p_h', 'split', 'rh', 'rw'], items)
    c = collections.Counter(r['tier'] for r in items); s = collections.Counter(r.get('split', '-') for r in items)
    print('ink 63 y tokens', len(items), 'tiers', dict(c), 'split', dict(s), 'top sub', collections.Counter(r.get('sub') for r in q))


def cmd_gates():
    import viv63_test as t, viv54_decode as vd, judge_plaintext as jp, vivanchor_gates as vg
    tok = {(r['line'], r['pos']): r for r in es.rd(os.path.join(OUT, 'tokens.tsv'))}
    L = seqs()
    base = [c for p, l, seq in L for c, _ in seq]
    split, ypos = [], []
    for p, l, seq in L:
        for i, (c, _) in enumerate(seq):
            r = tok.get((f'{p}_{l}', str(i + 1)))
            if c == 'y':
                ypos.append(len(split))
            split.append('y_l' if (c == 'y' and r and r.get('split') == 'y_l') else c)
    nsplit = sum(c == 'y_l' for c in split)
    k = {c: v for c, (v, g) in vd.key().items()}
    k2 = dict(k, y_l='l')
    model = jp.NgramModel([jp.read_corpus(p) for p in t.FR16])
    t.SEED = '20261014ES-63'
    res = {'pages': list(PAGES), 'letters': len(base), 'y_tokens': len(ypos), 'y_l': nsplit, 'threshold': THR}
    res['unsplit'], _ = vg.wrong(model, k, base, 200, 200, '20261014ES-63u', 'U')
    res['split'], _ = vg.wrong(model, k2, split, 200, 200, '20261014ES-63s', 'S')
    # null: the same number of y positions sent to l at random
    import viv63b_test as tb
    score = tb.fast(model)
    sc = lambda seq, km: score(''.join(km.get(c, '') for c in seq))
    real = sc(split, k2); rng = random.Random(SEED); null = []
    for i in range(200):
        pick = set(rng.sample(ypos, nsplit)); s = [('y_l' if j in pick else c) for j, c in enumerate(base)]
        null.append(sc(s, k2))
    null.sort()
    res['random_split'] = {'real': round(real, 4), 'null_mean': round(float(np.mean(null)), 4), 'null_p95': round(null[189], 4),
                           'rank_above': sum(n >= real for n in null), 'unsplit': round(sc(base, k), 4), 'all_y_l': round(sc(['y_l' if c == 'y' else c for c in base], k2), 4)}
    json.dump(res, open(os.path.join(OUT, 'gates.json'), 'w'), indent=1, ensure_ascii=False)
    for x in ('unsplit', 'split'):
        r = res[x]; print(x, r['letters'], r['s'], 'b2 p99', r['b2']['null_p99'], r['b2']['pass'], 'wrong', r['c'])
    print('random split', res['random_split'])


if __name__ == '__main__':
    {'seg': cmd_seg, 'label': cmd_label, 'gates': cmd_gates}[sys.argv[1]]()
