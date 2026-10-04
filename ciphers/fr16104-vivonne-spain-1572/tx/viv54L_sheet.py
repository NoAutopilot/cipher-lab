#!/usr/bin/env python3
"""N7-VIV54L: a text candidate sheet for tools/lookalike_pass.py (ids + the tx/SIGNS.md shape description, no values).

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv54L_sheet.py

The two blind passes read against tx/SIGNS.md's words, not a picture, so the look-alike sheet carries the same words:
one 110 px cell per label (9 columns), the id large and SIGNS.md's description small. Writes tx/lookalike54/sheet.png + sheet_map.json.
"""
import json, os
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'lookalike54')
DESC = {'m': 'three humps', 'n': 'two humps', 'd': 'round body, ascender curling left (delta)', 'y': 'y / long swash y',
        'p': 'p with descender', 'tz': 't joined to z-like descender', 'to': 't + closed loop', '3': 'round-topped 3 with descender',
        'z': 'FLAT-topped z', '#': 'double-crossed sign #/H', ':': 'two dots side by side', 'P': 'pi-like, two uprights + top bar',
        'S': 'long s, below line, no crossbar', 'f': 'f with crossbar', 'A': 'capital A', '@': 'a with big curl on left',
        'V': 'long backslash / V stroke', 'R': 'r-like with loop, R / rt', 'L': 'capital L', 'o': 'small round o', 's': 'short s',
        'a': 'a', '4': 'digit 4 (crossed descender)', '+': 'plus / cross', 'x': 'x', 'g': 'g', 'r': 'r', 'c': 'c', 'e': 'e',
        'h': 'h', 'k': 'k', 'b': 'b', 'j': 'j', 'l': 'l', '2': 'digit 2', '6': 'digit 6', '7': 'digit 7', '8': 'digit 8', 't': 't'}


def main():
    ids = []
    for ln in open(os.path.join(OUT, 'confusion.tsv'), encoding='utf-8'):
        f = ln.rstrip('\n').split('\t')
        if f[0] != 'label_a':
            ids += [x for x in f[:2] if x not in ids]
    ids = sorted(set(ids) | set(DESC))
    cell, cols = 110, 9
    im = Image.new('RGB', (cols * cell, ((len(ids) + cols - 1) // cols) * cell), 'white')
    dr = ImageDraw.Draw(im)
    big = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 30)
    sm = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 10)
    for n, t in enumerate(ids):
        x, y = (n % cols) * cell, (n // cols) * cell
        dr.rectangle((x, y, x + cell - 1, y + cell - 1), outline='grey')
        dr.text((x + 6, y + 6), t[:8], fill='black', font=big)
        words, line, yy = DESC.get(t, t.strip('{}')).split(), '', y + 50
        for w in words:
            if len(line) + len(w) > 16:
                dr.text((x + 4, yy), line, fill='black', font=sm); yy += 12; line = ''
            line = (line + ' ' + w).strip()
        dr.text((x + 4, yy), line, fill='black', font=sm)
    im.save(os.path.join(OUT, 'sheet.png'))
    json.dump([{'id': t} for t in ids], open(os.path.join(OUT, 'sheet_map.json'), 'w'), indent=0)
    print(len(ids), 'cells')


if __name__ == '__main__':
    main()
