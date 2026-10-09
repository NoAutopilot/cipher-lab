#!/usr/bin/env python3
"""UNA-BIR3252 (9 Oct 2026): per-sign 4x tiles of the f.36-37 rule-pair splits and the known-answer tiles, cut from the
native bands of ../../../ceppo-nevers-fr3251-1570s/harvest/witness_f36/ (no network). x = the sign's centre on the native
band, located by this worker from passD/recon neighbours on 1x strips with an x ruler (not by "pos k of n"); y = the row-ink
peak of the sign column inside the line band (the band centres of cut_lines.BLOCKS), so the tile holds the sign body and not
the gloss line above it. Tiles are shuffled with a fixed seed and numbered; the id <-> tile map goes to tiles/tiles_key.tsv.
Usage: python3 cut_una_tiles.py   (run from harvest/f3637)"""
import random, sys
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
W36 = Path(__file__).resolve().parents[3] / 'ceppo-nevers-fr3251-1570s/harvest/witness_f36'
sys.path.insert(0, str(W36))
from cut_lines import BLOCKS
OUT = Path(__file__).resolve().parent / 'tiles'
# id, line, pos, x, role (K = known answer, T = target), candidates
T = [
 ("K1", "v36top_L01", 3, 1230, "K", "X_THETA2|S69"), ("K2", "v36top_L01", 5, 1410, "K", "S80|S65"),
 ("K3", "v36top_L01", 18, 2310, "K", "S69|X_THETA2"), ("K4", "v36top_L02", 2, 1130, "K", "S88|S24"),
 ("K5", "v36top_L03", 2, 1110, "K", "S88|S24"), ("K6", "v36top_L03", 18, 2290, "K", "S65|S80"),
 ("r36_L01.6", "r36_L01", 6, 2270, "T", "S80|S65"), ("r36_L02.37", "r36_L02", 37, 2420, "T", "S80|S65"),
 ("r36_L03.37", "r36_L03", 37, 2600, "T", "S80|S65"), ("r36_L08.8", "r36_L08", 8, 500, "T", "S80|S65"),
 ("v36top_L02.16", "v36top_L02", 16, 2160, "T", "S88|S24"), ("v36top_L02.37", "v36top_L02", 37, 3740, "T", "S24|S88"),
 ("v36top_L05.16", "v36top_L05", 16, 2240, "T", "S24|S88"), ("v36mid_L04.8", "v36mid_L04", 8, 1510, "T", "S24|S88"),
 ("r36_L01.1", "r36_L01", 1, 1960, "T", "S54|S74"), ("r36_L04.31", "r36_L04", 31, 2110, "T", "S74|S54"),
 ("v36top_L01.33", "v36top_L01", 33, 3400, "T", "S74|S54"), ("v36top_L04.37", "v36top_L04", 37, 3200, "T", "S74|S54"),
 ("v36top_L05.26", "v36top_L05", 26, 2880, "T", "S74|S54"), ("v36mid_L02.4", "v36mid_L02", 4, 1260, "T", "S74|S54"),
 ("v36mid_L03.3", "v36mid_L03", 3, 1200, "T", "S74|S54"),
 ("v36top_L03.8", "v36top_L03", 8, 1570, "T", "S69|X_THETA2"), ("v36top_L04.33", "v36top_L04", 33, 2860, "T", "S69|X_THETA2"),
 ("v36top_L05.4", "v36top_L05", 4, 1310, "T", "S69|X_THETA2"), ("v36top_L05.17", "v36top_L05", 17, 2310, "T", "S69|X_THETA2"),
 ("v36top_L05.37", "v36top_L05", 37, 3640, "T", "S69|X_THETA2"), ("v36mid_L02.31", "v36mid_L02", 31, 3070, "T", "S69|X_THETA2"),
 ("v36mid_L03.24", "v36mid_L03", 24, 2560, "T", "S69|X_THETA2"), ("v36mid_L06.11", "v36mid_L06", 11, 1880, "T", "S69|X_THETA2"),
 ("v36top_L04.19", "v36top_L04", 19, 2150, "T", "S88|X_THETA2"),
 ("r36_L04.4", "r36_L04", 4, 240, "T", "S23|S97"), ("r36_L06.22", "r36_L06", 22, 1390, "T", "S23|S97"),
 ("v36mid_L02.19", "v36mid_L02", 19, 2240, "T", "S23|S97"), ("v36mid_L02.28", "v36mid_L02", 28, 2840, "T", "S23|S97"),
 ("v36mid_L06.3", "v36mid_L06", 3, 1200, "T", "S23|S97"),
]

def band(line):
    pref, n = line.rsplit('_L', 1)
    for src, p, lines, x0, x1 in BLOCKS:
        if p == pref:
            return src, lines[int(n) - 1][0]

def centre_y(im, x, c):
    """Row-ink peak of the column x-40..x+40 in c-90..c+60, smoothed over 31 rows."""
    g = im.crop((x - 40, c - 90, x + 40, c + 60)); w, h = g.size; px = g.load()
    prof = [sum(255 - px[i, j] for i in range(w)) for j in range(h)]
    sm = [sum(prof[max(0, j - 15):j + 16]) for j in range(h)]
    return c - 90 + max(range(h), key=lambda j: sm[j])

if __name__ == '__main__':
    OUT.mkdir(exist_ok=True); ims = {}
    order = list(range(len(T))); random.Random(3252).shuffle(order)
    key = ["tile\tid\tline\tpos\tx\ty\trole\tcands\tsrc"]; tiles = []
    for k, i in enumerate(order, 1):
        tid, line, pos, x, role, cands = T[i]; src, c = band(line)
        im = ims.setdefault(src, Image.open(W36 / src).convert('L'))
        y = centre_y(im, x, c)
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
