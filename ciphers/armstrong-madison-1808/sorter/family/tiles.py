"""Cut padded one-mark tiles for exemplars.tsv from the sorter boxes (sorter/signs.tsv) on the NARA frames.
Line index = position among that line's sorter tiles ordered by (run, x), as on the worker's contact sheets.
Neighbour ink is masked: pixels outside the mark's own box (plus 3 px) are set to paper white."""
import csv
from collections import defaultdict
from PIL import Image
ROOT = 'ciphers/armstrong-madison-1808/'
def tiles(pad=14, size=150):
    rows = list(csv.DictReader(open(ROOT + 'sorter/signs.tsv'), delimiter='\t'))
    by = defaultdict(list)
    for r in rows:
        by[r['run'][:-1]].append(r)
    for k in by:
        by[k].sort(key=lambda r: (r['run'], int(r['x'])))
    frames, out = {}, []
    for e in csv.DictReader(open(ROOT + 'sorter/family/exemplars.tsv'), delimiter='\t'):
        r = by[e['line']][int(e['idx']) - 1]
        if r['page'] not in frames:
            frames[r['page']] = Image.open(ROOT + f"images/{r['page']}.jpg").convert('L')
        x, y, w, h = (int(r[c]) for c in 'xywh')
        m = 3
        c = frames[r['page']].crop((x - m, y - m, x + w + m, y + h + m))
        side = max(c.width, c.height) + 2 * pad
        t = Image.new('L', (side, side), 255)
        t.paste(c, ((side - c.width) // 2, (side - c.height) // 2))
        t = t.resize((size, size), Image.LANCZOS) if side > size else t
        out.append((e['type'], r['sid'], t))
    return out
