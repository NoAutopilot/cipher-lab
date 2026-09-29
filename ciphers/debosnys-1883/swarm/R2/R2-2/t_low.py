#!/usr/bin/env python3
"""R2-2 T-LOW (DEB-SWARM2-R2-2, 29 Sept 2026). Subcommands:
  tiles              cut glyphs/inventory.png into 8 reference tiles (+ id list) -> $OUT/ref/
  control            build the synthetic known-answer page (PREREG.md) -> $OUT/control/ crops + truth (kept out of
                     the readers' folder) ; writes control_design.tsv here (targets' true ids, written after scoring)
  real               cut the real target crops (156 disputed + 90 audit, c1+c2) -> $OUT/real/, targets.tsv here
  score-control R1.tsv R2.tsv   control error per PREREG.md
  score-real R1.tsv R2.tsv      adjudication + noise estimate per PREREG.md
Crops: target box plus two neighbours each side, target outlined red, 4x Lanczos. Public PNGs only."""
import csv, json, os, sys, random, collections
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '../../..'))
OUT = os.environ.get('OUT', '/tmp/r22'); SEED = 20260929
FOLDS = {'PCT-SLASH': 'PCT', 'X-DOT': 'X', 'X-CURL': 'X'}
MARKS = {'BLOB', 'BAR-SOLID', 'HOOK-L', 'DASH-V', '_', 'MARK'}   # RULE.md: marks, not signs
def fold(s, rule=True):
    s = FOLDS.get(s, s)
    return '_' if rule and s in MARKS else s
R = lambda *p: os.path.join(ROOT, *p)
pages = json.load(open(R('glyphs/pages.json')))
signs = {r['sid']: r for r in csv.DictReader(open(R('glyphs/signs.tsv')), delimiter='\t')}
def sid(line, pos): pg, l = line.split('_L'); return f"{pg}_{int(l):02d}_{int(pos):03d}"
def draft(p): return {(r['line'], int(r['position'])): r for r in csv.DictReader(open(R(p)), delimiter='\t')}
D12 = {**draft('ciphertext_c1_draft.tsv'), **draft('ciphertext_c2_draft.tsv')}
D34 = draft('ciphertext_c34_draft.tsv')
_imgs = {}
def page(p):
    if p not in _imgs: _imgs[p] = Image.open(R('images', os.path.basename(pages[p]['image']))).convert('L')
    return _imgs[p]
def box(s):
    r = signs[s]; bx, by = pages[r['page']]['box'][:2]; return int(r['x']) + bx, int(r['y']) + by, int(r['w']), int(r['h'])
def crop_real(line, pos, name, outdir):
    """Target (line,pos) with two neighbours each side, from the page itself."""
    ks = [sid(line, p) for p in range(pos - 2, pos + 3) if sid(line, p) in signs]
    bs = [box(k) for k in ks]; x0 = min(b[0] for b in bs) - 8; x1 = max(b[0] + b[2] for b in bs) + 8
    y0 = min(b[1] for b in bs) - 8; y1 = max(b[1] + b[3] for b in bs) + 8
    im = page(signs[sid(line, pos)]['page']).crop((x0, y0, x1, y1)).convert('RGB')
    x, y, w, h = box(sid(line, pos)); d = ImageDraw.Draw(im); d.rectangle((x - x0 - 2, y - y0 - 2, x - x0 + w + 1, y - y0 + h + 1), outline=(255, 0, 0))
    im.resize((im.width * 4, im.height * 4), Image.LANCZOS).save(os.path.join(outdir, name + '.png'))
def tiles():
    o = os.path.join(OUT, 'ref'); os.makedirs(o, exist_ok=True); im = Image.open(R('glyphs/inventory.png'))
    ids = [r['sign'] for r in csv.DictReader(open(R('glyphs/inventory.tsv')), delimiter='\t')]
    step = im.height / len(ids)
    for t in range(0, len(ids), 20):
        im.crop((0, round(t * step), im.width, round(min(len(ids), t + 20) * step))).save(os.path.join(o, f'inv_{t // 20:02d}.png'))
    open(os.path.join(o, 'ids.txt'), 'w').write(' '.join(ids) + ' MULTI _\n'); print(len(ids), 'ids,', (len(ids) + 19) // 20, 'tiles in', o)
def control():
    rnd = random.Random(SEED); o = os.path.join(OUT, 'control'); os.makedirs(o, exist_ok=True)
    ex = set(); [ex.update(r['exemplars'].split(',')) for r in csv.DictReader(open(R('glyphs/inventory.tsv')), delimiter='\t')]
    elig = collections.defaultdict(list)
    for d in (D12, D34):
        for (l, p), r in d.items():
            s = sid(l, p)
            if r['why'] == 'agree-AB' and r['sign'] not in ('_', 'MULTI') and s in signs and s not in ex: elig[r['sign']].append(s)
    votes = []
    for (l, p), r in D12.items():
        if r['why'] in ('three-way', 'seg-flag-C', 'family-settled', 'base-settled'):
            vs = [r['sign']] + [a.split(':')[1] for a in r['alt'].split(';') if ':' in a]
            votes += [v for v in vs if v in elig]
    neigh = [r['sign'] for r in D12.values() if r['sign'] in elig]
    used = set(); rows = []; med = 23
    for L in range(12):
        seq = [('n', rnd.choice(neigh)) for _ in range(2)] + [('t', rnd.choice(votes)) for _ in range(8)] + [('n', rnd.choice(neigh)) for _ in range(2)]
        inst = []
        for kind, s in seq:
            pool = [k for k in elig[s] if k not in used] or elig[s]; k = rnd.choice(pool); used.add(k); inst.append((kind, s, k))
        # render the line: each box with 3 px of its own surround, on paper grey, gap 9 px, vertical by dy
        bs = [box(k) for _, _, k in inst]; W = sum(b[2] + 6 for b in bs) + 9 * (len(bs) + 1); H = 100
        canvas = Image.new('L', (W, H), 222); x = 9; pos = []
        for (kind, s, k), (bx, by, w, h) in zip(inst, bs):
            patch = page(signs[k]['page']).crop((bx - 3, by - 3, bx + w + 3, by + h + 3))
            yc = int(50 + float(signs[k]['dy'] or 0) * med - (h + 6) / 2); canvas.paste(patch, (x, yc)); pos.append((x + 3, yc + 3, w, h)); x += w + 6 + 9
        for i in range(2, 10):
            xs = pos[i - 2:i + 3]; x0 = min(p[0] for p in xs) - 8; x1 = max(p[0] + p[2] for p in xs) + 8
            y0 = max(0, min(p[1] for p in xs) - 8); y1 = min(H, max(p[1] + p[3] for p in xs) + 8)
            im = canvas.crop((x0, y0, x1, y1)).convert('RGB'); tx, ty, w, h = pos[i]
            ImageDraw.Draw(im).rectangle((tx - x0 - 2, ty - y0 - 2, tx - x0 + w + 1, ty - y0 + h + 1), outline=(255, 0, 0))
            name = f's{L + 1:02d}_{i - 1}'; im.resize((im.width * 4, im.height * 4), Image.LANCZOS).save(os.path.join(o, name + '.png'))
            rows.append((name, inst[i][1], inst[i][2]))
    tp = os.path.join(OUT, 'truth_ctl.tsv'); open(tp, 'w').write('crop\ttrue\tsource_box\n' + ''.join('\t'.join(r) + '\n' for r in rows))
    print(len(rows), 'targets;', len(set(r[1] for r in rows)), 'ids; truth ->', tp)
def load_reads(p):
    return {r[0].strip(): r[1].strip() for r in csv.reader(open(p), delimiter='\t') if len(r) >= 2 and not r[0].startswith('crop')}
def score_control(p1, p2):
    T = {r['crop']: r['true'] for r in csv.DictReader(open(os.path.join(OUT, 'truth_ctl.tsv')), delimiter='\t')}
    a, b = load_reads(p1), load_reads(p2); res = {}
    for mode, f in (('unfolded', lambda s: s), ('folds only', lambda s: fold(s, False)), ('folds+rule', fold)):
        e1 = sum(f(a.get(c, '?')) != f(t) for c, t in T.items()); e2 = sum(f(b.get(c, '?')) != f(t) for c, t in T.items())
        uns = sum(f(a.get(c, '?')) != f(b.get(c, '?')) for c in T); wrong = sum(f(a.get(c, '?')) == f(b.get(c, '?')) != f(t) for c, t in T.items())
        n = len(T); res[mode] = dict(n=n, R1_err=e1, R2_err=e2, unsettled=uns, settled_wrong=wrong, control_err_pct=round(100 * (uns + wrong) / n, 1))
        print(mode, res[mode])
    miss = [(c, T[c], a.get(c), b.get(c)) for c in T if fold(a.get(c, '?')) != fold(T[c]) or fold(b.get(c, '?')) != fold(T[c])]
    for m in miss: print('  ', *m)
    json.dump(dict(result=res, misses=miss), open(os.path.join(HERE, 'control_result.json'), 'w'), indent=1)
if __name__ == '__main__':
    c = sys.argv[1] if len(sys.argv) > 1 else ''
    {'tiles': tiles, 'control': control, 'score-control': lambda: score_control(*sys.argv[2:4])}.get(c, lambda: print(__doc__))()
