#!/usr/bin/env python3
"""SORTER-STEP1-INK63 (15 Oct 2026): the certain-answer tile pool of the truth leaves and the step-1 sample.

A certain-answer tile = a single pen-unit box mapped 1:1 to a scored, unflagged truth position whose reader label is one of the
position's truth letters and whose key meaning is the clerk's letter there (tx/vivhuman/build_inputs.py packet3's `ok`, without
its cap of 12). Leaves: f.102r, f.103r (maps tx/vivcls/train/map_r2_*), f.201r (tx/vivcls/real/map_r2_f201r.tsv via pass A's
alignment). f.201v, f.202r, f.211r, f.211v have no box map (their VIV-67C/70C2 line crops were cut in a scratchpad, not committed):
not available. Sample: per key code min(n, Q), Q the largest quota keeping the total <= CAP (seed 20261015).

  python3 ciphers/fr16104-vivonne-spain-1572/tx/sorter_step1/pool.py           # writes pool.tsv, sample.tsv, signs_disk.tsv, pages/
  python3 ciphers/fr16104-vivonne-spain-1572/tx/sorter_step1/pool.py --check   # exit 1 if pool.tsv/sample.tsv are stale
Code labels stay in these files (the answer key of the consuming test); none reaches the page.
"""
import collections, csv, io, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
FOLD = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(FOLD, 'tx', 'vivhuman'))
import sets  # noqa: E402
import build_inputs as bi  # noqa: E402
CAP, SEED, MINEX = 300, 20261015, 6


def pool():
    key = {r['code']: r['meaning'] for r in sets.rd(os.path.join(FOLD, 'key.tsv'))}
    ms = {r['sid']: r for r in sets.rd(os.path.join(FOLD, 'tx', 'vivcls', 'map_signs.tsv'))}

    def ok(r, lab):
        return (r and r['status'] == 'scored' and not r['flag'] and lab in key and lab in set(filter(None, r['truth'].split('|')))
                and r['plain'] == key[lab])
    out = []
    for leaf, (tf, mf) in bi.LEAF2.items():
        tr = {(r['line'], r['pos']): r for r in sets.rd(os.path.join(sets.BT, tf))}
        per = collections.defaultdict(list)
        for m in sets.rd(os.path.join(FOLD, 'tx', 'vivcls', 'train', mf)):
            if m['op'] == '1:1':
                per[(m['line'], m['pos'])].append(m['sid'])
        for (ln, pos), sids in per.items():
            r = tr.get((ln, pos))
            if len(sids) == 1 and r and ok(r, r['ref_sign']):
                out.append(dict(sid=sids[0], leaf=leaf, line=ln, pos=pos, code=r['ref_sign'], plain=r['plain'], crop_page=ms[sids[0]]['crop_page'],
                                x=ms[sids[0]]['x'], w=ms[sids[0]]['w']))
    truth = sets.rd(sets.TRUTH)
    tl = collections.defaultdict(list)
    for r in truth:
        tl[r['line']].append(r)
    for ln in tl:
        tl[ln].sort(key=lambda r: float(r['pos']))
    A = sets.aligned(tl, sets.rd(os.path.join(sets.OUTS, 'passA.tsv')))
    a2t = {(ln, ap): tp for (ln, tp), (sg, ap) in A.items()}
    trow = {(r['line'], r['pos']): r for r in truth}
    per = collections.defaultdict(list)
    for m in sets.rd(sets.MAP):
        if m['op'] == '1:1':
            per[(m['line'], m['pos'])].append(m['sid'])
    for (ln, ap), sids in per.items():
        tp = a2t.get((ln, ap))
        r = trow.get((ln, tp)) if tp is not None else None
        if len(sids) == 1 and r and ok(r, r['ref_sign']):
            out.append(dict(sid=sids[0], leaf='f201r', line=ln, pos=tp, code=r['ref_sign'], plain=r['plain'], crop_page='', x='', w=''))
    out.sort(key=lambda z: (z['leaf'], z['line'], float(z['pos'])))
    return out, key


def sample(rows):
    by = collections.defaultdict(list)
    for z in rows:
        by[z['code']].append(z)
    q = max(k for k in range(1, 1000) if sum(min(len(v), k) for v in by.values()) <= CAP or k == 1)
    rng = random.Random(SEED)
    pick = []
    for code in sorted(by):
        v = by[code]
        pick += v if len(v) <= q else rng.sample(v, q)
    pick.sort(key=lambda z: (z['leaf'], z['line'], float(z['pos'])))
    return pick, q, by


COLS = ['sid', 'leaf', 'line', 'pos', 'code', 'plain']


def tsv(rows, head):
    s = io.StringIO()
    s.write(head + '\t'.join(COLS) + '\n')
    for r in rows:
        s.write('\t'.join(str(r[c]) for c in COLS) + '\n')
    return s.getvalue()


def main():
    rows, key = pool()
    pick, q, by = sample(rows)
    files = {'pool.tsv': tsv(rows, '# SORTER-STEP1-INK63 certain-answer tiles of f.102r, f.103r, f.201r (pool.py); code = truth-consistent reader label\n'),
             'sample.tsv': tsv(pick, f'# SORTER-STEP1-INK63 sample: per code min(n, {q}), total <= {CAP}, seed {SEED}\n')}
    if '--check' in sys.argv:
        stale = [f for f, s in files.items() if open(os.path.join(HERE, f)).read() != s]
        print('stale: ' + ', '.join(stale) if stale else 'pool.py --check: OK')
        sys.exit(1 if stale else 0)
    for f, s in files.items():
        open(os.path.join(HERE, f), 'w').write(s)
    # f.102r/f.103r tiles: line crops on disk -> signs_disk.tsv + pages/ (sign_sorter --signs/--pages); f.201r comes from the committed page
    from PIL import Image
    man = {e['crop']: e for e in json.load(open(os.path.join(FOLD, 'images', 'manifest.json')))['iiif_lines']}
    os.makedirs(os.path.join(HERE, 'pages'), exist_ok=True)
    crops, sg = {}, []
    for z in pick:
        if z['leaf'] == 'f201r':
            continue
        cname = next(c for c in man if c.endswith('_' + z['crop_page'] + '.jpg'))
        if cname not in crops:
            crops[cname] = Image.open(os.path.join(FOLD, 'images', cname))
        X0 = man[cname]['box'][0]
        X, w = int(z['x']), int(z['w'])
        cy, h = bi.ink_rows(crops[cname], X - X0, X - X0 + w)
        sg.append(dict(sid=z['sid'], page=cname[:-4], x=X - X0, y=cy, w=w, h=h))
    with open(os.path.join(HERE, 'signs_disk.tsv'), 'w') as f:
        f.write('sid\tpage\tx\ty\tw\th\n' + ''.join(f"{s['sid']}\t{s['page']}\t{s['x']}\t{s['y']}\t{s['w']}\t{s['h']}\n" for s in sg))
    for c in crops:
        os.symlink(os.path.join('..', '..', '..', 'images', c), os.path.join(HERE, 'pages', c)) if not os.path.exists(os.path.join(HERE, 'pages', c)) else None
    n = collections.Counter(z['code'] for z in pick)
    print(f'pool {len(rows)} tiles ({dict(collections.Counter(z["leaf"] for z in rows))}), {len(by)} codes; quota {q}; sample {len(pick)} '
          f'({dict(collections.Counter(z["leaf"] for z in pick))}); codes under {MINEX}: ' +
          (', '.join(f'{c}:{n[c]}' for c in sorted(n) if n[c] < MINEX) or 'none') + '; key codes with no tile: ' +
          (', '.join(sorted(set(key) - set(n))) or 'none'))


if __name__ == '__main__':
    main()
