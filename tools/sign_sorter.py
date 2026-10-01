#!/usr/bin/env python3
"""Build a sign-sorter page: every sign of a cipher cut out as a tile, piled by its current label, for a person to
settle the alphabet (merge piles, split piles, move single tiles, mark non-letters and bad cuts).

  python3 tools/sign_sorter.py --signs signs.tsv --labels labels.tsv --pages DIR [--marks marks.tsv]
      --title "Name Sign Sorter" --out page.html [--lede TEXT] [--data-out data.json]

Inputs (the tools/glyph_atlas.py layout, which most targets already have):
  --signs   TSV with sid, page, x, y, w, h (base box of each sign, in the page image's pixels)
  --labels  TSV with sid, sign, family (the current reading: pile = sign, piles grouped by family)
  --pages   directory holding <page>.png or <page>.jpg for every page named in --signs
  --marks   optional TSV with x, y, w, h, sid: small marks attached to a sign (dots, bars, tildes). The tile is cut
            around the union of the sign and its marks, so a mark that tells two signs apart is never cut off
            (lesson of 1 Oct 2026, Debosnys: tight base boxes dropped the dot of X-DOT and the bar over X).

Each tile also gets an "oddness" score: its distance from the mean tile of its own pile (24x24 grey, normalised),
so the page can show the likeliest misfits first. The page embeds the page images for a context view (the tile on
its line with its neighbours). Output is one self-contained HTML page for the Artifact tool, to be published with
capabilities {"db": {}}; the person's choices land in the db collections piles / moves / newpiles
(see the template's script and ciphers/debosnys-1883/sorter/README.md).

Never feed it restricted material (a holder's scans under RESTRICTED.md): the page carries the images.
"""
import argparse, base64, csv, io, json, math, os, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, 'sign_sorter', 'template.html')


def tsv(path):
    return list(csv.DictReader(open(path, newline=''), delimiter='\t'))


def build(signs_p, labels_p, pages_dir, marks_p=None, thumb=96):
    from PIL import Image, ImageOps
    signs = {r['sid']: r for r in tsv(signs_p)}
    labels = tsv(labels_p)
    marks = defaultdict(list)
    if marks_p:
        for m in tsv(marks_p):
            if m.get('sid'):
                marks[m['sid']].append(tuple(int(m[k]) for k in ('x', 'y', 'w', 'h')))
    pages, piles, fam, vecs, skipped = {}, defaultdict(list), {}, {}, []
    for r in labels:
        s = signs.get(r['sid'])
        if not s:
            skipped.append(r['sid']); continue
        p = s['page']
        if p not in pages:
            path = next((os.path.join(pages_dir, p + e) for e in ('.png', '.jpg', '.jpeg')
                         if os.path.exists(os.path.join(pages_dir, p + e))), None)
            if not path:
                pages[p] = None
            else:
                pages[p] = ImageOps.autocontrast(Image.open(path).convert('L'), cutoff=1)
        if pages[p] is None:
            skipped.append(r['sid']); continue
        x, y, w, h = (int(s[k]) for k in ('x', 'y', 'w', 'h'))
        x0, y0, x1, y1 = x, y, x + w, y + h
        for (mx, my, mw, mh) in marks[r['sid']]:
            x0, y0, x1, y1 = min(x0, mx), min(y0, my), max(x1, mx + mw), max(y1, my + mh)
        # generous margin above (marks the segmenter missed), less below and at the sides
        top, bot, side = max(10, int(.9 * h)), max(6, int(.35 * h)), 5
        im = pages[p]
        if x0 >= im.width or y0 >= im.height or x1 <= 0 or y1 <= 0:   # box outside the page image: cannot cut
            skipped.append(r['sid']); continue
        c = im.crop((max(0, x0 - side), max(0, y0 - top), min(im.width, x1 + side), min(im.height, y1 + bot)))
        v = list(im.crop((x0, y0, x1, y1)).resize((24, 24)).tobytes())
        mu = sum(v) / len(v); sd = math.sqrt(sum((a - mu) ** 2 for a in v) / len(v)) or 1
        vecs[r['sid']] = [(a - mu) / sd for a in v]
        c.thumbnail((thumb, thumb), Image.LANCZOS)
        buf = io.BytesIO(); c.save(buf, 'PNG', optimize=True)
        piles[r['sign']].append({'sid': r['sid'], 'img': base64.b64encode(buf.getvalue()).decode(),
                                 'p': p, 'b': [x0, y0, x1 - x0, y1 - y0]})
        fam[r['sign']] = r.get('family') or r['sign']
    means = {}
    for k, items in piles.items():   # oddness = distance from the pile's mean tile
        n = len(items); mean = [sum(vecs[it['sid']][i] for it in items) / n for i in range(576)]
        means[k] = mean
        for it in items:
            it['d'] = round(math.sqrt(sum((a - b) ** 2 for a, b in zip(vecs[it['sid']], mean)) / 576), 3) if n > 1 else 0
    # look-alike piles: the three piles whose mean tile is nearest, as merge candidates for the person to check
    # cosine similarity of mean tiles; only piles of 3+ tiles are offered (a 1-2 tile mean is mostly noise)
    def cos(u, v):
        nu = math.sqrt(sum(a * a for a in u)) or 1; nv = math.sqrt(sum(b * b for b in v)) or 1
        return sum(a * b for a, b in zip(u, v)) / nu / nv
    big = [j for j in piles if len(piles[j]) >= 3]
    near = {}
    for k in piles:
        sims = sorted(((cos(means[k], means[j]), j) for j in big if j != k), reverse=True)
        near[k] = [j for sim, j in sims[:3] if sim > 0.5]
    page_img = {}
    for p, im in pages.items():
        if im is None: continue
        buf = io.BytesIO(); im.save(buf, 'JPEG', quality=82, optimize=True)
        page_img[p] = base64.b64encode(buf.getvalue()).decode()
    return {'piles': [{'id': k, 'family': fam[k], 'items': v, 'near': near.get(k, [])} for k, v in piles.items()],
            'skipped': len(skipped), 'pages': page_img}


def render(data, title, lede):
    t = open(TEMPLATE).read()
    esc = lambda s: s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return t.replace('__TITLE__', esc(title)).replace('__LEDE__', esc(lede)).replace('__DATA__', json.dumps(data))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--signs', required=True); ap.add_argument('--labels', required=True)
    ap.add_argument('--pages', required=True); ap.add_argument('--marks')
    ap.add_argument('--title', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--lede', default='Every sign of the cipher, cut out and piled by the label our readers gave it. '
                    'Settle the alphabet: which piles are one sign, which tiles sit in the wrong pile, and which '
                    'marks are not letters at all.')
    ap.add_argument('--data-out')
    a = ap.parse_args(argv)
    data = build(a.signs, a.labels, a.pages, a.marks)
    if a.data_out:
        json.dump(data, open(a.data_out, 'w'))
    html = render(data, a.title, a.lede)
    open(a.out, 'w').write(html)
    n = sum(len(p['items']) for p in data['piles'])
    print(f"{len(data['piles'])} piles, {n} tiles, {data['skipped']} skipped, {len(html) // 1024} KB -> {a.out}")
    if len(html) > 15 * 1024 * 1024:
        print('WARNING: over 15 MB; the Artifact limit is 16 MB', file=sys.stderr)


if __name__ == '__main__':
    main()
