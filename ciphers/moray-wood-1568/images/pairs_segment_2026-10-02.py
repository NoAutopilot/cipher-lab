import json, sys, numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage
from scipy.signal import find_peaks
SRC = sys.argv[1]; OUT = sys.argv[2]
im = Image.open(SRC).convert('L')
BANDS = {'L1': (7370, 7556, 1500, 5800), 'L2': (7526, 7738, 1500, 5800), 'L3': (7708, 7894, 1500, 5800), 'L4': (7864, 8050, 1500, 2450)}
EXPECT = {'L1': 46, 'L2': 43, 'L3': 38, 'L4': 7}
res = {}
for ln, (y0, y1, X0, X1) in BANDS.items():
    band = np.array(im.crop((X0, y0, X1, y1)))
    ink = (band < 150)
    rows = ink.sum(axis=1)
    # core rows: contiguous zone around the max row containing rows >= 25% of max
    peak = int(rows.argmax()); thr = rows.max() * 0.25
    a = peak
    while a > 0 and rows[a-1] >= thr: a -= 1
    b = peak
    while b < len(rows)-1 and rows[b+1] >= thr: b += 1
    core = ink[a:b+1]
    col = core.sum(axis=0).astype(float)
    sm = np.convolve(col, np.ones(5)/5, mode='same')
    # runs of ink columns
    on = sm > 0.6
    runs = []
    i = 0
    while i < len(on):
        if on[i]:
            j = i
            while j < len(on) and on[j]: j += 1
            runs.append([i, j]); i = j
        else: i += 1
    # merge runs separated by < 4 px
    merged = []
    for r in runs:
        if merged and r[0] - merged[-1][1] < 4: merged[-1][1] = r[1]
        else: merged.append(r)
    # drop tiny runs
    merged = [r for r in merged if (r[1]-r[0]) >= 12 and col[r[0]:r[1]].sum() > 80]
    # split wide runs at valleys
    glyphs = []
    for r0, r1 in merged:
        w = r1 - r0
        if w > 115:
            seg = sm[r0:r1]
            inv = seg.max() - seg
            peaks, props = find_peaks(inv, prominence=seg.max()*0.25, distance=40)
            cuts = [r0] + [r0+int(p) for p in peaks if 35 <= p <= w-35] + [r1]
            for k in range(len(cuts)-1): glyphs.append([cuts[k], cuts[k+1]])
        else:
            glyphs.append([r0, r1])
    print(ln, 'core rows', a, b, 'runs', len(merged), 'glyphs', len(glyphs), 'expected', EXPECT[ln])
    print('  widths', [g[1]-g[0] for g in glyphs])
    print('  gaps', [glyphs[i+1][0]-glyphs[i][1] for i in range(len(glyphs)-1)])
    res[ln] = dict(band=[X0, y0, X1, y1], core=[a, b], glyphs=[[X0+g[0], y0, X0+g[1], y1] for g in glyphs])
json.dump(res, open(OUT+'/glyphs2.json','w'), indent=1)
# overlays: each line in two halves at 0.5 scale, numbered
font = ImageFont.load_default(size=28) if hasattr(ImageFont, 'load_default') else None
for ln, r in res.items():
    X0, y0, X1, y1 = r['band']
    crop = im.crop((X0, y0, X1, y1)).convert('RGB')
    d = ImageDraw.Draw(crop)
    for i, (gx0, gy0, gx1, gy1) in enumerate(r['glyphs'], 1):
        d.rectangle([gx0-X0, 2, gx1-X0-1, y1-y0-3], outline=(255,0,0) if i % 2 else (0,0,255), width=2)
        d.text((gx0-X0+2, 2), str(i), fill=(0,120,0), font=font)
    W = crop.width
    if ln == 'L4':
        crop.resize((W//2, (y1-y0)//2)).save(f'{OUT}/overlay_{ln}.png')
    else:
        halves = [crop.crop((0,0,W//2+60,y1-y0)), crop.crop((W//2-60,0,W,y1-y0))]
        canvas = Image.new('RGB', ((W//2+60)//2*1, 2*((y1-y0)//2)+10), 'white')
        for k,h in enumerate(halves):
            canvas.paste(h.resize((h.width//2, h.height//2)), (0, k*((y1-y0)//2+10)))
        canvas.save(f'{OUT}/overlay_{ln}.png')
