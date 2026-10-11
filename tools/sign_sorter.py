#!/usr/bin/env python3
"""Build a sign-sorter page: every sign of a cipher cut out as a tile, piled by its current label, for a person to
settle the alphabet (merge piles, split piles, move single tiles, mark non-letters and bad cuts).

  python3 tools/sign_sorter.py (--signs signs.tsv --labels labels.tsv | --atlas-topk T.tsv [T.tsv ...]) --pages DIR [--marks marks.tsv]
      --title "Name Sign Sorter" --out page.html [--lede TEXT] [--data-out data.json]
      [--clusters clusters.tsv | --auto-clusters K] [--atlas labels.json]
      [--rank rank.tsv | --rank-lattice topk.tsv --rank-key key.tsv [--rank-lang it] |
       --rank-confusion confusion.tsv] [--rank-out rank.tsv] [--focus focus.tsv] [--no-focus-to-tray] [--key box]

Questions in the tray (template 2026-10-09.1; owner, 9 Oct 2026, Harley 287): by default the --focus tiles ("Check these
first") and the rank tiles ("Most useful first") open in the "Taken out" tray and the page lands on step 2, one tile at a
time over the pile cards, its own pile the first card ("it was right" = one tap, saved as a keep). Nothing is written to the
db until the person acts, and a tile with a saved move or keep is never put back in the tray. Review fixes the same day: no
tile waits, and step 2 takes no answer, until the saved answers are in ("Loading your earlier answers..."); a keep is written
only by the explicit "it was right" / "Right pile: keep it" controls and clears any move of the tile; waiting tiles stay in
view, dimmed, in their own pile in step 1; a tap anywhere on a step-2 pile card places the sign ("View pile" opens the pile).
--no-focus-to-tray builds the old layout (the tiles stay in their piles with a "?"). tools/sorter_rerender.py takes the same
flag and, without it, keeps the old page's own setting.

--key box (template 2026-10-09.6; owner, 10 Oct 2026, on a box-check page: "add a simple key at the top explaining what to do in
different situations with examples"): a "What to do: a key" block under the lede, one drawn example per case (one sign fits, two
signs in one box, one sign cut in two, a box that cuts the sign, a stain or shadow, a sign with no box, a dot or tick, not sure) and
a line on step 2's "Fix the cut". Neutral drawn shapes, the machine's box a solid outline and the fixed box a dashed one (no
colour-only cue); folded or open as the person last left it. A page option like --focus-to-tray; tools/sorter_rerender.py
--key box adds it to a page built without it, --key none takes it off, and with neither it keeps the old page's own setting.

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
  --region    region.json (tools/sorter_recut.py, SORTER-PAGEVIEW 4 Oct 2026): the larger view opens on the ORIGINAL page
              region around the tile, its (sheared) box drawn there, "Whole page" by default with a "Line strips" toggle.
              The image goes beside --out as <stem>_region.jpg: publish it with the page (Artifact files), or --region-embed.
  --refs      TSV with a sid column (BIR87-SORTER, 4 Oct 2026): tiles the person already sorted on an earlier page, put in
              --labels under the pile the person chose and shown with a check as examples for sorting new tiles
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

Preflight (SORTER-PREFLIGHT, 6 Oct 2026): after the build, tools/sorter_preflight.py runs on the page and prints its
verdict (template, answerable focus box, tiles on the cipher lines, contact sheet <out stem>.preflight.png); a FAIL
is not published. Give --cipher-lines, or keep cipher_lines.tsv / segment_pages.txt beside --signs; --no-preflight skips it.

Blind first (MQS-SORTER, 9 Oct 2026; TRANSCRIPTION.md: the person sorting is never shown key values or machine guesses):
  The default page shows no key value, no decode choice, no top-1 label, no reader weight and no score. The rank order stays
  (an order, not a displayed value). A ranked or focus tile is captioned "Which pile?" with its candidate piles in a seeded
  random order (--blind-seed), never marked "(decode)" or "(top-1)" and never with a percentage; a --focus-note that calls a
  placement "the computer's pick" is replaced by a neutral note. A seed placement by nearest pile (shape only, no key or
  decode input) is allowed and the page says so. Must NOT be blocked: pile ids (shape cluster names) and the rank order.
  --show-values KEY --key-family NAME --blind-sort DB_EXPORT   declared non-blind mode (key.tsv: sign, value[, status]). Refused
              (exit 2, naming TRANSCRIPTION.md) unless --blind-sort is a saved blind export (a --db folder with piles/ moves/
              whose rows are not mode=keyed) and tools/data/sorter_families.tsv lists no open blind sort in that key family.
              The page says "Non-blind view: values shown; decisions here are not transcription evidence", writes values in
              CAPITALS when the key confirms (status confirmed/owner or no status column), lower case for status guess/
              machine/topk, a "_" prefix for nulls, "?" for unknown (decode_key.py --style case), offers "Group by value"
              (I/J and U/V merged) and "Sort piles by value". Building one stamps the family's nonblind_shown date in the
              register (pass --no-register to only test). Exports from then on carry mode=keyed (sign_sorter_apply.py).
  --oddness-audit  known-answer measure of the "Odd ones first" order (see below); prints per seed recall@10% and shuffled p95.

Never feed it restricted material (a holder's scans under RESTRICTED.md): the page carries the images.
"""
import argparse, base64, csv, datetime, io, json, math, os, random, re, sys
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, 'sign_sorter', 'template.html')
FAMILIES = os.path.join(HERE, 'data', 'sorter_families.tsv')
BLIND_SEED = 20261009
NONBLIND_BANNER = 'Non-blind view: values shown; decisions here are not transcription evidence'
NEUTRAL_NOTE = 'Each of these tiles is about as close to two of the piles; which pile is right is for you to say.'
SEED_NOTE = 'first piled by our readers’ labels; this page shows no key values and no decode choices, so what you decide is blind.'
SEED_SHAPE_NOTE = ('first piled by nearest pile on the image alone (shape only: no key, no decode, no reader guess); '
                   'this page shows no key values, so what you decide is blind.')
# machine guesses a blind page must not carry (a decode choice, a top-1 label, a reader weight, a letters-changed count)
_MACHINE = re.compile(r"\s*\((?:decode|top-1)\)|\s*reader weight \d+%(?: on \S+)?;?|\s*~\d+ letters change;?", re.I)
_MACHINE_NOTE = re.compile(r"computer|decode|top-1|reader weight|\bguess|\bpick\b", re.I)


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


def pile_oddness(vecs, sids):
    """(mean tile, {sid: oddness}) for one pile: oddness = root-mean-square distance of the tile's normalised 24x24 grey vector from
    the pile's mean tile, rounded to 3 places; 0 for a pile of one. The one function the page's "Odd ones first" order and
    --oddness-audit both use (MQS-SORTER, 9 Oct 2026)."""
    n = len(sids); mean = [sum(vecs[x][i] for x in sids) / n for i in range(576)]
    return mean, {x: (round(math.sqrt(sum((a - b) ** 2 for a, b in zip(vecs[x], mean)) / 576), 3) if n > 1 else 0) for x in sids}


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
        means[k], dd = pile_oddness(vecs, [it['sid'] for it in items])
        for it in items:
            it['d'] = dd[it['sid']]
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


def rank_from_lattice(data, topk, key_p, lang='it', corpus=None, sid_fmt='{line}_{pos:02d}', cap=20, beam=64, blind=False, seed=BLIND_SEED):
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
        if blind:   # an order only: candidates in a seeded random order, no decode choice, no weight, no letters-changed count
            out.append({'sid': sid, 'score': tot, 'alt': '', 'why': blind_why(sid, [pile, other], seed),
                        'detail': f'group of {len(vs)} tiles' if len(vs) > 1 else ''})
            continue
        out.append({'sid': sid, 'score': tot, 'alt': other, 'why': q,
                    'detail': f'~{changed} letters change; reader weight {int(round(pa * 100))}% on {alt}'
                              + (f'; group of {len(vs)} tiles' if len(vs) > 1 else '')})
    out.sort(key=lambda x: (-x['score'], x['sid']))
    return (rank_only(out[:cap]) if blind else out[:cap]), unmapped


def rank_from_confusion(data, conf_rows, focus_sids=(), cap=20, blind=False, seed=BLIND_SEED):
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
        if blind:
            why, alt, detail = blind_why(rep['sid'], [pile, alt], seed), '', f'flips {len(items)} tile' + ('s' if len(items) != 1 else '')
        out.append({'sid': rep['sid'], 'score': round(conf * len(items), 3), 'alt': alt, 'why': why, 'detail': detail})
    out.sort(key=lambda x: (-x['score'], x['sid']))
    return rank_only(out[:cap]) if blind else out[:cap]


def blind_why(sid, cands, seed=BLIND_SEED):
    """Blind caption: "Which pile? A / B", the candidate piles in a random order seeded by (seed, sid); never marks which one a
    decode or a top-1 reader chose. Pile ids only (shape cluster names, not key values)."""
    c = sorted({x for x in cands if x})
    random.Random(f'{seed}:{sid}').shuffle(c)
    return 'Which pile? ' + ' / '.join(c) if c else 'Which pile?'


def rank_only(rows):
    """A blind ranked list keeps its order but not its numbers: score = N..1 by position (the page shows no score)."""
    return [dict(r, score=len(rows) - i) for i, r in enumerate(rows)]


def blind_text(t):
    """Strip decode / top-1 / reader-weight / letters-changed phrases from a person-facing string (a --rank TSV, a focus.tsv question)."""
    return re.sub(r'\s{2,}', ' ', _MACHINE.sub('', t or '')).strip(' ;')


def blind_note(t):
    """A --focus-note that speaks of "the computer's pick" or a guess is replaced by a neutral note."""
    return NEUTRAL_NOTE if (t and _MACHINE_NOTE.search(t)) else t


def read_families(path=None):
    path = path or FAMILIES
    return tsv(path) if os.path.exists(path) else []


def nonblind_refusal(family, blind_sort, page_sids, fam_path=None):
    """None if a declared non-blind page may be built, else the refusal message (TRANSCRIPTION.md, blind first).
    Needs (1) --blind-sort naming a saved blind export (a --db folder with piles/moves/checked docs, none mode=keyed) that
    touches this page's tiles or piles, and (2) no open blind sort listed for the key family in sorter_families.tsv."""
    if not family:
        return '--show-values needs --key-family NAME (TRANSCRIPTION.md: the person sorting is never shown key values while a blind sort is open)'
    if not blind_sort or not os.path.isdir(blind_sort):
        return '--show-values needs --blind-sort DB_EXPORT, a saved blind export for the same tiles (TRANSCRIPTION.md, blind first)'
    import sign_sorter_apply as ap_
    docs = {c: ap_.load(blind_sort, c) for c in ('piles', 'moves', 'checked')}
    if not any(docs.values()):
        return f'--blind-sort {blind_sort} holds no saved piles/moves/checked documents (TRANSCRIPTION.md, blind first)'
    if any(d.get('mode') == 'keyed' for ds in docs.values() for d in ds):
        return f'--blind-sort {blind_sort} is itself a keyed (non-blind) export; it is not a blind sort (TRANSCRIPTION.md)'
    seen = {d.get('sid') for c in ('moves', 'checked') for d in docs[c]} | {d.get('pile') for d in docs['piles']}
    if not (seen & set(page_sids)):
        return f'--blind-sort {blind_sort} names none of this page\'s tiles or piles: not a blind sort of the same tiles (TRANSCRIPTION.md)'
    for r in read_families(fam_path):
        if r.get('family') == family and (r.get('open_blind_sorts') or '').strip():
            return (f'key family {family!r} has open blind sorts ({r["open_blind_sorts"]}) in tools/data/sorter_families.tsv: '
                    'no non-blind page until they are saved (TRANSCRIPTION.md, blind first)')
    return None


def stamp_nonblind(family, fam_path=None, today=None):
    """Set the family's nonblind_shown date (first time only); add the row when the family is not listed. Returns the date held."""
    path = fam_path or FAMILIES
    rows = read_families(path)
    cols = ['family', 'open_blind_sorts', 'nonblind_shown', 'note']
    today = today or datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
    row = next((r for r in rows if r.get('family') == family), None)
    if row is None:
        row = {'family': family, 'open_blind_sorts': '', 'nonblind_shown': '', 'note': ''}; rows.append(row)
    if not row.get('nonblind_shown'):
        row['nonblind_shown'] = today
    with open(path, 'w', newline='') as f:
        w = csv.DictWriter(f, cols, delimiter='\t', extrasaction='ignore'); w.writeheader(); w.writerows(rows)
    return row['nonblind_shown']


def value_group(v):
    """Group-by-value key: upper case, I/J and U/V merged (the period alphabet), '_' nulls and '?' unknowns kept apart."""
    return v.upper().replace('J', 'I').replace('V', 'U') if v[:1] not in ('_', '?') else v[:1]


def show_values(data, key_p):
    """Non-blind only. DATA.values = {pile: {v, g}}: CAPITALS when the key confirms (status confirmed/owner or no status column),
    lower case for status guess/machine/topk, '_' for a null (value NULL or empty), '?' for a pile with no key row."""
    key = {}
    for r in tsv(key_p):
        sign, val = (r.get('sign') or '').strip(), (r.get('value') or '').strip()
        if sign:
            key[sign] = (val, (r.get('status') or r.get('grade') or '').strip().lower())
    vals = {}
    for p in data['piles']:
        row = key.get(p['id']) or key.get(p['family'])
        if row is None:
            v = '?'
        elif row[0].upper() == 'NULL' or not row[0]:
            v = '_'
        else:
            v = row[0].lower() if row[1] in ('guess', 'machine', 'topk', 'top-k') else row[0].upper()
        vals[p['id']] = {'v': v, 'g': value_group(v)}
    data['values'] = vals
    return vals


def mark_categories(data, marks_p):
    """DATA.markCat = {pile: category}: the commonest `kind` (or `mark`/`type`/`category`) of the --marks rows attached to the pile's
    tiles (among marked tiles only), 'plain' when none. A marks TSV with no such column gives 'marked' / 'plain'."""
    rows = tsv(marks_p)
    kind = lambda r: next((r[k] for k in ('kind', 'mark', 'type', 'category') if r.get(k)), 'marked')
    by = defaultdict(list)
    for r in rows:
        if r.get('sid'):
            by[r['sid']].append(kind(r))
    cat = {}
    for p in data['piles']:
        cnt = defaultdict(int)
        for it in p['items']:
            for k in by.get(it['sid'], ()):
                cnt[k] += 1
        cat[p['id']] = max(sorted(cnt), key=lambda k: cnt[k]) if cnt else 'plain'
    data['markCat'] = cat


def variant_oddness(vecs, sids, variant):
    """Audit-only rival orders (PREREG-MQS-SORTER A1): 'medoid' = distance to the pile member with the smallest summed distance to its
    pile mates; 'knn3' = mean distance to the 3 nearest pile mates. Not used by the page."""
    import numpy as np
    X = np.array([vecs[x] for x in sids], dtype=float); n = len(sids)
    if n < 2:
        return {x: 0 for x in sids}
    D = np.sqrt(((X[:, None, :] - X[None]) ** 2).mean(-1))
    if variant == 'medoid':
        m = int(D.sum(1).argmin()); return {x: float(D[i, m]) for i, x in enumerate(sids)}
    k = min(3, n - 1)
    return {x: float(np.sort(D[i])[1:k + 1].mean()) for i, x in enumerate(sids)}


def oddness_audit(signs_p, labels_p, pages_dir, frac=0.05, kind='random', confusion_p=None, seeds=20, shuffles=200, top=0.10, min_pile=3, variant='mean'):
    """--oddness-audit (MQS-SORTER, 9 Oct 2026; pre-registered in tools/tests/PREREG-MQS-SORTER.md). Known-answer measure of the
    "Odd ones first" order on piles whose labels are right (--labels is the truth): per seed, plant round(frac x tiles) tiles into a
    wrong pile (kind 'random': a uniformly random other pile; 'lookalike': the pile of the tile's top confusion partner in
    --confusion label_a, label_b, n, only tiles whose pile has a surviving partner pile), recompute every pile's oddness with the
    page's own function, and report recall@10% = the share of planted tiles in the first ceil(10% x pile size) of their new pile, beside
    the shuffled-order p95 (same piles, each pile's order shuffled, `shuffles` times: the null changes which tiles are in the first 10%,
    which is exactly the statistic). Piles under `min_pile` tiles are dropped first. Returns per-seed rows and a summary.
    Meant to catch: a page order that does not put planted misfits first. Must NOT be read as: a probability that a tile in the
    first 10% is wrong, or as the order's power on real errors that are not plantable (a look-alike error is a different tile, not
    a moved one). Python numbers only; no network."""
    import numpy as np
    data = build(signs_p, labels_p, pages_dir, thumb=24)
    vecs = data['_vecs']; pile_of = {it['sid']: p['id'] for p in data['piles'] for it in p['items']}
    cnt = defaultdict(int)
    for v in pile_of.values():
        cnt[v] += 1
    keep = {k for k, n in cnt.items() if n >= min_pile}
    pile_of = {sid: v for sid, v in pile_of.items() if v in keep}
    sids = sorted(pile_of); piles = sorted(keep)
    partner = {}
    if kind == 'lookalike':
        pair = defaultdict(lambda: defaultdict(float))
        for r in tsv(confusion_p):
            a, b, n = r.get('label_a'), r.get('label_b'), float(r.get('n') or 0)
            if a and b:
                pair[a][b] += n; pair[b][a] += n
        for k in piles:
            c = [(n, b) for b, n in pair.get(k, {}).items() if b in keep and b != k]
            if c:
                partner[k] = max(c)[1]
    pool = [x for x in sids if kind == 'random' or pile_of[x] in partner]
    k_plant = max(1, round(frac * len(sids)))
    rows = []
    for seed in range(1, seeds + 1):
        rng = random.Random(seed)
        planted = rng.sample(pool, min(k_plant, len(pool)))
        now = dict(pile_of)
        for x in planted:
            now[x] = partner[pile_of[x]] if kind == 'lookalike' else rng.choice([q for q in piles if q != pile_of[x]])
        members = defaultdict(list)
        for x in sids:
            members[now[x]].append(x)
        pl = set(planted); hits = 0; slots = []
        for q, xs in members.items():
            d = pile_oddness(vecs, xs)[1] if variant == 'mean' else variant_oddness(vecs, xs, variant)
            m = max(1, math.ceil(top * len(xs)))
            order = sorted(xs, key=lambda x: (-d[x], x))
            hits += sum(1 for x in order[:m] if x in pl)
            slots.append((len(xs), m, sum(1 for x in xs if x in pl)))
        nrng = np.random.default_rng(seed)
        null = []
        for _ in range(shuffles):   # same piles, each pile's order shuffled
            h = 0
            for n_, m_, p_ in slots:
                if p_:
                    h += int(nrng.permutation(n_)[:m_].__lt__(p_).sum())   # planted = the first p_ positions of a random permutation
            null.append(h / len(planted))
        rows.append({'seed': seed, 'planted': len(planted), 'recall': round(hits / len(planted), 3),
                     'shuffled_p95': round(float(np.percentile(null, 95)), 3), 'shuffled_mean': round(float(np.mean(null)), 3)})
    return rows, {'kind': kind, 'variant': variant, 'tiles': len(sids), 'piles': len(piles), 'planted_per_seed': k_plant,
                  'eligible': len(pool), 'mean_recall': round(float(np.mean([r['recall'] for r in rows])), 3),
                  'seeds_above_p95': sum(1 for r in rows if r['recall'] > r['shuffled_p95']),
                  'seeds_recall_ge_0.6_and_above_p95': sum(1 for r in rows if r['recall'] >= 0.6 and r['recall'] > r['shuffled_p95'])}


def mark_refs(data, sids):
    """--refs: flag tiles as the person's earlier picks (item 'r': 1, no cluster id; movable, shown with a check). Returns the number flagged."""
    sids, n = set(sids), 0
    for p in data['piles']:
        for it in p['items']:
            if it['sid'] in sids:
                it['r'] = 1; it.pop('c', None); n += 1
    return n


def add_region(data, region_p, out, long_side=4000, quality=60, embed=False):
    """SORTER-PAGEVIEW (4 Oct 2026; owner on Longlee f101v_L32_49: "can we just show the full graphic?"): DATA.region for the
    larger view's "Whole page" mode. region.json (tools/sorter_recut.py write_region) gives each line's centre trace on the
    region; a strip-page box [x, y, w, h] is drawn on the region as the parallelogram x..x+w, trace(x) - half + y.. (+h).
    The region image (autocontrast like the pages, downscaled to long_side) is written beside the page as
    <out stem>_region.jpg (src = its file name, published as a supporting file) or embedded (b64)."""
    from PIL import Image, ImageOps
    doc = json.load(open(region_p)); root = os.path.dirname(HERE)
    path = doc['image'] if os.path.isabs(doc['image']) else os.path.join(root, doc['image'])
    im = ImageOps.autocontrast(Image.open(path).convert('L'), cutoff=1)
    if (im.width, im.height) != (doc['W'], doc['H']):
        raise SystemExit(f"region image {im.size} is not region.json's {doc['W']}x{doc['H']}")
    sc = min(1.0, long_side / max(im.width, im.height))
    if sc < 1: im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
    used = {it['p'] for p in data['piles'] for it in p['items']}
    reg = {k: doc[k] for k in ('W', 'H', 'half', 'pitch', 'step')}
    reg.update(scale=im.width / doc['W'], lines={k: v for k, v in doc['lines'].items() if k in used})
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=quality, optimize=True)
    if embed:
        reg['b64'] = base64.b64encode(buf.getvalue()).decode()
    else:
        name = os.path.splitext(os.path.basename(out))[0] + '_region.jpg'
        open(os.path.join(os.path.dirname(os.path.abspath(out)), name), 'wb').write(buf.getvalue()); reg['src'] = name
    data['region'] = reg
    print(f"region {im.width}x{im.height} ({len(buf.getvalue()) // 1024} KB, {'embedded' if embed else reg.get('src')}), "
          f"{len(reg['lines'])} lines", file=sys.stderr)


KEYS = ('box',)   # page keys the template carries (OPTS.key): 'box' = "What to do: a key" for a box-check page (template 2026-10-09.6)


def render(data, title, lede, focus_to_tray=True, key=None):
    """The page HTML. focus_to_tray (template 2026-10-09.1, default on): the "Check these first" / "Most useful first" tiles
    open in the "Taken out" tray and the page lands on step 2 (CLI --no-focus-to-tray keeps the old in-pile layout). key
    (template 2026-10-09.6, CLI --key box): 'box' shows the box-check key ("What to do: a key", drawn examples of each case)
    under the lede; None shows none. The options are baked into the page as `const OPTS = {...};`, outside DATA, so DATA stays
    byte for byte what the build made (a page without a key carries no 'key' in OPTS)."""
    if key is not None and key not in KEYS:
        raise ValueError(f'unknown page key {key!r} (known: {", ".join(KEYS)})')
    t = open(TEMPLATE).read()
    esc = lambda s: s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    data = {k: v for k, v in data.items() if not k.startswith('_')}
    if data.get('focus'):   # a focus.tsv header row ("sid<TAB>question") or a stale sid is not a tile: drop it (preflight 'not a tile')
        sids = {it['sid'] for p in data.get('piles', []) for it in p.get('items', [])}
        data['focus'] = [f for f in data['focus'] if f.get('sid') in sids]
    # '</' inside the JSON would close the <script> element early (a pile named "</script>", a note); escape it
    opts = {'focusToTray': bool(focus_to_tray)}
    if key:
        opts['key'] = key
    opts = json.dumps(opts)
    return (t.replace('__TITLE__', esc(title)).replace('__LEDE__', esc(lede)).replace('__OPTS__', opts)
            .replace('__DATA__', json.dumps(data).replace('</', '<\\/')))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--signs'); ap.add_argument('--labels')
    ap.add_argument('--atlas-topk', nargs='+', help='glyph_atlas classify --topk files instead of --signs/--labels')
    ap.add_argument('--pages', required=True); ap.add_argument('--marks')
    ap.add_argument('--title'); ap.add_argument('--out')
    ap.add_argument('--lede', default='Every sign of the cipher, cut out and piled by the label our readers gave it. '
                    'Settle the alphabet: which piles are one sign, which tiles sit in the wrong pile, and which '
                    'marks are not letters at all.')
    ap.add_argument('--data-out')
    ap.add_argument('--thumb', type=int, default=96, help='tile thumbnail size in px (default 96)')
    ap.add_argument('--tile-quality', type=int, help='store tiles as greyscale JPEG at this quality (default: PNG); for large letters')
    ap.add_argument('--page-scale', type=float, default=1.0, help='scale the embedded context page images (boxes are scaled in the page)')
    ap.add_argument('--page-quality', type=int, default=82, help='JPEG quality of the embedded context page images')
    ap.add_argument('--region', help='region.json from tools/sorter_recut.py: the larger view shows the tile on the original page '
                    'region (continuous, its sheared box drawn on it), default on, toggle back to line strips')
    ap.add_argument('--region-long', type=int, default=4000, help='downscale the region image to this long side (px, default 4000)')
    ap.add_argument('--region-quality', type=int, default=60, help='JPEG quality of the region image (default 60)')
    ap.add_argument('--region-embed', action='store_true', help='embed the region image in the page instead of writing '
                    '<out stem>_region.jpg beside it (a supporting file to publish with the page)')
    ap.add_argument('--focus', help='TSV sid<TAB>question: tiles shown first in a "Check these first" box')
    ap.add_argument('--focus-note', default='')
    ap.add_argument('--focus-to-tray', action=argparse.BooleanOptionalAction, default=True,
                    help='the "Check these first" (and "Most useful first") tiles start in the "Taken out" tray and the page opens on '
                    'step 2, one tile at a time, its own pile the first card (default on; --no-focus-to-tray: they start in their piles)')
    ap.add_argument('--key', choices=KEYS, help='a "What to do" key under the lede: box = the box-check key (drawn examples of each case; '
                    'template 2026-10-09.6)')
    ap.add_argument('--ref-image', help='a reference sheet (e.g. a published sign table) shown in a collapsible panel above the piles')
    ap.add_argument('--ref-caption', default='Reference sheet', help='heading and credit line for --ref-image')
    ap.add_argument('--ref-width', type=int, default=1400, help='max width in px the reference image is scaled to')
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
    ap.add_argument('--cipher-lines', help='cipher-line list for the preflight (tools/sorter_preflight.py; default cipher_lines.tsv '
                    'or segment_pages.txt beside --out or --signs)')
    ap.add_argument('--seed-shape', action='store_true', help='say on the page that the first piling is by nearest pile on the image alone '
                    '(shape only; use when --labels came from image distance, with no key or decode input)')
    ap.add_argument('--blind-seed', type=int, default=BLIND_SEED, help='seed for the order of the candidate piles in a blind caption')
    ap.add_argument('--show-values', metavar='KEY', help='declared non-blind mode: key.tsv (sign, value[, status]); needs --key-family and --blind-sort')
    ap.add_argument('--key-family', help='key family of this page (tools/data/sorter_families.tsv) for --show-values')
    ap.add_argument('--blind-sort', metavar='DB_EXPORT', help='a saved blind export (a --db folder) of the same tiles, required by --show-values')
    ap.add_argument('--no-register', action='store_true', help='with --show-values: do not stamp the family register (tests)')
    ap.add_argument('--oddness-audit', action='store_true', help='known-answer recall@10%% of the "Odd ones first" order on --signs/--labels (the truth); no page is built')
    ap.add_argument('--oddness-variant', choices=('mean', 'medoid', 'knn3'), default='mean', help='--oddness-audit: order to measure (mean = the page\'s own)')
    ap.add_argument('--plant', type=float, default=0.05, help='--oddness-audit: share of tiles planted into a wrong pile (default 0.05)')
    ap.add_argument('--plants', choices=('random', 'lookalike'), default='random', help='--oddness-audit: plant kind')
    ap.add_argument('--confusion', help='--oddness-audit --plants lookalike: confusion TSV label_a, label_b, n')
    ap.add_argument('--seeds', type=int, default=20, help='--oddness-audit: number of seeds (default 20)')
    ap.add_argument('--no-preflight', action='store_true', help='skip tools/sorter_preflight.py after the build')
    a = ap.parse_args(argv)
    if not a.oddness_audit and not (a.title and a.out):
        ap.error('--title and --out are required')
    if a.oddness_audit:
        if not (a.signs and a.labels):
            ap.error('--oddness-audit needs --signs and --labels (the truth piles)')
        if a.plants == 'lookalike' and not a.confusion:
            ap.error('--plants lookalike needs --confusion')
        rows, summ = oddness_audit(a.signs, a.labels, a.pages, a.plant, a.plants, a.confusion, a.seeds, variant=a.oddness_variant)
        print('seed\tplanted\trecall@10%\tshuffled_p95\tshuffled_mean')
        for r in rows:
            print(f"{r['seed']}\t{r['planted']}\t{r['recall']}\t{r['shuffled_p95']}\t{r['shuffled_mean']}")
        print(json.dumps(summ)); return
    if a.atlas_topk:
        import tempfile
        a.signs, a.labels = atlas_topk_inputs(a.atlas_topk, tempfile.mkdtemp(prefix='sorter_'))
    elif not (a.signs and a.labels):
        ap.error('give --signs and --labels, or --atlas-topk')
    if a.rank_lattice is not None and not a.rank_lattice:
        if not a.atlas_topk:
            ap.error('--rank-lattice with no file needs --atlas-topk')
        a.rank_lattice = a.atlas_topk
    blind = not a.show_values
    if a.show_values:
        sids_ = {r['sid'] for r in tsv(a.labels)}
        why = nonblind_refusal(a.key_family, a.blind_sort, sids_)
        if why:
            print('refused: ' + why, file=sys.stderr); sys.exit(2)
    data = build(a.signs, a.labels, a.pages, a.marks, thumb=a.thumb, clusters=read_clusters(a.clusters) if a.clusters else None,
                 tile_q=a.tile_quality, page_scale=a.page_scale, page_q=a.page_quality)
    data['blind'] = blind
    if blind:
        data['mode'] = 'blind'; data['seedNote'] = SEED_SHAPE_NOTE if a.seed_shape else SEED_NOTE
    else:
        data['mode'] = 'keyed'; data['nonblind'] = True; data['banner'] = NONBLIND_BANNER; data['keyFamily'] = a.key_family
        show_values(data, a.show_values)
    if a.marks:
        mark_categories(data, a.marks)
    if a.refs:
        mark_refs(data, [r['sid'] for r in tsv(a.refs)])
    if a.auto_clusters:
        auto_clusters(data, a.auto_clusters)
    elif any('c' in it for p in data['piles'] for it in p['items']):
        data['clusterSource'] = 'atlas'
    if a.atlas:
        data['atlas'] = a.atlas
    if a.ref_image:
        from PIL import Image as _I
        import io as _io, base64 as _b64
        im = _I.open(a.ref_image).convert('RGB')
        if im.width > a.ref_width: im = im.resize((a.ref_width, round(im.height * a.ref_width / im.width)))
        buf = _io.BytesIO(); im.save(buf, 'JPEG', quality=85)
        data['refImg'] = 'data:image/jpeg;base64,' + _b64.b64encode(buf.getvalue()).decode()
        data['refCaption'] = a.ref_caption
    focus_sids = []
    if a.focus:
        data['focus'] = [{'sid': r[0], 'q': blind_text(r[1]) if blind else r[1]}
                         for r in (l.rstrip('\n').split('\t') for l in open(a.focus)) if len(r) >= 2]
        data['focusNote'] = blind_note(a.focus_note) if blind else a.focus_note
        focus_sids = [f['sid'] for f in data['focus']]
    if a.rank:
        data['rank'] = read_rank(a.rank)
        if blind:   # an order only: strip machine phrases, keep the candidate piles as a seeded-random "Which pile?"
            for r_ in data['rank']:
                r_['why'] = blind_text(r_['why']); r_['detail'] = blind_text(r_['detail']); r_['alt'] = ''
            data['rank'] = rank_only(data['rank'])
    elif a.rank_lattice:
        if not a.rank_key:
            ap.error('--rank-lattice needs --rank-key')
        data['rank'], unm = rank_from_lattice(data, a.rank_lattice, a.rank_key, a.rank_lang, a.rank_corpus, a.rank_sid, blind=blind, seed=a.blind_seed)
        if unm:
            print(f'{unm} lattice positions had no tile of that sid (check --rank-sid)', file=sys.stderr)
    elif a.rank_confusion:
        data['rank'] = rank_from_confusion(data, tsv(a.rank_confusion), focus_sids, blind=blind, seed=a.blind_seed)
    if a.rank_out and 'rank' in data and not a.rank:
        with open(a.rank_out, 'w') as f:
            f.write('sid\tscore\talt\twhy\tdetail\n' + ''.join(f"{x['sid']}\t{x['score']}\t{x['alt']}\t{x['why']}\t{x.get('detail', '')}\n"
                                                             for x in data['rank']))
    if 'rank' in data:
        data['rankNote'] = a.rank_note or ('Ordered by how much a placement could change the reading (an order only, no guess shown)' if blind else 'Scored by ' + ('the decode lattice: expected letters changed if the tile flips'
                                           if (a.rank or a.rank_lattice) else
                                           'look-alike confusion x tiles flipped (a triage order, not a reading)'))
    if a.region:
        add_region(data, a.region, a.out, a.region_long, a.region_quality, a.region_embed)
    if a.data_out:
        json.dump({k: v for k, v in data.items() if not k.startswith('_')}, open(a.data_out, 'w'))
    html = render(data, a.title, a.lede, focus_to_tray=a.focus_to_tray, key=a.key)
    open(a.out, 'w').write(html)
    n = sum(len(p['items']) for p in data['piles'])
    nc = len({it['c'] for p in data['piles'] for it in p['items'] if 'c' in it})
    print(f"{len(data['piles'])} piles, {n} tiles, {data['skipped']} skipped, {nc} clusters "
          f"({data.get('clusterSource', 'none')}), {len(data.get('rank', []))} ranked, {len(html) // 1024} KB -> {a.out}")
    if len(html) > 15 * 1024 * 1024:
        print('WARNING: over 15 MB; the Artifact limit is 16 MB', file=sys.stderr)
    if not a.no_preflight:   # SORTER-PREFLIGHT (6 Oct 2026): the gate before publishing; a FAIL is printed, the build stands
        import sorter_preflight
        sorter_preflight.run(page=a.out, cipher_lines=a.cipher_lines, search=[os.path.dirname(os.path.abspath(a.signs))],
                             pages_json=a.pages if a.pages.endswith('.json') else None)   # real page colours for the colour check's box test


if __name__ == '__main__':
    main()
