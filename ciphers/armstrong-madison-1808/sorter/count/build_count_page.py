#!/usr/bin/env python3
"""Armstrong 1808 mark counter (owner, 4 Oct 2026: the mark sorter is hard, "many signs look very similar"; a
counting-only page instead). One card per passage (sorter/passages.tsv), its mark run(s) shown in place on the
manuscript line with a box around the run; the owner answers only "how many marks?". The two transcriptions'
counts are NOT shown (blind third reader); disputed passages come first.

    python3 ciphers/armstrong-madison-1808/sorter/count/build_count_page.py OUT.html

Answers save to the page's db collection "counts" (doc id = passage): {passage, count, unsure, note, updated}.
Export with ArtifactData list (collection counts) and compare with ms_marks / glyph_tokens in passages.tsv."""
import base64, csv, io, json, re, sys
from pathlib import Path
from PIL import Image, ImageDraw
H = Path(__file__).resolve().parent; T = H.parents[1]
runs = {r['run']: r for r in csv.DictReader(open(H.parent / 'runs.tsv'), delimiter='\t')}
pas = list(csv.DictReader(open(H.parent / 'passages.tsv'), delimiter='\t'))
frames = {}
def frame(f):
    if f not in frames: frames[f] = Image.open(T / 'images' / f'M34-014-{f}.jpg').convert('RGB')
    return frames[f]
def strip(run):
    r = runs[run]; im = frame(r['frame']); x0, y0, x1, y1 = (int(r[k]) for k in ('x0', 'y0', 'x1', 'y1'))
    cx0, cy0 = max(0, x0 - 140), max(0, y0 - 40); cx1, cy1 = min(im.width, x1 + 140), min(im.height, y1 + 40)
    c = im.crop((cx0, cy0, cx1, cy1)).copy(); d = ImageDraw.Draw(c)
    d.rectangle((x0 - cx0 - 4, y0 - cy0 - 4, x1 - cx0 + 4, y1 - cy0 + 4), outline=(214, 64, 32), width=4)
    if c.width > 1400: c = c.resize((1400, int(c.height * 1400 / c.width)))
    b = io.BytesIO(); c.save(b, 'JPEG', quality=72); return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
cards = []
for p in pas:
    ms, gl = int(p['ms_marks']), int(p['glyph_tokens'])
    where = re.sub(r'\s*\(.*\)\s*$', '', p['where']).strip()
    cards.append({'id': p['passage'], 'page': p['passage'][1], 'where': where, 'gap': abs(ms - gl),
                  'imgs': [strip(r) for r in p['runs'].split(',')]})
cards.sort(key=lambda c: (-c['gap'], c['id']))
for c in cards: c['disputed'] = c.pop('gap') > 0
html = (H / 'count_template.html').read_text().replace('/*DATA*/[]', json.dumps(cards))
Path(sys.argv[1]).write_text(html); print(len(cards), 'passages,', sum(c['disputed'] for c in cards), 'disputed,', len(html) // 1024, 'KB')
