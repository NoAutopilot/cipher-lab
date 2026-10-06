#!/usr/bin/env python3
"""R12A-BALS (6 Oct 2026): the 13 cipher lines of Baluze 170 f.228r-v as (line, source region file, centre y, x0, x1) in
that region's own pixels, from images/crops/manifest.json (D1-BAL170/170B crops). Imported by build_inputs.py."""
import json
from pathlib import Path
T = Path(__file__).resolve().parents[1]
LINES = ['b170f228r_a_L02', 'b170f228r_c_L01', 'b170f228r_b_L01', 'b170f228r_b_L02',
         'b170f228v_a_L01', 'b170f228v_a_L02'] + [f'b170f228v_b_L0{i}' for i in range(1, 8)]


def geometry():
    m = json.load(open(T / 'images/crops/manifest.json'))['iiif_lines']
    out = {}
    for e in m:
        c = e.get('crop', '')
        ln = c.rsplit('_s', 1)[0]
        if ln not in LINES: continue
        sf = e['source_file']; parts = sf.replace('.jpg', '').split('_'); rx, ry = int(parts[-4]), int(parts[-3])
        x0, y0, x1, y1 = e['box']
        if e.get('source_url'): x0, x1, y0, y1 = x0 - rx, x1 - rx, y0 - ry, y1 - ry   # page coords -> region coords
        g = out.setdefault(ln, dict(src=sf, y0=y0, y1=y1, x0=x0, x1=x1))
        g['x0'] = min(g['x0'], x0); g['x1'] = max(g['x1'], x1)
    for ln in LINES: out[ln]['yc'] = (out[ln]['y0'] + out[ln]['y1']) // 2
    return out


if __name__ == '__main__':
    for k, v in geometry().items(): print(k, v)
