#!/usr/bin/env python3
"""Cut tall native crops of the four L-grade gloss sites on no.37 f.60r and lay them out as one labelled sheet.

GAPS-fr4715-vieuville-pool-3 (2 Oct 2026, account-4). Reads only the on-disk native region (Gallica canvas 135,
region 560,1600,3250,1850; images/manifest.json); no request. Windows are in region pixels, taken from
scripts/cut_f60r_bands.py CENTRES and pass C's segment notes (600 px segments: s3 1080-1680, s4 1620-2220,
s5 2160-2760, s6 2700-3250). Each window runs from the centre of the line above to below the line itself, so the
interline gloss and both neighbours stay in view (the band edge cut L01's gloss in the earlier pass).

    python3 ciphers/fr4715-vieuville-pool/scripts/cut_f60r_gloss_sites.py [--out DIR]
"""
import argparse, os
from PIL import Image, ImageDraw

SRC = 'ciphers/fr4715-vieuville-pool/images/src_ark_12148_btv1b52509819x_f135_560_1600_3250_1850.jpg'
SITES = [  # label, (x0, y0, x1, y1) region px
    ('A  L01 right: run 16 65 40 25 50 90, glosses labr?/de?', (2050, 105, 3250, 250)),
    ('B  L20 middle: run 50 23 30 25 95, gloss legat', (1500, 1015, 2450, 1120)),
    ('C  L20 right-middle: du [16|bar], gloss dn', (2250, 1015, 3100, 1120)),
    ('D  L22 middle: interline above remede, barred 2 + pen? D^v', (1000, 1120, 2300, 1215)),
]
SCALE = 1.5

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--out', default='/tmp/f60r_gloss_sites'); a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    im = Image.open(SRC)
    crops = []
    for lab, (x0, y0, x1, y1) in SITES:
        c = im.crop((x0, y0, x1, y1)); c = c.resize((int(c.width * SCALE), int(c.height * SCALE)), Image.LANCZOS)
        c.save(os.path.join(a.out, f'site_{lab[0]}.jpg'), quality=92); crops.append((lab, (x0, y0, x1, y1), c))
    W = max(c.width for _, _, c in crops); H = sum(c.height + 34 for _, _, c in crops)
    sheet = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(sheet); y = 0
    for lab, box, c in crops:
        d.rectangle([0, y, W, y + 32], fill=(230, 230, 230))
        d.text((6, y + 10), f'{lab}   region x{box[0]}-{box[2]} y{box[1]}-{box[3]} (native +560,+1600), x{SCALE}', fill=(180, 0, 0))
        sheet.paste(c, (0, y + 34)); y += c.height + 34
    p = os.path.join(a.out, 'f60r_gloss_sites_sheet.jpg'); sheet.save(p, quality=92); print(p, sheet.size)

if __name__ == '__main__':
    main()
