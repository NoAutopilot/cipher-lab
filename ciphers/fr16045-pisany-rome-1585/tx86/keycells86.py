#!/usr/bin/env python3
"""Cut Tomokiyo's 1586-87 table (sources/cryptiana/web/henryiii_Vivonne5.png, captioned "Vivonne's Cipher (1586-1587)")
into value-blind labelled cells T01.. -> SIGNSHEET86.png, and write ../key86.tsv (values, published: Tomokiyo).
Cell centres are in the PNG's own pixels (688x245), read by eye on a 2x grid (RUN3-PISA, 4 Oct 2026)."""
import os
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '../../../sources/cryptiana/web/henryiii_Vivonne5.png')
R = {1: 34, 2: 52, 3: 73, 4: 89}
# (value, cx, cy, circled/uncertain note)
cells = [
 ("a",8,R[1],""),("b",30,R[1],""),("c",53,R[1],""),("d",75,R[1],""),("e",98,R[1],""),("f",120,R[1],"circled"),
 ("g",142,R[1],""),("h",165,R[1],""),("i",188,R[1],""),("l",210,R[1],""),("m",233,R[1],""),("n",255,R[1],""),
 ("o",278,R[1],""),("p",302,R[1],""),("q",326,26,"small, raised"),("r",347,R[1],"circled"),("s",370,R[1],"circled"),
 ("t",393,R[1],""),("u",413,R[1],""),("x",435,R[1],""),("y",458,R[1],""),("<null>",525,R[1],""),
 ("a",8,R[2],""),("c",57,R[2],""),("d",75,R[2],""),("e",98,R[2],""),("f",123,R[2],""),("g",142,R[2],""),
 ("i",188,R[2],""),("l",210,R[2],""),("m",236,R[2],"circled with n2"),("n",258,R[2],"circled with m2"),
 ("o",280,R[2],""),("p",300,R[2],"circled"),("r",347,R[2],"circled with s2"),("s",370,R[2],"circled with r2"),
 ("t",393,R[2],""),("u",413,R[2],"circled"),("<null>",525,R[2],""),
 ("a",8,R[3],""),("e",100,R[3],""),("f",120,R[3],""),("i",188,R[3],""),("l",210,R[3],""),("o",275,R[3],"circled"),
 ("u",413,R[3],""),
 ("m",235,R[4],""),("n",257,R[4],""),("s",370,R[4],""),("t",393,R[4],""),("u",413,R[4],""),
 ("ambassadeur",50,150,""),("pour",112,150,""),("est",165,150,""),("faict",220,150,""),("faire",258,150,""),
 ("la",325,150,"circled"),("le",352,150,""),("ligue",392,150,""),("ont",435,150,"circled"),("par",475,150,"circled"),
 ("que",525,150,""),("qui",572,150,"circled"),("roy",615,150,""),("votre",657,150,""),
 ("le",352,172,"alternative, marked ?"),("le",352,192,"alternative, marked ?"),
 ("Angleterre",52,193,""),("entreprise",127,193,""),("car",190,193,""),("Espagne",252,190,"circled"),
 ("monsieur",528,186,""),("monsieur",532,215,"alternative, marked ?"),
]
def main():
    im = Image.open(SRC).convert('RGB')
    S, half = 4, 13
    cw, ch = 2 * half * S + 10, 2 * half * S + 26
    cols = 10
    rows = (len(cells) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * cw, rows * ch), 'white')
    d = ImageDraw.Draw(sheet)
    out = ["sign\tvalue\tcell_xy\tnote\tsource"]
    for i, (v, x, y, note) in enumerate(cells):
        lab = "T%02d" % (i + 1)
        box = (x - half, y - half, x + half, y + half)
        c = Image.new('RGB', (2 * half, 2 * half), 'white'); c.paste(im.crop((max(box[0], 0), box[1], box[2], box[3])), (max(box[0], 0) - box[0], 0))
        c = c.resize((2 * half * S, 2 * half * S), Image.LANCZOS)
        # blank any magenta header pixels so no printed value leaks into a cell
        px = c.load()
        for a in range(c.width):
            for b in range(c.height):
                r, g, bb = px[a, b]
                if r - g > 25 and bb - g > 10:
                    px[a, b] = (255, 255, 255)
        gx, gy = (i % cols) * cw, (i // cols) * ch
        sheet.paste(c, (gx + 5, gy + 22))
        d.rectangle([gx + 4, gy + 21, gx + cw - 5, gy + ch - 3], outline=(160, 160, 160))
        d.text((gx + 6, gy + 4), lab, fill=(200, 0, 0))
        out.append(f"{lab}\t{v}\t{x},{y}\t{note}\tpublished: Tomokiyo, cryptiana henryiii.htm 'Vivonne's Cipher (1586-1587)' (henryiii_Vivonne5.png)")
    sheet.save(os.path.join(HERE, 'SIGNSHEET86.png'))
    open(os.path.join(HERE, '../key86.tsv'), 'w').write("\n".join(out) + "\n")
    print(len(cells), "cells")
if __name__ == '__main__':
    main()
