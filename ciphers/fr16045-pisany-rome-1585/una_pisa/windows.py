"""UNA-PISA locating aid (not evidence): for each T45/T47/T57 token of a page, a 600 px window of its line strip around the
predicted x (piecewise linear between eye anchors from pist40/pissd tokens_pos where the line has them, else linear over the
ink extent with near-solid columns -- the gutter -- dropped), ticks at every predicted sign position labelled with the ordinal.
usage: windows.py PAGE OUT.png  (prints the predicted x per target)"""
import sys, csv, numpy as np
from PIL import Image, ImageDraw
sys.path.insert(0, 'ciphers/fr16045-pisany-rome-1585/una_pisa')
from strips import strip, tokens, D
TGT = {'T45', 'T47', 'T57'}
def anchors(page, line):
    a = {}
    if page == 'f302v':
        for f in (f'{D}/pist40/tokens_pos.tsv', f'{D}/pissd/tokens.tsv'):
            for r in csv.DictReader(open(f), delimiter='\t'):
                x = r.get('x_centre_strip', '-')
                if r['line'] == line and x not in ('-', ''): a[int(r['tok_index'])] = int(x)
    return a
def predict(page, line):
    s = strip(page, line); arr = np.array(s) < 140; frac = arr.mean(0)
    xs = np.where((arr.sum(0) > 2) & (frac < 0.5))[0]; x0, x1 = xs.min(), xs.max()
    toks = tokens(page, line); n = len(toks)
    pts = {0: x0 - (x1 - x0) / n / 2, n + 1: x1 + (x1 - x0) / n / 2}; pts.update(anchors(page, line))
    ks = sorted(pts); px = [pts[k] for k in ks]
    return s, toks, [float(np.interp(k + 1, ks, px)) for k in range(n)]
def windows(page, out):
    lines = sorted({l for l, _ in [(r.split('\t')[0], 0) for r in open(f'{D}/reading_{page}_tokens.tsv')][1:]})
    tiles = []
    for line in lines:
        toks = tokens(page, line)
        if not any(sg in TGT for _, sg in toks): continue
        s, toks, xs = predict(page, line)
        for k, (pos, sg) in enumerate(toks):
            if sg not in TGT: continue
            c = int(xs[k]); w0 = max(0, c - 300); win = s.crop((w0, 0, w0 + 600, s.size[1])).convert('RGB')
            im = Image.new('RGB', (600, s.size[1] + 40), 'white'); im.paste(win, (0, 0)); d = ImageDraw.Draw(im)
            for j, x in enumerate(xs):
                if w0 <= x < w0 + 600:
                    d.line([(x - w0, s.size[1]), (x - w0, s.size[1] + 10)], fill='red' if j == k else 'black', width=3 if j == k else 1)
                    d.text((x - w0 - 6, s.size[1] + 12), str(j + 1), fill='black')
            d.text((4, 4), f'{line} ord{k+1} pos{pos}', fill='red')
            tiles.append(im); print(f'{page}\t{line}\t{pos}\t{k+1}\t{sg}\t{c}')
    H = sum(t.size[1] for t in tiles); sheet = Image.new('RGB', (600, H), 'white'); y = 0
    for t in tiles: sheet.paste(t, (0, y)); y += t.size[1]
    sheet.save(out)
if __name__ == '__main__':
    windows(sys.argv[1], sys.argv[2])
