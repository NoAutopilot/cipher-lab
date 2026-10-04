#!/usr/bin/env python3
"""N7-VIV54R: per-position windows for the value-blind col-u row-3 judge (PREREG-N7VIV54R.md).

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv54R_windows.py

Every passD position of ink 54 labelled z, x, R, 3 or 2 gets a window (tx/viv53L_windows.py window/montage, imported), 6 per montage,
plus tx/lookalike54/viv54R_win/ref.png (key cells col u row 3 and col a row 3 from henryiii_Vivonne1.png). Writes
tx/lookalike54/viv54R_items.tsv and viv54R_prompt.md. No decoded text, key value or hypothesis goes into the prompt.
"""
import csv, os, sys
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import viv53L_windows as w53  # noqa: E402
w53.IMG = os.path.join(T, 'images')
LA = os.path.join(HERE, 'lookalike54')
OUT = os.path.join(LA, 'viv54R_win')
LABELS = ('z', 'x', 'R', '3', '2')
KEY = os.path.join(T, '..', '..', 'sources', 'cryptiana', 'web', 'henryiii_Vivonne1.png')


def ref():
    im = Image.open(KEY).convert('L')
    # cells in the 543x213 image (3x view: col u x~1205-1265, col a x~0-45; row 3 y~185-230 -> /3)
    a = im.crop((0, 58, 22, 80)).resize((132, 132)); u = im.crop((400, 58, 425, 80)).resize((150, 132))
    out = Image.new('L', (330, 170), 255); out.paste(u, (5, 30)); out.paste(a, (190, 30))
    d = ImageDraw.Draw(out); d.text((5, 5), 'REF A (Sigma class)', fill=0); d.text((190, 5), 'REF B (Zed class)', fill=0)
    out.save(os.path.join(OUT, 'ref.png'))


def main():
    os.makedirs(OUT, exist_ok=True); ref()
    items, wins, strips, lines = [], [], {}, []
    for page in ('f173r', 'f173v'):
        nline = {}
        for r in csv.DictReader(open(os.path.join(LA, 'align', page, 'passC.tsv')), delimiter='\t'):
            nline[f"{page}_{r['passage']}"] = nline.get(f"{page}_{r['passage']}", 0) + 1
        bx = {page: w53.boxes(page)}
        rows = list(csv.DictReader(open(os.path.join(LA, f'viv54L_{page}_passD.tsv')), delimiter='\t'))
        byl = {}
        for r in rows:
            byl.setdefault(r['passage'], []).append(r['sign_id'])
        for r in rows:
            if r['sign_id'] not in LABELS:
                continue
            seq, p = byl[r['passage']], int(r['pos'])
            tid = f"{page}.{r['passage']}.{p}"
            items.append({'id': tid, 'page': page, 'passage': r['passage'], 'pos': p, 'label': r['sign_id']})
            wins.append((tid, w53.window(strips, bx, nline, f"{page}_{r['passage']}", p)))
            lines.append(f"{tid}\tbefore: {' '.join(seq[max(0, p - 4):p - 1])} | after: {' '.join(seq[p:p + 3])}")
    pngs = w53.montage(wins, OUT, 'viv54R')
    with open(os.path.join(LA, 'viv54R_items.tsv'), 'w') as o:
        wr = csv.DictWriter(o, fieldnames=list(items[0]), delimiter='\t', lineterminator='\n'); wr.writeheader(); wr.writerows(items)
    prompt = f"""# Shape judge by window, ink 54 (value-blind)

{len(items)} positions. First open the reference image {os.path.join(OUT, 'ref.png')}: REF A and REF B are two signs from a 16th-century
cipher table. Then open the montages IN ORDER (6 windows each, captioned in blue with the position id). In each window the red ticks mark
the ESTIMATED position of the sign (can be 1-3 signs off); find it using the keyboard labels of the signs just before and after it.

For each position give ONE class for the sign's SHAPE:
  SIGMA  = two horizontal bars (top and bottom) joined by a near-upright stem, or a stem that bends back; NO diagonal stroke running
           from upper right to lower left (like REF A, a Sigma or a capital I with bars)
  ZED    = top bar and bottom bar joined by a DIAGONAL stroke (like REF B), including a crossed z or a 2-shaped z with a diagonal
  OTHER  = a round-topped 3 (curved top, descender), an x, an r-like loop, a digit 2 without a bottom bar, or anything else
  UNSURE = you cannot find the sign or cannot tell
conf H clear / M probable / L guess.

Montages: {', '.join(pngs)}

Answer with one TSV row per position, header: id<TAB>class<TAB>conf<TAB>note   (note = the stroke feature you SAW, e.g. "upright stem").
Write the answer to {os.path.join(LA, 'viv54R_judge.tsv')}. Judge shapes only; do not guess any meaning.

Positions (id, neighbours):
""" + '\n'.join(lines) + '\n'
    open(os.path.join(LA, 'viv54R_prompt.md'), 'w').write(prompt)
    print(len(items), 'positions,', len(pngs), 'montages')


if __name__ == '__main__':
    main()
