"""D22-CEPPO21: cut 4x tiles of every f.21v 8-token (S65/S80) from c23_cipher_w.jpg for the R-8 witness-shape read.
Centres are the worker's own estimates from the 13 iiif_lines bands (band centre y, x located by passC neighbours).
Usage: python3 cut_r8_tiles.py  (run from harvest/f21v/lookalike)"""
from PIL import Image, ImageOps, ImageDraw
T = [  # id, x, y, role
 ("L01.4",545,132,"P"),("L01.10",1105,132,"P"),("L01.27",2360,132,"P"),("L01.32",2750,132,"S"),
 ("L02.2.2",3305,210,"P"),
 ("L03.20",1925,283,"P"),("L03.26",2380,283,"P"),("L03.28",2520,283,"P"),("L03.34",2980,283,"P"),("L03.39",3315,283,"P"),
 ("L04.17",3210,367,"P"),
 ("L06.2.1",2040,542,"P"),("L06.2.6",2475,542,"P"),("L06.2.13",3145,542,"P"),
 ("L07.2",490,604,"S"),("L07.9",1050,604,"S"),("L07.15",1545,604,"S"),("L07.21",2040,604,"S"),("L07.31",2980,604,"S"),
 ("L08.1.4",655,691,"S"),("L08.2.1",3275,691,"S"),
 ("L09.5",650,771,"P"),("L09.12",1265,771,"S"),
 ("L10.2",2415,865,"S"),
 ("L11.9",1105,936,"P"),("L11.14",1560,936,"S"),("L11.28",2775,936,"S"),
]
if __name__ == "__main__":
    im = Image.open("../c23_cipher_w.jpg").convert("L")
    tiles = []
    for tid, x, y, role in T:
        t = im.crop((x-75, y-50, x+75, y+50)).resize((600, 400), Image.LANCZOS)
        t = ImageOps.autocontrast(t)
        t.save(f"r8_tiles/{tid}.jpg", quality=92)
        tiles.append((tid, t))
    for k in range(0, len(tiles), 6):
        batch = tiles[k:k+6]
        sheet = Image.new("L", (1220, 3*430), 255); d = ImageDraw.Draw(sheet)
        for j, (tid, t) in enumerate(batch):
            X, Y = (j % 2)*610, (j//2)*430
            sheet.paste(t, (X, Y+28)); d.text((X+4, Y+4), f"tile {k+j+1}", fill=0)
        sheet.save(f"r8_tiles/sheet{k//6+1}.jpg", quality=90)
