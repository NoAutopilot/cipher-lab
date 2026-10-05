#!/usr/bin/env python3
"""DEF1-VIV54: placement sheets for hand-marking x of ink 54 positions (PREREG-N7VIV54R, hand-placed instrument).

    python3 tx/viv54H_place.py OUTDIR [--to-only]

For each passD position labelled z/x/R/3/2 (--to-only: only those right after a "to" label) cuts a native window of the line strip
(tx/viv53L_windows.py strip) around the pos/len estimate +-8 signs, draws a pixel ruler (strip x every 50 px, labelled every 100),
and stacks 3 per sheet with the id and the label sequence around it. The worker reads the sheet and records the sign's strip x by hand
in tx/lookalike54/viv54H_xmarks.tsv. Sheets are scratch (regenerable), not committed.
"""
import csv, os, sys
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import viv53L_windows as w53  # noqa: E402
w53.IMG = os.path.join(T, 'images')
LA = os.path.join(HERE, 'lookalike54')


def items(to_only):
    out = []
    for page in ('f173r', 'f173v'):
        rows = list(csv.DictReader(open(os.path.join(LA, f'viv54L_{page}_passD.tsv')), delimiter='\t'))
        byl = {}
        for r in rows:
            byl.setdefault(r['passage'], []).append(r['sign_id'])
        for r in rows:
            p, s = int(r['pos']), byl[r['passage']]
            if r['sign_id'] in ('z', 'x', 'R', '3', '2') and (not to_only or (p >= 2 and s[p - 2] == 'to')):
                out.append((page, r['passage'], p, s))
    return out


def strip_of(cache, page, ln):
    if (page, ln) not in cache:
        S = w53.strip(w53.boxes(page)[ln]); px = S.load(); W, H = S.size
        ink = [sum(1 for y in range(H) if px[x, y] < 110) for x in range(W)]
        cols = [x for x in range(W) if ink[x] >= 2]
        cache[(page, ln)] = (S, cols[0] if cols else 0, cols[-1] if cols else W)
    return cache[(page, ln)]


def estx(cache, page, ln, p, n):
    S, a, b = strip_of(cache, page, ln)
    return a + (p - 0.5) * (b - a) / n


def main():
    od = sys.argv[1]; os.makedirs(od, exist_ok=True)
    its = items('--to-only' in sys.argv); cache = {}; panels = []
    for page, ln, p, s in its:
        S, a, b = strip_of(cache, page, ln); x = estx(cache, page, ln, p, len(s)); sw = (b - a) / len(s)
        lo, hi = int(max(0, x - 8 * sw)), int(min(S.width, x + 8 * sw))
        c = S.crop((lo, 0, hi, S.height)).convert('RGB')
        P = Image.new('RGB', (1500, c.height + 60), 'white'); P.paste(c, (0, 40)); d = ImageDraw.Draw(P)
        for xx in range((lo // 50 + 1) * 50, hi, 50):
            t = xx - lo; d.line((t, 28, t, 40 if xx % 100 else 36), fill='blue')
            if xx % 100 == 0:
                d.text((t - 10, 16), str(xx), fill='blue')
        d.text((2, 2), f"{page}.{ln}.{p}  seq {p-6}..: {' '.join(s[max(0, p - 7):p - 1])} [{s[p-1]}] {' '.join(s[p:p + 6])}", fill='black')
        panels.append(P)
    for i in range(0, len(panels), 3):
        g = panels[i:i + 3]; H = sum(q.height for q in g)
        M = Image.new('RGB', (1500, H), 'white'); y = 0
        for q in g:
            M.paste(q, (0, y)); y += q.height
        M.save(os.path.join(od, f'place_{i // 3:02d}.png'))
    print(len(its), 'items', (len(panels) + 2) // 3, 'sheets')


if __name__ == '__main__':
    main()
