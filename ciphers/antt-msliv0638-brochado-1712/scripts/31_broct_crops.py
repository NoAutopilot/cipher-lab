#!/usr/bin/env python3
"""BRO-CT (9 Oct 2026): cut glyph crops for the crossed-t compare from leaves on disk.

Boxes are leaf pixel coordinates (x0, y0, x1, y1), located from the iiif_lines.py line crops in images/crops_broct/ and
BRO-DF's band crops (images/crops_brodf/). Writes images/crops_broct/glyphs/<id>.jpg at a common height, and two
shuffled candidate sheets per look under neutral labels; the label->id map is written to broct_lookmap.tsv (not shown
to the looks). Deterministic (fixed seeds); a second run rewrites identical files.
"""
import random, os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(HERE, 'images')
OUT = os.path.join(IMG, 'crops_broct', 'glyphs')
GLYPHS = {
    # id: (leaf file, box, what it is)
    'X_l134_m0276r2p16': ('body/full_PT-TT-MSLIV-0638_m0276.jpg.jpg', (458, 420, 508, 466), 'letter 134 unkeyed t, target'),
    'T1_m0281_c15_p78': ('full_PT-TT-MSLIV-0638_m0281.jpg.jpg', (432, 608, 476, 652), 'appendix crossed t, Carta 15 idx78'),
    'T2_m0281_c15_p83': ('full_PT-TT-MSLIV-0638_m0281.jpg.jpg', (636, 608, 678, 652), 'appendix crossed t, Carta 15 idx83'),
    'T3_m0286_c74_p49': ('full_PT-TT-MSLIV-0638_m0286.jpg.jpg', (366, 1612, 414, 1652), 'appendix crossed t, Carta 74 idx49'),
    'D1_m0281_4': ('full_PT-TT-MSLIV-0638_m0281.jpg.jpg', (268, 608, 308, 652), 'decoy: code 4 (s), crossed'),
    'D2_m0281_7': ('full_PT-TT-MSLIV-0638_m0281.jpg.jpg', (238, 608, 270, 652), 'decoy: code 7 (e)'),
    'D3_m0286_fslash': ('full_PT-TT-MSLIV-0638_m0286.jpg.jpg', (898, 1600, 975, 1665), 'decoy: slashed f (s)'),
    'D4_m0286_20': ('full_PT-TT-MSLIV-0638_m0286.jpg.jpg', (1040, 1606, 1097, 1650), 'decoy: code 20 (l)'),
}
H = 160

def cut(gid):
    f, box, _ = GLYPHS[gid]
    im = Image.open(os.path.join(IMG, f)).convert('RGB').crop(box)
    w = round(im.width * H / im.height)
    return im.resize((w, H), Image.LANCZOS)

def sheet(labels_ids, path):
    tiles = [(lab, cut(g)) for lab, g in labels_ids]
    W = sum(t.width + 40 for _, t in tiles) + 20
    s = Image.new('RGB', (W, H + 60), 'white'); d = ImageDraw.Draw(s); x = 20
    for lab, t in tiles:
        s.paste(t, (x, 50)); d.text((x + t.width // 2 - 6, 10), lab, fill='black'); x += t.width + 40
    s.save(path, quality=92)

def main():
    os.makedirs(OUT, exist_ok=True)
    for g in GLYPHS:
        cut(g).save(os.path.join(OUT, g + '.jpg'), quality=92)
    cands = [g for g in GLYPHS if not g.startswith('X')]
    rows = ['look\tlabel\tglyph_id\tdescription']
    for look, seed in (('A', 1309), ('B', 7741)):
        order = cands[:]; random.Random(seed).shuffle(order)
        labs = [(str(i + 1), g) for i, g in enumerate(order)]
        sheet([('X', 'X_l134_m0276r2p16')], os.path.join(IMG, 'crops_broct', 'look%s_target.jpg' % look))
        sheet(labs, os.path.join(IMG, 'crops_broct', 'look%s_candidates.jpg' % look))
        rows += ['%s\t%s\t%s\t%s' % (look, l, g, GLYPHS[g][2]) for l, g in labs]
    open(os.path.join(HERE, 'broct_lookmap.tsv'), 'w').write('\n'.join(rows) + '\n')

if __name__ == '__main__':
    main()
