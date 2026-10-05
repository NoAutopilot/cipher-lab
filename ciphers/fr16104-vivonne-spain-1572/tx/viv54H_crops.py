#!/usr/bin/env python3
"""DEF1-VIV54: hand-placed per-position crops for the value-blind judge (PREREG-N7VIV54R decision rule; hand-placed instrument).

    python3 tx/viv54H_crops.py OUTDIR

Reads tx/lookalike54/viv54H_xmarks.tsv (x marked by eye on the native line strip), cuts strip x +-110 px at native resolution, 2x,
red ticks at the marked x, captions each crop with an opaque id (C01..), order shuffled with seed 20261054H, 6 per montage; also
regenerates the key reference image (tx/viv54R_windows.py ref). Writes tx/lookalike54/viv54H_key.tsv (opaque id -> position).
"""
import csv, os, random, sys
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import viv54H_place as pl  # noqa: E402
import viv54R_windows as rw  # noqa: E402
LA = os.path.join(HERE, 'lookalike54')


def main():
    od = sys.argv[1]; os.makedirs(od, exist_ok=True)
    rw.OUT = od; rw.ref()
    rows = list(csv.DictReader(open(os.path.join(LA, 'viv54H_xmarks.tsv')), delimiter='\t'))
    random.Random('20261054H').shuffle(rows)
    cache, crops = {}, []
    for i, r in enumerate(rows):
        r['cid'] = f'C{i + 1:02d}'
        S, a, b = pl.strip_of(cache, r['page'], r['passage']); x = int(r['x_hand'])
        lo, hi = max(0, x - 110), min(S.width, x + 110)
        c = S.crop((lo, 0, hi, S.height)).convert('RGB'); c = c.resize((c.width * 2, c.height * 2))
        d = ImageDraw.Draw(c); t = (x - lo) * 2
        d.line((t, 0, t, 16), fill='red', width=3); d.line((t, c.height - 16, t, c.height), fill='red', width=3)
        P = Image.new('RGB', (440, c.height + 22), 'white'); P.paste(c, (0, 22)); ImageDraw.Draw(P).text((4, 4), r['cid'], fill='blue')
        crops.append(P)
    for k in range(0, len(crops), 6):
        g = crops[k:k + 6]; M = Image.new('RGB', (440 * 2, ((len(g) + 1) // 2) * g[0].height), 'white')
        for j, q in enumerate(g):
            M.paste(q, ((j % 2) * 440, (j // 2) * q.height))
        M.save(os.path.join(od, f'judge_{k // 6:02d}.png'))
    with open(os.path.join(LA, 'viv54H_key.tsv'), 'w') as o:
        w = csv.DictWriter(o, fieldnames=['cid'] + [f for f in rows[0] if f != 'cid'], delimiter='\t', lineterminator='\n')
        w.writeheader(); w.writerows(rows)
    print(len(rows), 'crops')


if __name__ == '__main__':
    main()
