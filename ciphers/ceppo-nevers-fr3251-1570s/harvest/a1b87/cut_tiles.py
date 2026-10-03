"""A1B-CEPPO-87 (3 Oct 2026): tight tiles for the blind reads. Line crops first came from
  python3 tools/iiif_lines.py --image ciphers/ceppo-nevers-fr3251-1570s/harvest/f87/c88_cipher_wt.jpg --out <scratch> --debug
(f.87, 7 bands) and from the bands already in birago harvest/f36r/cut_f36r.py and f36gloss/cut_gloss.py (fr.3252).
Boxes are native px of the committed regions; autocontrast, upscaled 3x. python3 cut_tiles.py -> a1b87/tiles/*.png"""
from pathlib import Path
from PIL import Image, ImageOps
H = Path(__file__).resolve().parent
W = H / '../witness_f36'
TILES = {
    'T1': (H / '../f87/c88_cipher_wt.jpg', (2820, 670, 3060, 790)),   # f.87 L04.37-L04.41 (target L04.39)
    'T2': (W / 'c37_f36r_cipher.jpg', (40, 1250, 520, 1450)),        # f.36r r36n_L11 pos 1-6 + gloss band
    'T3': (W / 'c37_f36r_cipher.jpg', (2150, 1450, 2720, 1640)),     # f.36r r36n_L13 ~pos 27-33 + gloss band
    'T4': (W / 'c38_f37r_cipher.jpg', (1150, 87, 1800, 250)),        # f.37r r37_L01 ~pos 12-19 + gloss band
}
if __name__ == '__main__':
    (H / 'tiles').mkdir(exist_ok=True)
    for k, (src, box) in TILES.items():
        im = ImageOps.autocontrast(Image.open(src).convert('L').crop(box), cutoff=1)
        im = im.resize((im.width * 3, im.height * 3), Image.LANCZOS)
        im.save(H / 'tiles' / f'{k}.png'); print(k, box, im.size)
