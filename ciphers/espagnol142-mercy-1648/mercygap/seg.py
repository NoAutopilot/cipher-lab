"""MERCY-GAP segmentation: ink runs per row band of f22r (r16-r24), aligned to ciphertext.tsv digits."""
import json, sys, numpy as np
from PIL import Image
D = 'ciphers/espagnol142-mercy-1648/'
ROWS = ['r%02d' % i for i in range(16, 25)]

def otsu(a):
    h = np.bincount(a.ravel().astype(int), minlength=256).astype(float); p = h / h.sum()
    w = np.cumsum(p); mu = np.cumsum(p * np.arange(256)); mt = mu[-1]
    s = (mt * w - mu) ** 2 / (w * (1 - w) + 1e-12); return int(np.argmax(s))

def bands():
    m = json.load(open(D + 'mercyimg/crops/manifest.json'))['iiif_lines']
    out = {}
    for e in m:
        b = e['band']; x0, y0, x1, y1 = e['box']; out.setdefault(b, [9e9, y0, 0, y1])
        out[b][0] = min(out[b][0], x0); out[b][2] = max(out[b][2], x1)
    return [out[k] for k in sorted(out)]

def digits(row):
    seq = []
    for l in open(D + 'ciphertext.tsv'):
        f = l.rstrip('\n').split('\t')
        if f[0] == row: seq.append((int(f[1]), f[2]))
    return seq

def runs(page, box, merge=2, strip=(0.2, 0.85), minw=3, mink=20):
    x0, y0, x1, y1 = map(int, box); g = page[y0:y1, x0:x1]
    t = otsu(g); ink = g < t
    h = ink.shape[0]; s = ink[int(h * strip[0]):int(h * strip[1])]
    col = s.sum(0) > 0
    rr = []; i = 0; n = len(col)
    while i < n:
        if col[i]:
            j = i
            while j < n and col[j]: j += 1
            rr.append([i, j]); i = j
        else: i += 1
    m = []
    for r in rr:
        if m and r[0] - m[-1][1] < merge: m[-1][1] = r[1]
        else: m.append(r)
    m = [r for r in m if r[1] - r[0] >= minw and s[:, r[0]:r[1]].sum() >= mink]
    return [(a + x0, b + x0) for a, b in m]

if __name__ == '__main__':
    page = np.asarray(Image.open(D + 'images/f22r_canvas58.jpg').convert('L'))
    for row, box in zip(ROWS, bands()):
        r = runs(page, box); ds = ''.join(s for _, s in digits(row))
        print(row, box, 'runs', len(r), 'digits', len(ds), ds)
