#!/usr/bin/env python3
"""UNA2-BIR3252 (9 Oct 2026): attempt 2 of the UNA-BIR3252 tile design (PREREG-UNA2.md). Re-cuts the 7 target tiles that
attempt 1 left UNDECIDED for location (mislocated row or tile edge) at x,y set by this worker's eye on 2x ruler strips of the
native band (the row-ink peak search is not used), plus the same 6 known-answer tiles at attempt 1's x,y (tiles/tiles_key.tsv).
Same geometry as cut_una_tiles.py: 150 x 80 native px, autocontrast cutoff 1, 4x LANCZOS. Shuffled with seed 32522; the
id <-> tile map goes to tiles2/tiles_key.tsv (not opened until reads_una2_blind.tsv is pushed).
Usage: python3 cut_una2_tiles.py   (run from harvest/f3637; disk only)"""
import csv, random
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
HERE = Path(__file__).resolve().parent
W36 = HERE.parents[2] / 'ceppo-nevers-fr3251-1570s/harvest/witness_f36'
OUT = HERE / 'tiles2'
# id, line, pos, x, y, role, candidates, src  (eye-set x,y; attempt-1 x,y in the comment)
T = [
 ("v36top_L02.37", "v36top_L02", 37, 3785, 372, "T", "S24|S88", "c38_f36v_top.jpg"),     # was 3740,261 (L01 row)
 ("r36_L02.37", "r36_L02", 37, 2480, 262, "T", "S80|S65", "c37_f36r_cipher.jpg"),        # was x 2420 (the theta)
 ("r36_L01.1", "r36_L01", 1, 1988, 150, "T", "S54|S74", "c37_f36r_cipher.jpg"),          # was 1960,95 (above the row)
 ("v36top_L05.26", "v36top_L05", 26, 2878, 670, "T", "S74|S54", "c38_f36v_top.jpg"),     # was y 566 (L04 row)
 ("r36_L04.4", "r36_L04", 4, 293, 428, "T", "S23|S97", "c37_f36r_cipher.jpg"),           # was x 240 (between delta and lambda)
 ("r36_L08.8", "r36_L08", 8, 555, 1070, "T", "S80|S65", "c37_f36r_cipher.jpg"),          # was x 500 (the theta)
 ("v36top_L05.16", "v36top_L05", 16, 2240, 672, "T", "S24|S88", "c38_f36v_top.jpg"),     # was y 566 (L04 row)
]

if __name__ == '__main__':
    for r in csv.DictReader(open(HERE / 'tiles/tiles_key.tsv'), delimiter='\t'):
        if r['role'] == 'K':
            T.append((r['id'], r['line'], int(r['pos']), int(r['x']), int(r['y']), 'K', r['cands'], r['src']))
    OUT.mkdir(exist_ok=True); ims = {}
    order = list(range(len(T))); random.Random(32522).shuffle(order)
    key = ["tile\tid\tline\tpos\tx\ty\trole\tcands\tsrc"]; tiles = []
    for k, i in enumerate(order, 1):
        tid, line, pos, x, y, role, cands, src = T[i]
        im = ims.setdefault(src, Image.open(W36 / src).convert('L'))
        t = ImageOps.autocontrast(im.crop((x - 75, y - 40, x + 75, y + 40)), cutoff=1).resize((600, 320), Image.LANCZOS)
        t.save(OUT / f't{k:02d}.jpg', quality=92); tiles.append((k, t))
        key.append(f"{k}\t{tid}\t{line}\t{pos}\t{x}\t{y}\t{role}\t{cands}\t{src}")
    (OUT / 'tiles_key.tsv').write_text("\n".join(key) + "\n")
    for s in range(0, len(tiles), 8):
        b = tiles[s:s + 8]; sheet = Image.new('L', (1220, 4 * 350), 255); d = ImageDraw.Draw(sheet)
        for j, (k, t) in enumerate(b):
            X, Y = (j % 2) * 610, (j // 2) * 350
            sheet.paste(t, (X, Y + 26)); d.text((X + 4, Y + 6), f"tile {k}", fill=0)
        sheet.save(OUT / f'sheet{s // 8 + 1}.jpg', quality=88)
    print(len(tiles), 'tiles,', (len(tiles) + 7) // 8, 'sheets')
