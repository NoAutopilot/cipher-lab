# TX-ATLAS-B72 (3 Oct 2026): the page list of the Birago 1572 family atlas, from images already on disk (no refetch).
# Each page is a native-resolution Gallica region fetched by tools/iiif_lines.py (its src_*.jpg); where that source
# file is no longer on disk (f184v, f185r) the page is re-assembled from the line crops at their manifest boxes.
# Usage (from the repo root): python3 ciphers/nevers-birago-fr3251-1572/atlas/pages.py  -> prints --page args, writes
# atlas/pages/<name>.jpg only for re-assembled pages (gitignored, regenerable).
import json, os, sys, glob
from PIL import Image
R = os.path.dirname(os.path.abspath(__file__)); H = os.path.join(R, '..', 'harvest')
F117 = os.path.join(R, '..', '..', 'birago-fr3252-1571-72', 'images', 'f117')
# page name -> (letter, harvest folder). f170 holds no.86's f.174r source (canvas 177).
PAGES = [('f139v', 'no71', 'f139v'), ('f144r', 'no73', 'f144r'), ('f152r', 'no77', 'f152r'), ('f162r', 'no82', 'f162r'),
         ('f168r', 'no85', 'f168r'), ('f168v', 'no85', 'f168v'), ('f174r', 'no86', 'f174r'), ('f174v', 'no86', 'f174v'),
         ('f174vB', 'no86', 'f174vB'), ('f175r', 'no86', 'f175r'), ('f175v', 'no86', 'f175v'), ('f178r', 'no87', 'f178r'),
         ('f178v', 'no87', 'f178v'), ('f179r', 'no87', 'f179r'), ('f184r', 'no90', 'f184r'), ('f184v', 'no90', 'f184v'),
         ('f185r', 'no90', 'f185r'), ('f117r', 'fr3252-no77', F117)]


def entries(folder):
    return json.load(open(os.path.join(folder, 'manifest.json')))['iiif_lines']


def source(name, folder):
    folder = folder if os.path.isabs(folder) else os.path.join(H, folder)
    es = entries(folder)
    sf = es[0]['source_file']
    for cand in (os.path.join(folder, sf), *glob.glob(os.path.join(H, '*', sf))):
        if os.path.exists(cand):
            return cand, es
    # re-assemble from the crops at their boxes (canvas coordinates)
    x0 = min(e['box'][0] for e in es); y0 = min(e['box'][1] for e in es)
    W = max(e['box'][2] for e in es) - x0; Hh = max(e['box'][3] for e in es) - y0
    can = Image.new('L', (W, Hh), 255)
    for e in es:
        can.paste(Image.open(os.path.join(folder, e['crop'])).convert('L'), (e['box'][0] - x0, e['box'][1] - y0))
    os.makedirs(os.path.join(R, 'pages'), exist_ok=True)
    out = os.path.join(R, 'pages', f'{name}.jpg'); can.save(out, quality=95)
    return out, es


if __name__ == '__main__':
    for name, letter, folder in PAGES:
        p, _ = source(name, folder)
        print(f'--page {name}={os.path.relpath(p)}', end=' ')
    print()
