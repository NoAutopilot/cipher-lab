#!/usr/bin/env python3
"""C1161-EXC (15 Oct 2026): exemplar windows of the 24 LKEY-unmapped labels (+4 controls), anchored on hand-placed S (shc/hand.tsv),
window format of shc/cut_hc.py. Montages go to OUTDIR only (scratchpad; never git). PREREG exc/PREREG-C1161-EXC.md.
  python3 exc/exc_windows.py OUTDIR            -> exc/tokens.tsv (chosen tokens), exc/groups.tsv, untestable list on stdout
  python3 exc/exc_windows.py OUTDIR A 14411    -> OUTDIR/A_g{1..4}.jpg, exc/ids_A.tsv (id -> label)
  python3 exc/exc_windows.py OUTDIR C 14413 L1,L2,...  -> reconciliation montage of the named labels, exc/ids_C.tsv"""
import csv, collections, os, random, sys
from PIL import Image, ImageDraw, ImageFont
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
TEST = "+ 0 2 6 6r K Sorn blot d dia eloop f iii l ls o psi rot s spiralG th tri vdash x".split()
CTRL = ['qb', '9', 'sd', 'y']
rows = list(csv.DictReader(open(os.path.join(T, 'ciphertext.tsv')), delimiter='\t'))
hand = {(r['line'], int(r['pos'])): r for r in csv.DictReader(open(os.path.join(T, 'shc', 'hand.tsv')), delimiter='\t')}
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 26)
_img = {}
def piece(src, pc):
    k = (src, pc)
    if k not in _img:
        _img[k] = Image.open(os.path.join(T, 'images', f'{src}_{pc}.jpg')).convert('RGB')
    return _img[k]
def anchor(ln, p):
    for d in (1, 2, 3, 4):
        for s in (p - d, p + d):
            a = hand.get((ln, s))
            if a:
                x = int(a['x']) + (p - s) * float(a['pitch'])
                if 0 < x < piece(a['src'], a['piece']).width:
                    return d, dict(src=a['src'], piece=a['piece'], x=int(x), y=int(a['y']), pitch=float(a['pitch']))
    return None
def window(r):
    S = piece(r['src'], r['piece']); x, c, p = int(r['x']), int(r['y']), float(r['pitch'])
    lo, hi = int(max(0, x - 2 * p)), int(min(S.width, x + 2 * p))
    w = S.crop((lo, max(0, c - 90), hi, min(S.height, c + 90)))
    f = max(2, -(-300 // max(1, w.width)))
    w = w.resize((w.width * f, w.height * f)); d = ImageDraw.Draw(w); tx = (x - lo) * f
    d.line((tx, 0, tx, 14), fill='red', width=3); d.line((tx, w.height - 14, tx, w.height), fill='red', width=3)
    return w
def montage(items, path):
    """items: [(id, [tokrow,...])]; one row per id."""
    W = [(i, [window(t) for t in ts]) for i, ts in items]
    cw = max(w.width for _, ws in W for w in ws); rh = max(w.height for _, ws in W for w in ws) + 8
    M = Image.new('RGB', (110 + 3 * (cw + 12), len(W) * (rh + 10)), 'white'); d = ImageDraw.Draw(M)
    for j, (i, ws) in enumerate(W):
        y = j * (rh + 10); d.text((6, y + rh // 2 - 14), i, fill='blue', font=font)
        for k, w in enumerate(ws):
            M.paste(w, (110 + k * (cw + 12), y))
        d.line((0, y + rh + 4, M.width, y + rh + 4), fill=(160, 160, 160), width=2)
    M.thumbnail((2400, 2400)); M.save(path, quality=90)
toks = os.path.join(H, 'tokens.tsv')
if len(sys.argv) == 2:
    rng = random.Random(1441); bylab = collections.defaultdict(list)
    for r in rows:
        if r['sign'] in TEST + CTRL:
            a = anchor(r['line'], int(r['pos']))
            if a:
                bylab[r['sign']].append((a[0], rng.random(), r['line'], r['pos'], a[1]))
    with open(toks, 'w') as f:
        f.write('label\tline\tpos\tdist\tsrc\tpiece\tx\ty\tpitch\n')
        for lab in TEST + CTRL:
            for d, _, ln, p, a in sorted(bylab[lab])[:3]:
                f.write(f"{lab}\t{ln}\t{p}\t{d}\t{a['src']}\t{a['piece']}\t{a['x']}\t{a['y']}\t{a['pitch']:.1f}\n")
    testable = [l for l in TEST if bylab[l]]; print('UNTESTABLE', [l for l in TEST if not bylab[l]])
    rng2 = random.Random(1442); rng2.shuffle(testable)
    with open(os.path.join(H, 'groups.tsv'), 'w') as f:
        f.write('group\tlabel\trole\n')
        for g in range(4):
            for l in testable[g::4]:
                f.write(f'{g+1}\t{l}\ttest\n')
            f.write(f'{g+1}\t{CTRL[g]}\tcontrol\n')
    print({l: len(bylab[l]) for l in TEST + CTRL})
    sys.exit()
P, seed = sys.argv[2], int(sys.argv[3]); rng = random.Random(seed)
T_ = collections.defaultdict(list)
for r in csv.DictReader(open(toks), delimiter='\t'):
    T_[r['label']].append(r)
if len(sys.argv) > 4:
    groups = {1: sys.argv[4].split(',')}
else:
    groups = collections.defaultdict(list)
    for r in csv.DictReader(open(os.path.join(H, 'groups.tsv')), delimiter='\t'):
        groups[int(r['group'])].append(r['label'])
with open(os.path.join(H, f'ids_{P}.tsv'), 'w') as f:
    f.write('group\tid\tlabel\n')
    for g, labs in sorted(groups.items()):
        labs = labs[:]; rng.shuffle(labs)
        ids = [f'{P}{g}-{k:02d}' for k in range(1, len(labs) + 1)]
        for i, l in zip(ids, labs):
            f.write(f'{g}\t{i}\t{l}\n')
        items = []
        for i, l in zip(ids, labs):
            ts = T_[l][:]; rng.shuffle(ts); items.append((i, ts))
        montage(items, os.path.join(out, f'{P}_g{g}.jpg'))
print('written', P, sorted(groups))
