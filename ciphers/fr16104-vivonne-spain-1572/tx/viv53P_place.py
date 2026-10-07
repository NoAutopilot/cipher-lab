#!/usr/bin/env python3
"""D07-VIV53: placement sheets for hand-marking x of ink 53 positions (PREREG-D07VIV53P; DEF1-VIV54's hand-placed method on ink 53).

    python3 tx/viv53P_place.py OUTDIR

Items: every label e (16) and o (33) token of reading_piece53_G.tsv (targets), plus the pre-registered known-answer control: 3 positions
each of the settled labels d, m, p, g graded H, drawn with seed "20261053P" (tx/lookalike53P/viv53P_items.tsv). For each item cuts a native
window of the line strip (tx/viv53L_windows.py strip, images/p53 crops) around the pos/len estimate +-6 signs, numbers each ink run (red, its centre and span
in strip x go to OUTDIR/blobs.tsv) and the label sequence around it, 4 per sheet. The worker records each sign's strip x by eye in
tx/lookalike53P/viv53P_xmarks.tsv. Sheets are scratch (regenerable), not committed.
"""
import csv, os, random, sys
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import viv53L_windows as w53  # noqa: E402
LA = os.path.join(HERE, 'lookalike53P')
CONTROL = {'d': 'o1', 'm': 'e1', 'p': 'n1', 'g': 'r1'}   # settled label -> its key cell (key.tsv)


def lines():
    return [(r['page'], r['line'], r['codes'].split(), r['grades']) for r in
            csv.DictReader(open(os.path.join(T, 'reading_piece53_G.tsv')), delimiter='\t')]


def items():
    out, ctl = [], {k: [] for k in CONTROL}
    for page, ln, toks, gr in lines():
        for i, t in enumerate(toks):
            if t in ('e', 'o'):
                out.append({'kind': 'target', 'page': page, 'line': ln, 'pos': i + 1, 'label': t, 'n': len(toks)})
            elif t in CONTROL and len(gr) == len(toks) and gr[i] == 'H':
                ctl[t].append({'kind': 'control', 'page': page, 'line': ln, 'pos': i + 1, 'label': t, 'n': len(toks)})
    rng = random.Random('20261053P')
    for k in sorted(ctl):
        out += rng.sample(ctl[k], 3)
    return out


def strip_of(cache, page, ln):
    if (page, ln) not in cache:
        S = w53.strip(w53.boxes(page)[ln]); px = S.load(); W, H = S.size
        ink = [sum(1 for y in range(H) if px[x, y] < 110) for x in range(W)]
        cols = [x for x in range(W) if ink[x] >= 2]
        cache[(page, ln)] = (S, cols[0] if cols else 0, cols[-1] if cols else W)
    return cache[(page, ln)]


def main():
    od = sys.argv[1]; os.makedirs(od, exist_ok=True); os.makedirs(LA, exist_ok=True)
    its = items(); cache = {}; panels = []; blobs = []; seqs = {(p, l): t for p, l, t, _ in lines()}
    with open(os.path.join(LA, 'viv53P_items.tsv'), 'w') as o:
        w = csv.DictWriter(o, fieldnames=list(its[0]), delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(its)
    for k, it in enumerate(its):
        S, a, b = strip_of(cache, it['page'], it['line']); sw = (b - a) / it['n']; x = a + (it['pos'] - 0.5) * sw
        lo, hi = int(max(0, x - 7 * sw)), int(min(S.width, x + 7 * sw))
        c = S.crop((lo, 0, hi, S.height)).convert('RGB')
        P = Image.new('RGB', (max(900, c.width), c.height + 44), 'white'); P.paste(c, (0, 40)); d = ImageDraw.Draw(P)
        cpx = c.convert('L').load(); prof = [sum(1 for y in range(c.height) if cpx[x, y] < 110) for x in range(c.width)]
        runs, st = [], None
        for x in range(c.width + 1):
            on = x < c.width and prof[x] >= 2
            if on and st is None:
                st = x
            if not on and st is not None:
                if x - st >= 4:
                    runs.append((st, x - 1))
                st = None
        for j, (r0, r1) in enumerate(runs):   # numbered ink runs: centre and span in strip x
            t = (r0 + r1) // 2; d.line((r0, 36, r1, 36), fill='red'); d.line((t, 30, t, 40), fill='red')
            d.text((t - 4, 17), str(j), fill='red'); blobs.append((k, j, lo + r0, lo + r1, lo + t))
        for xx in range((lo // 100 + 1) * 100, hi, 100):
            d.line((xx - lo, 40, xx - lo, 44), fill='blue')
        s, p = seqs[(it['page'], it['line'])], it['pos']
        d.text((2, 2), f"#{k} {it['page']}.{it['line']}.{p}/{it['n']}: {' '.join(s[max(0, p - 6):p - 1])} [{s[p-1]}] {' '.join(s[p:p + 5])}", fill='black')
        panels.append(P)
    for i in range(0, len(panels), 4):
        g = panels[i:i + 4]; H = sum(q.height for q in g); W = max(q.width for q in g)
        M = Image.new('RGB', (W, H), 'white'); y = 0
        for q in g:
            M.paste(q, (0, y)); y += q.height
        M.save(os.path.join(od, f'place_{i // 4:02d}.png'))
    with open(os.path.join(od, 'blobs.tsv'), 'w') as o:
        o.write('item\tblob\tx0\tx1\txc\n'); o.writelines('\t'.join(map(str, b)) + '\n' for b in blobs)
    print(len(its), 'items', (len(panels) + 3) // 4, 'sheets')


if __name__ == '__main__':
    main()
