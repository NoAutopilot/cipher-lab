#!/usr/bin/env python3
"""BIR-ADJ (4 Oct 2026): value-blind image adjudication of the tiles where the owner's sort overrode two agreeing blind
machine readers (three_reader.tsv: A == B != owner_family, status moved; 109 tiles), with a known-answer control first.
Per PREREG_adj.md beside this file. Run from the repo root:
  python3 ciphers/nevers-birago-fr3251-1572/harvest/ownersort/adj/build_adj.py --out <scratch dir>
Writes items.tsv + key.tsv (here) and one composite PNG per item (in --out): the tile on its line with two neighbours
each side (red box on the tile), then 'Strip 1' and 'Strip 2', six reference tiles each, order shuffled per item.
No sign names, values or pile names appear on any image or in items.tsv. Disk only: the page strips already on disk
(sorter/pages, birago-fr3252-1571-72/sorter/pages, the same public Gallica regions the owner sorted)."""
import csv, os, random, sys
from collections import defaultdict, Counter
from PIL import Image, ImageDraw, ImageFont
N = 'ciphers/nevers-birago-fr3251-1572'; H = os.path.dirname(os.path.abspath(__file__))
SEED = 20261004; K = 6; NCTL = 30
def tsv(p): return list(csv.DictReader(open(p), delimiter='\t'))
signs = {r['sid']: r for r in tsv(N + '/harvest/tx_decode/eye/open/sorter/owner-2026-10-03/signs.tsv')}
PDIRS = ['ciphers/birago-fr3252-1571-72/sorter/pages', N + '/sorter/pages']
def page(p):
    for d in PDIRS:
        f = f'{d}/{p}.jpg'
        if os.path.exists(f): return f
TR = tsv(N + '/harvest/ownersort/three_reader.tsv')
rows = {r['sid']: r for r in TR}
def fam(p): return p.rsplit('-', 1)[0] if p and '-' in p and len(p.rsplit('-', 1)[1]) == 1 else p
NEW = lambda p: p != fam(p)  # owner-made new pile (T60-c, X_NEW-l, ...)
# confident members of a sheet pile: all three readers agree and the owner kept the tile in that exact pile
conf = defaultdict(list); members = defaultdict(list); ab = defaultdict(list)
for r in TR:
    if r['status'] in ('kept', 'moved') and r['A'] and r['A'] == r['B']: ab[r['A']].append(r['sid'])
    if r['status'] in ('kept', 'moved'): members[r['owner_pile']].append(r['sid'])
    if r['status'] == 'kept' and r['A'] == r['B'] == r['owner_pile'] and r['A']: conf[r['A']].append(r['sid'])
def nbrs(sid):
    ln, i = sid.rsplit('_', 1); i = int(i); return {f'{ln}_{j:02d}' for j in range(i - 2, i + 3)}
def pick(pool, sid, rnd, fill=()):
    """K tiles from pool (not the tile or its neighbours); when pool is short, fill from `fill` (the second tier)."""
    pool = sorted(s for s in set(pool) if s != sid and s not in nbrs(sid) and s in signs)
    got = rnd.sample(pool, min(K, len(pool)))
    if len(got) < K:
        f2 = sorted(s for s in set(fill) if s != sid and s not in nbrs(sid) and s in signs and s not in got)
        got += rnd.sample(f2, min(K - len(got), len(f2)))
    return got
def owner_strip(r, rnd):
    q = r['owner_pile']
    if NEW(q) or q.startswith('X_'): src = [s for s in members[q] if s != r['sid']]
    else:
        return pick(conf[q], r['sid'], rnd, fill=members[q])
    return pick(src, r['sid'], rnd)

def build():
    rnd = random.Random(SEED); items = []
    # ---- target set
    D = [r for r in TR if r['status'] == 'moved' and r['A'] and r['A'] == r['B'] and r['A'] != r['owner_family']]
    for r in D:
        m = pick(conf[r['A']], r['sid'], rnd, fill=ab[r['A']]); o = owner_strip(r, rnd)
        items.append(dict(kind='target', sid=r['sid'], leaf=r['leaf'], mach_pile=r['A'], owner_pile=r['owner_pile'], m=m, o=o))
    # ---- control: all three agree, kept; wrong pile = nearest look-alike (most reader confusions with the true pile)
    cf = defaultdict(Counter)
    for r in TR:
        o = r['owner_family']
        for a, b in ((r['A'], r['B']), (r['A'], o), (r['B'], o)):
            if a and b and a != b: cf[a][b] += 1; cf[b][a] += 1
    def wrong(p, sid):
        for q, _ in sorted(cf[p].items(), key=lambda x: (-x[1], x[0])):
            if q != p and not NEW(q) and len([s for s in conf[q] if s not in nbrs(sid)]) >= K: return q
    disputed = {r['sid'] for r in D}
    cand = [r for r in TR if r['status'] == 'kept' and r['A'] == r['B'] == r['owner_pile'] and r['A'] and r['sid'] not in disputed
            and len([s for s in conf[r['A']] if s not in nbrs(r['sid'])]) > K and wrong(r['A'], r['sid'])]
    # stratify: piles in the disputed pairs first, at most 2 tiles per pile, leaves mixed
    dp = Counter(r['A'] for r in D) + Counter(fam(r['owner_pile']) for r in D)
    rnd.shuffle(cand); cand.sort(key=lambda r: -dp[r['A']])
    used = Counter(); ctl = []
    for r in cand:
        if used[r['A']] >= 4: continue
        used[r['A']] += 1; ctl.append(r)
        if len(ctl) == NCTL: break
    for r in ctl:
        w = wrong(r['A'], r['sid']); tpool = [s for s in conf[r['A']] if s != r['sid']]
        items.append(dict(kind='control', sid=r['sid'], leaf=r['leaf'], mach_pile=r['A'], owner_pile=w,
                          m=pick(tpool, r['sid'], rnd), o=pick(conf[w], r['sid'], rnd)))
    # ---- opaque ids, strip order, batches (controls: c01..; targets: t001..), shuffled within kind
    for kind, pre in (('control', 'c'), ('target', 't')):
        its = [it for it in items if it['kind'] == kind]; rnd.shuffle(its)
        for i, it in enumerate(its):
            it['item'] = f'{pre}{i + 1:03d}'; it['first'] = rnd.choice(['m', 'o'])
            it['batch'] = f'{pre}B{i // 10 + 1:02d}'
    return sorted(items, key=lambda it: it['item'])

def crop(sid, pad=6):
    s = signs[sid]; im = Image.open(page(s['page'])).convert('L'); x, y, w, h = (int(s[k]) for k in 'xywh')
    return im.crop((max(0, x - pad), max(0, y - pad), min(im.width, x + w + pad), min(im.height, y + h + pad)))
def ctx(sid):
    ln, i = sid.rsplit('_', 1); i = int(i); s = signs[sid]
    nb = [signs[f'{ln}_{j:02d}'] for j in range(i - 2, i + 3) if f'{ln}_{j:02d}' in signs]
    im = Image.open(page(s['page'])).convert('RGB')
    x0 = min(int(b['x']) for b in nb) - 10; x1 = max(int(b['x']) + int(b['w']) for b in nb) + 10
    c = im.crop((max(0, x0), 0, min(im.width, x1), im.height)); d = ImageDraw.Draw(c)
    x, y, w, h = (int(s[k]) for k in 'xywh'); x -= max(0, x0)
    d.rectangle((x - 3, y - 3, x + w + 3, y + h + 3), outline=(230, 0, 0), width=3)
    return c
def fit(im, H):
    return im.resize((max(1, round(im.width * H / im.height)), H))
def composite(it, out):
    font = ImageFont.load_default(size=22) if hasattr(ImageFont, 'load_default') else None
    c = fit(ctx(it['sid']), 170)
    strips = [it['m'], it['o']] if it['first'] == 'm' else [it['o'], it['m']]
    rows = []
    for k, st in enumerate(strips, 1):
        tl = [fit(crop(s), 100).convert('RGB') for s in st]
        W = 110 + sum(t.width + 16 for t in tl); r = Image.new('RGB', (W, 116), 'white'); dr = ImageDraw.Draw(r)
        dr.text((6, 44), f'Strip {k}', fill='black', font=font); x = 110
        for t in tl: r.paste(t, (x, 8)); x += t.width + 16
        rows.append(r)
    W = max([c.width + 20] + [r.width for r in rows]); Hh = 40 + c.height + 20 + sum(r.height + 10 for r in rows)
    im = Image.new('RGB', (W, Hh), 'white'); dr = ImageDraw.Draw(im)
    dr.text((6, 6), f'{it["item"]}: which strip shows the same sign as the one in the red box?', fill='black', font=font)
    im.paste(c, (10, 40)); y = 40 + c.height + 20
    for r in rows: im.paste(r, (0, y)); dr.line((0, y - 5, W, y - 5), fill=(160, 160, 160)); y += r.height + 10
    if im.width > 1800: im = im.resize((1800, round(im.height * 1800 / im.width)))
    im.save(f'{out}/{it["item"]}.png')

if __name__ == '__main__':
    out = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else None
    items = build()
    with open(H + '/key.tsv', 'w') as f:
        cols = ['item', 'batch', 'kind', 'sid', 'leaf', 'mach_pile', 'owner_pile', 'first', 'strip1_is', 'n_m', 'n_o', 'm_tiles', 'o_tiles']
        f.write('\t'.join(cols) + '\n')
        for it in items:
            f.write('\t'.join(str(x) for x in (it['item'], it['batch'], it['kind'], it['sid'], it['leaf'], it['mach_pile'], it['owner_pile'], it['first'],
                    'machine' if it['first'] == 'm' else 'owner', len(it['m']), len(it['o']), ','.join(it['m']), ','.join(it['o']))) + '\n')
    with open(H + '/items.tsv', 'w') as f:
        f.write('item\tbatch\n')
        for it in items: f.write(f"{it['item']}\t{it['batch']}\n")
    print(Counter(it['kind'] for it in items), 'short strips:', sum(1 for it in items if min(len(it['m']), len(it['o'])) < K),
          'empty:', [it['item'] for it in items if not it['m'] or not it['o']])
    if out:
        os.makedirs(out, exist_ok=True)
        for it in items:
            if it['m'] and it['o']: composite(it, out)
