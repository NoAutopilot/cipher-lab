#!/usr/bin/env python3
"""Name cards for the f.23r sign sorter (A4-SORTFIX, 5 Oct 2026).

Why: the first published page (DIN-SORTER) had piles only for the labels the two R4 passes agreed on, so the
21 "Check these first" tiles asked "which sheet label?" with no 0' / v' / o / D / t ... pile to drop them into
(account-3 orchestrator's flag, ROOM.md 5 Oct 2026 22:52). tools/sign_sorter.py makes a pile only from a
labelled tile, so this script adds one grey *name card* per missing label -- every f.130 sheet label
(f130/inventory.tsv, 'plus' written '+') plus any label a check-first reader offered (t, Z, ...) -- drawn on
a synthetic page `pages/cards.png`. A card is not a sign: its sid starts `card_`, and anything applying the
owner's sort drops `card_` rows (sorter/README.md). It also rewrites each check-first question as a
pick-one choice naming the piles.

Run from ciphers/fr3621-dinteville-1592:  python3 sorter/add_cards.py
Writes sorter/signs_cards.tsv, sorter/labels_cards.tsv, sorter/focus_cards.tsv, sorter/pages/cards.png.
No sign values: card texts are sheet labels only.
"""
import csv, os, re
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FAM = 'Sheet labels with no tile yet (grey name card; drop real tiles here)'


def rows(p):
    with open(p, newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main():
    signs = rows(os.path.join(HERE, 'signs.tsv'))
    labels = rows(os.path.join(HERE, 'labels.tsv'))
    have = {r['sign'] for r in labels}
    inv = [r['sign'] for r in rows(os.path.join(HERE, '..', 'f130', 'inventory.tsv'))]
    inv = ['+' if s == 'plus' else s for s in inv]
    focus = [l.rstrip('\n').split('\t', 1) for l in open(os.path.join(HERE, 'focus.tsv')) if l.strip()]
    offered = []
    for sid, q in focus:
        m = re.search(r'pass A (\S+), pass B (\S+);', q)
        offered += [x for x in (m.group(1), m.group(2)) if x != '-']
    want = []
    for s in inv + offered:
        if s not in have and s not in want and s != 'UNREAD':
            want.append(s)
    # page of cards: 100 px boxes, 220 px apart, 140 px clear above (the tile cut takes 0.9 h of margin above)
    W, top, step, box = 220 * 6, 140, 300, 100
    H = top + step * ((len(want) + 5) // 6)
    im = Image.new('L', (W, H), 255)
    d = ImageDraw.Draw(im)
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 34)
    small = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 14)
    out_s, out_l = [], []
    for i, s in enumerate(want):
        x, y = 60 + 220 * (i % 6), top + step * (i // 6)
        d.rectangle([x, y, x + box, y + box], fill=200, outline=90, width=3)
        t = s if len(s) <= 6 else s[:6]
        tw = d.textlength(t, font=font)
        d.text((x + (box - tw) / 2, y + 22), t, fill=0, font=font)
        cw = d.textlength('name card', font=small)
        d.text((x + (box - cw) / 2, y + 74), 'name card', fill=60, font=small)
        sid = 'card_' + re.sub(r'[^A-Za-z0-9]', lambda m: 'x%02x' % ord(m.group()), s)
        out_s.append({'sid': sid, 'page': 'cards', 'x': x, 'y': y, 'w': box, 'h': box})
        out_l.append({'sid': sid, 'sign': s, 'family': FAM})
    im.save(os.path.join(HERE, 'pages', 'cards.png'), optimize=True)
    for name, base, extra, cols in (('signs_cards.tsv', signs, out_s, ['sid', 'page', 'x', 'y', 'w', 'h']),
                                    ('labels_cards.tsv', labels, out_l, ['sid', 'sign', 'family'])):
        with open(os.path.join(HERE, name), 'w', newline='') as f:
            w = csv.DictWriter(f, cols, delimiter='\t', lineterminator='\n', extrasaction='ignore')
            w.writeheader(); w.writerows(base + extra)
    with open(os.path.join(HERE, 'focus_cards.tsv'), 'w') as f:
        for sid, q in focus:
            m = re.search(r'^(\S+): pass A (\S+), pass B (\S+);', q)
            pos, a, b = m.groups()
            opts = [x for x in (a, b) if x != '-']
            if len(opts) == 2:
                ask = f'{pos}: readers split {a} / {b}. Tap the {a} pile or the {b} pile'
            else:
                ask = f'{pos}: one reader saw {opts[0]}, the other nothing. Tap the {opts[0]} pile, or Not a letter'
            f.write(f'{sid}\t{ask} (or 0, 0\', o, v, v\', D or any other pile if it is none of these).\n')
    print(f'{len(want)} name cards: {" ".join(want)}')


if __name__ == '__main__':
    main()
