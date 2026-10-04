#!/usr/bin/env python3
"""Build a sign-sorter page: every sign of a cipher cut out as a tile, piled by its current label, for a person to
settle the alphabet (merge piles, split piles, move single tiles, mark non-letters and bad cuts).

  python3 tools/sign_sorter.py (--signs signs.tsv --labels labels.tsv | --atlas-topk T.tsv [T.tsv ...]) --pages DIR [--marks marks.tsv]
      --title "Name Sign Sorter" --out page.html [--lede TEXT] [--data-out data.json]
      [--clusters clusters.tsv | --auto-clusters K] [--atlas labels.json]
      [--rank rank.tsv | --rank-lattice topk.tsv --rank-key key.tsv [--rank-lang it] |
       --rank-confusion confusion.tsv] [--rank-out rank.tsv] [--focus focus.tsv]

Inputs (the tools/glyph_atlas.py layout, which most targets already have):
  --signs   TSV with sid, page, x, y, w, h (base box of each sign, in the page image's pixels)
  --labels  TSV with sid, sign, family (the current reading: pile = sign, piles grouped by family)
  --pages   directory holding <page>.png or <page>.jpg for every page named in --signs, or a glyph_atlas pages.json
            ({page: {"image": path relative to the repo root or absolute, ...}}; a page with a "box" is not supported)
  --marks   optional TSV with x, y, w, h, sid: small marks attached to a sign (dots, bars, tildes). The tile is cut
            around the union of the sign and its marks, so a mark that tells two signs apart is never cut off
            (lesson of 1 Oct 2026, Debosnys: tight base boxes dropped the dot of X-DOT and the bar over X).

Each tile also gets an "oddness" score: its distance from the mean tile of its own pile (24x24 grey, normalised),
so the page can show the likeliest misfits first. The page embeds the page images for a context view (the tile on
its line with its neighbours). Output is one self-contained HTML page for the Artifact tool, to be published with
capabilities {"db": {}}; the person's choices land in the db collections piles / moves / newpiles
(see the template's script and ciphers/debosnys-1883/sorter/README.md).

Active sorter (TX-SORTER, 3 Oct 2026; TRANSCRIPTION.md pipeline step 7):
  --clusters  TSV of sid, cluster (tools/glyph_atlas.py's clusters.tsv works as is: id, kind, cluster; marks skipped),
              or a `cluster` column in --labels. A tile with a cluster id carries it into the page; when the person
              moves one tile, the page offers "apply to all N in this cluster" and saves that as one cluster decision
              (db collection `clusters`) besides the per-tile moves, so tools/sign_sorter_apply.py --atlas-labels can
              write it to the family atlas's labels.json and every sibling letter's next glyph_atlas build reads it.
  --auto-clusters K  no atlas yet: provisional shape clusters inside each pile (k-means on the 24x24 tiles, up to K
              per pile, about 3+ tiles each). Ids are "<pile>~<n>"; the page says they are provisional. They propagate
              a decision across the tiles on this page only; they are not atlas clusters and are never written to one.
  --atlas-topk  instead of --signs/--labels: one or more `glyph_atlas.py classify --topk 3` files (page, line, box,
              pos, x, y, w, h, k1..k3, s1..s3); tiles are the boxes whose k1 is a cipher sign (not '_'), piled by k1.
              --rank-lattice also takes these files (or with no file named, uses them): candidates k1..k3 ('_' dropped),
              weights s1..s3 renormalised, lattice line = <page>_<line>, and the tile id is the box id.
  --atlas     the family atlas labels.json the decisions are meant for (shown on the page and kept in the data).
  --refs      TSV with a sid column (BIR87-SORTER, 4 Oct 2026): tiles the person already sorted on an earlier page, put in
              --labels under the pile the person chose and shown with a green check as examples for sorting new tiles
              into the person's own piles. Since 4 Oct 2026 (owner: "give me a way to fix, I might make mistakes") they
              move like any tile (tap out, place, drag, Undo), so a wrong earlier pick can be corrected. Leave them out
              of the --labels file given to sign_sorter_apply.py; a move stored for a ref sid is a correction to the
              earlier sort, applied by the page's own README step (ciphers/nevers-birago-fr3251-1572/sorter/no87/).
  --rank      TSV sid, score[, alt[, why[, detail]]]: tile value scores (expected change in the key rank or decode if the tile
              flips between its top-2 labels; tools/key_decode_lattice.py output where it exists). The top 20 by
              score fill a "Most useful first" box at the top of the page.
  --rank-lattice  tile value from tools/key_decode_lattice.py (TX-DECODE): a top-k TSV (line, pos, cand, score; its
              from-passes output) plus --rank-key and --rank-lang/--rank-corpus. Rule, fixed before the Birago demo
              was scored: decode the lattice once (beam Viterbi, lam 1); for every position with 2+ candidates force
              the best candidate other than the chosen one and decode again; value = p_alt x letters changed, where
              p_alt = prior(alt) / (prior(chosen) + prior(alt)) is the readers' own chance the person picks the other
              sign and "letters changed" = plaintext letters not matched by difflib between the two decodes (the
              expected change in the decode if the tile flips between its top-2 labels). Lattice (line, pos) maps to
              the sorter sid by --rank-sid (default "{line}_{pos:02d}"). Tiles that share a cluster are one group:
              their values add, the shown tile is the group's highest.
  --rank-confusion  no lattice yet: score from a look-alike confusion table (tools/lookalike_pass.py confusion, or
              any TSV label_a, label_b, n). Per group (a cluster, or a single tile without one): the pile label's most
              frequent swap partner b; conf = n(a,b) / the table's largest n, raised to 1.0 when the readers split on
              a tile of the group (--focus row); score = conf x tiles the decision flips (the group's size). The
              group's shown tile is its focus tile if any, else its oddest tile. --rank-out keeps the computed TSV.
  Must NOT be read as: a probability that the label is wrong, or a decode score. The confusion score is a triage
  order; only a lattice score (--rank) speaks for the reading, and even that ranks, it does not grade.

Size (N4-NXS, 4 Oct 2026): the page embeds every tile and every page image, so a long letter overruns the Artifact's
16 MB (Noailles c510-516, 9,863 tiles: 92 MB at the defaults). --thumb, --tile-quality (greyscale JPEG tiles) and --page-scale /
--page-quality (smaller context images; the page scales the boxes by DATA.pageScale) bring it down; the build prints the size.

Never feed it restricted material (a holder's scans under RESTRICTED.md): the page carries the images.
"""
import argparse, base64, csv, io, json, math, os, sys
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, 'sign_sorter', 'template.html')


def tsv(path):
    return list(csv.DictReader(open(path, newline=''), delimiter='\t'))


def read_clusters(path):
    """sid -> cluster from a sid/cluster TSV or glyph_atlas clusters.tsv (id, kind, cluster; marks skipped)."""
    out = {}
    for r in tsv(path):
        if r.get('kind', 'sign') != 'sign':
            continue
        sid = r.get('sid') or r.get('id')
        if sid and r.get('cluster') not in (None, ''):
            out[sid] = r['cluster']
    return out


def build(signs_p, labels_p, pages_dir, marks_p=None, thumb=96, clusters=None, tile_q=None, page_scale=1.0, page_q=82):
    from PIL import Image, ImageOps
    signs = {r['sid']: r for r in tsv(signs_p)}
    labels = tsv(labels_p)
    marks = defaultdict(list)
    if marks_p:
        for m in tsv(marks_p):
            if m.get('sid'):
                marks[m['sid']].append(tuple(int(m[k]) for k in ('x', 'y', 'w', 'h')))
    pages, piles, fam, vecs, skipped = {}, defaultdict(list), {}, {}, []
    page_json = None
    if pages_dir.endswith('.json') and os.path.isfile(pages_dir):
        root = os.path.dirname(HERE)
        page_json = {k: (v['image'] if os.path.isabs(v['image']) else os.path.join(root, v['image']))
                     for k, v in json.load(open(pages_dir)).items() if not v.get('box')}
    for r in labels:
        s = signs.get(r['sid'])
        if not s:
            skipped.append(r['sid']); continue
        p = s['page']
        if p not in pages:
            if page_json is not None:
                path = page_json.get(p) if page_json.get(p) and os.path.exists(page_json[p]) else None
            else:
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
        buf = io.BytesIO()
        if tile_q: c.save(buf, 'JPEG', quality=tile_q, optimize=True)
        else: c.save(buf, 'PNG', optimize=True)
        item = {'sid': r['sid'], 'img': base64.b64encode(buf.getvalue()).decode(), 'p': p, 'b': [x0, y0, x1 - x0, y1 - y0]}
        cid = (clusters or {}).get(r['sid']) or r.get('cluster')
        if cid:
            item['c'] = str(cid)
        piles[r['sign']].append(item)
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
        if page_scale != 1.0:
            im = im.resize((max(1, round(im.width * page_scale)), max(1, round(im.height * page_scale))), Image.LANCZOS)
        buf = io.BytesIO(); im.save(buf, 'JPEG', quality=page_q, optimize=True)
        page_img[p] = base64.b64encode(buf.getvalue()).decode()
    return {'piles': [{'id': k, 'family': fam[k], 'items': v, 'near': near.get(k, [])} for k, v in piles.items()],
            'skipped': len(skipped), 'pages': page_img, '_vecs': vecs,
            'tileMime': 'image/jpeg' if tile_q else 'image/png', 'pageScale': page_scale}


def auto_clusters(data, k, seed=7):
    """Provisional shape clusters inside each pile: k-means (numpy, fixed seed) on the 24x24 tile vectors, about 3+
    tiles per cluster, at most k per pile. Sets item['c'] = '<pile>~<n>' only where a cluster has 2+ tiles."""
    import numpy as np
    vecs = data['_vecs']
    for p in data['piles']:
        items = p['items']; n = len(items)
        kk = max(1, min(k, n // 3))
        X = np.array([vecs[it['sid']] for it in items], dtype=float)
        if kk == 1:
            lab = np.zeros(n, dtype=int)
        else:
            rng = np.random.default_rng(seed)
            C = X[rng.choice(n, kk, replace=False)]
            for _ in range(30):
                lab = np.argmin(((X[:, None, :] - C[None]) ** 2).sum(-1), axis=1)
                C2 = np.array([X[lab == j].mean(0) if (lab == j).any() else C[j] for j in range(kk)])
                if np.allclose(C2, C): break
                C = C2
        sizes = np.bincount(lab, minlength=kk)
        for it, l in zip(items, lab):
            if sizes[l] >= 2:
                it['c'] = f"{p['id']}~{int(l) + 1}"
    data['clusterSource'] = 'provisional'


def read_rank(path, cap=20):
    rows = []
    for r in (l.rstrip('\n').split('\t') for l in open(path)):
        if len(r) < 2 or r[0] == 'sid':
            continue
        try:
            sc = float(r[1])
        except ValueError:
            continue
        rows.append({'sid': r[0], 'score': sc, 'alt': r[2] if len(r) > 2 else '', 'why': r[3] if len(r) > 3 else '',
                     'detail': r[4] if len(r) > 4 else ''})
    rows.sort(key=lambda x: -x['score'])
    return rows[:cap]


def value_from_lattice(lat, key, lm, lam=1.0, beam=64):
    """Per position: (chosen, alt, p_alt, letters_changed, value). See --rank-lattice in the module docstring."""
    import difflib
    import key_decode_lattice as kdl
    best, _ = kdl.viterbi(lat, key, lm, lam, beam)
    base = kdl.text_of(best, key)
    out = []
    for i, (pk, cands) in enumerate(lat):
        others = sorted(((p, c) for c, p in cands.items() if c != best[i]), reverse=True)
        if not others:
            continue
        p_alt, alt = others[0]
        forced = lat[:i] + [(pk, {alt: p_alt})] + lat[i + 1:]
        seq, _ = kdl.viterbi(forced, key, lm, lam, beam)
        txt = kdl.text_of(seq, key)
        sm = difflib.SequenceMatcher(None, base, txt, autojunk=False)
        changed = max(len(base), len(txt)) - sum(b.size for b in sm.get_matching_blocks())
        pa = p_alt / (p_alt + cands[best[i]])
        out.append((pk, best[i], alt, round(pa, 3), changed, round(pa * changed, 3)))
    return out


def atlas_topk_rows(paths):
    rows = []
    for p in paths:
        rows += [r for r in tsv(p) if r.get('k1') and r['k1'] != '_']
    return rows


def atlas_topk_inputs(paths, out_dir):
    """--atlas-topk: write signs.tsv / labels.tsv for build() from glyph_atlas classify --topk files."""
    rows = atlas_topk_rows(paths)
    sp, lp = os.path.join(out_dir, 'signs.tsv'), os.path.join(out_dir, 'labels.tsv')
    with open(sp, 'w') as f:
        f.write('sid\tpage\tx\ty\tw\th\n' + ''.join(f"{r['box']}\t{r['page']}\t{r['x']}\t{r['y']}\t{r['w']}\t{r['h']}\n" for r in rows))
    with open(lp, 'w') as f:
        f.write('sid\tsign\tfamily\n' + ''.join(f"{r['box']}\t{r['k1']}\t{r['k1']}\n" for r in rows))
    return sp, lp


def lattice_from_atlas_topk(paths):
    """[((line, box), {cand: weight})] in reading order; the position key's second item is the tile id itself."""
    lat = []
    for r in atlas_topk_rows(paths):
        c = {}
        for k in '123':
            lab = r.get('k' + k)
            if lab and lab != '_':
                c[lab] = c.get(lab, 0) + float(r.get('s' + k) or 0)
        t = sum(c.values())
        if t <= 0:
            c, t = {r['k1']: 1.0}, 1.0
        c = {k: v / t for k, v in c.items() if v / t >= 0.02}
        lat.append(((f"{r['page']}_{int(r['line']):02d}", r['box']), c))
    return lat


def rank_from_lattice(data, topk, key_p, lang='it', corpus=None, sid_fmt='{line}_{pos:02d}', cap=20, beam=64):
    import key_decode_lattice as kdl
    from judge_plaintext import LANG_CORPORA, NgramModel, read_corpus
    paths = corpus or LANG_CORPORA.get(lang)
    if not paths:
        sys.exit(f'no corpus for --rank-lang {lang!r}')
    lm = kdl.LM(NgramModel([read_corpus(p) for p in paths]))
    key = kdl.read_key(key_p)
    topk = [topk] if isinstance(topk, str) else list(topk)
    if 'k1' in (tsv(topk[0])[:1] or [{}])[0]:
        lat, sid_fmt = lattice_from_atlas_topk(topk), '{pos}'
    else:
        lat = [x for t in topk for x in kdl.read_topk(t)]
    item = {it['sid']: (p['id'], it) for p in data['piles'] for it in p['items']}
    by_line = defaultdict(list)          # decode each line on its own (a lattice file may hold several leaves)
    for k, c in lat:
        by_line[k[0]].append((k, c))
    groups = defaultdict(list); unmapped = 0
    for ln, sub in by_line.items():
        for (line, pos), chosen, alt, pa, changed, val in value_from_lattice(sub, key, lm, beam=beam):
            sid = sid_fmt.format(line=line, pos=pos)
            if sid not in item:
                unmapped += 1; continue
            pile, it = item[sid]
            groups[(pile, it.get('c') or 'tile:' + sid)].append((val, sid, chosen, alt, pa, changed))
    out = []
    for (pile, g), vs in groups.items():
        vs.sort(reverse=True)
        val, sid, chosen, alt, pa, changed = vs[0]
        tot = round(sum(v[0] for v in vs), 3)
        if tot <= 0:
            continue
        # the question is always the tile's pile vs the other label in play: when the decode chose a sign other than
        # the readers' pile label, that choice is the alternative (the decode overrode the readers there)
        other = chosen if chosen != pile else alt
        q = f'{pile} (top-1) or {other} (decode)?' if chosen != pile else f'{pile} or {alt}?'
        out.append({'sid': sid, 'score': tot, 'alt': other, 'why': q,
                    'detail': f'~{changed} letters change; reader weight {int(round(pa * 100))}% on {alt}'
                              + (f'; group of {len(vs)} tiles' if len(vs) > 1 else '')})
    out.sort(key=lambda x: (-x['score'], x['sid']))
    return out[:cap], unmapped


def rank_from_confusion(data, conf_rows, focus_sids=(), cap=20):
    """Fallback tile value (no lattice): see the module docstring, --rank-confusion."""
    pair = defaultdict(dict)
    for r in conf_rows:
        a, b, n = r.get('label_a'), r.get('label_b'), r.get('n')
        if not a or not b:
            continue
        n = float(n or 0)
        pair[a][b] = pair[a].get(b, 0) + n; pair[b][a] = pair[b].get(a, 0) + n
    top = max((n for d in pair.values() for n in d.values()), default=0) or 1
    focus_sids = set(focus_sids)
    groups = defaultdict(list)
    for p in data['piles']:
        for it in p['items']:
            groups[(p['id'], it.get('c') or ('tile:' + it['sid']))].append(it)
    out = []
    for (pile, g), items in groups.items():
        partners = pair.get(pile, {})
        alt, n = max(partners.items(), key=lambda kv: kv[1]) if partners else ('', 0)
        conf = n / top
        foc = [it for it in items if it['sid'] in focus_sids]
        if foc:
            conf = 1.0
        if conf <= 0:
            continue
        rep = foc[0] if foc else max(items, key=lambda it: it.get('d', 0))
        why = f'{pile} or {alt}?' if alt else f'{pile}?'
        detail = ('readers split here; ' if foc else '') + f'flips {len(items)} tile' + ('s' if len(items) != 1 else '')
        out.append({'sid': rep['sid'], 'score': round(conf * len(items), 3), 'alt': alt, 'why': why, 'detail': detail})
    out.sort(key=lambda x: (-x['score'], x['sid']))
    return out[:cap]


def mark_refs(data, sids):
    """--refs: flag tiles as the person's earlier picks (item 'r': 1, no cluster id; movable, shown with a check). Returns the number flagged."""
    sids, n = set(sids), 0
    for p in data['piles']:
        for it in p['items']:
            if it['sid'] in sids:
                it['r'] = 1; it.pop('c', None); n += 1
    return n


def render(data, title, lede):
    t = open(TEMPLATE).read()
    esc = lambda s: s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    data = {k: v for k, v in data.items() if not k.startswith('_')}
    # '</' inside the JSON would close the <script> element early (a pile named "</script>", a note); escape it
    return t.replace('__TITLE__', esc(title)).replace('__LEDE__', esc(lede)).replace('__DATA__', json.dumps(data).replace('</', '<\\/'))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--signs'); ap.add_argument('--labels')
    ap.add_argument('--atlas-topk', nargs='+', help='glyph_atlas classify --topk files instead of --signs/--labels')
    ap.add_argument('--pages', required=True); ap.add_argument('--marks')
    ap.add_argument('--title', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--lede', default='Every sign of the cipher, cut out and piled by the label our readers gave it. '
                    'Settle the alphabet: which piles are one sign, which tiles sit in the wrong pile, and which '
                    'marks are not letters at all.')
    ap.add_argument('--data-out')
    ap.add_argument('--thumb', type=int, default=96, help='tile thumbnail size in px (default 96)')
    ap.add_argument('--tile-quality', type=int, help='store tiles as greyscale JPEG at this quality (default: PNG); for large letters')
    ap.add_argument('--page-scale', type=float, default=1.0, help='scale the embedded context page images (boxes are scaled in the page)')
    ap.add_argument('--page-quality', type=int, default=82, help='JPEG quality of the embedded context page images')
    ap.add_argument('--focus', help='TSV sid<TAB>question: tiles shown first in a "Check these first" box')
    ap.add_argument('--focus-note', default='')
    ap.add_argument('--refs', help='TSV with a sid column: tiles the person already sorted, shown with a check as examples (correctable)')
    g = ap.add_mutually_exclusive_group()
    g.add_argument('--clusters', help='TSV sid<TAB>cluster, or glyph_atlas clusters.tsv: cluster-level decisions')
    g.add_argument('--auto-clusters', type=int, metavar='K', help='provisional shape clusters inside each pile (no atlas yet)')
    ap.add_argument('--atlas', help='the family atlas labels.json the decisions are meant for (sign_sorter_apply.py --atlas-labels)')
    r = ap.add_mutually_exclusive_group()
    r.add_argument('--rank', help='TSV sid, score[, alt, why]: "Most useful first" box, top 20')
    r.add_argument('--rank-confusion', help='confusion TSV (label_a, label_b, n): fallback score when no lattice exists')
    r.add_argument('--rank-lattice', nargs='*', help='key_decode_lattice.py top-k TSV(s) or glyph_atlas topk files '
                   '(none named: the --atlas-topk files): score = expected decode change per tile')
    ap.add_argument('--rank-key'); ap.add_argument('--rank-lang', default='it'); ap.add_argument('--rank-corpus', nargs='*')
    ap.add_argument('--rank-sid', default='{line}_{pos:02d}', help='lattice (line, pos) -> sorter sid format')
    ap.add_argument('--rank-out', help='write the computed --rank-confusion scores as TSV')
    ap.add_argument('--rank-note', default='')
    a = ap.parse_args(argv)
    if a.atlas_topk:
        import tempfile
        a.signs, a.labels = atlas_topk_inputs(a.atlas_topk, tempfile.mkdtemp(prefix='sorter_'))
    elif not (a.signs and a.labels):
        ap.error('give --signs and --labels, or --atlas-topk')
    if a.rank_lattice is not None and not a.rank_lattice:
        if not a.atlas_topk:
            ap.error('--rank-lattice with no file needs --atlas-topk')
        a.rank_lattice = a.atlas_topk
    data = build(a.signs, a.labels, a.pages, a.marks, thumb=a.thumb, clusters=read_clusters(a.clusters) if a.clusters else None,
                 tile_q=a.tile_quality, page_scale=a.page_scale, page_q=a.page_quality)
    if a.refs:
        mark_refs(data, [r['sid'] for r in tsv(a.refs)])
    if a.auto_clusters:
        auto_clusters(data, a.auto_clusters)
    elif any('c' in it for p in data['piles'] for it in p['items']):
        data['clusterSource'] = 'atlas'
    if a.atlas:
        data['atlas'] = a.atlas
    focus_sids = []
    if a.focus:
        data['focus'] = [{'sid': r[0], 'q': r[1]} for r in (l.rstrip('\n').split('\t') for l in open(a.focus)) if len(r) >= 2]
        data['focusNote'] = a.focus_note
        focus_sids = [f['sid'] for f in data['focus']]
    if a.rank:
        data['rank'] = read_rank(a.rank)
    elif a.rank_lattice:
        if not a.rank_key:
            ap.error('--rank-lattice needs --rank-key')
        data['rank'], unm = rank_from_lattice(data, a.rank_lattice, a.rank_key, a.rank_lang, a.rank_corpus, a.rank_sid)
        if unm:
            print(f'{unm} lattice positions had no tile of that sid (check --rank-sid)', file=sys.stderr)
    elif a.rank_confusion:
        data['rank'] = rank_from_confusion(data, tsv(a.rank_confusion), focus_sids)
    if a.rank_out and 'rank' in data and not a.rank:
        with open(a.rank_out, 'w') as f:
            f.write('sid\tscore\talt\twhy\tdetail\n' + ''.join(f"{x['sid']}\t{x['score']}\t{x['alt']}\t{x['why']}\t{x.get('detail', '')}\n"
                                                             for x in data['rank']))
    if 'rank' in data:
        data['rankNote'] = a.rank_note or ('Scored by ' + ('the decode lattice: expected letters changed if the tile flips'
                                           if (a.rank or a.rank_lattice) else
                                           'look-alike confusion x tiles flipped (a triage order, not a reading)'))
    if a.data_out:
        json.dump({k: v for k, v in data.items() if not k.startswith('_')}, open(a.data_out, 'w'))
    html = render(data, a.title, a.lede)
    open(a.out, 'w').write(html)
    n = sum(len(p['items']) for p in data['piles'])
    nc = len({it['c'] for p in data['piles'] for it in p['items'] if 'c' in it})
    print(f"{len(data['piles'])} piles, {n} tiles, {data['skipped']} skipped, {nc} clusters "
          f"({data.get('clusterSource', 'none')}), {len(data.get('rank', []))} ranked, {len(html) // 1024} KB -> {a.out}")
    if len(html) > 15 * 1024 * 1024:
        print('WARNING: over 15 MB; the Artifact limit is 16 MB', file=sys.stderr)


if __name__ == '__main__':
    main()
