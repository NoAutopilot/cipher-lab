#!/usr/bin/env python3
"""D07-VIV53: hand-placed per-position crops + key-cell reference for the value-blind judge (PREREG-D07VIV53P).

    python3 tx/viv53P_crops.py OUTDIR

Reads tx/lookalike53P/viv53P_xmarks.tsv (x marked by eye on the native line strip), cuts strip x +-110 px native, 2x, red ticks at the
mark, opaque ids (K01.., order shuffled with seed "20261053P"; map in tx/lookalike53P/viv53P_key.tsv). Montages of 6 for pass A and pass B
in two different orders (seeds "20261053P-A", "-B"). Reference: 10 key cells of sources/cryptiana/web/henryiii_Vivonne1.png under opaque
letters A..J (shuffled, seed "20261053P-ref"; map in viv53P_refkey.tsv). Montages and ref.png are scratch (regenerable), not committed.
"""
import csv, os, random, sys
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); sys.path.insert(0, HERE)
import viv53P_place as pl  # noqa: E402
LA = os.path.join(HERE, 'lookalike53P')
KEY = os.path.join(T, '..', '..', 'sources', 'cryptiana', 'web', 'henryiii_Vivonne1.png')
# cell boxes in the 543x213 key image (x0, y0, x1, y1), read at 3x
CELLS = {'f1': (104, 19, 136, 44), 'g1': (127, 19, 157, 44), 'm1': (216, 19, 250, 42), 'm2': (214, 40, 246, 62),
         'm5': (214, 95, 248, 118), 'p1': (288, 19, 316, 44), 'o1': (264, 19, 292, 44), 'e1': (84, 19, 112, 42),
         'n1': (240, 19, 270, 46), 'r1': (334, 19, 362, 46)}


def ref(od):
    im = Image.open(KEY).convert('L'); names = sorted(CELLS); random.Random('20261053P-ref').shuffle(names)
    out = Image.new('L', (5 * 170, 2 * 160), 255); d = ImageDraw.Draw(out); mp = []
    for i, n in enumerate(names):
        x0, y0, x1, y1 = CELLS[n]; c = im.crop(CELLS[n]); c = c.resize((c.width * 4, c.height * 4))
        X, Y = (i % 5) * 170, (i // 5) * 160; out.paste(c, (X + 5, Y + 24)); L = 'ABCDEFGHIJ'[i]
        d.text((X + 5, Y + 4), f'REF {L}', fill=0); mp.append((L, n))
    out.save(os.path.join(od, 'ref.png'))
    with open(os.path.join(LA, 'viv53P_refkey.tsv'), 'w') as o:
        o.write('ref\tcell\n'); o.writelines(f'{a}\t{b}\n' for a, b in mp)


def main():
    od = sys.argv[1]; os.makedirs(od, exist_ok=True); ref(od)
    rows = list(csv.DictReader(open(os.path.join(LA, 'viv53P_xmarks.tsv')), delimiter='\t'))
    rows = [r for r in rows if int(r['x_hand']) >= 0]
    random.Random('20261053P').shuffle(rows); cache, crops = {}, {}
    for i, r in enumerate(rows):
        r['cid'] = f'K{i + 1:02d}'
        S, a, b = pl.strip_of(cache, r['page'], r['line']); x = int(r['x_hand'])
        lo, hi = max(0, x - 110), min(S.width, x + 110)
        c = S.crop((lo, 0, hi, S.height)).convert('RGB'); c = c.resize((c.width * 2, c.height * 2))
        d = ImageDraw.Draw(c); t = (x - lo) * 2
        d.line((t, 0, t, 16), fill='red', width=3); d.line((t, c.height - 16, t, c.height), fill='red', width=3)
        P = Image.new('RGB', (440, c.height + 22), 'white'); P.paste(c, (0, 22)); ImageDraw.Draw(P).text((4, 4), r['cid'], fill='blue')
        crops[r['cid']] = P
    for ps in ('A', 'B'):
        ids = sorted(crops); random.Random(f'20261053P-{ps}').shuffle(ids)
        for k in range(0, len(ids), 6):
            g = [crops[j] for j in ids[k:k + 6]]; h = max(q.height for q in g)
            M = Image.new('RGB', (440 * 2, ((len(g) + 1) // 2) * h), 'white')
            for j, q in enumerate(g):
                M.paste(q, ((j % 2) * 440, (j // 2) * h))
            M.save(os.path.join(od, f'pass{ps}_{k // 6:02d}.png'))
        open(os.path.join(od, f'pass{ps}_order.txt'), 'w').write('\n'.join(ids) + '\n')
    with open(os.path.join(LA, 'viv53P_key.tsv'), 'w') as o:
        rows.sort(key=lambda r: r['cid'])
        w = csv.DictWriter(o, fieldnames=['cid'] + [f for f in rows[0] if f != 'cid'], delimiter='\t', lineterminator='\n')
        w.writeheader(); w.writerows(rows)
    print(len(rows), 'crops')


if __name__ == '__main__':
    main()
