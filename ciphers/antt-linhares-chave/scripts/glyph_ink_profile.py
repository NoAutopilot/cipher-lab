#!/usr/bin/env python3
"""D2-LINK (5 Oct 2026): script ink-profile comparison of the p2l2pos6 first glyph (329011 vs 829011)
against every labelled 3 and 8 on m0002. Pre-registration: NOTES.md "Ink-profile comparison ... (D2-LINK)".
numpy + PIL only. Usage: glyph_ink_profile.py [--debug OUT.png] [--score]"""
import argparse, csv, os, random
import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
IMG = os.path.join(T, 'images', 'full_PT-TT-CLNH-0086-11_m0002.jpg.jpg')
# group boxes (x0, x1, y0, y1) on the main digits, set by eye on the full image and the debug overlay
# before any feature was computed (pre-registration step 1); order = ciphertext.tsv order per line
GROUPS = {(2, 1): [(76, 175, 68, 98), (200, 278, 68, 100), (314, 372, 72, 100), (436, 512, 74, 102),
                   (544, 640, 72, 104), (672, 790, 74, 104), (804, 900, 78, 106), (904, 982, 80, 108),
                   (1010, 1108, 86, 116)],
          (2, 2): [(66, 140, 112, 140), (184, 292, 116, 140), (294, 376, 118, 142), (378, 500, 120, 144),
                   (512, 580, 120, 146), (620, 702, 120, 146), (874, 940, 128, 154), (996, 1100, 132, 160)],
          (3, 1): [(68, 212, 262, 294), (226, 356, 266, 292), (374, 482, 264, 294), (502, 610, 262, 296),
                   (612, 730, 262, 294), (742, 872, 264, 294), (890, 1008, 264, 294), (1010, 1102, 264, 294)],
          (3, 2): [(66, 192, 306, 334)]}
MAXW = 40
MINPX, MINH, GAP = 12, 6, 9

def otsu(v):
    h, _ = np.histogram(v, bins=256, range=(0, 256)); p = h / h.sum(); w = np.cumsum(p); m = np.cumsum(p * np.arange(256))
    with np.errstate(divide='ignore', invalid='ignore'):
        s = (m[-1] * w - m) ** 2 / (w * (1 - w))
    return int(np.nanargmax(s))

def components(mask, conn8=True):
    H, W = mask.shape; lab = np.zeros((H, W), int); out = []; n = 0
    nb = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] if conn8 else [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for y in range(H):
        for x in range(W):
            if mask[y, x] and not lab[y, x]:
                n += 1; st = [(y, x)]; lab[y, x] = n; pts = []
                while st:
                    a, b = st.pop(); pts.append((a, b))
                    for da, db in nb:
                        c, d = a + da, b + db
                        if 0 <= c < H and 0 <= d < W and mask[c, d] and not lab[c, d]:
                            lab[c, d] = n; st.append((c, d))
                out.append(np.array(pts))
    return out

def load():
    g = np.asarray(Image.open(IMG).convert('RGB'), float).mean(2)
    rows = list(csv.DictReader(open(os.path.join(T, 'ciphertext.tsv')), delimiter='\t'))
    lines = {}
    for (p, l), boxes_ in GROUPS.items():
        groups = []
        for (x0, x1, y0, y1) in boxes_:
            box = g[y0:y1, x0:x1]; th = otsu(box); mask = box < th
            comps = [c for c in components(mask) if len(c) >= MINPX and np.ptp(c[:, 0]) + 1 >= MINH
                     and np.ptp(c[:, 1]) + 1 <= MAXW]
            gr = []
            for c in comps:
                ys, xs = c[:, 0], c[:, 1]
                gr.append(dict(x0=xs.min() + x0, x1=xs.max() + x0, y0=ys.min() + y0, y1=ys.max() + y0,
                               pts=c + [y0, x0], th=th))
            gr.sort(key=lambda b: b['x0']); groups.append(gr)
        trans = [r for r in rows if int(r['page_of_letter']) == p and int(r['line']) == l]
        lines[(p, l)] = (groups, trans)
    return g, lines

def label(lines):
    """returns list of (glyph box, digit, row, index) for groups whose component count matches; plus log"""
    out, log = [], []
    for k, (groups, trans) in lines.items():
        if len(groups) != len(trans):
            log.append(f'{k}: {len(groups)} groups segmented vs {len(trans)} transcribed -- line dropped'); continue
        for gr, r in zip(groups, trans):
            if len(gr) != len(r['group']):
                log.append(f"{k} pos{r['pos']} {r['group']}: {len(gr)} components vs {len(r['group'])} digits -- dropped"); continue
            for i, (b, dch) in enumerate(zip(gr, r['group'])):
                out.append((b, dch, r, i))
    return out, log

def f1vec(g, b):
    sub = 255 - g[b['y0']:b['y1'] + 1, b['x0']:b['x1'] + 1]
    m = np.zeros_like(sub); pts = b['pts'] - [b['y0'], b['x0']]; m[pts[:, 0], pts[:, 1]] = 1
    sub = sub * m
    v = np.asarray(Image.fromarray(sub.astype(np.uint8)).resize((12, 18), Image.BILINEAR), float).ravel()
    v -= v.mean(); n = np.linalg.norm(v); return v / n if n else v

def holes(b):
    h, w = b['y1'] - b['y0'] + 1, b['x1'] - b['x0'] + 1
    m = np.zeros((h + 2, w + 2), bool); pts = b['pts'] - [b['y0'] - 1, b['x0'] - 1]; m[pts[:, 0], pts[:, 1]] = True
    bg = components(~m, conn8=False)
    return sum(1 for c in bg if len(c) >= 2 and not ((c[:, 0] == 0).any() or (c[:, 1] == 0).any()
               or (c[:, 0] == h + 1).any() or (c[:, 1] == w + 1).any()))

def bal(calls, truth):
    r = [np.mean([c == t for c, t in zip(calls, truth) if t == k]) for k in '38']
    return float(np.mean(r)), r

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--debug'); ap.add_argument('--score', action='store_true')
    a = ap.parse_args()
    g, lines = load(); lab, log = label(lines)
    for x in log: print('seg:', x)
    target = [t for t in lab if t[2]['page_of_letter'] == '2' and t[2]['line'] == '2' and t[2]['pos'] == '6' and t[3] == 0]
    print('target isolated:', bool(target))
    if a.debug:
        im = Image.open(IMG).convert('RGB'); dr = ImageDraw.Draw(im)
        for groups, _ in lines.values():
            for gr in groups:
                for b in gr: dr.rectangle([b['x0'], b['y0'], b['x1'], b['y1']], outline=(0, 0, 255))
        for b, dch, r, i in lab:
            col = (255, 0, 0) if dch == '3' else (0, 160, 0) if dch == '8' else None
            if col: dr.rectangle([b['x0'] - 1, b['y0'] - 1, b['x1'] + 1, b['y1'] + 1], outline=col, width=2)
        im = im.crop((60, 60, 1120, 340)); im = im.resize((im.width * 2, im.height * 2)); im.save(a.debug)
        print('debug ->', a.debug)
    if not a.score: return
    lbl = [t for t in lab if t[1] in '38' and t[2]['grade'] == 'H'
           and not (t[2]['page_of_letter'] == '2' and t[2]['line'] == '2' and t[2]['pos'] == '6')]
    truth = [t[1] for t in lbl]; print(f'labelled: n3={truth.count("3")} n8={truth.count("8")}')
    V = np.array([f1vec(g, t[0]) for t in lbl]); HO = [holes(t[0]) for t in lbl]
    def f1_loo(tr):
        calls = []
        for i in range(len(tr)):
            s = {k: np.mean([V[i] @ V[j] for j in range(len(tr)) if j != i and tr[j] == k]) for k in '38'}
            calls.append('3' if s['3'] >= s['8'] else '8')
        return calls
    f2c = ['8' if h >= 1 else '3' for h in HO]
    rng = random.Random(20261005); res = {}
    for name, fn in (('F1', f1_loo), ('F2', lambda tr: f2c)):
        b, r = bal(fn(truth), truth); perm = []
        for _ in range(200):
            p = truth[:]; rng.shuffle(p); perm.append(bal(fn(p), p)[0])
        p95 = float(np.percentile(perm, 95)); ok = truth.count('8') >= 4 and b >= 0.80 and b > p95
        res[name] = ok
        print(f'{name}: balanced acc {b:.3f} (recall3 {r[0]:.3f}, recall8 {r[1]:.3f}); permuted p95 {p95:.3f}; gate {"PASS" if ok else "FAIL"}')
    if not target: print('target: not isolated -> non-test'); return
    tb = target[0][0]; tv = f1vec(g, tb)
    s = {k: float(np.mean([tv @ V[j] for j in range(len(lbl)) if truth[j] == k])) for k in '38'}
    th = holes(tb)
    print(f"target F1: score3 {s['3']:.3f} score8 {s['8']:.3f} margin {s['3'] - s['8']:+.3f} -> {'3' if s['3'] >= s['8'] else '8'}")
    print(f"target F2: holes {th} -> {'8' if th >= 1 else '3'}")
    print('target box', tb['x0'], tb['y0'], tb['x1'], tb['y1'])

if __name__ == '__main__':
    main()
