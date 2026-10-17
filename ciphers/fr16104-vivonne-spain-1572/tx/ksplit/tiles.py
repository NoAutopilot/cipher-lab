#!/usr/bin/env python3
"""VIV-KSPLIT step 2 (PREREG-VIV-KSPLIT.md): sign tiles for tx/kcells2/packet.tsv rows that have a line crop.

    VIVKSPLIT_SCRATCH=<dir> python3 tx/ksplit/tiles.py

Per leaf (f102r, f102v, f103r): tools/glyph_atlas.py segment of the line crops (--median-h pool; s1/s2 overlap deduped at its
midpoint, as tx/vivgsplit/gsplit.py leaf_units), then tools/box_token_align.build_map (label-aware: classify top-3 box labels, lam LAM, --loo guard) of the committed
reading tx/<leaf>_rec.tsv (tx/kcells/kcells.py row_tokens, pos = its index) onto the boxes. A row gets a tile only when its (line, pos)
is mapped 1:1. ':' tokens (two-dot marks; the segmenter files them as marks) are left out of the DP. Writes tiles/<id>.png, tiles.tsv (id, page, line, pos, label: no clerk letter) and truth.tsv (id, clerk_letter, kind).
"""
import collections, csv, json, os, random, re, subprocess, sys
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); TX = os.path.dirname(H); FOLD = os.path.dirname(TX)
REPO = os.path.dirname(os.path.dirname(FOLD))
sys.path.insert(0, os.path.join(REPO, 'tools')); sys.path.insert(0, os.path.join(TX, 'kcells'))
import box_token_align as bta  # noqa: E402
import kcells as kc  # noqa: E402
W = os.environ.get('VIVKSPLIT_SCRATCH') or sys.exit('set VIVKSPLIT_SCRATCH')
PAD = 6
SKIP = {':', 'non]', '{flourish', 'cross}'}   # ':' = two dots, segmented as marks (tools/glyph_atlas marks.tsv), not boxes


def units(leaf):
    man = os.path.join(FOLD, 'images', 'manifest.json')
    cr = {}
    for e in json.load(open(man))['iiif_lines']:
        c = e['crop']
        if f'_{leaf}_L' not in c:
            continue
        ln = c.split(f'_{leaf}_')[1].split('_')[0]; sg = int(c.split('_s')[-1].split('.')[0])
        cr[(ln, sg)] = dict(path=os.path.join(FOLD, 'images', c), x0=e['box'][0], x1=e['box'][2], page=f'{leaf}_{ln}_s{sg}')
    at = os.path.join(W, f'atlas_{leaf}')
    if not os.path.exists(os.path.join(at, 'signs.tsv')):
        pages = []
        for k, e in sorted(cr.items()):
            pages += ['--page', f"{e['page']}={e['path']}"]
        p = subprocess.run([sys.executable, os.path.join(REPO, 'tools', 'glyph_atlas.py'), 'segment', '--out', at, '--median-h', 'pool'] + pages,
                           capture_output=True, text=True)
        if p.returncode:
            sys.exit(p.stdout + p.stderr)
    byline = collections.defaultdict(list)
    for r in csv.DictReader(open(os.path.join(at, 'signs.tsv')), delimiter='\t'):
        _, ln, s_ = r['page'].split('_'); sg = int(s_[1:]); e = cr[(ln, sg)]
        byline[ln].append(dict(r, seg=sg, xl=e['x0'] + int(r['x']), xc=e['x0'] + int(r['x']) + int(r['w']) / 2, img=e['path']))
    out = []
    for ln in sorted(byline):
        segs = sorted({s_ for (l2, s_) in cr if l2 == ln})
        for b in byline[ln]:
            sg = b['seg']
            lo = -1e9 if sg == segs[0] else (cr[(ln, sg)]['x0'] + cr[(ln, sg - 1)]['x1']) / 2
            hi = 1e9 if sg == segs[-1] else (cr[(ln, sg + 1)]['x0'] + cr[(ln, sg)]['x1']) / 2
            if lo <= b['xc'] < hi:
                out.append(dict(sid=b['sid'], page=leaf, line=str(int(ln[1:])), x=str(int(b['xl'])), w=b['w'], img=b['img'],
                                cx=int(b['x']), cy=int(b['y']), cw=int(b['w']), ch=int(b['h'])))
    return out


def topk(leaf, us):
    """Truth-blind box labels for the label-aware DP: classify (k=5, top 3) against tx/vivcls/train/labels_r2_both.tsv (reader
    reference signs of f.102r/f.103r, never a clerk letter), on the f.102r+f.103r atlas of tx/vivcls/seg.py (f.201r left out: its
    crops are not on disk), as tx/vivgsplit/gsplit.py new_leaf_tiles."""
    at = os.path.join(TX, 'vivcls', 'atlas')
    tk = os.path.join(W, f'topk_{leaf}.tsv')
    if os.path.exists(tk):
        return tk
    bx = os.path.join(W, f'boxes_{leaf}.tsv')
    with open(bx, 'w') as f:
        f.write('box_id\timage\tx\ty\tw\th\tline\tpos\tkind\n')
        for u in us:
            f.write(f"{u['sid']}\t{u['img']}\t{u['cx']}\t{u['cy']}\t{u['cw']}\t{u['ch']}\t{u['line']}\t{u['x']}\tsign\n")
    have = {r['sid'] for r in csv.DictReader(open(os.path.join(at, 'signs.tsv')), delimiter='\t')}
    tl = os.path.join(W, 'train_labels.tsv')        # labels_r2_both less the 3 boxes the f.201r-free atlas does not hold
    with open(tl, 'w') as f:
        src = open(os.path.join(TX, 'vivcls', 'train', 'labels_r2_both.tsv')).read().splitlines()
        f.write('\n'.join([src[0]] + [l for l in src[1:] if l.split('\t')[0] in have]) + '\n')
    lj = os.path.join(W, 'labels_stub.json')
    json.dump({'signs': {}, 'marks': {}, 'override': {}}, open(lj, 'w'))
    ct = os.path.join(at, 'clusters.tsv')
    if not os.path.exists(ct):
        open(ct, 'w').write('kind\tid\tcluster\n')
    p = subprocess.run([sys.executable, os.path.join(REPO, 'tools', 'glyph_atlas.py'), 'classify', '--out', at, '--labels', lj, '--boxes', bx,
                        '--boxes-median-h', '58', '--only-train-labels', '--train-labels',
                        tl, '--knn', '5', '--topk', '3', '--tsv', tk],
                       capture_output=True, text=True)
    if p.returncode:
        sys.exit(p.stdout + p.stderr)
    return tk


def read(leaf):
    rows = []
    for ln in open(os.path.join(TX, f'{leaf}_rec.tsv'), encoding='utf-8'):
        if ln.startswith('row\t') or not ln.strip():
            continue
        parts = ln.rstrip('\n').split('\t', 1)
        if len(parts) < 2 or parts[1].strip() == 'DUP':
            continue
        for i, t in enumerate(kc.row_tokens(parts[1])):
            if re.fullmatch(r'\{.*\}', t) or t in SKIP:
                continue
            rows.append(dict(line=f'{leaf}_L{int(parts[0][1:]):02d}', pos=str(i), sign=t, rline=parts[0]))
    return rows


def main():
    pk = [r for r in csv.DictReader(open(os.path.join(TX, 'kcells2', 'packet.tsv')), delimiter='\t') if r['crop']]
    os.makedirs(os.path.join(H, 'tiles'), exist_ok=True)
    tiles, truth, cnt = [], [], collections.Counter()
    for leaf in sorted({r['page'] for r in pk}):
        us = units(leaf); usid = {u['sid']: u for u in us}
        rd = read(leaf)
        rows, per = bta.build_map(us, rd, labels=bta.read_labels(topk=topk(leaf, us)), lam=bta.LAM, loo=True)
        by = collections.defaultdict(list)
        for r in rows:
            if r['sid']:
                by[(r['line'], str(r['pos']))].append(r)
        one = {k: v[0]['sid'] for k, v in by.items() if len(v) == 1 and v[0]['op'] == '1:1'}
        for r in [r for r in pk if r['page'] == leaf]:
            key = (f"{leaf}_L{int(r['line'][1:]):02d}", r['pos'])
            cnt[(r['label'], 'rows')] += 1
            s = one.get(key)
            if not s:
                cnt[(r['label'], 'unmapped')] += 1
                continue
            u = usid[s]
            im = Image.open(u['img']).convert('L')
            box = (max(0, u['cx'] - PAD), max(0, u['cy'] - PAD), min(im.width, u['cx'] + u['cw'] + PAD), min(im.height, u['cy'] + u['ch'] + PAD))
            tid = f"{leaf}_{r['line']}_{int(r['pos']):03d}"
            im.crop(box).save(os.path.join(H, 'tiles', tid + '.png'))
            tiles.append(dict(id=tid, page=leaf, line=r['line'], pos=r['pos'], label=r['label'], sid=s,
                              img=os.path.relpath(u['img'], FOLD), x=box[0], y=box[1], w=box[2] - box[0], h=box[3] - box[1]))
            truth.append(dict(id=tid, clerk_letter=r['clerk_letter'], kind=r['kind']))
            cnt[(r['label'], 'tile')] += 1
    tiles.sort(key=lambda t: t['id']); truth.sort(key=lambda t: t['id'])
    for name, rows, cols in (('tiles.tsv', tiles, ['id', 'page', 'line', 'pos', 'label', 'sid', 'img', 'x', 'y', 'w', 'h']),
                             ('truth.tsv', truth, ['id', 'clerk_letter', 'kind'])):
        with open(os.path.join(H, name), 'w') as f:
            f.write('\t'.join(cols) + '\n' + ''.join('\t'.join(str(t[c]) for c in cols) + '\n' for t in rows))
    print(dict(cnt))


if __name__ == '__main__':
    main()
