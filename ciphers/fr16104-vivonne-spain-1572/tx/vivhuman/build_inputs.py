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

--packet3 (PREREG-VIVPACKET3.md, VIV-PACKET3): question tiles from f.191r L08-L16/L29-L32 (M/U/split tokens, the five V_strict
stretches first, cap 40, pen units segmented on the VIV-F191 crops and mapped 1:1 to pass C's tokens); piles one per key.tsv code,
members only truth-consistent tiles of f.102r, f.103r, f.201r (cap 12, seed 20261014), every tile shown on its own line crop;
output tx/sorter_f191/ (questions.tsv, piles.tsv, signs/labels/focus/cipher_lines; pages/ and atlas/ untracked).
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
CAP = 12
LEAF2 = {'f102r': ('vivonne1573-f102r-dev2.truth.tsv', 'map_r2_f102r.tsv'),
         'f103r': ('vivonne1573-f103r-confirm2.truth.tsv', 'map_r2_f103r.tsv')}


def extra_leaves(cand, ms, qsids, crops, out):
    """Addendum C: truth-consistent look-alike tiles of f.102r and f.103r, each shown on its own line crop (page = crop stem)."""
    man = {e['crop']: e for e in json.load(open(os.path.join(FOLD, 'images', 'manifest.json')))['iiif_lines']}
    for leaf, (tf, mf) in LEAF2.items():
        tr = {(r['line'], r['pos']): r for r in sets.rd(os.path.join(sets.BT, tf))}
        per = collections.defaultdict(list)
        for m in sets.rd(os.path.join(FOLD, 'tx', 'vivcls', 'train', mf)):
            if m['op'] == '1:1':
                per[(m['line'], m['pos'])].append(m['sid'])
        for (ln, pos), sids in per.items():
            r = tr.get((ln, pos))
            if len(sids) != 1 or sids[0] in qsids or not r or r['ref_sign'] not in FILTERED:
                continue
            if r['status'] != 'scored' or r['flag'] or r['ref_sign'] not in set(filter(None, r['truth'].split('|'))):
                continue
            m = ms[sids[0]]
            cname = next(c for c in man if c.endswith('_' + m['crop_page'] + '.jpg'))
            e = man[cname]
            if cname not in crops:
                crops[cname] = Image.open(os.path.join(FOLD, 'images', cname))
            X, w = int(m['x']), int(m['w'])
            cy, h = ink_rows(crops[cname], X - e['box'][0], X - e['box'][0] + w)
            pg = cname[:-4]
            dst = os.path.join(out, 'pages', cname)
            if not os.path.exists(dst):
                crops[cname].save(dst, quality=92)
            cand[r['ref_sign']].append((leaf, ln, int(float(pos)), dict(sid=sids[0], page=pg, x=X - e['box'][0], y=cy, w=w, h=h)))
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
    cand = collections.defaultdict(list)   # Addendum C: look-alike label -> [(leaf, line, pos, sign row)]
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
        signs_row = dict(sid=sid, page='f201r', x=xr, y=int(round(yr)), w=w, h=h)
        signs.append(signs_row)
        if sid in q:
            labels.append(dict(sid=sid, sign=QPILE, family='to place'))
        else:
            lab = ref[(ln, tp)]
            if attempt == 2 and lab in FILTERED:
                signs.pop()
                r = trow[(ln, tp)]
                if r['status'] == 'scored' and not r['flag'] and lab in set(filter(None, r['truth'].split('|'))):
                    cand[lab].append(('f201r', ln, int(float(tp)), signs_row))
                continue
            labels.append(dict(sid=sid, sign=lab, family='f201r'))
    if attempt == 2:
        before = collections.Counter(l['sign'] for l in sets.rd(os.path.join(OUT, 'labels.tsv')) if l['family'] == 'f201r')
        extra_leaves(cand, ms, set(q), crops, out)
        rng = random.Random(sets.SEED)
        filt = []
        for lab in sorted(FILTERED):
            c = sorted(cand[lab], key=lambda z: (z[0], z[1], z[2]))
            pick = c if len(c) <= CAP else rng.sample(c, CAP)
            for z in pick:
                signs.append(z[3]); labels.append(dict(sid=z[3]['sid'], sign=lab, family='f201r'))
            by = collections.Counter(z[0] for z in pick)
            filt.append(dict(label=lab, attempt1_f201r=before.get(lab, 0), qualifying=len(c), shown=len(pick),
                             f102r=by['f102r'], f103r=by['f103r'], f201r=by['f201r']))
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
        cols = ['label', 'attempt1_f201r', 'qualifying', 'shown', 'f102r', 'f103r', 'f201r']
        with open(os.path.join(out, 'filter.tsv'), 'w') as fh:
            fh.write('# PREREG-VIVHUMAN.md Addendum C pile members (build_inputs.py --attempt 2; cap %d, seed %d)\n' % (CAP, sets.SEED))
            fh.write('\t'.join(cols) + '\n')
            for r in filt:
                fh.write('\t'.join(str(r[c]) for c in cols) + '\n')
        for r in filt:
            print(r)
        with open(os.path.join(out, 'cipher_lines.tsv'), 'w') as fh:
            fh.write('# f.201r cipher region + the f.102r/f.103r line crops holding pile tiles (Addendum C); every page image is cipher\n')
            for pg in sorted({s['page'] for s in signs}):
                fh.write(pg + '\n')
    print('tiles', len(signs), 'question tiles', len(q), 'piles', len({l['sign'] for l in labels}), 'skipped', dict(skipped))


P3_LINES = [f'L{i:02d}' for i in list(range(8, 17)) + list(range(29, 33))]
P3_CROPS = os.path.join(FOLD, 'images', 'p63', 'f191')
P3_CAP = 40


def p3_questions(out):
    """PREREG-VIVPACKET3 section 1-2: candidates, priority, f.191r pen units, 1:1 tile per candidate."""
    import subprocess
    sys.path.insert(0, os.path.join(FOLD, 'tx', 'viv63_f191'))
    import f191, viv53G_decode as g, viv53L_stretches as st, box_token_align as bta
    P, lines, _, _ = f191.build()
    s, meta = f191.page_letters(lines)
    V, _ = g.strict_vocab()
    tops = st.top(s, V, 5)
    tier = {}
    for rank, (ln, b, e, words) in enumerate(tops, 1):
        for i in range(b, e):
            tier.setdefault(i, rank)
    # rec position -> pass C token index (1-based), following f191.build's columns and its oo merge
    cidx = {}
    for line in P3_LINES:
        toks, ci = [], 0
        for c in f191.cols(P, line):
            sgn, flag, how = f191.decide(c)
            k = None
            if c[2] != '-':
                ci += 1; k = ci
            if sgn is None:
                continue
            toks.append([sgn, k])
        seq, i = [], 0
        while i < len(toks):
            if toks[i][0] == 'o' and i + 1 < len(toks) and toks[i + 1][0] == 'o':
                seq.append(None); i += 2
            else:
                seq.append(toks[i][1]); i += 1
        for pos, k in enumerate(seq, 1):
            cidx[(line, pos)] = k
    # pen units on the eligible lines' crops (as tx/vivcls/seg.py)
    man = {e['crop']: e for e in json.load(open(os.path.join(P3_CROPS, 'manifest.json')))['iiif_lines']}
    cr = {}
    for c, e in man.items():
        ln, sg = c.split('_')[3], int(c.split('_s')[-1].split('.')[0])
        if ln in P3_LINES:
            cr[(ln, sg)] = dict(path=os.path.join(P3_CROPS, c), x0=e['box'][0], x1=e['box'][2], page=f'f191r_{ln}_s{sg}', crop=c)
    atl = os.path.join(out, 'atlas')
    os.makedirs(atl, exist_ok=True)
    cmd = [sys.executable, os.path.join(sets.REPO, 'tools/glyph_atlas.py'), 'segment', '--out', atl, '--median-h', 'pool']
    for k, e in sorted(cr.items()):
        cmd += ['--page', f"{e['page']}={e['path']}"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stdout + r.stderr)
    byline = collections.defaultdict(list)
    for row in sets.rd(os.path.join(atl, 'signs.tsv')):
        _, ln, sgs = row['page'].split('_')
        sg = int(sgs[1:]); e = cr[(ln, sg)]
        byline[ln].append(dict(row, seg=sg, xl=e['x0'] + int(row['x']), xc=e['x0'] + int(row['x']) + int(row['w']) / 2))
    units = []
    for ln, bs in byline.items():
        segs = sorted(sg for (l2, sg) in cr if l2 == ln)
        for b in bs:
            sg = b['seg']
            lo = -1e9 if sg == segs[0] else (cr[(ln, sg)]['x0'] + cr[(ln, sg - 1)]['x1']) / 2
            hi = 1e9 if sg == segs[-1] else (cr[(ln, sg + 1)]['x0'] + cr[(ln, sg)]['x1']) / 2
            if lo <= b['xc'] < hi:
                units.append(dict(sid=b['sid'], page='f191r', line=str(int(ln[1:])), x=b['xl'], w=b['w'], crop=cr[(ln, sg)]['crop']))
    read = [dict(line=f'f191r_{ln}', pos=str(k), sign=t) for ln in P3_LINES for k, t in enumerate(P['C'].get(ln, []), 1)]
    rows, _ = bta.build_map(units, read)
    by = collections.defaultdict(list)
    for m in rows:
        if m['sid']:
            by[(m['line'], str(m['pos']))].append(m)
    tile = {k: v[0]['sid'] for k, v in by.items() if len(v) == 1 and v[0]['op'] == '1:1'}
    ub = {u['sid']: u for u in units}
    cand = []
    for i, m in enumerate(meta):
        if m['line'] not in P3_LINES:
            continue
        v = m['votes']; code = m['code']
        cells = list(v[:3]) + ([v[3]] if int(m['line'][1:]) <= 21 else [])
        split = len(set(cells)) > 1
        if not (m['g'] in 'MU' or split):
            continue
        why = '' ; sid = ''
        k = cidx.get((m['line'], m['pos']))
        if code == 'oo':
            why = 'oo token (two columns)'
        elif k is None:
            why = 'pass C has no token here'
        else:
            sid = tile.get((f"f191r_{m['line']}", str(k)), '')
            if not sid:
                why = 'no single 1:1 box on pass C token %d' % k
        cand.append(dict(tier=tier.get(i, 9), line=m['line'], pos=m['pos'], code=code, grade=m['g'], split=int(split),
                         votes='/'.join(v), letter=s[i], ctok=k or '', sid=sid, why=why))
    cand.sort(key=lambda c: (c['tier'], c['line'], c['pos']))
    take = [c for c in cand if c['sid']][:P3_CAP]
    for c in cand:
        c['taken'] = int(c in take)
    return cand, take, ub


def packet3():
    out = os.path.join(FOLD, 'tx', 'sorter_f191')
    os.makedirs(os.path.join(out, 'pages'), exist_ok=True)
    cand, take, ub = p3_questions(out)
    rng = random.Random(sets.SEED)
    order = list(take); rng.shuffle(order)
    for n, c in enumerate(order, 1):
        c['qid'] = f'Q{n:02d}'
    key = {r['code']: r['meaning'] for r in sets.rd(os.path.join(FOLD, 'key.tsv'))}
    crops, signs, labels = {}, [], []

    def add_tile(sid, path, cname, X0, X, w, lab, fam):
        if cname not in crops:
            crops[cname] = Image.open(path)
            crops[cname].save(os.path.join(out, 'pages', cname), quality=92)
        cy, h = ink_rows(crops[cname], X - X0, X - X0 + w)
        signs.append(dict(sid=sid, page=cname[:-4], x=X - X0, y=cy, w=w, h=h))
        labels.append(dict(sid=sid, sign=lab, family=fam))
    m191 = {e['crop']: e for e in json.load(open(os.path.join(P3_CROPS, 'manifest.json')))['iiif_lines']}
    for c in order:
        u = ub[c['sid']]
        add_tile(c['sid'], os.path.join(P3_CROPS, u['crop']), u['crop'], m191[u['crop']]['box'][0], int(u['x']), int(u['w']),
                 QPILE, 'to place')
    # piles: every key code, truth-consistent tiles of the three mapped truth leaves
    ms = {r['sid']: r for r in sets.rd(os.path.join(FOLD, 'tx', 'vivcls', 'map_signs.tsv'))}
    pool = collections.defaultdict(list)

    def ok(r, lab):
        return (r and r['status'] == 'scored' and not r['flag'] and lab in key and lab in set(filter(None, r['truth'].split('|')))
                and r['plain'] == key[lab])
    mimg = {e['crop']: e for e in json.load(open(os.path.join(FOLD, 'images', 'manifest.json')))['iiif_lines']}
    for leaf, (tf, mf) in LEAF2.items():
        tr = {(r['line'], r['pos']): r for r in sets.rd(os.path.join(sets.BT, tf))}
        per = collections.defaultdict(list)
        for m in sets.rd(os.path.join(FOLD, 'tx', 'vivcls', 'train', mf)):
            if m['op'] == '1:1':
                per[(m['line'], m['pos'])].append(m['sid'])
        for (ln, pos), sids in per.items():
            r = tr.get((ln, pos))
            if len(sids) != 1 or not r or not ok(r, r['ref_sign']):
                continue
            m = ms[sids[0]]
            cname = next(cn for cn in mimg if cn.endswith('_' + m['crop_page'] + '.jpg'))
            pool[r['ref_sign']].append((leaf, ln, float(pos), sids[0], os.path.join(FOLD, 'images', cname), cname,
                                        mimg[cname]['box'][0], int(m['x']), int(m['w']), r['plain']))
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
    mcut = {e['crop']: e for e in json.load(open(os.path.join(CUT, 'manifest.json')))['iiif_lines']}
    for (ln, ap), sids in per.items():
        tp = a2t.get((ln, ap))
        r = trow.get((ln, tp)) if tp is not None else None
        if len(sids) != 1 or not r or not ok(r, r['ref_sign']):
            continue
        m = ms[sids[0]]
        cname = 'c206_' + m['crop_page'] + '.jpg'
        pool[r['ref_sign']].append(('f201r', ln, float(tp), sids[0], os.path.join(CUT, cname), cname, mcut[cname]['box'][0],
                                    int(m['x']), int(m['w']), r['plain']))
    piles = []
    for code in key:
        c = sorted(pool.get(code, []), key=lambda z: (z[0], z[1], z[2]))
        pick = c if len(c) <= CAP else random.Random(sets.SEED).sample(c, CAP)
        for z in pick:
            add_tile(z[3], z[4], z[5], z[6], z[7], z[8], code, 'pile')
        by = collections.Counter(z[0] for z in pick)
        piles.append(dict(code=code, meaning=key[code], qualifying=len(c), shown=len(pick), f102r=by['f102r'], f103r=by['f103r'],
                          f201r=by['f201r'], truth_letters='|'.join(sorted({z[9] for z in pick})), members=','.join(z[3] for z in pick)))
    def w(name, cols, rows, head=''):
        with open(os.path.join(out, name), 'w') as fh:
            fh.write(head + '\t'.join(cols) + '\n')
            for r in rows:
                fh.write('\t'.join(str(r[c]) for c in cols) + '\n')
    w('signs.tsv', ['sid', 'page', 'x', 'y', 'w', 'h'], signs)
    w('labels.tsv', ['sid', 'sign', 'family'], labels)
    with open(os.path.join(out, 'focus.tsv'), 'w') as fh:
        for c in order:
            fh.write(f"{c['sid']}\t{c['qid']}: {QUESTION}\n")
    with open(os.path.join(out, 'cipher_lines.tsv'), 'w') as fh:
        fh.write('# f.191r question line crops + the f.102r/f.103r/f.201r line crops holding pile tiles; every page image is cipher\n')
        for pg in sorted({s['page'] for s in signs}):
            fh.write(pg + '\n')
    qid = {c['sid']: c['qid'] for c in order}
    for c in cand:
        c['qid'] = qid.get(c['sid'], '') if c['taken'] else ''
    w('questions.tsv', ['qid', 'tier', 'line', 'pos', 'code', 'letter', 'grade', 'split', 'votes', 'ctok', 'sid', 'taken', 'why'], cand,
      '# PREREG-VIVPACKET3 candidates (f.191r L08-L16/L29-L32 M/U/split), priority order; taken = the page\'s questions (cap 40)\n')
    w('piles.tsv', ['code', 'meaning', 'qualifying', 'shown', 'f102r', 'f103r', 'f201r', 'truth_letters', 'members'], piles,
      '# PREREG-VIVPACKET3 piles: one per key.tsv code, truth-consistent tiles only (cap %d, seed %d)\n' % (CAP, sets.SEED))
    print('candidates', len(cand), 'tileable', sum(bool(c['sid']) for c in cand), 'questions', len(order),
          'piles', sum(p['shown'] > 0 for p in piles), 'no pile', [p['code'] for p in piles if not p['shown']],
          'tiles', len(signs), 'pages', len(crops))


if __name__ == '__main__' and '--packet3' in sys.argv:
    packet3()
elif __name__ == '__main__':
    main(attempt=int(sys.argv[sys.argv.index('--attempt') + 1]) if '--attempt' in sys.argv else 1)
