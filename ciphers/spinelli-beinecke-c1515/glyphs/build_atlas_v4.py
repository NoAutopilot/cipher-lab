#!/usr/bin/env python3
"""atlas_v4 (TXE2-SHEETAUDIT, 9 Oct 2026): atlas.png v3 with its mislabelled exemplar tiles removed, read-free otherwise.

Tile surgery on atlas.png (v3 left untouched): rows of 72 px, tile k of a row at x = (k + 2) * 72 (tools/glyph_atlas.py
cmd_atlas layout); labels and cluster counts are kept as drawn in v3.
  removed  SIX       p1_01_025  h-shaped; the box is a committed ESS (= h, key.tsv H) sign (V2 / TXV-SPIN; sheet audit MISLABELLED)
  removed  SIX       p1_05_010  h-shaped (the published key's h, not SIX's 6 null cell); its row is excluded, never scored
  moved    SIX->ESS  p1_08_030  h-shaped; the box is in no committed reconciliation, so no truth position at all
  removed  OMEGABAR  p1_03_017  omega with dots above; committed OMEGADOT (sheet audit MISLABELLED)
  removed  TEE       p1_03_001  plus with a foot; committed PLUS (sheet audit MISLABELLED)
No tile was chosen by looking up an eval position's truth; the one tile added (p1_08_030) has no truth position.

    python3 build_atlas_v4.py           # writes atlas_v4.png, atlas_v4.tsv
    python3 build_atlas_v4.py --check   # exit 1 if the committed atlas_v4.* differ from a rebuild
"""
import csv, hashlib, io, os, sys
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
CELL = 72
REMOVE = {('SIX', 'p1_01_025'), ('SIX', 'p1_05_010'), ('SIX', 'p1_08_030'), ('OMEGABAR', 'p1_03_017'), ('TEE', 'p1_03_001')}
ADD = {'ESS': [('SIX', 'p1_08_030')]}   # target row <- (source row, sid)


def build():
    im = Image.open(os.path.join(HERE, 'atlas.png')).convert('L')
    rows = list(csv.DictReader(open(os.path.join(HERE, 'atlas.tsv')), delimiter='\t'))
    tile = {}
    for i, r in enumerate(rows):
        for k, sid in enumerate(r['exemplars'].split(',')):
            x = (k + 2) * CELL
            tile[(r['code'], sid)] = im.crop((x, i * CELL, x + CELL, (i + 1) * CELL))
    out = Image.new('L', im.size, 255)
    trows = []
    for i, r in enumerate(rows):
        out.paste(im.crop((0, i * CELL, 2 * CELL, (i + 1) * CELL)), (0, i * CELL))
        ex = [(r['code'], s) for s in r['exemplars'].split(',') if (r['code'], s) not in REMOVE] + ADD.get(r['code'], [])
        for k, key in enumerate(ex):
            out.paste(tile[key], ((k + 2) * CELL, i * CELL))
        for x in range(im.size[0]):
            out.putpixel((x, (i + 1) * CELL - 1), 190)
        trows.append({**r, 'exemplars': ','.join(s for _, s in ex)})
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=list(rows[0].keys()), delimiter='\t', lineterminator='\n')
    w.writeheader(); w.writerows(trows)
    png = io.BytesIO(); out.save(png, format='PNG', optimize=False)
    return png.getvalue(), buf.getvalue()


if __name__ == '__main__':
    png, tsv = build()
    pp, tp = os.path.join(HERE, 'atlas_v4.png'), os.path.join(HERE, 'atlas_v4.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(pp) and open(pp, 'rb').read() == png and open(tp).read() == tsv
        print('atlas_v4:', 'ok' if ok else 'STALE', hashlib.sha256(png).hexdigest()); sys.exit(0 if ok else 1)
    open(pp, 'wb').write(png); open(tp, 'w').write(tsv)
    print('atlas_v4.png sha256', hashlib.sha256(png).hexdigest())
